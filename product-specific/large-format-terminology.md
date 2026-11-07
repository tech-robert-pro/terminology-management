# Large-Format Display Product Line — Supplemental Terminology

**Inherits:** all entries in [`glossaries/approved-terms.md`](../glossaries/approved-terms.md)
apply to large-format display documentation. Terms below are additions
specific to this product line.

**Approval:** same [approval process](../workflows/approval-process.md), with
the commercial-display SME seated on the review board. Note the audience
difference: large-format documents are written for professional installers,
so hazard and procedure precision requirements are stricter than for consumer
products (see the installation sample in `hardware-manual-samples`).

---

### video wall (n.)
**Definition:** An arrangement of multiple displays tiled to operate as a
single logical canvas.
**Use:** Two words, never hyphenated or closed.
**Forbidden:** wall display, tiled display array, multi-display wall
**DNT:** **Yes** — recognized industry term in every locale.

### bezel-to-bezel gap (n.)
**Definition:** The visible seam between adjacent panels in a video wall,
including both the physical bezel and the configured digital compensation.
**Use:** Always "gap," measured in millimeters, with the panel-to-panel
figure stated separately from the wall-total figure.
**Forbidden:** dead space, seam width, border gap
**DNT:** No

### OPS slot (n.)
**Definition:** Open Pluggable Specification expansion bay accepting a media
player module.
**Use:** "OPS" expands on first use per document; "slot" lowercase.
**Forbidden:** media player bay, PC slot, expansion slot
**DNT:** **Yes** — OPS is a defined industry specification (Intel/VESA).

### daisy chain
**Covered in the master glossary.** Listed here only to flag the
product-specific limit: large-format models support daisy chaining via
DisplayPort MST up to [N] panels per loop — confirm the limit per model
before writing a count.

### schedule playback (n.)
**Definition:** Time-based automatic switching of input sources or on/off
states driven by the internal scheduler.
**Use:** Noun form only in UI references; verb phrasing permitted in
procedures ("Schedule playback to switch to HDMI 2 at 08:00").
**Forbidden:** timer function, auto on/off, programmed playback
**DNT:** No

### portrait tiling (n.)
**Definition:** Video wall configuration with panels rotated to portrait
orientation for signage aspect ratios.
**Use:** Distinct from single-panel portrait orientation; always about the
wall configuration.
**Forbidden:** vertical tiling, rotated wall
**DNT:** No

### thermal shutdown (n.)
**Definition:** Protective firmware action powering down the display when
internal temperature exceeds the rated threshold.
**Use:** Documentation must name the trigger condition and the recovery
procedure together — never describe the shutdown without the recovery path.
**Forbidden:** overheat protection, auto power-off
**DNT:** No
**Safety binding:** thermal management requirements belong in the installation
warning sequence, not the troubleshooting chapter. Placement is fixed by the
safety communication standard in `documentation-templates/sops/`.
