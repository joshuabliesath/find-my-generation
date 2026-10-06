// Compare site/core.js against Python results in expected.json.
// Run: node tests/js_parity/check.js   (after dump_expected.py)
"use strict";
const fs = require("fs");
const path = require("path");
const core = require("../../site/core.js");

const dataDir = path.join(__dirname, "..", "..", "data");
const expected = JSON.parse(fs.readFileSync(path.join(__dirname, "expected.json"), "utf8"));
const gens = JSON.parse(fs.readFileSync(path.join(dataDir, "generations.json"), "utf8")).generations;
const pop = JSON.parse(fs.readFileSync(path.join(dataDir, expected.population_file), "utf8"));

const TOL = 1e-9; // relative tolerance for floats; ints/strings/booleans must match exactly
let failures = 0;
function fail(msg) {
  failures++;
  if (failures <= 20) console.log("MISMATCH " + msg);
}

function same(a, b) {
  if (typeof a === "number" && typeof b === "number") {
    if (Number.isInteger(a) && Number.isInteger(b)) return a === b;
    return Math.abs(a - b) <= TOL * Math.max(1, Math.abs(a), Math.abs(b));
  }
  return a === b;
}

function compareLists(label, got, want) {
  if (got.length !== want.length) return fail(`${label}: length ${got.length} vs ${want.length}`);
  got.forEach((g, i) => {
    for (const k of Object.keys(want[i])) {
      if (!same(g[k], want[i][k])) fail(`${label}[${i}].${k}: JS ${g[k]} vs Python ${want[i][k]}`);
    }
  });
}

function errorOf(fn) {
  try { fn(); return null; } catch (e) { return e.message; }
}

for (const c of expected.cases) {
  const y = c.input;
  if ("rank_error" in c) {
    const e1 = errorOf(() => core.rankBirthYear(y, gens, pop));
    const e2 = errorOf(() => core.membershipBirthYear(y, gens, pop));
    if (e1 !== c.rank_error) fail(`rank error for ${JSON.stringify(y)}: JS "${e1}" vs Python "${c.rank_error}"`);
    if (e2 !== c.membership_error) fail(`membership error for ${JSON.stringify(y)}: JS "${e2}" vs Python "${c.membership_error}"`);
  } else {
    compareLists(`rank ${y}`, core.rankBirthYear(y, gens, pop), c.rank);
    compareLists(`membership ${y}`, core.membershipBirthYear(y, gens, pop), c.membership);
  }
}

console.log(failures ? `FAIL: ${failures} mismatches` : `PASS: ${expected.cases.length} cases match Python`);
process.exit(failures ? 1 : 0);
