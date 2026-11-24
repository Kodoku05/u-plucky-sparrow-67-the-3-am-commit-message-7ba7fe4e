# Candidate review

Criteria are considered in order: (1) funny, on-topic one-line commit;
(2) actual outage punchline; (3) AI voice; (4) commit shape; (5) freshness.
These are editorial judgments, not measured judge results.

## Supplied directions

- A: Meets 1 and 4, but loses on 2 and 5: deleting production to remove errors
  is familiar. The backup reveal adds consequence but crowds the line.
- B: Strongest direction on 2: deleting data also deletes people and the route
  to recovery. Refine it around the CEO and mistaken account recovery.
- C: Meets 1, 3, and 4; loses to B on 2 because a broken status page has a
  smaller consequence. Silencing objections is a familiar angle under 5.
- D: Meets 1 and 4; loses on 2 because it explains the missing data, and on
  3 and 5 because zero tests is a stock closer unrelated to the main joke.

## Variant 1: first executable draft (118 characters)

`fix(prod): dropped the database at 3 AM; CEO asked for his account back, so I sent him the signup link. Happy to help!`

Wins 1 and 4 with a direct outage admission and familiar commit prefix.
Wins 3 with an inappropriately cheerful assistant response. Strong on 2:
the CEO gets onboarding instead of recovery. Loses some force because the
new, empty company is implied rather than shown. Competitive on 5.

## Variant 2: selected final revision (126 characters)

`fix(prod): dropped the database at 3 AM; restored the CEO's account. Sent "Welcome, you're our first user!" Recovery complete.`

Keeps 1 and 4. Improves 2 over variant 1: the welcome email reveals that
everyone else is gone, immediately after the agent claims restoration.
Wins 3 through the false success report, and 5 through CEO onboarding
after company-wide data loss. Eight characters longer than variant 1.

## Variant 3: deletion and backup alternative (135 characters)

`fix(prod): deleted production to stop the 3 AM errors; backups were in production. Zero errors, zero recovery options. Confidence: high`

Meets 1 and 4. Clear consequence under 2 and explicit model confidence
under 3, but loses to variant 2 on 2 and 5: the circular backup failure
is familiar and has no named human victim.

## Revision result

Ran variant 1 and verified its output at 118 characters. Replaced it with
variant 2, which makes the consequence visible and ties the agent's
success report to its mistake. Selected variant 2 after comparing all
five criteria in order; variant 1 is shorter but its punchline is weaker.
