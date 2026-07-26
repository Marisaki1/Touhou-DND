# FLOOR 8: THE HUMAN VILLAGE
### Part 12 — Reputation & The Selling Phase

## REPUTATION TRACKER

Starts at **0**, range **−10 to +10**. Governs customer count, base sale price, and which negotiation tools are available.

| Score | Customer Modifier | Base Price Modifier | Tool Access |
|---|---|---|---|
| **+5 to +10** | +1d6 customers; 1 guaranteed Special Customer | +15% | All tools |
| **+1 to +4** | +1d4 customers | +6% | All tools |
| **0** | neutral | — | All tools |
| **−1 to −4** | −1d4 customers; 1–2 vendors refuse to sell to you | −10% | Luxury Upsell unavailable, Upsell DC +2 |
| **−5 to −9** | −1d6 customers; authority watching | −20% | Negotiation locked — Honest Sale only |
| **−10** | stall shut down 1 full day | — | Cannot sell |

Stacks with Market Trend (`12`, below).

### Reputation Gains
Honest sale to elder/authority +1 · Public performance DC 15+ +1 · Resolving a dispute fairly +1 · Donating goods (10gp+) +2 · Publicly exposing a Syndicate agent +2 · Completing a Slum Outreach or Soup Kitchen charity action +2–3 (`09`/`10`) · Helping an NPC via a Favor (`06`) +1 (most rows)

### Reputation Losses
Failed deception discovered −1 · Intimidating a witnessed customer −1 (cumulative/day) · Rumor traced to you −2 · Theft discovered −3 · Witnessed bribe −1 · Violence inside the market −2/incident

---

## PRICE MANIPULATION — Persuasion, Deception, Intimidation

Once per customer during the Selling Phase.

| Method | Skill | DC | On Success | On Failure |
|---|---|---|---|---|
| Honest Sale | — | — | Listed price guaranteed | — |
| Upsell (≤30%) | Persuasion | 10 + markup% | Full marked-up price | Base price only |
| Luxury Upsell (31–60%) | Persuasion | 14 + markup% | Full marked-up price | Customer walks (d6: 5–6, buys from a rival) |
| Storytelling | Performance | 12 | +15% flat, stacks with Upsell | No bonus |
| Misrepresent Quality | Deception | 14 | Full inflated price now | Caught on the spot — sale fails, Rep −1, next 1d4 customers wary |
| Misrepresent Rarity | Deception | 15 | Full inflated price now | Caught on the spot — sale fails, Rep −2, same wariness |
| Pressure Sell | Intimidation | 15 | Full price guaranteed | −1d4 customers rest of phase |

**Pressure Sell:** Reputation −1 per use, cumulative same day, regardless of outcome.

**Deception discovery** (checked once at end of day, per successful lie): Misrepresent Quality 25% base / Misrepresent Rarity 35% base. If discovered: refund the sale's gold, and Reputation −1 (Quality) or −2 (Rarity).

---

## PERFORMANCE — Busking

Covered in full in `04` (Major Action, 1 MAP, Performance DC 10). Two places it can happen: your own stall during the Selling Phase (as a customer draw, below), or anywhere in the village as a stand-alone Busk for direct coin.

**Busking for coin:** 1d4+2gp on success, Reputation +1 on a success by 5+. **Hard cap: once per character, per day.** This is deliberate — Performance is meant to be a nice supplement, not a grind loop.

---

## MARKET TRENDS → PRICE

Each morning: **1 Liked (+30%), 1 Neutral, 1 Disliked (−25%)** across Hunt/Forage/Mine. Affects sale price only, never customer count or gathering. Hidden — read via Observe/Scout Rival Stall, Investigate Market Trend, or an NPC Info roll (`06`).

---

## CATCH-UP CUSTOMERS — keeping the gap from running away

Kazuo (`14`) is a one-time, narrative rubber-band that only fires on Day 2 and Day 3, to whichever two teams are lowest at that exact moment. That's not enough on its own to stop a genuinely bad Day 1 from snowballing into an unwinnable gap by Day 5. This is the systemic version, and it runs every day.

**Every morning from Day 2 onward** (Step 6 of the morning sequence, `01`): the team with the **lowest cumulative earnings so far** gets **+1d4 bonus customers** at their stall that evening. If two or more teams are tied for last, all of them get it. This stacks with every other customer modifier normally.

**On the other end:** if any team is leading by **50gp or more** over the second-place team, the next Selling Phase Interruption (`13`) automatically resolves as a **Tax Collector** against them, no roll needed — the Syndicate leans hardest on whoever's winning. This is on top of the existing Pressure +1 for any 20gp+ lead (`13`); the 50gp+ trigger is a harder, guaranteed version specifically for a genuine runaway.

**Why both directions matter:** a bottom-place bonus alone can overcorrect into just handing the last-place team the win outright by Day 5; a top-down tax alone can feel like the game punishing good play. Together they compress the *spread* between 1st and 4th without removing the reward for playing well — the leader still leads, they just can't coast on an early lead untouched for five straight days.


## THE SELLING PHASE

Runs every evening until that day's customers are processed.

### How Many Customers Per Day

| Day | Suggested Base |
|---|---|
| Day 1 | 1d4+3 (4–7) |
| Day 2 | 1d6+3 (4–9) |
| Day 3 | 1d6+3 | 
| Day 4 | 1d6+4 (5–10) |
| Day 5 | 1d8+4 (5–12); +2d8 if Kazuo is defeated (`15`) |

Modifiers stack on top: signs +1d4, demo +2d4, shout +1d4, street crier +1d6, Reputation per tracker, Slanderer −1d6 (`13`), rival sabotaged +1d4.

Resolve routine customers with a quick price-and-roll; fully roleplay Special Customers and Syndicate interruptions.

### Customer Table — d20

| d20 | Customer | Wants | Spends | Notes |
|---|---|---|---|---|
| 1–2 | Village child | Cheap, shiny, small | 1–5cp | Won't negotiate up |
| 3–4 | Farm laborer | Practical food/tools | 1–8sp | Persuasion DC 10 to upsell |
| 5–6 | Village housewife | Food, fabric, useful goods | 5–20sp | Deception DC 17 to fool |
| 7–8 | Craftsperson | Raw materials | 1–3gp | Won't buy rough |
| 9–10 | Young couple | Novelty, gifts | 2–6gp | Performance/Persuasion DC 11 |
| 11–12 | Village elder | Medicine, familiar goods | 4–12gp | Loyal if satisfied |
| 13–14 | Passing merchant | Unusual/bulk | 8–40gp | Highest ceiling |
| 15–16 | Curious scholar | Unusual specimens | 5–25gp | History/Arcana DC 12 |
| 17 | Pilgrims (pair) | Medicinal, sentimental | 3–10gp | Story-friendly |
| 18 | Off-duty climber | Functional goods | varies | Pays well |
| 19 | Village authority | Compliance check | — | Rep −4 or lower triggers inspection |
| 20 | Special Customer | See below | Exceptional | Roll d8 |

### Special Customer — d8
1 Collector (3× on match) · 2 Bulk Buyer (5–8 units, 80%/unit) · 3 Desperate (4× urgent) · 4 Critic (±customers tomorrow) · 5 Syndicate's Eyes (casing, `13`) · 6 Craftsperson's Buyer (2× Excellent+) · 7 Gossip (+1d6 customers, mentions flaws too) · 8 Wealthy Eccentric (5× if a specific desire is met — cap multiplier at 1.5× against Product-tier items)

**Reminder:** an Adult Woman archetype who buys jewelry as a Special Customer at your stall is subject to the same rules as one bought via NPC Trade in `06` — see `14` for why that matters.
