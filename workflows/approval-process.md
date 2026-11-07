# Term Approval Process

**Decision SLA:** 10 business days · **Escalation:** docs-lead after 15 days stalled

## Pipeline

1. **Triage** — docs-lead · 1 day — *reject duplicates or redundancies*
2. **Research** — requester · 3 days — *standards check, competitor scan, translation audit*
3. **Review board** — docs-lead + SME + loc-lead · 5 days — *writer / SME / localization lenses*
4. **Resolution** — docs-lead · 1 day — *approve / approve-modified / reject, reason recorded*
5. **Propagation** — docs-lead · 2 days — *glossary, CSV, validator rules, translator notification, deprecation entry*

## Review Board Composition

| Role | Answers | Can veto |
|------|---------|----------|
| docs-lead | Editorial consistency, glossary hygiene | Yes |
| Subject-matter expert | Technical accuracy | Yes (technical grounds only) |
| localization-lead | Translatability, DNT flag, TM impact | Yes (cost/consistency grounds) |

Three reviewers, three veto grounds. A term cannot enter the glossary unless
all three lenses are satisfied — this is the mechanism that prevents the
"three names for one feature" problem this repository exists to solve.

## Decision Outcomes

Every closed request receives one of:

- **Approved** — term enters the master glossary
- **Approved with modification** — definition, casing, or DNT flag adjusted;
  requester notified of the change and why
- **Rejected** — reason recorded. "We already have a term for this" is a
  complete rejection reason; it keeps the glossary small, which is its main
  virtue.

## Metrics Tracked

- Median request-to-decision time
- Rejection rate — a healthy system rejects a lot; a rubber stamp means
  triage is failing
- Post-approval drift: occurrences of forbidden alternatives in new content,
  per validator runs
