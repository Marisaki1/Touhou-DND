# FLOOR 8: THE MERCHANT'S CROSSING
### Part 7 — NPC GP Values & Economic Balance

This file exists to answer one question precisely: **how much gold can players actually extract from talking to NPCs, and does it break the Town Economy Pool?** Short answer: no — it's deliberately kept to roughly 6% of the 3,000gp Pool, so Selling, Gathering-into-Crafting, and Robbery remain the floor's real earning engines. NPC trading is a supplement, not a substitute.

---

## The Formula

Instead of hand-assigning a unique gp value to all 42+ individual houses, every NPC's gold value is generated from two inputs:

**NPC Gold Value = Archetype Base Roll × House Tier Multiplier**

### Archetype Base Roll (Trade results, per `06`)

| Archetype | Base Roll | Notes |
|---|---|---|
| Young Boy / Young Girl | **0gp, always** | Never carry tradeable gold. Item-for-item trades only. |
| Teenage Boy / Teenage Girl | **1d3gp** | Pocket money only |
| Adult Man / Adult Female | **1d6+1gp** (range 2–7gp) | The floor's main NPC trading partners |
| Old Man / Old Woman | **1d4+3gp** (range 4–7gp) for Trade results; **flat +6gp** for the rarer Favor result | Elders pay the best, but the Favor payout only triggers once per NPC and requires the full 6-round Do a Favor action |

### House Tier Multiplier

| House Tier | Multiplier |
|---|---|
| Small | ×1 |
| Medium | ×1.5 (round up) |
| Large | ×2 |

**Worked examples:**
- An Adult Man at a Small house rolls 1d6+1 (say, 4gp) × 1 = **4gp** on a Trade result.
- An Old Woman at a Medium house rolls 1d4+3 (say, 6gp) × 1.5 = **9gp**, rounded up.
- An Old Man's Do a Favor at a Large house pays a flat 6gp × 2 = **12gp** — the single richest NPC payout on the floor, and it's gated behind a 6-round Major Action, a DC 12 check, and "once per NPC."

---

## Why this stays balanced

**Ceiling check across all 42 Common Houses**, assuming (generously) every house's resident NPC is engaged for their single best Trade result once during the floor:

| House Tier | Count | Avg. NPC Trade Value (after multiplier) | Subtotal |
|---|---|---|---|
| Small | 22 | ~4gp | ~88gp |
| Medium | 14 | ~7gp | ~98gp |
| Large | 6 | ~11gp | ~66gp |

**Total ceiling: ~252gp** if every single house's NPC sells to the party exactly once. In practice this never happens — Reputation gates (the "Wary/Gate" results in `06`), the once-per-NPC Favor limit, "Absent" rolls, and the sheer time cost of RAP mean real tables extract closer to **120–180gp** across a five-day floor. That lands the system comfortably inside the ~175gp (6%) share allotted to NPC trading in `01`'s Pool breakdown.

**Guild Quests, Church Alms, Graveyard finds, and the Fence (`10`) are tracked separately** and are *not* part of this ceiling — they already have their own payout ranges defined in their respective files. Don't double-count a Guild quest reward as an NPC Favor just because an NPC handed it to you; if it's listed on the Quest Board (`09`), it draws from the Quest share of the Pool, not the NPC share.

---

## DM Quick-Roll Table (skip the math at the table)

If you'd rather not calculate the formula live, use this pre-rolled reference for a Trade result:

| Archetype | Small House | Medium House | Large House |
|---|---|---|---|
| Teenage Boy / Girl | 1–2gp | 2–3gp | 3–4gp |
| Adult Man / Adult Female | 3–5gp | 5–8gp | 8–11gp |
| Old Man / Old Woman (Trade) | 5–6gp | 7–9gp | 9–11gp |
| Old Man / Old Woman (Favor, once only) | 6gp | 9gp | 12gp |
| Young Boy / Young Girl | 0gp (items only) | 0gp | 0gp |

**Reminder:** these numbers are *payments to players* (an NPC buying something off the cart, or a Favor reward) and count against the Pool the moment gold changes hands. Item-for-item trades (most of the "Trade" rows in `06`) move no gold at all and don't touch the Pool — they're pure barter.
