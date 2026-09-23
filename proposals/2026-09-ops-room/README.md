# Ops Room Proposals — 2026-09

Standalone HTML demos responding to the dual-agent design critique
(19/40, first run — snapshot in the frontend repo under
`.impeccable/critique/2026-09-23T14-02-41Z__src-layouts-mainlayout-vue.md`).

Direction chosen by the product owner: **finish the Alpine Ops Room**
(dark system everywhere), hut detail stays **photo-first**.

## Files

| File | Surface | Open with |
|---|---|---|
| `map-shell.html` | App shell, map, search, rail, map controls | any browser (needs internet for Google Fonts) |
| `hut-detail.html` | Hut drawer/panel: hero, availability, weather, booking | any browser |
| `assets/` | Real captures from the running app (map canvas, hut hero, logo) | — |

Both demos share one token layer: night pine `#0a140f` page, pine panel
`#112119`, pine deep `#0e1b14`, forest green actions, glacier turquoise
information, gold as scarce instrument marks only, signal green/red reserved
for availability truth.

## Critique findings → proposal

| Finding | Severity | Demo answer |
|---|---|---|
| Drawer abandons the dark system (`bg-grey-3/4`) | P0 | Whole panel in pine tones; tonal layer steps instead of greys; gold only as 3px section ticks and the favorite heart |
| Side-tab borders in `WdAccommodationDay` (detector) | warning | Flat tonal day pills; status via color text + 3px capacity bar, no border stripes |
| Icon-only 12-button rail | P1 | Three labeled clusters (Hütten / Aktivitäten / Transport), ≤4 each, 40px targets, active states; collapses to one "Ebenen & Filter" bar on mobile |
| Booking hand-off without reassurance | P1 | Source card: provider name, "ab CHF 45", availability echo, explicit "Externe Buchung öffnen" + "wodo.re verlässt" exit framing; distinct secondary contact option |
| QA language + raw coordinates leaked | P2 | No review badge; coordinates demoted to footer "GPS kopieren" action |
| Pin legend missing | P2 | The Hütten cluster doubles as the pin legend (colored dots + counts), so filters and legend teach the same vocabulary |
| Availability pills too small for gloves | P2 | Day pills 62px tall, months 40px, all controls ≥40px |
| Search results dry | — | Result rows carry availability verdicts (FREI / 3 FREI / GESCHLOSSEN) and pin colors consistent with the legend |
| No invitation on first land | — | Bottom status line "Kartenansicht · 408 Hütten eingeblendet", `/` keyboard hint in the search field |
| Halo signature underused | — | Floating map label + hero briefing use the halo text-shadow |

## Deliberately kept (binding)

Palette, logo, dark map-centric character, Roboto Condensed/Roboto pairing,
6px/20px radii, no drop shadows, uppercase condensed control labels,
availability color monopoly. Typography, density, grouping, component
treatment are the proposal.

## Not in these demos

Live map interaction, i18n beyond German master copy, real booking links.
These are static proposals, not app code.
