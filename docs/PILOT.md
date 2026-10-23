# Five-student exploratory pilot kit

Status: ready to run; no participants recruited or results collected. This is formative product feedback, not a causal study of learning effectiveness.

## Consent and setup

Invite five adult students who voluntarily agree to test a local study tool. Explain that participation is optional, they can stop or skip questions, this is not an examination, and feedback will not affect grades. Ask separate permission before audio/video recording; the default is no recording. Use IDs P01–P05. Do not collect names, emails, grades or private course files in the observation sheet. Keep the local data file private and agree a deletion date with participants.

Use a separate database per consenting participant. Never share one learner's sessions with another:

```sh
RECALLLAB_DB="$PWD/data/pilot-P01.sqlite3" RECALLLAB_ENABLE_BEDROCK=0 ./run.sh
```

Stop the existing server before switching database. Use the same assessment mode for every participant and record that mode. Enable Bedrock only after verified access; do not mix unavailable AI with live AI without reporting the difference.

## Interview: five minutes before practice

1. Describe the last time you understood a worked solution but could not solve a similar question alone.
2. What do you currently do when stuck? What works poorly?
3. When do you use AI help, if at all? How do you check the answer?
4. Would you prefer typing, voice or both for a short explanation? Why?
5. What would make you distrust feedback from a tool like this?

Do not suggest the expected answers or ask whether they like our idea before hearing about their current behaviour.

## Session: about 15 minutes

- Give the baseline form below before the app. No hints, sources, AI or feedback.
- Ask the student to open the optimisation path, explain the zero-derivative example and explore a hint/source only if they choose. Record help used and confusing feedback. Do not rescue them immediately.
- Ask them to try one mathematical question, then the built-in independent check. Record whether they discover that feedback appears only after completion.
- Give the immediate parallel form without assistance.
- Ask what they thought the tool had checked, what remained unclear, and whether they would return voluntarily. Record misleading feedback verbatim only with consent and without identifiers.
- After about one day, administer the delayed parallel form without sources or hints. Record actual elapsed time and missing follow-up honestly.

## Parallel forms — observer answers below

Score each item out of one, three points total. Explain criteria consistently; do not use LLM judgment for these pilot measures.

| Form | Item 1: marginal cost | Item 2: constrained maximum | Item 3: explain-back |
| --- | --- | --- | --- |
| Baseline | C(q)=30+5q+q². Find C′(3). | Maximise −(q−5)² on [0,2]. Give q. | Does f′(a)=0 alone establish a maximum? Explain one counterexample or further check. |
| Immediate | C(q)=20+3q+2q². Find C′(2). | Maximise −(q−7)² on [0,4]. Give q. | Does f′(a)=0 alone establish a maximum? Explain using a minimum, neither, or another required check. |
| Next day | C(q)=40+2q+3q². Find C′(2). | Maximise −(q−8)² on [0,5]. Give q. | Does f′(a)=0 alone establish a maximum? Explain a case that invalidates the claim or the missing analysis. |

Observer keys: baseline 11, 2; immediate 11, 4; delayed 14, 5. Explain-back earns one only for saying no/insufficient and giving a valid minimum/neither example or an appropriate additional check. A bare “no” earns zero. Forms are authored candidates, not a validated psychometric instrument; similar wording and repeated checks may create practice effects.

## Observation data

Copy pilot-observations.csv into ignored data/ before entering results. Record phase as baseline, immediate or delayed. Use blank values for missing observations; never put zero for a missed visit. Record raw scores and denominator, not an inferred learning percentage. Help used in practice is separate from independent scores.

Report participant count, completion, missing delayed follow-ups, individual paired scores, misleading-feedback examples and the changes made. A five-person uncontrolled pilot cannot establish general learning gains. Do not manufacture results to complete the package.
