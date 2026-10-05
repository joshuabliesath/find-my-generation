"""B: how much of each generation a birth year is (membership %). No display code.
Method: docs/B-METHOD.md."""
import math
from dataclasses import dataclass

from core.rank import DATA_DIR, check_birth_year, load_data

FADE_YEARS = 8  # blend width at every Pew line; must be <= half the shortest generation


@dataclass
class Membership:
    name: str
    label: str
    pct: int  # whole percent


def _share(g):
    return Membership(g["name"], g["label"], 0)


def membership_birth_year(birth_year, data_dir=DATA_DIR):
    """birth year -> [Membership, ...], own generation first, then partner (if any).
    Generations not listed are 0%."""
    gens, pop = load_data(data_dir)
    check_birth_year(birth_year, gens, pop)

    i = next((k for k, g in enumerate(gens)
              if g["start_year"] <= birth_year and (g["end_year"] is None or birth_year <= g["end_year"])),
             0)  # nothing earlier than the first generation is possible after the check
    own = gens[i]
    m = birth_year + 0.5

    dists = []  # (distance to line, neighbour index)
    if i > 0:
        dists.append((m - own["start_year"], i - 1))
    if own["end_year"] is not None:
        dists.append(((own["end_year"] + 1) - m, i + 1))
    if not dists:
        return [Membership(own["name"], own["label"], 100)]

    u, partner = min(dists)
    span = FADE_YEARS - 0.5
    t = max(0.0, (span - u) / span)
    partner_share = 0.5 * (3 * t**2 - 2 * t**3)
    own_pct = math.floor(100 * (1 - partner_share) + 0.5)  # round half up
    if own_pct == 50:
        own_pct = 51  # no-tie rule
    partner_pct = 100 - own_pct

    out = [Membership(own["name"], own["label"], own_pct)]
    if partner_pct:
        p = gens[partner]
        out.append(Membership(p["name"], p["label"], partner_pct))
    return out
