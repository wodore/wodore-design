# Product

<!-- impeccable:product-schema 1 -->

> Provenance: rebuilt via guided init interview with the product owner,
> 2026-09-23. All fields below are confirmed unless marked otherwise.

## Platform

web

## Users

**Primary: alpine tour planners.** Hikers, climbers and ski-tourers planning
multi-day tours. They compare huts on the map, check live bed availability,
shortlist favorites and continue to booking via external deep links. Working
at the planning desk (desktop web) and on tour (installable PWA, mobile).

**Secondary: place explorers.** People browsing the map for interesting huts
and places without a fixed plan — discovery-minded visitors the design must
not alienate with planner-only density.

## Product Purpose

Wodore is a map-first web app to discover, evaluate and shortlist alpine
huts. Success is planning success: users find and favorite the right huts,
return during the season, and reach a booking. Bookings initiated at
external providers are the lagging outcome, not the primary measure.

## Positioning

Two pillars a neighbor could not truthfully copy together:

1. A living map whose hut availability aggregates across external booking
   services (SAC, HRS, and others via hut-services), with clearly framed
   deep links into booking.
2. Richer, better-curated hut data (photos, facilities, meta) than
   incumbent portals.

Geographic scope: the Alps today — architected and designed so any
mountain-hut region can be added without rework.

## Operating Context

- Planning happens beside other tools: topographic maps, weather services,
  tour planners — hence map layers, overlays and weather.
- On tour: the PWA is used outdoors — glare, gloves, unstable connections.
- UI languages: German (master copy), English, French, Italian; localized
  API data with fallback.
- Themes: light and dark, light as default; manual toggle plus follow-system
  on first visit, persisted like the language setting.
- Booking is external by design: Wodore is the planning and discovery layer;
  providers (SAC, HRS, ...) close the transaction.

## Capabilities and Constraints

- Place search across huts and other places (peaks, cable cars, regions).
- Interactive MapLibre map: basemaps, overlays, map styles; hut pins with
  availability-driven states.
- Hut detail: photos, facilities/meta, availability calendar, weather,
  booking entry via external deep links (in-app checkout is not a commitment).
- Favorites, feedback, support, contribute, data policy.
- Auth (Zitadel OIDC); Stripe present for payments where applicable.
- Constraints: Quasar (Vue 3) PWA component base; data shape owned by
  wodore-backend + hut-services.
- Offline-ready, not offline-first: cache-friendly patterns, nothing promised.
- Open (future direction, explicitly undecided): support finding a good
  tour in general, beyond single huts.

## Brand Commitments

- Logo: monochrome charcoal mark (`logo/wodore_logo_original.svg`,
  `#1c1c1c` on `#0a140f`) + wordmark "wo" (black) "dore" (accent gold),
  rendered as text; white mono variant (`favicon_mono_white`) for dark
  surfaces. Binding.
- Palette: wodore green (primary), turquoise (secondary), gold (accent) with
  100–900 ramps; canonical source `colors/wodore_palette.py`. Binding —
  including the approved adjustments: scalar/ramp realignment and the
  pine-tinted daylight neutrals recorded in DESIGN.md.
- Themes: light and dark are one system — "one instrument, two lighting
  conditions". Light default. Binding.
- Voice: warm alpine — inviting, a touch of mountain romance in
  marketing-adjacent copy — with precise, factual data language.
  German master copy.

## Evidence on Hand

- This repo: logo variants + exports, palette, product meta images, map and
  overlay assets.
- Frontend repo: design spec `docs/specs/wd_design.md`, feature specs,
  i18n copy, running app at https://wodo.re.
- Guided init interview, 2026-09-23 (this file's source).
- Absent (do not fabricate): testimonials, press, usage metrics.

## Product Principles

1. The map is the product — every element must earn space away from it.
2. Availability truth first: bed status is the primary signal; green and
   red belong to it exclusively.
3. Plan fast, decide deep: quick compare on the map, depth in the hut
   detail.
4. One instrument, two lighting conditions: daylight and night share
   character, labels and rules; both must survive glare and gloves.
5. Warm welcome, precise numbers: the voice is alpine and inviting, the
   data is exact.

## Accessibility & Inclusion

WCAG 2.1 AA is the formal target (text contrast 4.5:1, visible focus,
adequate target sizes). Outdoor realities — glare, gloves, unstable
networks — are treated as accessibility contexts, not edge cases.
