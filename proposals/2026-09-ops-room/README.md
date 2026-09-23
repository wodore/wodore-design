# Alpine Instrument Proposals — 2026-09 (Day & Night)

Standalone HTML demos implementing the approved design system
(`../DESIGN.md`, "The Alpine Instrument — Day & Night") on top of the
dual-agent critique findings (19/40 first run; snapshot in the frontend
repo `.impeccable/critique/`).

## Files

| File | Surface | Notes |
|---|---|---|
| `map-shell.html` | App shell: search, rail, map controls | Day default, toggle in the top bar; mobile collapse at ≤700px |
| `hut-detail.html` | Hut panel: hero, availability, weather, booking | Day default, toggle floats left of the panel |
| `day-night-sheet.html` | System sheet: palette, Barlow specimen, radii, components | Day and Night side by side, no toggle |
| `assets/` | Real captures from the running app (map canvas, hut hero) | — |

All three use: Barlow Semi Condensed (labels, headings, display,
wordmark) + Barlow (body); the 4/8/16 radius ramp; tonal depth without
shadows; theme-correct text shades per the Shade-Role table; ≥40px
controls and ≥62px availability pills.

## Demo theme behavior

The demos default to Day (light), per the approved theme decision: light
default, manual toggle, follow-system on first visit. The demo toggle is
manual-only (no system detection in a static file). The map backdrop is
the real light basemap capture; Night applies a pine scrim over it, which
is also the proposed treatment for a future dark basemap.

## Critique findings → proposal (carried over from v1, now dual-theme)

| Finding | Severity | Demo answer |
|---|---|---|
| Drawer abandons the dark system (bg-grey-3/4) | P0 | Replaced by the theme token layer: Day = day-panel on day-paper, Night = pine panel; one system, two lights |
| Side-tab borders in WdAccommodationDay (detector) | warning | Flat tonal day pills; status via text shade + 3px capacity bar |
| Icon-only 12-button rail | P1 | Three labeled clusters (Hütten / Aktivitäten / Transport), ≤4 each, 40px targets; mobile "Ebenen & Filter" bar |
| Booking hand-off without reassurance | P1 | Source card: provider, "ab CHF 45", availability echo, explicit exit framing ("wodo.re verlässt") |
| QA language + raw coordinates leaked | P2 | No review badge; GPS demoted to a copy action |
| Pin legend missing | P2 | Hütten cluster doubles as the pin legend (colored dots + counts) |
| Availability pills too small for gloves | P2 | 62px day pills, 40px months, all controls ≥40px |
| Generic wordmark font (Roboto) | — | Wordmark follows the family: Barlow Semi Condensed, black "wo" + gold "dore" (gold shade per theme) |
| Incoherent radius ramp (6/20) | — | 4/8/16 ramp with pills round |

## Binding (from PRODUCT.md / DESIGN.md)

Palette ramps (canonical `colors/wodore_palette.py`) plus the approved
daylight neutrals; monochrome charcoal logo mark + text wordmark; light
default with Night as first-class; warm-alpine voice (German master copy);
WCAG 2.1 AA (text shades verified per theme); external booking model.

## Not in these demos

Live map interaction, system-preference detection, i18n beyond German,
real booking links. Static proposals, not app code.
