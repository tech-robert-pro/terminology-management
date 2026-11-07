# Before / After — The Effect of Terminology Control

## Before (2022, pre-glossary)

Excerpt reconstructed from three product-line manuals written the same year
by the same team:

> **Quick start guide:** "Press the MENU key to open the settings menu."
> **User guide:** "Use the onscreen menu to adjust the image."
> **Install guide:** "Access the OSD control panel via the function button."

Three features behaved identically; three documents described them with three
different nouns — none of which matched the label printed on the hardware
("Hotkey"). Consequences observed at the time:

- Support macros couldn't reliably keyword-search tickets
- Translators invented per-locale renderings for each variant, fragmenting
  the translation memory
- QA checklists had no stable vocabulary to check *against*

## After (current)

> "Press the **hotkey** to open the **on-screen display (OSD)**."

One rendering, one term, everywhere — bound to the physical bezel label,
flagged DNT, and enforceable by script:

$ python tooling/term_validator.py --rules tooling/rules.json --path . Validating against: glossaries/approved-terms.md v4.2 No terminology violations found.


## The Diff

| Aspect | Before | After |
|--------|--------|-------|
| Names for the menu system in live docs | 3 (+ translator inventions) | 1 |
| Vocabulary governance | Unmanaged list of ~200 overlapping entries | 84 curated master entries + line supplements |
| Forbidden synonyms detectable by script | None | Every pattern in `rules.json` |
| Translator onboarding for a product line | Self-taught | One glossary + one DNT list |

## Why This Is Hard Without a System

Terminology drift is not a discipline problem — it's a systems problem.
Individual writers choose reasonable words every time. Drift emerges from the
accumulation of reasonable choices made independently. The fix is not "try
harder"; it is a single decision point (the approval pipeline), a
machine-checkable contract (the glossary + validator), and a retirement
register (deprecated terms) so old content stays interpretable.
