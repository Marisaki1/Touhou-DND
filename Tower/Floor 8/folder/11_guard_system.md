# FLOOR 8: THE HUMAN VILLAGE
### Part 11 — Stealing, Alertness & The Guard System

Stealing is a great way to make money on this floor. Doing it repeatedly is what gets a team caught. This file is the whole of that tradeoff.

## Town Guard (Combat Stats)

| Stat | Value |
|---|---|
| AC | 15 |
| HP | 26 |
| Speed | 30ft |
| Attack | Shortsword +5, 1d6+3 slashing (nonlethal by default — guards subdue, they don't execute) |
| Special | **Backup (1/combat):** on being reduced below half HP, a guard calls for reinforcements — a second guard arrives in 1d4 rounds |

Guards originate from the Guild and patrol Residential & Market and the graveyards. They're the enforcement layer *outside* the market square, where the Masked White Girl's Violence Penalties (`01`) don't reach.

---

## Real-Time Patrol Check

Once per Robbery Major Action (`05`), or once per witnessed act of misconduct outside the market, roll a **Patrol Check** using the current shared Alertness tier (`05`):

| Alertness | Patrol Check Chance |
|---|---|
| 0–2 (Quiet) | 1-in-8 (roll a d8, 1 triggers) |
| 3–5 (Watching) | 1-in-5 (roll a d5, 1 triggers) |
| 6+ (Hunted) | Residential houses are already locked to robbery entirely (`05`) — this row only matters for non-robbery misconduct, where a patrol triggers on a 1-in-3 |

**If a patrol triggers:** the acting player's original check is contested against the patrol's **passive Perception 13**.

- **Beats 13:** the patrol passes without noticing. The action continues, resolved normally.
- **Fails to beat 13:** the patrol notices *immediately* — treat as an instant **Guard Chase** (`05`'s Getting Caught table, result 1), regardless of what the original roll would have been. The action is aborted; no item is gained.

**DM Note:** Casing the House (`04`, learn a house's schedule) and Set a Watch (`04`) are how players reduce real exposure to patrols, on top of managing shared Alertness.

---

## Morning Guard Investigation

Triggered automatically each morning (Step 2 of the morning sequence, `01`) for any robberies committed the previous day that weren't already caught by a real-time patrol.

Roll d20, modified: **+2** per Large house robbed that day, **+1** per Medium, **+0** per Small, **−2** if Case the House was used first, **+3** if Alertness ended the day at 6+ (Hunted).

| Total | Result |
|---|---|
| ≤10 | No leads |
| 11–15 | Guards increase patrols — Alertness +1 town-wide, no further consequence |
| 16–20 | A witness comes forward. Any team that robbed a house yesterday makes a group Stealth or Deception check (DC 13) or is formally suspected: Reputation −2, and a Guard NPC visits their stall during the next Selling Phase to "ask questions" (costs 1 customer slot) |
| 21+ | Culprits identified outright. That team is fined 2× the value of everything stolen that day, plus Reputation −4. If they were already Hunted (Alertness 6+), the Masked White Girl personally investigates their stall. |

**The point of this table:** one robbery is a footnote. A team that robs houses every single day will eventually roll into the 16+ range and pay for it — that's the intended tradeoff, not a punishment for using the mechanic at all.

---

## Guards and Player Misconduct Outside the Market

Violence, theft caught in the act, or open disruption in Residential & Market or the graveyards draws a Town Guard response directly via the Patrol Check above — treat as an immediate combat or Intimidation/Persuasion-to-de-escalate encounter using the statline above.

**Aid response:** if an occupied house's NPC is being robbed or harassed and the interaction table (`06`) rolls a "Gate" or witnessed-misconduct result, treat that as an automatic patrol trigger on top of the normal chance above — a frightened or angry NPC shouting for help draws attention fast, especially near a Large household's deterrent (`05`).
