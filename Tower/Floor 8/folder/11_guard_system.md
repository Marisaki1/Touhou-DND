# FLOOR 8: THE MERCHANT'S CROSSING
### Part 11 — The Guard System

Guards originate from the Guild House and patrol the Common Houses, Church, Graveyards, and Market Square exterior. They are the enforcement layer *outside* the bazaar, where Soren's Violence Penalties (`01`) don't reach.

## Town Guard (Combat Stats)

| Stat | Value |
|---|---|
| AC | 15 |
| HP | 26 |
| Speed | 30ft |
| Attack | Shortsword +5, 1d6+3 slashing (nonlethal by default — guards subdue, they don't execute) |
| Special | **Guild Backup (1/combat):** on being reduced below half HP, a guard calls for reinforcements — a second guard arrives in 1d4 rounds |

---

## Guard Patrols — Real-Time Response *(new)*

Previously, robbery consequences were resolved entirely the next morning. Now, a patrol can intervene **while a robbery or a witnessed act of harassment is actually happening**, not just after the fact.

**When it triggers:** once per Robbery Major Action (Small/Medium/Large, `05`), or once per witnessed Intimidation/violence outside the bazaar boundary, roll a **Patrol Check** using the current shared Alertness tier (`05`):

| Alertness | Patrol Check Chance |
|---|---|
| 0–1 (Quiet) | 1-in-8 (roll a d8, 1 triggers) |
| 2–3 (Noticed) | 1-in-6 (roll a d6, 1 triggers) |
| 4–5 (Watching) | 1-in-4 (roll a d4, 1 triggers) |
| 6+ (Hunted) | Common Houses are already locked to robbery entirely (`05`) — this row only matters for non-robbery misconduct, where a patrol triggers on a 1-in-3 |

**If a patrol triggers:** the acting player's original Stealth or Sleight of Hand result (or Intimidation, if this was a witnessed act of misconduct) is contested against the patrol's **passive Perception 13**.

- **Beats 13:** the patrol passes without noticing. The robbery/action continues as normal, resolved by its usual check as written in `05`.
- **Fails to beat 13:** the patrol notices *immediately*, interrupting the action. This is treated as an instant **Guard Chase** (`05`'s Getting Caught table, result 1) — regardless of what the player's original robbery roll would have been. The action is aborted; no item is gained.

**DM Note:** this mechanic is why Casing the House (`04`, 1 RAP, learn a house's schedule) and Set a Watch (`04`) matter — good intel and careful timing are how players reduce their real exposure to patrols, on top of managing shared Alertness.

---

## Post-Robbery Guard Investigation

Triggered automatically each morning (Step 2 of the morning sequence, `01`) for any robberies committed the previous day that weren't already caught by a real-time patrol.

Roll d20, modified: **+2** per Large house robbed that day, **+1** per Medium, **+0** per Small, **−2** if Case the House was used first, **+3** if Alertness ended the day at 6+ (Hunted).

| Total | Result |
|---|---|
| ≤10 | No leads |
| 11–15 | Guards increase patrols — Alertness +1 town-wide, no further consequence |
| 16–20 | A witness comes forward. Any team that robbed a house yesterday makes a group Stealth or Deception check (DC 13) or is formally suspected: Reputation −2, and a Guard NPC visits their stall during the next Selling Phase to "ask questions" (costs 1 customer slot) |
| 21+ | Culprits identified outright. That team is fined 2× the value of everything stolen that day, plus Reputation −4. If they were already Hunted (Alertness 6+), Soren personally investigates their stall. |

---

## Guards and Player Misconduct Outside the Bazaar

Violence, theft caught in the act, or open disruption in the Common Houses, Church, Graveyards, or Market Square exterior draws a Town Guard response directly via the Patrol Check above — treat as an immediate combat or Intimidation/Persuasion-to-de-escalate encounter using the statline above, independent of the bazaar's Violence Penalties table (which only governs inside the stalls themselves).

**Aid response:** if an occupied house's NPC is being robbed or harassed and the interaction table (`06`) rolls a "Wary" or witnessed-misconduct result, treat that as an automatic patrol trigger on top of the normal chance above — a frightened or angry NPC shouting for help draws attention fast, especially near a Large household's deterrent (`05`).
