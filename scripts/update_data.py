"""Convert a downloaded Census NC-EST agesex CSV to data/population_<year>.json.

Usage: python scripts/update_data.py data/raw/nc-est2025-agesex-res.csv [--year 2025]
Year defaults to the newest POPESTIMATE column in the file. Older files are kept.
"""
import argparse, csv, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOP_AGE = 100  # Census top bucket = "100 and older"


def convert(raw, year=None, source_url=None):
    raw = Path(raw)
    m = re.match(r"nc-est(\d{4})-agesex-res", raw.name.lower())
    if not m:
        raise SystemExit(f"Unexpected file name {raw.name}; expected nc-est<vintage>-agesex-res.csv")
    vintage = int(m.group(1))
    with open(raw, newline="") as f:
        reader = csv.DictReader(f)
        years = sorted(int(c[11:]) for c in reader.fieldnames if re.fullmatch(r"POPESTIMATE\d{4}", c))
        year = year or years[-1]
        if year not in years:
            raise SystemExit(f"No POPESTIMATE{year} column. Available: {years}")
        col = f"POPESTIMATE{year}"
        ages, total = {}, None
        for row in reader:
            if row["SEX"] != "0":  # 0 = both sexes
                continue
            age, n = int(row["AGE"]), int(row[col])
            if age == 999:
                total = n
            else:
                ages[age] = n
    check(ages, total)
    return {
        "dataset": f"NC-EST{vintage}-AGESEX-RES",
        "vintage": year,
        "estimate_date": f"{year}-07-01",
        "source_url": source_url or (
            f"https://www2.census.gov/programs-surveys/popest/datasets/"
            f"{vintage - 5}-{vintage}/national/asrh/{raw.name.lower()}"),
        "sex": "both",
        "top_age_group": {"age": TOP_AGE, "open_ended": True, "label": "100+"},
        "census_total": total,
        "ages": [{"age": a, "count": ages[a]} for a in sorted(ages)],
    }


def check(ages, total):
    missing = [a for a in range(TOP_AGE + 1) if a not in ages]
    if missing or set(ages) != set(range(TOP_AGE + 1)):
        raise SystemExit(f"Ages 0-{TOP_AGE} not exactly present. Missing: {missing}")
    if total is None:
        raise SystemExit("No total row (AGE=999) found.")
    s = sum(ages.values())
    if abs(s - total) / total > 0.001:
        raise SystemExit(f"Ages sum {s:,} differs from Census total {total:,}.")
    if not 3.0e8 < total < 4.0e8:
        raise SystemExit(f"Total {total:,} is not a plausible US population.")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("raw", help="downloaded Census CSV")
    p.add_argument("--year", type=int, help="estimate year (default: newest column)")
    a = p.parse_args()
    data = convert(a.raw, a.year)
    out = ROOT / "data" / f"population_{data['vintage']}.json"
    out.write_text(json.dumps(data, indent=1) + "\n")
    print(f"wrote {out}  total={data['census_total']:,}  ages={len(data['ages'])}")
