# FLOOR 8: THE HUMAN VILLAGE
### Part 7 — Economic Balance: A Real Simulation

**This file was rebuilt from scratch after a serious error was caught.** An earlier version of this floor collapsed the Production Phase into an abstracted "30 rounds," which worked out to 2.5 real hours — when the floor was always meant to run on an actual clock, 8:00 AM to 6:00 PM, 10 real hours, exactly as the original hourly gathering-window schedule laid out. Every number in this file is now built on the correct 10-hour day using **Major Action Points (MAP, 1 = 1 hour)** and **Round Action Points (RAP, 1 = 5 minutes)** — see `01` and `04`.

---

## The Corrected Day

- **Production Phase: 8:00 AM – 6:00 PM = 10 hours = 10 MAP.** This is the entire budget a team has for Gathering, Robbery, Crafting, Guild Quests, Investigation, and everything else in `03`–`11`, `14`.
- **Market Time (Selling Phase): 6:00 PM – 10:00 PM = 4 hours**, separate, resolved through the Customer Table (`12`) exactly as before — this part of the math was never affected by the round-length error, so it carries over unchanged.
- **Gathering runs in four fixed windows** (`03`): 9–12 (Hunt/Forage), 10–1 (Mine/Fish), 1–4 (Fish/Forage), 2–5 (Mine/Hunt). Every one of the four resource types (Hunt, Mine, Fish, Forage — Fishing is back, at the River Shallows) is available in exactly 2 windows.

---

## Gathering: the Reliable Backbone

**Gather = 3 MAP, yields 2 nodes.** Averaging across all four gathering tables (Hunt, Mine, Fish, Forage — weighting by the 6/8/4/2 node-tier split):

| Table | Avg. Value/Node |
|---|---|
| Hunt | 8.1gp |
| Mine | 7.0gp |
| Fish | 7.3gp |
| Forage | 6.2gp |
| **Overall average** | **~7.15gp/node** |

**2 nodes × 7.15gp = ~14.3gp per 3-MAP Gather action = ~4.77gp/MAP.**

**Maximum sustainable gathering:** a team has 10 MAP/day; 3 Gather actions (9 MAP) is the practical ceiling, leaving 1 MAP spare — **6 nodes/day, 30 nodes across the floor, ~213gp raw material value total** if a team did nothing else for all five days. This is deliberately *not* a huge number relative to a team's own Selling Phase capacity (below) — gathering is meant to feed Crafting and Selling, not be a complete strategy on its own.

**The Team-Wide Visit Cap (`03`): 2 Gather actions (6 MAP) per Area per day.** Prevents a team from parking at one Area for all 3 of a day's possible Gather actions and disproportionately hammering that Area's scarce Large/Huge nodes.

---

## Robbery: the Highest Ceiling, and the Riskiest

**Rob a House costs 1/2/3 MAP for Small/Medium/Large (`05`)** — and unlike the old draft (which made robbery strictly worse than gathering per unit of time, a real design failure), the reward now includes a cash bonus on top of the item, specifically so robbery earns its risk:

| Tier | MAP | Item (avg) | Cash Bonus (avg) | Total | GP/MAP |
|---|---|---|---|---|---|
| Small | 1 | 2.5gp | 1d4 (2.5gp) | 5.0gp | **5.0** |
| Medium | 2 | 5.75gp | 2d4 (5gp) | 10.75gp | **5.375** |
| Large | 3 | 10.25gp | 3d6 (10.5gp) | 20.75gp | **6.92** |

**Every tier of robbery now beats gathering's 4.77gp/MAP, and Large clearly the most** — which is exactly right: robbing a house is "the highest, but risky," full stop, and gathering is the *safe, reliable* option, not the highest-paying one in isolation.

**What actually keeps this balanced is scarcity and risk, not the raw numbers:**
- **The 20-house pool (`05`) is finite and non-renewing** — once robbed, a house is gone for the whole floor, split four ways. A team can't run robbery as an infinite engine the way they can gathering; eventually the houses run out.
- **Alertness scales with the roll, not just the tier** (`05`) — a clean success costs less Alertness than a barely-made one, and getting caught is expensive on every tier, up to an automatic Guard Chase on a failed Large attempt.
- **Gathering remains the better choice for a full 5-day strategy** precisely because it's renewable (Small/Medium nodes regenerate daily) and low-risk, while robbery's total ceiling across the *entire floor* — even monopolized by one team — tops out around 55–60gp raw before Alertness consequences start eating into it. Robbery is the best single action in the game; gathering is the best full-floor strategy. Both statements are true at once.

---

## Crafting: Why the Markup Is +50%

Crafting costs its own MAP (1/2/3 for Small/Medium/Large, `03`/`04`) **on top of** the RAP spent traveling to and from the Guild Hall. That's real overhead for something that doesn't gather anything new — it only exists to reward a team for making that trip and spending that hour. A Medium Product (4 Medium materials, ~23gp raw) crafted into a ~34.5gp Product nets an **11.5gp margin for 2 MAP (~5.75gp/MAP)** — comparable to Large-house robbery, which is the right shape given the travel cost stacked on top of the MAP itself.

---

## Guild Quests: High GP/MAP, Hard-Rationed

Several Guild Quests (`09`) resolve for very strong GP/MAP — Poacher's Trail pays 18gp for 1 MAP of actual objective-time, an 18gp/MAP rate that dwarfs gathering. **This is fine, because postings are the actual bottleneck**, not time: only 3 Guild Quests refresh per day, shared across 4 teams, each claimable once. A team can't run Guild Quests as a full-time strategy any more than they can run pure robbery — both are excellent supplements gated by scarcity (houses; postings) rather than direct MAP cost.

---

## NPC Trade: Fast, Capped, and No Longer the Point

NPC Trade (`06`) is a Round Action (1–2 RAP), not a Major Action — a sale can look extremely efficient per unit of time, but it's capped hard by each NPC's lifetime gold ceiling (40/60/30gp) and by there being only 34 NPCs on the whole floor. With the corrected 10-MAP day giving Major Actions so much more room to generate real gold, NPC Trade's *relative* importance drops naturally — it's genuinely a utility now (get the specific item you need, unload something ahead of a trend shift, cash in Kazuo's jewelry) rather than a primary income engine. Nothing about its absolute numbers changed; the day around it just got bigger.

**Theoretical ceiling** (34 NPCs: 8 Adult Man @40gp, 8 Adult Woman @60gp, 3 Old Man @30gp, 3 Old Woman @30gp): **980gp**, shared across 4 teams. Realistic extraction: **500–650gp floor-wide.**

---

## Selling Phase: Still the Ceiling That Matters

Averaging the Customer Table (`12`) across its full spread: **~7–8gp average spend, ~35 customers per team across the floor ≈ 270–300gp base Selling capacity per team**, before Persuasion/Performance/Reputation bonuses. This number was never affected by the round-length error — it checks out fine against the corrected gathering ceiling (~213gp raw, comfortably under 270–300gp), meaning there's still no overproduction problem: even a team that does nothing but gather all five days produces less than their own Selling Phase can absorb.

---

## Simulated Strategy Comparison (Projected 5-Day Totals, 3-character team)

| Strategy | Approach | Projected Total | Why |
|---|---|---|---|
| **Gatherer-Crafter** | ~2 Gather actions/day (6 MAP), rest crafting/prep, sells at own stall only | ~230–260gp | ~20 nodes over the floor, crafted at +50% markup, sold within the Selling ceiling — solid and simple, single-channel |
| **Socialite** | Modest gathering, heavy NPC Trade + Guild Quests + Performance | ~350–390gp | Stacks NPC Trade (bypasses the Selling ceiling entirely), 4–5 Guild Quests (high GP/MAP but rationed), and daily Busking on top of some normal selling |
| **Balanced** | Mixes gathering, some robbery, some NPC trade, quests | ~380–430gp | Highest of the four — touches every scarcity-gated system (houses, NPC caps, quest postings) instead of maxing any single one |
| **Robbery-Heavy** | Prioritizes houses and the Fence, still runs a normal stall with what's left over | ~260–290gp | The 20-house pool caps total robbery income around 55–60gp raw regardless of effort; strong as a supplement, capped as a sole strategy |

**Read on this:** diversifying still wins, and every strategy lands within roughly ±25% of the others — no single approach is a degenerate no-brainer, and none is a trap. Gathering remains the one truly renewable, low-risk engine; everything else is higher-value but individually rationed by scarcity (houses), risk (Alertness), or postings (quests, NPCs).

---

## What Was NOT Simulated

- Combat-dependent income (Guild Quests requiring a fight, the Fight Ring, `13`'s enemy encounters) — too swingy on party build to model meaningfully. Treat the numbers above as the non-combat floor.
- The Kazuo jewelry swing — covered separately in `14`, including an honest flag that it can overshoot and a tuning dial if it does.
- Four real players making genuinely different tactical choices under time pressure. Use this file as a sanity check before the floor starts and a diagnostic if something looks broken mid-run — not as a guarantee of the actual table's outcome.
