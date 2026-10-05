"""One-off: convert Census NC-EST agesex CSV to data/population_<year>.json. T08 builds on this."""
import csv, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw" / "nc-est2025-agesex-res.csv"
YEAR = 2025
SOURCE_URL = ("https://www2.census.gov/programs-surveys/popest/datasets/"
              "2020-2025/national/asrh/nc-est2025-agesex-res.csv")

def convert(raw=RAW, year=YEAR):
    col = f"POPESTIMATE{year}"
    ages, total = [], None
    with open(raw, newline="") as f:
        for row in csv.DictReader(f):
            if row["SEX"] != "0":  # 0 = both sexes
                continue
            age, n = int(row["AGE"]), int(row[col])
            if age == 999:
                total = n
            else:
                ages.append({"age": age, "count": n})
    ages.sort(key=lambda a: a["age"])
    return {
        "dataset": "NC-EST2025-AGESEX-RES",
        "vintage": 2025,
        "estimate_date": f"{year}-07-01",
        "source_url": SOURCE_URL,
        "sex": "both",
        "top_age_group": {"age": 100, "open_ended": True, "label": "100+"},
        "census_total": total,
        "ages": ages,
    }

if __name__ == "__main__":
    out = ROOT / "data" / f"population_{YEAR}.json"
    out.write_text(json.dumps(convert(), indent=1) + "\n")
    print("wrote", out)
