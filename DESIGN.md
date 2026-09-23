---
name: Wodore
description: Dark, map-first alpine hut discovery and booking surface
colors:
  forest-green: "#346751"
  forest-green-deep: "#224e3b"
  glacier-turquoise: "#9dd9d2"
  glacier-turquoise-deep: "#3f9da2"
  meadow-gold: "#bfab25"
  meadow-gold-soft: "#e8c563"
  night-pine: "#0a140f"
  pine-panel: "#112119"
  pine-panel-deep: "#0e1b14"
  pine-ridge: "#315e47"
  ice-mint: "#a9f0d2"
  signal-green: "#25c15e"
  alpine-red: "#bf211e"
  glacier-blue: "#2673bf"
  warning-coral: "#ff3c38"
  paper-white: "#ffffff"
  charcoal: "#1c1c1c"
typography:
  display:
    fontFamily: "Roboto Condensed, Roboto, -apple-system, Helvetica Neue, sans-serif"
    fontSize: "3.75rem"
    fontWeight: 300
    lineHeight: "3.75rem"
    letterSpacing: "-0.00833em"
  headline:
    fontFamily: "Roboto Condensed, Roboto, -apple-system, Helvetica Neue, sans-serif"
    fontSize: "2.125rem"
    fontWeight: 400
    lineHeight: "2.5rem"
  title:
    fontFamily: "Roboto Condensed, Roboto, -apple-system, Helvetica Neue, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 500
    lineHeight: "2rem"
    letterSpacing: "0.0125em"
  body:
    fontFamily: "Roboto, -apple-system, Helvetica Neue, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: "1.5rem"
    letterSpacing: "0.03125em"
  label:
    fontFamily: "Roboto Condensed, Roboto, -apple-system, Helvetica Neue, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 500
    lineHeight: "2rem"
    letterSpacing: "0.16667em"
rounded:
  base: "6px"
  dialog: "20px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
components:
  button-primary:
    backgroundColor: "{colors.forest-green}"
    textColor: "{colors.paper-white}"
    rounded: "{rounded.base}"
    typography: "{typography.label}"
  button-primary-hover:
    backgroundColor: "{colors.forest-green-deep}"
  toolbar-button:
    backgroundColor: "transparent"
    textColor: "{colors.paper-white}"
  chip-hut-type:
    backgroundColor: "{colors.pine-panel}"
    textColor: "{colors.glacier-turquoise}"
    rounded: "{rounded.base}"
  card-surface:
    backgroundColor: "{colors.pine-panel}"
    textColor: "{colors.paper-white}"
    rounded: "{rounded.base}"
---

# Design System: Wodore

> Scan-mode record of the incumbent frontend (wodore-frontend-quasar),
> extracted 2025-09-23. North Star and atmosphere language are agent-proposed
> (user declined the language round); confirm or rework via `/impeccable document`.

## Overview

**Creative North Star: "The Alpine Ops Room"**

Wodore's UI is a night-vision instrument panel for the mountains: a dark pine
surface on which the map is the primary instrument and every control is a
low-glare, high-legibility instrument reading. The palette comes straight from
the alpine night: deep pine and pine-panel surfaces, a restrained forest green
as the brand voice, glacier turquoise for orientation and information, and a
rare gold accent that behaves like a head-torch beam: small, warm, pointed.

Density is compact and operational. Roboto Condensed, uppercase labels and
6px corners give controls a field-instrument feel rather than a consumer-app
feel. Depth comes from tonal layering of the pine surfaces and the map
itself, not from shadows.

**Key Characteristics:**

- Dark-first: page background Night Pine (#0a140f), panels Pine Panel (#112119)
- Map is the canvas; chrome floats over it in compact panels
- Green is identity, turquoise is orientation, gold is scarce emphasis
- Condensed uppercase labels; generous Roboto body
- Flat tonal surfaces, 6px corners, 20px only for dialogs
- Halo text-shadow keeps labels legible over map imagery

## Colors

The palette is a green-dominant alpine night scheme with cool turquoise
information hues; every color exists in 100–900 ramps (source:
`quasar.variables.scss`, mirrored in this repo's `colors/`).

### Primary
- **Forest Green** (#346751): brand actions, active states, primary buttons.
  The quiet center of the system; used sparingly enough to stay meaningful.
- **Forest Green Deep** (#224e3b): hover/pressed extension of the brand.

### Secondary
- **Glacier Turquoise** (#9dd9d2): orientation and information: links,
  meta text, type chips, selected overlays. Cooler and quieter than the
  brand green.
- **Ice Mint** (#a9f0d2): icon tint (`icon` token), map control glyphs.

### Tertiary
- **Meadow Gold** (#bfab25, soft #e8c563): scarce emphasis only: link
  underlines (dotted, 800 shade at rest, 300 on hover), highlights.
- **Signal Green** (#25c15e) / **Alpine Red** (#bf211e): availability
  semantics (open/closed, beds). The product's core data signal.
- **Glacier Blue** (#2673bf): information; **Warning Coral** (#ff3c38): alerts.

### Neutral
- **Night Pine** (#0a140f): page background behind the map.
- **Pine Panel** (#112119) / **Pine Panel Deep** (#0e1b14): surfaces, cards,
  drawers; **Pine Ridge** (#315e47): tonal ridge between layers.
- **Paper White** (#ffffff): primary text on dark. **Charcoal** (#1c1c1c):
  text on light surfaces.

### Named Rules
**The Head-Torch Rule.** Gold is a beam, not a wash: link underlines and
small highlights only. If gold covers more than a few percent of a surface,
the design has lost the night.

**The Availability Rule.** Signal green and alpine red belong to bed/availability
truth. Never spend them on decoration; a green button that doesn't mean
"available" dilutes the product's core signal.

## Typography

**Display Font:** Roboto Condensed (fallback Roboto, system sans)
**Body Font:** Roboto (fallback system sans)

**Character:** Condensed caps and near-light display weights read like
engraved instrument labels; the regular Roboto body keeps prose neutral and
outdoor-legible. It is a utility pairing, deliberately not editorial.

### Hierarchy
- **Display** (300, 3.75rem/3.75rem, -0.008em): rare; hero moments only.
- **Headline** (400, 2.125rem/2.5rem): page and dialog titles.
- **Title** (500, 1.25rem/2rem): card and section titles.
- **Body** (400, 1rem/1.5rem): running text.
- **Label** (500, 0.75rem/2rem, +0.167em, uppercase): buttons, chips,
  toolbar, overlines. The workhorse of the instrument character.

### Named Rules
**The Instrument Label Rule.** Interactive controls speak in condensed
uppercase labels (+0.167em tracking). Sentence case is for content, not
controls.

## Layout

Map-first single-canvas architecture: the MapLibre map fills the viewport;
chrome floats over it. Desktop: left-aligned search card (440px), floating
toolbar, right-side content drawer for hut detail (drawer slides in 140ms
ease-out). Mobile: the same elements collapse to full-screen dialogs (search
dialog 100vw × 100vh, content as bottom sheet/dialog). Breakpoints:
xs < 600px, sm < 769px, md < 1439px, lg < 1919px. Spacing follows Quasar's
4px gutter scale (8/16/24px steps).

## Elevation & Depth

No shadow vocabulary: depth is tonal layering. Night Pine page → Pine Panel
surfaces → Pine Ridge borders/tonal steps; floating chrome may use blur
backdrops over the map. Dialogs get the only "lift" cue via the 20px radius.

### Named Rules
**The Tonal Layer Rule.** To raise a surface, step the pine tone; do not
add drop shadows.

## Shapes

Compact instrument geometry: 6px base radius on controls, cards, menus;
20px reserved for dialogs and sheets. Icons are line-based Eva-style (Eva
Icons) plus the custom `wd-` set; map glyphs favor outline over fill.

## Components

### Buttons
- **Shape:** 6px radius, min-height 2.572em, uppercase condensed label.
- **Primary:** Forest Green fill, white label.
- **Hover / Focus:** deepened green (700); toolbar buttons take a
  rgba(255,255,255,0.1) wash.
- **Toolbar / Ghost:** transparent flat icon buttons (round dense), white
  glyphs; active opacity 0.7 on press.

### Chips
- **Hut type / meta chips:** Pine Panel fill, glacier turquoise text, 6px
  radius, condensed label. Availability chips speak in signal green/red.

### Cards / Containers
- **Corner Style:** 6px (dialogs 20px).
- **Background:** Pine Panel (#112119) or Deep (#0e1b14) over the map.
- **Shadow Strategy:** none; tonal separation from the map canvas.
- **Internal Padding:** Quasar gutter steps (8/16/24px).

### Inputs / Fields
- **Style:** dark filled fields on panel surfaces, 6px radius.
- **Focus:** turquoise-tinted emphasis; `.wd-input-button` icon fields take a
  white 10% wash on hover, 0.4 opacity when disabled.

### Navigation
- **Style:** floating compact toolbar over the map; flat round icon buttons;
  condensed uppercase labels where text appears.

### Signature: Map Label Halo
`.text-<c>--halo` (text-shadow: 0 0 4px rgba(color-700, 0.7)) keeps labels
and numbers legible over any map imagery; the system's most distinctive
utility.

## Do's and Don'ts

### Do:
- **Do** keep the map as the dominant surface; chrome floats in compact
  panels at the edges.
- **Do** use the halo effect for any text that sits directly on map imagery.
- **Do** step pine tones (Night Pine → Panel → Deep) to express hierarchy.
- **Do** keep controls uppercase condensed; content sentence case.
- **Do** respect the 100–900 ramps; pick existing shades over inventing
  new values.

### Don't:
- **Don't** introduce drop shadows for elevation; the system is tonal.
- **Don't** spend gold or the availability green/red on decoration.
- **Don't** exceed 6px radius outside dialogs/sheets (20px).
- **Don't** place large light surfaces over the map without a tonal bridge.
