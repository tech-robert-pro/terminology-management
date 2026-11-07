# Localization Handoff Guide

**Audience:** translation vendors and in-market reviewers
**Purpose:** Define exactly what translators receive, what they must never
change, and what they must do when the source text conflicts with this guide.

---

## What Translators Receive per Project

| Deliverable | Format | Contents |
|-------------|--------|----------|
| Approved glossary export | `.tbx` / `.xlsx` | Term, definition, DNT flag, part of speech, context sentence |
| Do-not-translate list | `.xlsx` | See below |
| Deprecated-term register | `.xlsx` | Legacy term → replacement mapping |
| Style notes | `.md` | Casing, abbreviation, and punctuation rules per locale |
| Translation memory | `.tmx` | Segments aligned against the previous release |

## Do-Not-Translate Terms

DNT terms appear verbatim in every locale. The current DNT set falls into
four categories:

1. **Bezel/label terms** — text physically printed on the product
   ("Hotkey", "MENU", "ENTER"). Translating these breaks the mapping between
   documentation and the physical device.
2. **Industry-standard abbreviations** — OSD, HDMI, DP, USB-C, VESA, MST,
   OPS, KVM
3. **Proper nouns** — standards bodies and certification names
   (ENERGY STAR, FCC, CE)
4. **UI strings shipped in English** — error codes, service menu items

The full list ships with each project package; it supersedes any list
embedded in older TMX files.

## Term Binding Rules

1. Every glossary term must be rendered per the glossary. Translators may
   not substitute synonyms, even if the synonym reads better in the target
   language. If a glossary rendering is wrong in your locale, flag it (see
   Conflict Procedure) rather than working around it.
2. Forbidden alternatives listed in the glossary apply in translation too.
   A source sentence saying "display" must not become "monitor" in German
   because "Bildschirm" is shorter.
3. Non-glossary vocabulary is unrestricted — translators choose natural
   phrasing freely. The glossary constrains a controlled subset, not the
   whole document.

## Segment Strategy (for TM leverage)

- Sentence-level segmentation; never join or split glossary-carrying
  sentences
- Glossary terms are kept position-stable across revisions: a term appearing
  in segment 214 of the quick start should still be in segment 214 next
  release, keeping the TM match exact
- Writers avoid embedding glossary terms inside product names, numbered
  headings, or tables that reorder between releases

## Conflict Procedure

When a translator finds any of these, stop and flag — do not improvise:

- Source text uses a deprecated term → flag to loc-lead; do not translate
  the deprecated term; wait for confirmation to use the replacement
- Source text contradicts a glossary definition → flag, do not guess
- A glossary term has no idiomatic rendering in your locale → propose an
  alternative to loc-lead; the glossary is amended centrally so all locales
  change together
- An acronym in the source is absent from the DNT list → flag; do not
  silently expand or translate it

Flags go to loc-lead with the segment ID and a proposed resolution.
Response SLA: 2 business days during a release cycle.
