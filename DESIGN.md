---
name: Wodore
description: Map-first alpine hut discovery — one instrument, two lighting conditions
colors:
  forest-green: "#346751"
  forest-green-deep: "#224e3b"
  forest-green-ice: "#8fd6b7"
  glacier-turquoise: "#9dd9d2"
  glacier-turquoise-deep: "#29626b"
  meadow-gold: "#bfab25"
  meadow-gold-deep: "#846a15"
  meadow-gold-soft: "#e8c563"
  night-pine: "#0a140f"
  pine-panel: "#112119"
  pine-panel-deep: "#0e1b14"
  pine-ridge: "#1c3629"
  day-paper: "#f6f9f7"
  day-panel: "#fdfefd"
  day-ridge: "#dde7e0"
  day-ink: "#1c1c1c"
  paper-white: "#f2f7f4"
  ice-mint: "#a9f0d2"
  signal-green: "#25bf5e"
  signal-green-deep: "#198053"
  alpine-red: "#bf211e"
  alpine-red-soft: "#f2acab"
  glacier-blue: "#2673bf"
  glacier-blue-ice: "#abcff2"
  warning-coral: "#ff3c38"
  warning-coral-deep: "#e6000b"
  amber: "#db892a"
  amber-soft: "#f6ad4b"
  amber-deep: "#8a4b1b"
typography:
  display:
    fontFamily: "Barlow Semi Condensed, Barlow, -apple-system, Helvetica Neue, sans-serif"
    fontSize: "3.75rem"
    fontWeight: 300
    lineHeight: "3.75rem"
    letterSpacing: "-0.00833em"
  headline:
    fontFamily: "Barlow Semi Condensed, Barlow, -apple-system, Helvetica Neue, sans-serif"
    fontSize: "2.125rem"
    fontWeight: 400
    lineHeight: "2.5rem"
  title:
    fontFamily: "Barlow Semi Condensed, Barlow, -apple-system, Helvetica Neue, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 500
    lineHeight: "2rem"
    letterSpacing: "0.0125em"
  body:
    fontFamily: "Barlow, -apple-system, Helvetica Neue, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: "1.5rem"
    letterSpacing: "0.03125em"
  label:
    fontFamily: "Barlow Semi Condensed, Barlow, -apple-system, Helvetica Neue, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 500
    lineHeight: "2rem"
    letterSpacing: "0.16667em"
rounded:
  control: "4px"
  card: "8px"
  dialog: "16px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
components:
  button-primary:
    backgroundColor: "{colors.forest-green}"
    textColor: "{colors.paper-white}"
    rounded: "{rounded.control}"
    typography: "{typography.label}"
  button-primary-hover:
    backgroundColor: "{colors.forest-green-deep}"
  card-surface-day:
    backgroundColor: "{colors.day-panel}"
    textColor: "{colors.day-ink}"
    rounded: "{rounded.card}"
  card-surface-night:
    backgroundColor: "{colors.pine-panel}"
    textColor: "{colors.paper-white}"
    rounded: "{rounded.card}"
---

# Design System: Wodore

> Scan-mode record of the incumbent frontend (wodore-frontend-quasar),
> rebuilt 2026-09-23 after the guided product init. Dual-theme architecture
> approved by the product owner; daylight neutrals are the approved palette
> extension. Night tokens document the incumbent dark surfaces; day tokens
> formalize the light mode the app actually ships today.

## Overview

**Creative North Star: "The Alpine Instrument — Day & Night"**

Wodore's UI is a field instrument for the mountains: the map is the primary
instrument, every control is a low-glare, high-legibility instrument
reading, and the whole system lives in two lighting conditions of the same
character. **Day** is warm paper: pine-tinted light surfaces, charcoal ink
(the logo mark's own black-500), forest green actions, deep gold accents —
readable in sunlight and glare. **Night** is the pine darkroom: night-pine
page, pine panels, ice tones for information — kind to dark-adapted eyes in
a hut dorm at 5am. Same labels, same geometry, same rules; only the light
changes.

The instrument character comes from Barlow Semi Condensed uppercase labels,
the 4/8/16 radius ramp, tonal (never shadow) depth, and the halo that
keeps readings legible over map imagery in both conditions. Green and red
are not decoration: they are
the availability truth, the product's core signal, in every lighting
condition.

**Key Characteristics:**

- Two themes, one character: Day (default) and Night share tokens, labels,
  geometry and rules
- The map is the canvas; chrome floats over it in compact panels
- Green is identity and action; turquoise is orientation; gold is scarce —
  a beam, never a wash
- Availability green/red have a semantic monopoly
- Condensed uppercase instrument labels (Barlow Semi Condensed); Barlow
  body for content
- Tonal layering only — no drop shadows; radius ramp 4/8/16 (controls /
  panels / dialogs), pills round
- Halo text-shadow on anything sitting directly over imagery

## Colors

Brand ramps (100–900) are canonical in `colors/wodore_palette.py` and
mirrored in the frontend `quasar.variables.scss`. One approved alignment is
pending in code: the scalar overrides `$positive`, `$info`, `$black` must
match their ramp-500 values (#25bf5e, #2673bf, #1c1c1c) — the ramps win.

### The Shade-Role Rule (dual theme)

| Role | Day (light) | Night (dark) |
|---|---|---|
| Page background | day-paper #f6f9f7 | night-pine #0a140f |
| Panels / cards | day-panel #fdfefd | pine-panel #112119 (deep #0e1b14) |
| Borders / ridges | day-ridge #dde7e0 | pine-ridge #1c3629 |
| Body text | day-ink #1c1c1c | paper-white #f2f7f4 |
| Brand fills (buttons, active) | forest-green #346751 (both themes) |
| Information / links text | glacier-turquoise-deep #29626b | glacier-turquoise #9dd9d2 |
| Gold accent text | meadow-gold-deep #846a15 | meadow-gold #bfab25 |
| Availability text | signal-green-deep #198053 | signal-green #25bf5e |
| Closed / error text | alpine-red #bf211e (passes on light) | alpine-red-soft #f2acab |
| Info text | glacier-blue #2673bf | glacier-blue-ice #abcff2 |
| Warning text | warning-coral-deep #e6000b | warning-coral #ff3c38 |

**Fills keep their 500 shade in both themes; text picks the shade that
passes WCAG AA (4.5:1) on its surface — deep shades on Day, ice shades on
Night.** Every value above already exists in the ramps except the four
daylight neutrals below.

### Availability / Occupancy Scale (new, approved)

One palette-native scale for map pins, drawer badges, icons and month
tiles. The middle steps use the new amber ramp (hue between brand gold
and warning coral, chroma matched to the family); anchors stay on the
existing positive/negative ramps.

**Amber ramp (100–900):** #ffd582 · #ffc064 · #f6ad4b · #ea9a37 ·
#db892a · #c3731f · #a95f1c · #8a4b1b · #69391c

| State | Fill (both themes) | Day text | Night text |
|---|---|---|---|
| free | positive-500 #25bf5e | positive-800 #198053 (4.9) | positive-500 #25bf5e (6.9) |
| free_unknown | positive-300 #50dd96 | positive-800 #198053 (4.9) | positive-300 #50dd96 (9.7) |
| low | amber-300 #f6ad4b | amber-800 #8a4b1b (6.7) | amber-300 #f6ad4b (8.8) |
| medium | amber-500 #db892a | amber-800 #8a4b1b (6.7) | amber-300 #f6ad4b (8.8) |
| high | amber-700 #a95f1c | amber-800 #8a4b1b (6.7) | amber-200 #ffc064 (10.3) |
| full | negative-500 #bf211e | negative-500 #bf211e (6.0) | negative-100 #f2acab (9.0) |
| unknown | black-100 #575757 | black-100 #575757 (7.2) | white-600 #fcfcfc (16.3) |

All ratios WCAG AA-verified. Hue carries the traffic reading (green →
amber → red); lightness steps the severity inside amber; every state also
carries a count, label or icon shape, never color alone.

Pending code alignment (implementation phase): map pin ramp in
`src/stores/map/utils/overlay-huts.ts` (currently Material hexes
#33FF33/#99CC33/#FFA726/#E09321/#EF6C00/#D32F2F + #3366ff fallback →
info-500), drawer badges in `WdAccommodationDay.vue` (#87b52d/#779F28/…),
`src/css/months.scss` pastels, and the occupation icon SVGs' #e16f07.

### Primary
- **Forest Green** (#346751): brand actions, active states, primary
  buttons — both themes. Hover deepens to #224e3b. Never text on Night
  panels (2.55:1); Night text uses forest-green-ice #8fd6b7 (9.9:1).

### Secondary
- **Glacier Turquoise** (#9dd9d2 fill / #9dd9d2 Day-fail as text):
  orientation and information — links, meta, type chips, selected states.
  Day text: glacier-turquoise-deep #29626b (6.9:1). Night text: 500
  (10.6:1 on pine).
- **Ice Mint** (#a9f0d2): icon tint and glyph color, strongest on Night.

### Tertiary
- **Meadow Gold** (#bfab25): scarce emphasis — link underlines (dotted,
  800 at rest, 300 on hover), the favorite heart, small instrument ticks.
  Day text: meadow-gold-deep #846a15 (5.2:1) or 900 #6f5610 (7.0:1).
- **Signal Green** (#25bf5e) / **Alpine Red** (#bf211e): availability
  semantics only. Day text: signal-green-deep #198053 (4.9:1). Night
  closed-text: alpine-red-soft #f2acab (9.0:1).
- **Glacier Blue** (#2673bf) information; **Warning Coral** (#ff3c38)
  alerts (Day text: #e6000b, 4.8:1).

### Neutral
- **Day** (new, approved): day-paper #f6f9f7 page, day-panel #fdfefd
  raised surfaces, day-ridge #dde7e0 borders, day-ink #1c1c1c text.
  Pine-tinted rather than pure white: daylight mode carries the brand
  instead of reading as a generic white app. day-ink deliberately equals
  black-500 — the logo mark's own charcoal — tying chrome to identity.
- **Night**: night-pine #0a140f page, pine-panel #112119 /
  pine-panel-deep #0e1b14 surfaces, pine-ridge #315e47 tonal steps.
- **Paper White** #f2f7f4: Night body text. **Charcoal** #1c1c1c: Day body
  text.

### Named Rules
**The Head-Torch Rule.** Gold is a beam, not a wash. If gold covers more
than a few percent of any surface, the design has lost the night — or
washed out the day. Amber is data, not brand: the availability scale owns
the amber ramp; brand gold never carries availability meaning.

**The Availability Rule.** The occupancy scale — free, low, medium, high,
full, unknown, free_unknown — is the product's core signal and owns its
colors exclusively. Never spend green, amber or red on decoration, and
never show a state by color alone: pair it with a count, label or icon
shape (color-blind safety).

**The Two-Lights Rule.** Every surface, text and state token is defined for
Day and Night together. A component that only works in one lighting
condition is not done. Light is the default; Night follows the system
preference until the user chooses.

## Typography

**Display/Label Font:** Barlow Semi Condensed (fallback Barlow, system sans)
**Body Font:** Barlow (fallback system sans)

**Character:** Barlow is drawn from public signage and utility lettering —
instrument DNA by birth — with a slightly rounded warmth that carries the
alpine voice. One family, two widths: Semi Condensed speaks in the
engraved-label voice (display, headings, uppercase controls, chips,
numerals in tables), regular Barlow keeps prose neutral and
outdoor-legible. Replaces Roboto/Roboto Condensed (the generic-Android
pairing) throughout, self-hosted via Fontsource exactly like today.

**Wordmark:** the "wo" + "dore" text wordmark follows the family — black
"wo", gold "dore", Semi Condensed — beside the monochrome charcoal mark.

### Hierarchy
- **Display** (300, 3.75rem/3.75rem, -0.008em): rare; hero moments only.
- **Headline** (400, 2.125rem/2.5rem): page and dialog titles.
- **Title** (500, 1.25rem/2rem): card and section titles.
- **Body** (400, 1rem/1.5rem): running text.
- **Label** (500, 0.75rem/2rem, +0.167em, uppercase): buttons, chips,
  toolbar, overlines — the workhorse of the instrument character.

### Named Rules
**The Instrument Label Rule.** Interactive controls speak in condensed
uppercase labels (+0.167em tracking). Sentence case is for content, not
controls.

## Layout

Map-first single canvas: the MapLibre map fills the viewport, chrome
floats over it. Desktop: left search card (440px), floating toolbar,
right-side drawer for hut detail (140ms ease-out slide). Mobile: the same
elements collapse to full-screen dialogs and sheets. Breakpoints: xs
<600px, sm <769px, md <1439px, lg <1919px. Spacing follows Quasar's 4px
gutter scale (8/16/24px). Controls target ≥40px; availability pills ≥60px
(gloves).

## Elevation & Depth

No shadow vocabulary in either theme: depth is tonal layering. Day:
day-paper → day-panel, separated by day-ridge hairlines. Night: night-pine
→ pine-panel → pine-panel-deep, with pine-ridge tonal steps. Dialogs and
sheets get the only "lift" cue via the 20px radius.

### Named Rules
**The Tonal Layer Rule.** To raise a surface, step the tone; do not add
drop shadows — in either lighting condition.

## Shapes

Compact instrument geometry on a disciplined radius ramp: **4px** controls,
chips, inputs and menus; **8px** cards and panels; **16px** dialogs and
sheets; pills and map markers fully round. Icons are line-based (Eva-style,
2px stroke) plus the custom `wd-` set; the logo mark is monochrome
charcoal with a white mono variant for Night surfaces.

## Components

### Buttons
- **Shape:** 6px radius, min-height 2.572em (≥40px targets), uppercase
  condensed label.
- **Primary:** Forest Green fill, paper-white label — both themes.
- **Hover / Focus:** deepen to forest-green-deep; focus ring glacier
  turquoise (deep on Day).
- **Toolbar / Ghost:** transparent flat icon buttons; hover wash
  rgba(black, 0.06) on Day, rgba(white, 0.1) on Night.

### Chips
- **Hut type / meta:** tonal panel fill, information-turquoise text (deep
  on Day), 6px radius. Availability chips speak in signal green/red with
  theme-correct text shades.

### Cards / Containers
- **Corner Style:** 6px (dialogs 20px).
- **Background:** day-panel / pine-panel over the map.
- **Shadow Strategy:** none — tonal separation from the map canvas.
- **Internal Padding:** Quasar gutter steps (8/16/24px).

### Inputs / Fields
- **Style:** filled fields on panel surfaces, 6px radius; Day fields are
  day-panel with day-ridge borders.
- **Focus:** turquoise emphasis; icon-fields take the hover wash; disabled
  at 0.4 opacity.

### Navigation
- Floating compact toolbar over the map; flat round icon buttons; grouped
  and labeled clusters (Hütten / Aktivitäten / Transport), ≤4 per cluster.

### Signature: Map Label Halo
`.text-<c>--halo` (text-shadow: 0 0 4px rgba(color-700, 0.7)) keeps labels
and numbers legible over any map imagery in both themes — the system's
most distinctive utility. Over light imagery the halo uses the dark 700
shade; over dark imagery the same rule holds.

### Signature: The Briefing Header
Elevation + current weather inline with the hut name (▲ 2731 m · ☀ Sonne,
10°) — the at-a-glance go/no-go read that opens every hut panel.

## Do's and Don'ts

### Do:
- **Do** define every surface, text and state for Day and Night together;
  light is default, Night follows system then choice.
- **Do** keep the map dominant; chrome floats in compact edge panels.
- **Do** use the halo for any text over map imagery, both themes.
- **Do** step tones (paper→panel / pine→panel) for hierarchy, never
  shadows.
- **Do** keep controls uppercase condensed; content sentence case.
- **Do** pick text shades by the Shade-Role table; verify 4.5:1 in the
  theme you are styling.

### Don't:
- **Don't** use 500 gold, turquoise, green or coral as text on Day
  surfaces — they fail AA; use the deep (700–900) shades.
- **Don't** use forest-green-500, alpine-red-500 or glacier-blue-500 as
  text on Night panels — use the 100/ice shades.
- **Don't** introduce drop shadows, side-strip borders, or gradients as
  depth in either theme.
- **Don't** spend gold or the availability colors on decoration.
- **Don't** mix off-ramp radii: 4px controls, 8px panels, 16px dialogs;
  pills round. Nothing else.
- **Don't** ship a component in only one theme — that includes demos and
  proposals.
