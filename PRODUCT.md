# Product

<!-- impeccable:product-schema 1 -->

> Provenance note: this record was initialized by an agent from repository
> evidence (frontend code + specs, wodore-design assets) on 2025-09-23. Facts
> marked *(inferred)* were not explicitly confirmed by the product owner;
> confirm or correct them in a later `init` round.

## Platform

web

## Users

Primary *(inferred)*: alpine tour planners — hikers, climbers and ski-tourers
planning multi-day tours in the Alps. They research huts on a map, compare
options, check live bed availability, favorite candidates and continue to
booking. Used both at the planning desk (desktop web) and on the go
(installable PWA, mobile). German-first audience (Swiss reality: de / fr / it,
plus en).

## Product Purpose

Wodore (wodo.re) is a map-first web app to discover, evaluate and book alpine
huts. Success means: a user finds the right hut for their tour, trusts its
availability information, and reaches a booking.

## Positioning

*(inferred)* One living map over alpine huts whose availability is aggregated
across external booking services (SAC, HRS, and others via hut-services),
with deep links into booking. Neighboring portals are list-first or bound to
a single operator's inventory.

## Operating Context

- Planning happens next to other tools: topographic maps, weather services,
  tour planners. The app therefore leans on map layers, overlays and
  weather *(inferred)*.
- On tour, the PWA is used outdoors: glare, gloves, unstable connections.
- UI languages: German (master copy), English, French, Italian; localized
  API data with fallback.
- Auth (Zitadel OIDC) unlocks favorites and contribution features; payments
  run through Stripe.

## Capabilities and Constraints

- Place search across huts and other places (peaks, cable cars, regions),
  min. 2 characters, debounced, keyboard-navigable.
- Interactive MapLibre map with selectable basemaps, overlays and map styles;
  hut pins with availability-driven states.
- Hut detail view: photos, facilities/meta, availability calendar, booking
  entry (external booking services; some huts have no online booking).
- Favorites, feedback, support, contribute and data-policy flows.
- Constraints: Quasar component base (Vue 3, PWA build), data shape owned by
  wodore-backend + hut-services libraries, dark theme incumbent.
- Open product facts: none recorded yet.

## Brand Commitments

- Logo: variants maintained in this repo (`logo/`), incl. favicon set and
  banner. Binding.
- Palette: wodore green (primary), turquoise (secondary), gold (accent) with
  100–900 shades (`colors/wodore_palette.py`, mirrored in the frontend
  `quasar.variables.scss`). Binding.
- Dark, map-centric product character *(inferred binding)*: the UI recedes
  behind the map; typography, layout, density and component treatment are
  open to evolution.
- Voice *(inferred)*: factual, compact, outdoor-practical; German master copy.

## Evidence on Hand

- This repo: logo variants and exports, color palette (GPL palette + script),
  product meta images (`meta/`), product icons (`products/`), map assets.
- Frontend repo: design spec `docs/specs/wd_design.md`, feature specs
  (`wd_place_search.md`, `wd_design_place_details.md`, `wd_image_viewer.md`),
  i18n copy (`src/i18n/locales/`), Histoire stories (`stories/`), running app
  at https://wodo.re.
- Absent (do not fabricate): testimonials, press, usage metrics, customer
  references.

## Product Principles

1. The map is the product — every UI element must earn space away from it.
2. Availability truth first: bed status is the primary signal, never
   decoration.
3. Plan fast, decide deep: quick compare on the map, depth in the hut detail.
4. Outdoor-robust over decorative: legible in glare, usable with gloves,
   stable on weak connections.
5. Swiss multilingual reality is the default, not an afterthought.
