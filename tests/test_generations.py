import json
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "data" / "generations.json"


def load():
    return json.loads(PATH.read_text(encoding="utf-8"))


def test_file_has_source_and_date():
    data = load()
    assert data["source_urls"]
    assert data["date_checked"]


def test_fields_present():
    for g in load()["generations"]:
        assert {"name", "label", "start_year", "end_year"} <= g.keys()


def test_no_overlap_no_gaps():
    gens = sorted(load()["generations"], key=lambda g: g["start_year"])
    for prev, nxt in zip(gens, gens[1:]):
        assert prev["end_year"] is not None
        assert prev["start_year"] <= prev["end_year"]
        assert nxt["start_year"] == prev["end_year"] + 1


def test_only_last_is_open_ended():
    gens = sorted(load()["generations"], key=lambda g: g["start_year"])
    assert gens[-1]["end_year"] is None
    assert all(g["end_year"] is not None for g in gens[:-1])
