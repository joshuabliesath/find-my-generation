"""Copy generations.json and the newest data/population_<year>.json into site/data/.

Usage: python scripts/sync_site_data.py
Site files get fixed names (generations.json, population.json) so index.html never changes.
"""
import re, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "site" / "data"


def newest_population():
    files = [p for p in DATA.glob("population_*.json") if re.fullmatch(r"population_\d{4}\.json", p.name)]
    if not files:
        raise SystemExit("No data/population_<year>.json found.")
    return max(files, key=lambda p: int(p.stem.split("_")[1]))


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    pop = newest_population()
    shutil.copyfile(DATA / "generations.json", OUT / "generations.json")
    shutil.copyfile(pop, OUT / "population.json")
    print(f"copied generations.json and {pop.name} -> {OUT}")
