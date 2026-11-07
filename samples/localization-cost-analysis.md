# Localization Cost Analysis — Mechanism and Measurement

**Honesty note:** This document explains *why* controlled vocabulary reduces
translation cost and *how to measure* that reduction. It does not publish
vendor-specific figures, which depend on pricing tiers that change and rates
that don't transfer between organizations.

## Mechanism: How Vocabulary Control Becomes Money

Translation vendors price largely by fuzzy-match tiers. Uncontrolled
vocabulary destroys translation-memory leverage in two ways:

1. **Source drift creates new segments.** If "standby mode" becomes
   "power-saving mode" in one release, the sentence re-enters TM as new work
   at the lowest match tier.
2. **Render divergence poisons the memory.** The same source sentence with
   two different target renderings across releases guarantees future fuzzy
   matches instead of exact ones — for every locale simultaneously.

Controlled vocabulary attacks both: stable terms keep source segments stable,
and DNT discipline keeps target renderings stable.

## Cost Levers

| Lever | Controlled-vocabulary effect |
|-------|------------------------------|
| Exact TM matches | Stable source segments with stable term renderings → higher exact-match rate |
| Fuzzy matches | Fewer forced-new segments from synonym drift |
| Review cycles | In-market reviewers spend time on style, not adjudicating which of three words is "correct" |
| Error correction | One glossary fix propagates everywhere; no per-locale whack-a-mole |
| DNT discipline | Documentation and physical product labels stay synchronized; fewer defect tickets |

## How to Measure This in Your Organization

1. Pull two comparable releases from vendor invoicing: one before glossary
   enforcement, one after
2. Compare segment distribution across match tiers (new / fuzzy / exact)
3. Multiply the delta by your tier-rate differential
4. Control for content-volume change between releases, or normalize per
   segment

Organizations that run this comparison consistently find the largest lever is
exact-match rate — which is precisely what the
[segment strategy](../workflows/localization-handoff.md) protects.
