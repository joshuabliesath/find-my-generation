import pytest
from core.membership import membership_birth_year


def result(year):
    return [(m.label, m.pct) for m in membership_birth_year(year)]


# (year, own label, own %, partner label, partner %)
GEN_X = [
    (1965, 51, 49), (1980, 51, 49), (1966, 55, 45), (1979, 55, 45),
    (1967, 63, 37), (1978, 63, 37), (1968, 73, 27), (1977, 73, 27),
    (1969, 82, 18), (1976, 82, 18), (1970, 91, 9), (1975, 91, 9),
    (1971, 98, 2), (1974, 98, 2),
]


@pytest.mark.parametrize("year,own,partner", GEN_X)
def test_gen_x_table(year, own, partner):
    r = result(year)
    assert r[0] == ("Gen X", own)
    assert r[1][1] == partner
    assert r[1][0] == ("Boomers" if year < 1973 else "Millennials")


@pytest.mark.parametrize("year", [1972, 1973])
def test_gen_x_core(year):
    assert result(year) == [("Gen X", 100)]


@pytest.mark.parametrize("year,expected", [
    (1920, [("Greatest", 100)]),
    (1926, [("Greatest", 55), ("Silent", 45)]),
    (1928, [("Silent", 51), ("Greatest", 49)]),
    (1946, [("Boomers", 51), ("Silent", 49)]),
    (1955, [("Boomers", 100)]),
    (1960, [("Boomers", 82), ("Gen X", 18)]),
    (1964, [("Boomers", 51), ("Gen X", 49)]),
    (1981, [("Millennials", 51), ("Gen X", 49)]),
    (1988, [("Millennials", 100)]),
    (2012, [("Gen Z", 51), ("Gen Alpha", 49)]),
    (2013, [("Gen Alpha", 51), ("Gen Z", 49)]),
    (2020, [("Gen Alpha", 100)]),
    (2025, [("Gen Alpha", 100)]),
])
def test_other_checks(year, expected):
    assert result(year) == expected


def test_pure_cores():
    cores = {"Greatest": range(1901, 1921), "Silent": range(1935, 1939),
             "Boomers": range(1953, 1958), "Gen X": range(1972, 1974),
             "Millennials": range(1988, 1990), "Gen Z": range(2004, 2006),
             "Gen Alpha": range(2020, 2026)}
    for label, years in cores.items():
        for y in years:
            assert result(y) == [(label, 100)], y


def test_never_more_than_two_never_tied_sums_100():
    for y in range(1901, 2026):
        r = membership_birth_year(y)
        assert len(r) <= 2
        assert sum(m.pct for m in r) == 100
        assert r[0].pct != 50 and r[0].pct > 50


@pytest.mark.parametrize("year", [1900, 2026, 1985.5, True, "1985"])
def test_invalid_input_rejected(year):
    with pytest.raises(ValueError):
        membership_birth_year(year)
