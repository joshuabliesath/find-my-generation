// Core math (A rank, B membership) in plain JS. Mirrors core/rank.py and core/membership.py.
// Python is the reference. No file reading here: pass in loaded JSON.
// Browser: <script src="core.js"> -> window.FMG. Node: require("./core.js").
(function (root) {
  "use strict";

  const FADE_YEARS = 8; // blend width at every Pew line (see docs/B-METHOD.md)

  // gens = generations.json "generations" array; pop = population_<year>.json object

  function birthsByYear(pop) {
    const est = pop.vintage;
    const top = pop.top_age_group.age;
    const firstYear = 1901;
    const out = new Map();
    for (const row of pop.ages) {
      if (row.age === top && pop.top_age_group.open_ended) {
        const n = est - top + 1 - firstYear; // years 1901..(est - top)
        for (let y = firstYear; y <= est - top; y++) {
          out.set(y, (out.get(y) || 0) + row.count / n);
        }
      } else {
        out.set(est - row.age, row.count);
      }
    }
    return out;
  }

  // Throws Error with the same message as the Python ValueError.
  function checkBirthYear(birthYear, gens, pop) {
    const est = pop.vintage;
    const firstYear = gens[0].start_year;
    if (typeof birthYear !== "number" || !Number.isInteger(birthYear)) {
      throw new Error("Birth year must be a whole number, e.g. 1985.");
    }
    if (birthYear > est) {
      throw new Error(`Birth year ${birthYear} is in the future (data runs to ${est}).`);
    }
    if (birthYear < firstYear) {
      throw new Error(`Birth year ${birthYear} is too early; data starts at ${firstYear}.`);
    }
  }

  // -> array of {name,label,start_year,end_year,population,older_pct,younger_pct,approximate}
  function rankBirthYear(birthYear, gens, pop) {
    const est = pop.vintage;
    checkBirthYear(birthYear, gens, pop);

    const births = birthsByYear(pop);
    const topBucketLastYear = est - pop.top_age_group.age;
    const results = [];
    for (const g of gens) {
      const end = g.end_year !== null ? g.end_year : est;
      const years = [];
      for (let y = g.start_year; y <= end; y++) if (births.has(y)) years.push(y);
      let total = 0;
      let older = 0;
      for (const y of years) total += births.get(y);
      for (const y of years) if (y < birthYear) older += births.get(y);
      const same = g.start_year <= birthYear && birthYear <= end ? (births.get(birthYear) || 0) : 0;
      older += same / 2; // same-birth-year rule: half count as older
      const olderPct = total ? (100 * older) / total : 0.0;
      const inBucket = years.some((y) => y <= topBucketLastYear);
      const approx = inBucket && birthYear <= topBucketLastYear;
      results.push({
        name: g.name,
        label: g.label,
        start_year: g.start_year,
        end_year: end,
        population: total,
        older_pct: olderPct,
        younger_pct: 100 - olderPct,
        approximate: approx,
      });
    }
    return results;
  }

  // -> array of {name,label,pct}, own generation first, then partner (if any)
  function membershipBirthYear(birthYear, gens, pop) {
    checkBirthYear(birthYear, gens, pop);

    let i = gens.findIndex(
      (g) => g.start_year <= birthYear && (g.end_year === null || birthYear <= g.end_year)
    );
    if (i < 0) i = 0;
    const own = gens[i];
    const m = birthYear + 0.5;

    const dists = []; // [distance to line, neighbour index]
    if (i > 0) dists.push([m - own.start_year, i - 1]);
    if (own.end_year !== null) dists.push([own.end_year + 1 - m, i + 1]);
    if (dists.length === 0) return [{ name: own.name, label: own.label, pct: 100 }];

    // Same tie-break as Python min() on tuples: smaller distance, then smaller index.
    dists.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
    const [u, partner] = dists[0];
    const span = FADE_YEARS - 0.5;
    const t = Math.max(0.0, (span - u) / span);
    const partnerShare = 0.5 * (3 * t ** 2 - 2 * t ** 3);
    let ownPct = Math.floor(100 * (1 - partnerShare) + 0.5); // round half up
    if (ownPct === 50) ownPct = 51; // no-tie rule
    const partnerPct = 100 - ownPct;

    const out = [{ name: own.name, label: own.label, pct: ownPct }];
    if (partnerPct) {
      const p = gens[partner];
      out.push({ name: p.name, label: p.label, pct: partnerPct });
    }
    return out;
  }

  const api = { FADE_YEARS, birthsByYear, checkBirthYear, rankBirthYear, membershipBirthYear };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.FMG = api;
})(typeof window !== "undefined" ? window : this);
