import json
from pathlib import Path

DATA = json.loads((Path(__file__).resolve().parent.parent / "data" / "population_2025.json").read_text())

def test_ages_0_to_100_once():
    assert [a["age"] for a in DATA["ages"]] == list(range(101))

def test_sum_matches_census_total():
    total = sum(a["count"] for a in DATA["ages"])
    assert abs(total - DATA["census_total"]) / DATA["census_total"] < 0.001

def test_total_plausible_us_population():
    assert 3.3e8 < DATA["census_total"] < 3.6e8

def test_top_age_group_recorded():
    assert DATA["top_age_group"]["open_ended"] is True
