# FLOOR 8: THE HUMAN VILLAGE
### Part 5 — The Residential Houses

**20 total: 10 Small, 6 Medium, 4 Large.** All of them sit inside Residential & Market (`02`), alongside the four player stalls. This is a finite, trackable pool for the whole floor — once robbed, a specific house doesn't regenerate its "robbable" status (the same household isn't hit twice). With four teams competing, houses genuinely run out over five days if robbery is popular.

Every occupied house has at least one resident NPC — see `06` for the archetype dialogue tables and gold caps. As a quick guide for populating houses:

| House Size | Count | Typical Residents |
|---|---|---|
| Small | 10 | 1 NPC — roll or pick any archetype |
| Medium | 6 | 2 NPCs — usually an Adult (Man or Woman) plus one Teenager or Young child |
| Large | 4 | 3 NPCs — an Adult or Old household head, plus family; these are the village's wealthiest and most connected residents |

### Suggested Archetype Population (34 NPCs total)

| Archetype | Count | Notes |
|---|---|---|
| Adult Man | 8 | Bread-and-butter trading partner, 40gp cap |
| Adult Woman | 8 | Bread-and-butter trading partner, 60gp cap — Kazuo's jewelry sells best here (`14`) |
| Old Man | 3 | 30gp cap, richest info |
| Old Woman | 3 | 30gp cap, richest info |
| Teenage Boy | 4 | 20gp on hand, cannot trade |
| Teenage Girl | 4 | 20gp on hand, cannot trade |
| Young Boy | 2 | 0gp, barter only |
| Young Girl | 2 | 0gp, barter only |

---

## Robbing a House

| House Size | MAP | Check | Base DC | Reward |
|---|---|---|---|---|
| Small | 1 | Stealth or Sleight of Hand | 12 | 1 Small-tier item + 1d4gp cash |
| Medium | 2 | Stealth or Sleight of Hand | 14 | 1 Medium-tier item + 2d4gp cash |
| **Large** | 3 | Stealth or Sleight of Hand | 16 | 1 Large-tier item + 3d6gp cash; automatic Guard Chase on failure |

**This is deliberately the single best GP/MAP in the game** — a Large house robbery (3 MAP) nets more raw value than a 3-MAP Gather action (`07` has the exact math). That's the point: robbery is the risky, high-ceiling option, gathering is the safe, reliable one. The risk is real — see Alertness below — and robbery's *total* ceiling across the floor is hard-capped by the 20-house pool in a way gathering (renewable) never is.

**Large houses (4 total)** each have an active deterrent: a private guard, a watchdog, or an alarm arrangement. This is baked into the automatic Guard Chase on failure. It's also why Large-house NPCs never appear alone.

---

## Alertness (shared across ALL four teams — 0–9+)

| Alertness | State | Effect |
|---|---|---|
| 0–2 | Quiet | No DC change |
| 3–5 | Watching | +3 to robbery DC |
| 6+ | Hunted | Residential houses locked to robbery for the rest of the day; attempting anyway is an automatic catch |

Decays −2 every morning, before Guard Investigation is resolved. See `11`.

### How Much Alertness a Robbery Actually Costs

Alertness gain scales with the house tier **and** how cleanly the job went — a barely-made check leaves more of a mess than a clean one, even on a success.

| Result | Small | Medium | Large |
|---|---|---|---|
| **Clean success** (beat the DC by 5+) | +0 | +1 | +4 |
| **Normal success** (beat the DC by 0–4) | +1 | +2 | +5 |
| **Caught** (failed the check) | +2 | +4 | **+8**, and always a Guard Chase — see below |

This rewards actually being good at the check, not just passing it — a Rogue with a real Stealth bonus who clears a Large house by 6+ leaves the village barely more alert than before, while a desperate barely-there success on the same house is nearly as costly as getting caught outright.

---

## Getting Caught

| d4 | Consequence |
|---|---|
| 1 | **Guard Chase** — Stealth or Athletics DC 10 + current Alertness's DC bonus (0/+3/locked, above). Failure: stall confiscated 1 day + Reputation −3. |
| 2 | **On-the-spot fine** — lose gold equal to 2× the house tier's base value. Reputation −1. |
| 3 | **Marked** — Reputation −2; further robbery Alertness gain doubled for the rest of today. |
| 4 | **Syndicate notices** — Syndicate Pressure +1 (`13`), and +1 to that team's Grudge (`13`). |

---

## NPC Whereabouts Table — d6

Used when a house is "Absent" (`06`), or when Case the House reveals a schedule.

| d6 | Location |
|---|---|
| 1 | The market square, browsing stalls |
| 2 | One of the graveyards, tending a grave (`08`) |
| 3 | The Guild, checking the board |
| 4 | The Syndicate house, paying dues |
| 5 | Another house, visiting a neighbor |
| 6 | On the road, traveling to/from the Slums or a Gathering Area |

**DM Note:** an Absent roll of 3, 4, or 5 means players can find that NPC out in the world, mid-interaction with someone else — a great spot to seed a Clue or a witness for the Guard system.
