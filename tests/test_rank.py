import pytest
from core.rank import rank_birth_year


def by_label(rs):
    return {r.label: r for r in rs}


def test_mid_generation():
    r = by_label(rank_birth_year(1985))
    assert r["Greatest"].older_pct == 100 and not r["Greatest"].approximate
    assert r["Gen Z"].older_pct == 0 and r["Gen Z"].younger_pct == 100
    m = r["Millennials"]
    assert 0 < m.older_pct < 100
    assert m.older_pct + m.younger_pct == pytest.approx(100)


def test_boundary_first_and_last_year():
    gens = rank_birth_year(1981)  # first Millennial year (Pew: 1981-1996)
    m = by_label(gens)["Millennials"]
    assert 0 < m.older_pct < 5  # half of one year's births
    assert by_label(gens)["Gen X"].older_pct == 100


def test_top_age_bucket_approximate():
    r = by_label(rank_birth_year(1910))
    assert r["Greatest"].approximate
    assert 0 < r["Greatest"].older_pct < 100
    assert r["Silent"].older_pct == 0 and not r["Silent"].approximate


def test_invalid_input():
    with pytest.raises(ValueError, match="future"):
        rank_birth_year(2999)
    with pytest.raises(ValueError, match="too early"):
        rank_birth_year(1850)
