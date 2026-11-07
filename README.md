# Terminology Management

> Controlled vocabulary system for hardware documentation: standardized glossaries and terminology conventions across monitor, projector, and display product lines. Reduces translation costs and support friction.

![Status](https://img.shields.io/badge/status-maintained-brightgreen)
![Localization](https://img.shields.io/badge/localization-ready-blue)

---

## Overview

Terminology drift is the silent killer of documentation quality. When the same feature gets three different names across product lines, customers get confused, translators charge more, and support tickets multiply. This repository holds the controlled vocabulary framework that eliminated that problem for 900+ user manuals over 8 years.

**At a glance:**

| Attribute | Detail |
| :--- | :--- |
| **Role** | Sole author and maintainer |
| **Duration** | Over 8 years of continuous maintenance |
| **Scope** | Multi-product glossaries, term approval workflows, localization handoff procedures |
| **Product Categories** | Monitors, projectors, large-format displays |
| **Status** | Active |

---

## What's Inside

```
/
├── README.md                     # This file
├── glossaries/
│   ├── master-terminology.xlsx   # Controlled vocabulary spreadsheet
│   ├── approved-terms.md         # Approved terminology list
│   └── deprecated-terms.md       # Retired terms with migration notes
├── workflows/
│   ├── term-submission-form.md   # Template for requesting new terms
│   ├── approval-process.md       # How new terms get vetted
│   └── localization-handoff.md   # Glossary export for translators
├── style-guide/
│   ├── voice-and-tone.md         # Writing conventions
│   ├── grammar-rules.md          # Syntax standards
│   └── capitalization-guidelines.md
├── product-specific/
│   ├── monitor-terminology.md    # Monitor product glossary
│   ├── projector-terminology.md  # Projector product glossary
│   └── large-format-terminology.md
└── samples/
    ├── before-after-example.md   # Shows impact of terminology control
    └── localization-cost-analysis.md
```
---

## Background

Before this system existed, terminology inconsistency created cascading problems:

- **Translation inflation**: Translators charged extra for inconsistent source text, since they couldn't reuse translated segments when the same concept had different names.
- **Customer confusion**: Identical features had different names across product lines (e.g., "On-Screen Display" vs. "OSD Menu" vs. "Screen Menu").
- **Support overhead**: Support teams answered the same questions repeatedly because users couldn't find information using inconsistent terminology.
- **Review friction**: Review cycles stalled on semantic debates rather than technical accuracy.

The constraint shaping the solution was straightforward: **one writer maintaining terminology across three hardware categories, no dedicated localization team, and no enterprise terminology management software budget.** Whatever I built had to be manual but scalable.

---

## Approach

Three decisions drove the design.

**1. Master glossary as single source of truth.**
All terminology converged on a central spreadsheet rather than scattered Word documents or InDesign comments. Writers consulted the master before drafting; reviewers checked it during QA. 

**2. Product-specific sub-glossaries for edge cases.**
While 80% of terminology overlapped across monitors, projectors, and displays, the remaining 20% was highly domain-specific. Instead of bloating the master glossary with exceptions, I created product-specific supplements that referenced back to the master. 

**3. Localization-first design.**
Glossaries were structured for translator consumption, not just writer reference. Each entry included definition, context examples, and forbidden alternatives. 

---

## Outcome

- Eliminated **term drift across three product lines** by centralizing vocabulary in a single master glossary.
- Reduced **translation review cycles** by providing translators with approved term lists upfront.
- Standardized **100+ key technical terms** that appeared consistently across 900+ user manuals.
- Enabled **reusable translation memory segments** that lowered localization costs.

---

## Notes & Limitations

**Sanitized content.** Term definitions and examples have been stripped of brand identifiers and proprietary specifications. The methodology and workflow structure are intact; specific product terminology has been generalized.

**Manual process.** This system predates enterprise terminology management platforms. It works because of discipline, not automation. 

**No automated enforcement.** Writers could theoretically ignore the glossary and no system would catch it. Compliance relied on reviewer vigilance, not technical constraints. This worked when I was the primary reviewer; scaling beyond one writer would require enforcement mechanisms.

**What I'd do differently.** Given another pass, I'd implement lightweight automated term checking in the writing workflow.

---

## Related Projects

- [Portfolio and case study](https://tech-robert-pro.github.io)
- [Hardware manual samples](https://github.com/tech-robert-pro/hardware-manual-samples)
- [Documentation wiki](https://github.com/tech-robert-pro/wiki-project)
- [LLM automation tools](https://github.com/tech-robert-pro/llm-tool-examples)

---

## License

© 2026 Robert. All rights reserved.

Shared for portfolio and reference purposes. Template architecture and process documentation are my original work. Any content depicting third-party products has been sanitized to remove proprietary information. Not licensed for redistribution or commercial use.

---

<!--
MAINTENANCE
Last reviewed: October 2026
Review cadence: Annually, or when product categories change materially
Contact: tech.robert@protonmail.com
-->
