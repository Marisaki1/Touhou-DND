# FLOOR 8: THE HUMAN VILLAGE — Master Index
*"Five days. One stall. The market doesn't care who you are — only what you're selling."*

This floor is split into linked files so it's easier to run at the table. Keep this index open as your hub.

## How the files are organized

| # | File | Contents |
|---|---|---|
| 01 | `01_lore_and_setup.md` | Lore, Tower Entry, the Briefing, Stalls, Cart, Violence Penalties, Structure of a Day, the Town Gold Pool |
| 02 | `02_town_map.md` | District layout matching the table map — Wildlife Forest, Mining Cave, Slums, Residential & Market, Guild, Syndicate, Forest Forage |
| 03 | `03_gathering.md` | The four Gathering Areas — Wildlife Forest (Hunt), Mining Cave (Mine), River Shallows (Fish), Forest Forage (Forage) — and the four gathering windows |
| 04 | `04_actions_reference.md` | Major Action Points (MAP) and Round Action Points (RAP) — the full action tables |
| 05 | `05_common_houses.md` | The Residential houses (10 Small / 6 Medium / 4 Large), robbery, NPC population |
| 06 | `06_npc_interactions.md` | The 8 NPC archetypes — dialogue tables, gold caps, trade rules |
| 07 | `07_npc_gp_values.md` | **The Balance Simulation** — actual GP-per-MAP math on the corrected 10-hour day, and a projected strategy comparison |
| 08 | `08_church_and_graveyards.md` | The Pristine Graveyard (one-time heist) and the Public Graveyard (repeatable salvage) |
| 09 | `09_crafting_and_guild.md` | Crafting at the Guild Hall, and the Guild Quest Board |
| 10 | `10_slums_and_road.md` | The Slums (Soup Kitchen, Fence, Fight Ring, Rumor Alley) and the connecting road |
| 11 | `11_guard_system.md` | Stealing, Alertness, and Guard Investigation |
| 12 | `12_reputation_and_selling.md` | Reputation, the Selling Phase, Performance, Customer tables |
| 13 | `13_syndicate_and_enemies.md` | The Syndicate — who they are, how they lean on teams, Selling Phase interruptions, and **Reiko's Wagon Concern** (the misleading "20%" gathering-transport contract) |
| 14 | `14_hidden_storyline.md` | **DM-only — Kazuo.** The hidden floor boss, his jewelry, the curse, and how he's tracked down |
| 15 | `15_boss_fight.md` | Kazuo's stat block and combat |
| 16 | `16_rewards_and_rivals.md` | Rival stalls, Victory Conditions, Final Rankings, Boss Rewards |
| 17 | `17_named_npcs.md` | 8 Syndicate members, 8 Guard types, 8 Guild members, 8 unique village specials — each with a voice, relationships, and real mechanical hooks |
| 18 | `18_simulations.md` | A full 5-day worked example of one team's Production Phase and Selling Phase, on the real clock throughout |

## What this revision changed

**Most recent addition — Reiko's Wagon Concern (`13`).** Reiko now owns the wagon service that ferries teams to and from the Gathering Areas. The posted price is "20% of what you bring back"; the actual contract (full text in `13`) defines settlement so that a team paying in goods instead of coin almost always hands over more than 20%, because gathered items aren't divisible and the collector picks what gets surrendered. Paying in coin gets the honest rate; so does beating Reiko at Persuasion DC 16 once the trick is caught — she has a second, genuinely fair contract already drawn up for exactly that outcome, also in `13`.

**Previous pass — the day-length fix.** An earlier version of this floor mistakenly collapsed the Production Phase into an abstracted "30 rounds," which only worked out to 2.5 real hours — nowhere near the actual 8:00 AM–6:00 PM (10-hour) day the floor was always meant to run on. That's corrected now:

- **Time runs on two explicit currencies** (`01`, `04`): **Major Action Points (MAP, 1 = 1 hour)** for anything that moves gold, goods, or influence, and **Round Action Points (RAP, 1 = 5 minutes)** for legwork — talking, traveling, quick prep. Both draw from the same real 10-hour Production Phase clock (8:00 AM–6:00 PM); Market Time (6:00–10:00 PM) is a separate 4-hour phase.
- **Fishing is back as a 4th Gathering Area** — the River Shallows, alongside Wildlife Forest (Hunt), Mining Cave (Mine), and Forest Forage (Forage) — matching the original four fixed gathering windows (`03`).
- **Gather costs 3 MAP; robbery costs 1/2/3 MAP for Small/Medium/Large** (`03`, `05`), with robbery now paying a real cash bonus on top of the item — the highest GP/MAP in the game, on purpose, balanced by Alertness (which now scales with how cleanly the check was made, not just the tier) and the hard-capped 20-house pool. Full math in `07`.
- **The entire balance simulation (`07`) and worked example (`18`) were rebuilt** on the corrected clock, with real clock times shown throughout `18` rather than abstract round counts.
- **Crafting's markup raised to +50%** (`03`) to properly reward the MAP cost plus the RAP spent traveling to and from the Guild Hall.

**Earlier passes:**

- **Renamed the floor's town to the Human Village.** No more Verath's Crossing, no Iron Ledger, no Hollow Ledger. The Syndicate is now just a local crime outfit that leans on the market — see `13`.
- **The map matches the table layout**: Wildlife Forest, Mining Cave, and the River Shallows to the west, the Slums as the connecting district, Residential & Market at the center, the Guild and the Syndicate flanking it, Forest Forage to the south.
- **NPC gold is a flat, fixed cap per archetype, not a formula.** Adult Man 40gp, Adult Woman 60gp, Old Man/Old Woman 30gp, Teenagers 20gp on hand but cannot trade, Young children 0gp but can barter small items. See `06`.
- **Crafting is a secret.** Nothing tells players they can craft at the Guild Hall — they only learn it by directly asking an Adult Man or Adult Woman. See `09`.
- **Rule 10 and Rule 11 are explicit** (`01`): a team never splits up across districts — it always acts as one unit — and moving between any two connected places costs a flat 2 RAP (10 minutes), with the exact hop count between every district laid out in `02`.
- **The Guild does a lot more now** (`09`): a Guild Standing track separate from Reputation, a permanent Bounty Board targeting specific named Syndicate members (`17`), Guild Storage, and formal Arbitration between rival teams.
- **All 32 named NPCs (`17`) got a full pass** — voice, relationships to each other, schedules, and mechanical hooks, so they can carry a scene without DM improvisation from scratch.
- **Cart upgrades no longer cost gold.** They cost materials and labor instead (`01`) — charging gold for a required upgrade just taxes the same number a team is being ranked on. Old Man/Old Woman Favors can hand over the components directly (`06`).
- **A systemic catch-up mechanic exists beyond Kazuo** (`12`): the lowest-earning team gets bonus customers every day from Day 2 on, and a team leading by 50gp+ automatically eats a Tax Collector visit.
- **The hidden floor boss is Kazuo** (`14`, `15`) — a servant of someone not yet revealed. He rubber-bands the two lowest-earning teams with cursed jewelry on Day 2 and Day 3, and the curse surfaces on Day 4. He vanishes the instant he's confronted and must be tracked down through the Guild or the Syndicate. **Flagged for DM attention:** the jewelry swing is large enough it can occasionally overshoot into first place — `14` has the math and a tuning dial if it does.
- **Soren Ash is gone.** The floor's appraiser is now the **Masked White Girl** — a different masked figure than the Tower's usual Masked Girl.

## The economy at a glance

- **Town Gold Pool: 2,400gp hard cap.** Every gp a player earns — from selling, quests, NPC trades, or graveyards — comes out of this pool. It never refills. See `01`.
- **NPC trading is a real, meaningful slice this time (~25%, ~600gp)** — not a footnote. Adult Women in particular are where Kazuo's jewelry does its damage. See `06`/`07`.
- Selling at your stall during the nightly Selling Phase is still the dominant way to earn — everything else feeds into that loop or supplements it.
