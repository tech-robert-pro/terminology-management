# Deprecated Terms — Retirement Register

**Rule:** Deprecated terms are never silently deleted. Each carries a
replacement, a retirement date, and a migration note, so that:

1. Legacy manuals and support records remain interpretable
2. The [validator](../tooling/term_validator.py) can still flag occurrences
3. Translators know what to do when they encounter one in legacy content

| Deprecated term | Replaced by | Deprecated | Reason | Migration note |
|-----------------|-------------|------------|--------|----------------|
| monitor | display | 2023-03 | Vocabulary consolidation across product lines | Allowed in pre-2023 manuals only; flagged in new content |
| onscreen menu | on-screen display | 2022-08 | Three competing spellings existed across locales | zh-TW translations already used the target term |
| AC adapter | power adapter | 2024-01 | Supplier packaging standardization | Update shipping inserts at next reprint |
| sleep mode | standby mode | 2024-06 | "Sleep" implies a user-invoked OS state | Update support macros at next release |
| PC audio-in | audio input | 2025-02 | Label changed on production bezels | Bezel and doc changed simultaneously, release 2.1 |
| lamp hours | light source hours | 2025-05 | Product range spans lamp, LED, and laser light sources | Projector-line docs migrated in release 3.0 |

## Case Study: "sleep mode" → "standby mode"

"Sleep mode" generated recurring support confusion because Windows and macOS
both define "sleep" as an OS-level state. Users entering OS sleep believed
the display's standby behavior was faulty; support ticket review repeatedly
attributed display-state complaints to this ambiguity.

Resolution: controlled-vocabulary change plus a migration map delivered to
localization, so all locale variants switched in the same release. Total
migration time: one release cycle (6 weeks).

## Adding an Entry to This Register

Deprecation follows the same [approval process](../workflows/approval-process.md)
as addition — the resolution stage simply outputs a retirement instead of an
approval. An entry here is authoritative: the validator's rule file is
generated from it, so the register, the rules, and the CSV can never
disagree.
