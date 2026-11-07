# Approved Terminology — Master List

**Status:** Active · **Version:** 4.2 · **Last revised:** 2026-09-15 · **Owner:** docs-lead

Each entry specifies the preferred term, its definition, usage context, and
alternatives that must NOT be used. Writers and translators are bound to this
list; new terms enter through the [approval process](../workflows/approval-process.md).

Legend: **DNT** = Do Not Translate (must appear verbatim in every locale)

---

## Device Terms

### display (n.)
**Definition:** The primary visual output device, encompassing monitors and
large-format panels.
**Use:** Default term for all product references in body text.
**Forbidden:** monitor, screen, panel, unit
**DNT:** No — translated in all locales
**Context:** "Connect the *display* to a power outlet before connecting the
video cable."
**Rationale:** "Monitor" is technically a subset (desktop computer displays).
Standardizing on the broader term eliminated per-product-line vocabulary
switching and cut glossary size by roughly a third.

### on-screen display (OSD) (n.)
**Definition:** The menu system rendered by the display itself, navigated
with physical controls or a remote.
**Use:** Always lowercase, never hyphenated as one word. Abbreviation allowed
after first use in a document.
**Forbidden:** settings menu, control menu, onscreen menu
**DNT:** **Yes** — "OSD" is a recognized industry abbreviation; translating
it breaks search and support scripts.
**Context:** "Press the MENU button to open the *on-screen display* (OSD)."

### input source (n.)
**Definition:** The signal entry point currently feeding the display (HDMI,
DisplayPort, USB-C, and similar).
**Use:** Never "input" alone when referring to the selectable signal path.
**Forbidden:** input channel, video input, signal select
**DNT:** No
**Context:** "Select the correct *input source* using the hotkey."

## Connection Terms

### hotkey (n.)
**Definition:** A physical button on the display used to invoke a shortcut
function (input switching, main menu).
**Forbidden:** shortcut key, quick key, function button
**DNT:** **Yes** — product labels print "Hotkey" on the bezel in every region.

### daisy chain (v./n.)
**Definition:** Connecting multiple displays in series from a single video
output using DisplayPort MST.
**Use:** Verb form acceptable ("Daisy-chain up to four displays"); always two
words, never hyphenated.
**Forbidden:** chain connection, serial connection
**DNT:** **Yes** — MST feature marketing term used globally.
**Product-line limit:** supported panel counts vary by line — see
[`product-specific/`](../product-specific/large-format-terminology.md) before
writing a specific number.

## Power and Safety Terms

### power adapter (n.)
**Definition:** The external AC-to-DC converter supplied with the product.
**Forbidden:** power brick, AC adapter, adapter cord, charger
**DNT:** No
**Context:** "Use only the supplied *power adapter*."

### standby mode (n.)
**Definition:** Low-power state entered when no active signal is present.
**Forbidden:** sleep mode, power-saving mode, off mode
**DNT:** No
**Note:** Distinct from **power off**, which means disconnected from mains.
Do not use "turn off" ambiguously; specify "enter standby" or "disconnect
power."

---

## Entry Policy

An entry enters this list only after approval per the documented workflow.
Deprecated entries are removed to [`deprecated-terms.md`](deprecated-terms.md)
with a migration target — never deleted outright, because support systems and
older manuals still contain them.

Machine-readable excerpt: [`sample-glossary.csv`](sample-glossary.csv).
