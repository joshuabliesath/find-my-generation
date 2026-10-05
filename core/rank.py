"""A: where a birth year sits inside each generation (rank). No display code."""
import json
from dataclasses import dataclass
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


@dataclass
class GenerationRank:
    name: str
    label: str
    start_year: int
    end_year: int  # Alpha: last year in the population data
    population: float
    older_pct: float  # % of this generation born before you
    younger_pct: float  # % born after you; same-birth-year people split 50/50
    approximate: bool  # True if top age bucket (100+) had to be spread out


def load_data(data_dir=DATA_DIR):
    gens = json.loads((Path(data_dir) / "generations.json").read_text())["generations"]
    pop = json.loads((Path(data_dir) / "population_2025.json").read_text())
    return gens, pop


def births_by_year(pop):
    """Return {birth_year: people}. The open-ended top age (100+) is spread evenly
    over birth years 1901..(estimate_year - top_age), so it is approximate."""
    est = pop["vintage"]
    top = pop["top_age_group"]["age"]
    first_year = 1901
    out = {}
    for row in pop["ages"]:
        if row["age"] == top and pop["top_age_group"]["open_ended"]:
            years = list(range(first_year, est - top + 1))
            for y in years:
                out[y] = out.get(y, 0) + row["count"] / len(years)
        else:
            out[est - row["age"]] = row["count"]
    return out


def check_birth_year(birth_year, gens, pop):
    """Shared input check (used by rank and membership). Raises ValueError."""
    est = pop["vintage"]
    first_year = gens[0]["start_year"]
    if not isinstance(birth_year, int) or isinstance(birth_year, bool):
        raise ValueError("Birth year must be a whole number, e.g. 1985.")
    if birth_year > est:
        raise ValueError(f"Birth year {birth_year} is in the future (data runs to {est}).")
    if birth_year < first_year:
        raise ValueError(f"Birth year {birth_year} is too early; data starts at {first_year}.")


def rank_birth_year(birth_year, data_dir=DATA_DIR):
    """birth year -> list of GenerationRank, oldest generation first."""
    gens, pop = load_data(data_dir)
    est = pop["vintage"]
    check_birth_year(birth_year, gens, pop)

    births = births_by_year(pop)
    top_bucket_last_year = est - pop["top_age_group"]["age"]
    results = []
    for g in gens:
        end = g["end_year"] if g["end_year"] is not None else est
        years = [y for y in range(g["start_year"], end + 1) if y in births]
        total = sum(births[y] for y in years)
        older = sum(births[y] for y in years if y < birth_year)
        same = births.get(birth_year, 0) if g["start_year"] <= birth_year <= end else 0
        older += same / 2  # same-birth-year rule: half count as older
        older_pct = 100 * older / total if total else 0.0
        in_bucket = any(y <= top_bucket_last_year for y in years)
        # approximate only if the top bucket's spread affects this answer
        approx = in_bucket and birth_year <= top_bucket_last_year
        results.append(GenerationRank(
            g["name"], g["label"], g["start_year"], end, total,
            older_pct, 100 - older_pct, approx))
    return results
