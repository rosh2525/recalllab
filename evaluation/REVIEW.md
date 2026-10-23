# Independent label review

independent-label-review.csv contains all 60 candidate responses without the developer expected labels. Ask an independent subject reviewer to label each response as correct, partial, incorrect or unable_to_assess against the listed rubric, and note supported diagnostic IDs from content.py. Record disagreements and resolve criteria before running a final benchmark. Do not edit labels merely to match model predictions. Keep a final holdout separate from prompt tuning.

The current developer-authored conceptual.json is a candidate benchmark, not proof of independently reviewed held-out accuracy. A live agreement result on it must be labelled accordingly. The benchmark runner reports valid completion rate separately from agreement and preserves returned input/output tokens and latency. Provider-side billing and current per-token pricing must be checked before claiming measured costs.

Pilot observation templates are blank by design. Store completed participant sheets under ignored data/, never in the public source tree.
