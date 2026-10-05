import json, sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from update_data import convert  # noqa: E402
from core.rank import latest_population_file  # noqa: E402

RAW = ROOT / "data" / "raw" / "nc-est2025-agesex-res.csv"


def test_rerun_reproduces_committed_json():
    assert convert(RAW) == json.loads((ROOT / "data" / "population_2025.json").read_text())


def test_missing_age_rejected(tmp_path):
    lines = RAW.read_text().splitlines()
    head = lines[0].split(",")
    age_i = head.index("AGE")
    bad = [l for i, l in enumerate(lines) if i == 0 or not (l.split(",")[age_i] == "50" and l.split(",")[head.index("SEX")] == "0")]
    f = tmp_path / "nc-est2025-agesex-res.csv"
    f.write_text("\n".join(bad) + "\n")
    with pytest.raises(SystemExit):
        convert(f)


def test_latest_population_file_picks_newest(tmp_path):
    for y in (2025, 2026, 2024):
        (tmp_path / f"population_{y}.json").write_text("{}")
    assert latest_population_file(tmp_path).name == "population_2026.json"
