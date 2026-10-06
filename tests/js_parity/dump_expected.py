"""Dump Python (reference) results to tests/js_parity/expected.json for the JS parity check.
Run from the project folder: python tests/js_parity/dump_expected.py"""
import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from core.membership import membership_birth_year  # noqa: E402
from core.rank import latest_population_file, load_data, rank_birth_year  # noqa: E402

gens, pop = load_data()
est = pop["vintage"]
first = gens[0]["start_year"]

cases = []
# every valid year
for y in range(first, est + 1):
    cases.append({
        "input": y,
        "rank": [asdict(r) for r in rank_birth_year(y)],
        "membership": [asdict(m) for m in membership_birth_year(y)],
    })
# invalid inputs (JSON-friendly): expect same error message
for bad in [first - 1, est + 1, 0, -5, 1985.5, "1985"]:
    case = {"input": bad}
    for key, fn in (("rank", rank_birth_year), ("membership", membership_birth_year)):
        try:
            fn(bad)
            case[key + "_error"] = None
        except ValueError as e:
            case[key + "_error"] = str(e)
    cases.append(case)

out = {
    "population_file": latest_population_file().name,
    "cases": cases,
}
(Path(__file__).parent / "expected.json").write_text(json.dumps(out, indent=1))
print(f"Wrote {len(cases)} cases to tests/js_parity/expected.json")
