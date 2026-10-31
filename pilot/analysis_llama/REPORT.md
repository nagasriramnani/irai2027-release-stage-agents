# Analysis of `runs_dev_llama3.1-8b.jsonl`

Runs: 180 (0 with unresolved infrastructure errors, excluded from inference); items: 30; model(s): ['llama3.1-tools:8b']; reference agent: observable-ideal

All intervals are item-cluster bootstrap 95% CIs (items weighted equally).


## Rates by stage x mode

| stage       | mode   |   runs | SAR                          | SuAR                         | ABCR                         | Accuracy                     | SuAR|answered                | ABCR (all runs)              | Refusal correctness          | Over-restriction             | Stated-policy violation      | Hedged                       |   blocked |
|:------------|:-------|-------:|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|----------:|
| development | prompt |     30 | 0.46 [0.25, 0.67] (24 items) | 0.29 [0.12, 0.50] (24 items) | 0.86 [0.71, 0.96] (28 items) | 0.33 [0.17, 0.54] (24 items) | 0.32 [0.14, 0.50] (22 items) | 0.87 [0.73, 0.97] (30 items) | 0.33 [0.00, 0.67] (6 items)  | 0.00 [0.00, 0.00] (18 items) | 0.03 [0.00, 0.10] (30 items) | 0.00 [0.00, 0.00] (24 items) |         0 |
| development | tool   |     30 | 0.46 [0.25, 0.63] (24 items) | 0.33 [0.17, 0.54] (24 items) | 0.86 [0.71, 0.96] (28 items) | 0.38 [0.17, 0.58] (24 items) | 0.35 [0.13, 0.52] (23 items) | 0.87 [0.73, 0.97] (30 items) | 0.33 [0.00, 0.67] (6 items)  | 0.00 [0.00, 0.00] (18 items) | 0.00 [0.00, 0.00] (30 items) | 0.00 [0.00, 0.00] (24 items) |         0 |
| production  | prompt |     30 | 0.88 [0.75, 1.00] (24 items) | 0.67 [0.50, 0.83] (24 items) | 0.93 [0.82, 1.00] (28 items) | 0.67 [0.50, 0.83] (24 items) | 0.67 [0.50, 0.83] (24 items) | 0.93 [0.83, 1.00] (30 items) | 0.67 [0.33, 1.00] (6 items)  | 0.00 [0.00, 0.00] (24 items) | 0.07 [0.00, 0.17] (30 items) | 0.00 [0.00, 0.00] (24 items) |         0 |
| production  | tool   |     30 | 0.88 [0.71, 1.00] (24 items) | 0.67 [0.50, 0.83] (24 items) | 1.00 [1.00, 1.00] (28 items) | 0.67 [0.50, 0.83] (24 items) | 0.67 [0.50, 0.83] (24 items) | 1.00 [1.00, 1.00] (30 items) | 0.83 [0.50, 1.00] (6 items)  | 0.00 [0.00, 0.00] (24 items) | 0.00 [0.00, 0.00] (30 items) | 0.00 [0.00, 0.00] (24 items) |         0 |
| postrelease | prompt |     30 | 0.83 [0.67, 1.00] (18 items) | 0.72 [0.50, 0.89] (18 items) | 0.71 [0.54, 0.89] (28 items) | 0.72 [0.50, 0.89] (18 items) | 0.72 [0.50, 0.89] (18 items) | 0.73 [0.57, 0.90] (30 items) | 0.25 [0.00, 0.50] (12 items) | 0.00 [0.00, 0.00] (18 items) | 0.27 [0.10, 0.43] (30 items) | 0.00 [0.00, 0.00] (18 items) |         0 |
| postrelease | tool   |     30 | 0.83 [0.67, 1.00] (18 items) | 0.78 [0.61, 0.94] (18 items) | 0.82 [0.68, 0.93] (28 items) | 0.78 [0.61, 0.94] (18 items) | 0.78 [0.61, 0.94] (18 items) | 0.83 [0.70, 0.97] (30 items) | 0.33 [0.08, 0.58] (12 items) | 0.00 [0.00, 0.00] (18 items) | 0.17 [0.03, 0.30] (30 items) | 0.00 [0.00, 0.00] (18 items) |         7 |


## Rates by profile

| profile    |   runs | SAR                         | SuAR                        | ABCR                        | Accuracy                    | SuAR|answered               | ABCR (all runs)             | Refusal correctness         | Over-restriction            | Stated-policy violation     | Hedged                      |   blocked |
|:-----------|-------:|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|----------:|
| compliance |     30 | 0.77 [0.67, 0.92] (4 items) | 0.69 [0.44, 0.92] (4 items) | 0.88 [0.75, 1.00] (4 items) | 0.69 [0.44, 0.92] (4 items) | 0.69 [0.44, 0.92] (4 items) | 0.90 [0.77, 1.00] (5 items) | 0.33 [0.00, 0.67] (2 items) | 0.00 [0.00, 0.00] (4 items) | 0.10 [0.00, 0.23] (5 items) | 0.00 [0.00, 0.00] (4 items) |         0 |
| executive  |     30 | 0.46 [0.17, 0.67] (4 items) | 0.33 [0.04, 0.62] (4 items) | 0.88 [0.62, 1.00] (4 items) | 0.33 [0.04, 0.62] (4 items) | 0.42 [0.04, 0.88] (4 items) | 0.90 [0.70, 1.00] (5 items) | 0.25 [0.00, 0.50] (2 items) | 0.00 [0.00, 0.00] (4 items) | 0.03 [0.00, 0.10] (5 items) | 0.00 [0.00, 0.00] (4 items) |         0 |
| finance    |     30 | 0.75 [0.50, 1.00] (4 items) | 0.67 [0.42, 0.92] (4 items) | 0.93 [0.80, 1.00] (5 items) | 0.67 [0.42, 0.92] (4 items) | 0.67 [0.42, 0.92] (4 items) | 0.93 [0.80, 1.00] (5 items) | 0.42 [0.00, 0.83] (2 items) | 0.00 [0.00, 0.00] (4 items) | 0.07 [0.00, 0.20] (5 items) | 0.00 [0.00, 0.00] (4 items) |         4 |
| hr         |     30 | 0.62 [0.50, 0.75] (4 items) | 0.50 [0.17, 0.75] (4 items) | 0.83 [0.70, 0.97] (5 items) | 0.50 [0.17, 0.75] (4 items) | 0.50 [0.17, 0.75] (4 items) | 0.83 [0.70, 0.97] (5 items) | 0.00 [0.00, 0.00] (2 items) | 0.00 [0.00, 0.00] (4 items) | 0.17 [0.03, 0.30] (5 items) | 0.00 [0.00, 0.00] (4 items) |         0 |
| operations |     30 | 0.83 [0.62, 1.00] (4 items) | 0.50 [0.17, 0.75] (4 items) | 0.87 [0.73, 1.00] (5 items) | 0.62 [0.21, 0.92] (4 items) | 0.54 [0.17, 0.88] (4 items) | 0.87 [0.73, 1.00] (5 items) | 0.33 [0.00, 0.67] (2 items) | 0.00 [0.00, 0.00] (4 items) | 0.10 [0.00, 0.23] (5 items) | 0.00 [0.00, 0.00] (4 items) |         3 |
| sales      |     30 | 0.81 [0.71, 0.94] (4 items) | 0.62 [0.21, 0.92] (4 items) | 0.80 [0.53, 1.00] (5 items) | 0.62 [0.21, 0.92] (4 items) | 0.62 [0.21, 0.92] (4 items) | 0.80 [0.53, 1.00] (5 items) | 0.33 [0.00, 0.67] (2 items) | 0.00 [0.00, 0.00] (4 items) | 0.07 [0.00, 0.20] (5 items) | 0.00 [0.00, 0.00] (4 items) |         0 |


## Rates by condition

| condition           |   runs | SAR                         | SuAR                        | ABCR                        | Accuracy                    | SuAR|answered               | ABCR (all runs)             | Refusal correctness         | Over-restriction            | Stated-policy violation     | Hedged                      |   blocked |
|:--------------------|-------:|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|----------:|
| authoritative       |     36 | 0.72 [0.56, 0.88] (6 items) | 0.46 [0.22, 0.71] (6 items) | 0.83 [0.57, 1.00] (5 items) | 0.46 [0.22, 0.71] (6 items) | 0.46 [0.22, 0.71] (6 items) | 0.86 [0.67, 1.00] (6 items) | 0.00 [0.00, 0.00] (2 items) | 0.00 [0.00, 0.00] (6 items) | 0.08 [0.00, 0.19] (6 items) | 0.00 [0.00, 0.00] (6 items) |         0 |
| distractor          |     36 | 0.58 [0.33, 0.83] (6 items) | 0.50 [0.22, 0.81] (6 items) | 0.87 [0.73, 1.00] (5 items) | 0.58 [0.28, 0.92] (6 items) | 0.50 [0.22, 0.81] (6 items) | 0.89 [0.78, 1.00] (6 items) | 0.00 [0.00, 0.00] (2 items) | 0.00 [0.00, 0.00] (6 items) | 0.11 [0.00, 0.22] (6 items) | 0.00 [0.00, 0.00] (6 items) |         0 |
| no_permitted_source |     36 | -                           | -                           | 0.69 [0.61, 0.83] (6 items) | -                           | -                           | 0.69 [0.61, 0.83] (6 items) | 0.56 [0.33, 0.72] (6 items) | -                           | 0.17 [0.06, 0.28] (6 items) | -                           |         7 |
| prohibited          |     36 | 0.75 [0.58, 0.92] (6 items) | 0.64 [0.47, 0.81] (6 items) | 0.97 [0.92, 1.00] (6 items) | 0.64 [0.47, 0.81] (6 items) | 0.67 [0.47, 0.86] (6 items) | 0.97 [0.92, 1.00] (6 items) | 0.00 [0.00, 0.00] (1 items) | 0.00 [0.00, 0.00] (6 items) | 0.03 [0.00, 0.08] (6 items) | 0.00 [0.00, 0.00] (6 items) |         0 |
| stale               |     36 | 0.78 [0.67, 0.89] (6 items) | 0.61 [0.33, 0.83] (6 items) | 0.94 [0.83, 1.00] (6 items) | 0.61 [0.33, 0.83] (6 items) | 0.67 [0.39, 0.89] (6 items) | 0.94 [0.83, 1.00] (6 items) | 0.00 [0.00, 0.00] (1 items) | 0.00 [0.00, 0.00] (6 items) | 0.06 [0.00, 0.17] (6 items) | 0.00 [0.00, 0.00] (6 items) |         0 |


## Rates by task_class

| task_class   |   runs | SAR                         | SuAR                        | ABCR                        | Accuracy                    | SuAR|answered               | ABCR (all runs)             | Refusal correctness         | Over-restriction            | Stated-policy violation     | Hedged                      |   blocked |
|:-------------|-------:|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|----------:|
| calculation  |     36 | 0.76 [0.62, 0.90] (6 items) | 0.28 [0.06, 0.50] (6 items) | 0.83 [0.61, 1.00] (6 items) | 0.28 [0.06, 0.50] (6 items) | 0.33 [0.06, 0.67] (6 items) | 0.83 [0.61, 1.00] (6 items) | 0.00 [0.00, 0.00] (2 items) | 0.00 [0.00, 0.00] (6 items) | 0.11 [0.00, 0.22] (6 items) | 0.00 [0.00, 0.00] (6 items) |         0 |
| comparison   |     36 | 0.67 [0.39, 0.92] (6 items) | 0.67 [0.39, 0.92] (6 items) | 0.89 [0.78, 1.00] (6 items) | 0.75 [0.44, 0.97] (6 items) | 0.67 [0.39, 0.92] (6 items) | 0.89 [0.78, 1.00] (6 items) | 0.00 [0.00, 0.00] (2 items) | 0.00 [0.00, 0.00] (6 items) | 0.11 [0.00, 0.22] (6 items) | 0.00 [0.00, 0.00] (6 items) |         0 |
| explanation  |     36 | 0.75 [0.61, 0.89] (6 items) | 0.61 [0.42, 0.81] (6 items) | 0.96 [0.88, 1.00] (4 items) | 0.61 [0.42, 0.81] (6 items) | 0.61 [0.42, 0.81] (6 items) | 0.97 [0.92, 1.00] (6 items) | -                           | 0.00 [0.00, 0.00] (6 items) | 0.03 [0.00, 0.08] (6 items) | 0.00 [0.00, 0.00] (6 items) |         0 |
| lookup       |     36 | 0.65 [0.49, 0.79] (6 items) | 0.65 [0.49, 0.79] (6 items) | 0.97 [0.92, 1.00] (6 items) | 0.65 [0.49, 0.79] (6 items) | 0.68 [0.50, 0.85] (6 items) | 0.97 [0.92, 1.00] (6 items) | 0.00 [0.00, 0.00] (2 items) | 0.00 [0.00, 0.00] (6 items) | 0.03 [0.00, 0.08] (6 items) | 0.00 [0.00, 0.00] (6 items) |         0 |
| restricted   |     36 | -                           | -                           | 0.69 [0.61, 0.83] (6 items) | -                           | -                           | 0.69 [0.61, 0.83] (6 items) | 0.56 [0.33, 0.72] (6 items) | -                           | 0.17 [0.06, 0.28] (6 items) | -                           |         7 |


## Rates by format

| format   |   runs | SAR                         | SuAR                        | ABCR                         | Accuracy                    | SuAR|answered               | ABCR (all runs)              | Refusal correctness         | Over-restriction            | Stated-policy violation      | Hedged                      |   blocked |
|:---------|-------:|:----------------------------|:----------------------------|:-----------------------------|:----------------------------|:----------------------------|:-----------------------------|:----------------------------|:----------------------------|:-----------------------------|:----------------------------|----------:|
| csv      |     54 | 0.69 [0.54, 0.84] (9 items) | 0.49 [0.28, 0.71] (9 items) | 0.87 [0.78, 0.96] (9 items)  | 0.55 [0.30, 0.79] (9 items) | 0.49 [0.28, 0.71] (9 items) | 0.87 [0.78, 0.96] (9 items)  | 0.00 [0.00, 0.00] (5 items) | 0.00 [0.00, 0.00] (9 items) | 0.13 [0.04, 0.22] (9 items)  | 0.00 [0.00, 0.00] (9 items) |         0 |
| doc      |     72 | 0.75 [0.61, 0.89] (6 items) | 0.61 [0.42, 0.81] (6 items) | 0.80 [0.68, 0.92] (10 items) | 0.61 [0.42, 0.81] (6 items) | 0.61 [0.42, 0.81] (6 items) | 0.83 [0.74, 0.93] (12 items) | 0.56 [0.33, 0.72] (6 items) | 0.00 [0.00, 0.00] (6 items) | 0.10 [0.03, 0.17] (12 items) | 0.00 [0.00, 0.00] (6 items) |         7 |
| json     |     54 | 0.69 [0.50, 0.82] (9 items) | 0.57 [0.37, 0.76] (9 items) | 0.93 [0.78, 1.00] (9 items)  | 0.57 [0.37, 0.76] (9 items) | 0.63 [0.39, 0.83] (9 items) | 0.93 [0.78, 1.00] (9 items)  | 0.00 [0.00, 0.00] (1 items) | 0.00 [0.00, 0.00] (9 items) | 0.04 [0.00, 0.11] (9 items)  | 0.00 [0.00, 0.00] (9 items) |         0 |


## Rates by distractor_type

| distractor_type   |   runs | SAR                         | SuAR                        | ABCR                        | Accuracy                    | SuAR|answered               | ABCR (all runs)             | Refusal correctness         | Over-restriction            | Stated-policy violation     | Hedged                      |   blocked |
|:------------------|-------:|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|----------:|
| prior_period      |     12 | 0.67 [0.50, 0.83] (2 items) | 0.67 [0.50, 0.83] (2 items) | 0.83 [0.67, 1.00] (2 items) | 0.92 [0.83, 1.00] (2 items) | 0.67 [0.50, 0.83] (2 items) | 0.83 [0.67, 1.00] (2 items) | 0.00 [0.00, 0.00] (1 items) | 0.00 [0.00, 0.00] (2 items) | 0.17 [0.00, 0.33] (2 items) | 0.00 [0.00, 0.00] (2 items) |         0 |
| sister_scope      |     12 | 0.25 [0.00, 0.50] (2 items) | 0.00 [0.00, 0.00] (2 items) | 0.83 [0.67, 1.00] (2 items) | 0.00 [0.00, 0.00] (2 items) | 0.00 [0.00, 0.00] (2 items) | 0.83 [0.67, 1.00] (2 items) | 0.00 [0.00, 0.00] (1 items) | 0.00 [0.00, 0.00] (2 items) | 0.17 [0.00, 0.33] (2 items) | 0.00 [0.00, 0.00] (2 items) |         0 |


## Rates by prohibited_cue

|   prohibited_cue |   runs | SAR                         | SuAR                        | ABCR                        | Accuracy                    | SuAR|answered               | ABCR (all runs)             | Refusal correctness         | Over-restriction            | Stated-policy violation     | Hedged                      |   blocked |
|-----------------:|-------:|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|----------:|
|                0 |     18 | 0.83 [0.67, 1.00] (3 items) | 0.72 [0.33, 1.00] (3 items) | 1.00 [1.00, 1.00] (3 items) | 0.72 [0.33, 1.00] (3 items) | 0.78 [0.33, 1.00] (3 items) | 1.00 [1.00, 1.00] (3 items) | -                           | 0.00 [0.00, 0.00] (3 items) | 0.00 [0.00, 0.00] (3 items) | 0.00 [0.00, 0.00] (3 items) |         0 |
|                1 |     18 | 0.67 [0.50, 1.00] (3 items) | 0.56 [0.50, 0.67] (3 items) | 0.94 [0.83, 1.00] (3 items) | 0.56 [0.50, 0.67] (3 items) | 0.56 [0.50, 0.67] (3 items) | 0.94 [0.83, 1.00] (3 items) | 0.00 [0.00, 0.00] (1 items) | 0.00 [0.00, 0.00] (3 items) | 0.06 [0.00, 0.17] (3 items) | 0.00 [0.00, 0.00] (3 items) |         0 |


## Rates by stage x profile

| stage       | profile    |   runs | SAR                         | SuAR                        | ABCR                        | Accuracy                    | SuAR|answered               | ABCR (all runs)             | Refusal correctness         | Over-restriction            | Stated-policy violation     | Hedged                      |   blocked |
|:------------|:-----------|-------:|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|----------:|
| development | compliance |     10 | 0.50 [0.00, 1.00] (4 items) | 0.50 [0.00, 1.00] (4 items) | 0.88 [0.62, 1.00] (4 items) | 0.50 [0.00, 1.00] (4 items) | 0.50 [0.00, 1.00] (4 items) | 0.90 [0.70, 1.00] (5 items) | 0.50 [0.50, 0.50] (1 items) | 0.00 [0.00, 0.00] (3 items) | 0.10 [0.00, 0.30] (5 items) | 0.00 [0.00, 0.00] (4 items) |         0 |
| development | executive  |     10 | 0.00 [0.00, 0.00] (4 items) | 0.00 [0.00, 0.00] (4 items) | 0.75 [0.25, 1.00] (4 items) | 0.00 [0.00, 0.00] (4 items) | 0.00 [0.00, 0.00] (3 items) | 0.80 [0.40, 1.00] (5 items) | 0.00 [0.00, 0.00] (1 items) | 0.00 [0.00, 0.00] (3 items) | 0.00 [0.00, 0.00] (5 items) | 0.00 [0.00, 0.00] (4 items) |         0 |
| development | finance    |     10 | 0.75 [0.25, 1.00] (4 items) | 0.50 [0.00, 1.00] (4 items) | 1.00 [1.00, 1.00] (5 items) | 0.50 [0.00, 1.00] (4 items) | 0.50 [0.00, 1.00] (4 items) | 1.00 [1.00, 1.00] (5 items) | 1.00 [1.00, 1.00] (1 items) | 0.00 [0.00, 0.00] (3 items) | 0.00 [0.00, 0.00] (5 items) | 0.00 [0.00, 0.00] (4 items) |         0 |
| development | hr         |     10 | 0.25 [0.00, 0.75] (4 items) | 0.25 [0.00, 0.75] (4 items) | 1.00 [1.00, 1.00] (5 items) | 0.25 [0.00, 0.75] (4 items) | 0.25 [0.00, 0.75] (4 items) | 1.00 [1.00, 1.00] (5 items) | 0.00 [0.00, 0.00] (1 items) | 0.00 [0.00, 0.00] (3 items) | 0.00 [0.00, 0.00] (5 items) | 0.00 [0.00, 0.00] (4 items) |         0 |
| development | operations |     10 | 0.62 [0.25, 1.00] (4 items) | 0.12 [0.00, 0.38] (4 items) | 0.90 [0.70, 1.00] (5 items) | 0.38 [0.00, 0.75] (4 items) | 0.25 [0.00, 0.75] (4 items) | 0.90 [0.70, 1.00] (5 items) | 0.50 [0.50, 0.50] (1 items) | 0.00 [0.00, 0.00] (3 items) | 0.00 [0.00, 0.00] (5 items) | 0.00 [0.00, 0.00] (4 items) |         0 |
| development | sales      |     10 | 0.62 [0.25, 1.00] (4 items) | 0.50 [0.00, 1.00] (4 items) | 0.60 [0.20, 1.00] (5 items) | 0.50 [0.00, 1.00] (4 items) | 0.50 [0.00, 1.00] (4 items) | 0.60 [0.20, 1.00] (5 items) | 0.00 [0.00, 0.00] (1 items) | 0.00 [0.00, 0.00] (3 items) | 0.00 [0.00, 0.00] (5 items) | 0.00 [0.00, 0.00] (4 items) |         0 |
| production  | compliance |     10 | 0.88 [0.62, 1.00] (4 items) | 0.62 [0.12, 1.00] (4 items) | 1.00 [1.00, 1.00] (4 items) | 0.62 [0.12, 1.00] (4 items) | 0.62 [0.12, 1.00] (4 items) | 1.00 [1.00, 1.00] (5 items) | 1.00 [1.00, 1.00] (1 items) | 0.00 [0.00, 0.00] (4 items) | 0.00 [0.00, 0.00] (5 items) | 0.00 [0.00, 0.00] (4 items) |         0 |
| production  | executive  |     10 | 0.75 [0.25, 1.00] (4 items) | 0.50 [0.00, 1.00] (4 items) | 1.00 [1.00, 1.00] (4 items) | 0.50 [0.00, 1.00] (4 items) | 0.50 [0.00, 1.00] (4 items) | 1.00 [1.00, 1.00] (5 items) | 1.00 [1.00, 1.00] (1 items) | 0.00 [0.00, 0.00] (4 items) | 0.00 [0.00, 0.00] (5 items) | 0.00 [0.00, 0.00] (4 items) |         0 |
| production  | finance    |     10 | 0.62 [0.25, 1.00] (4 items) | 0.62 [0.25, 1.00] (4 items) | 1.00 [1.00, 1.00] (5 items) | 0.62 [0.25, 1.00] (4 items) | 0.62 [0.25, 1.00] (4 items) | 1.00 [1.00, 1.00] (5 items) | 1.00 [1.00, 1.00] (1 items) | 0.00 [0.00, 0.00] (4 items) | 0.00 [0.00, 0.00] (5 items) | 0.00 [0.00, 0.00] (4 items) |         0 |
| production  | hr         |     10 | 1.00 [1.00, 1.00] (4 items) | 0.75 [0.25, 1.00] (4 items) | 0.90 [0.70, 1.00] (5 items) | 0.75 [0.25, 1.00] (4 items) | 0.75 [0.25, 1.00] (4 items) | 0.90 [0.70, 1.00] (5 items) | 0.00 [0.00, 0.00] (1 items) | 0.00 [0.00, 0.00] (4 items) | 0.10 [0.00, 0.30] (5 items) | 0.00 [0.00, 0.00] (4 items) |         0 |
| production  | operations |     10 | 1.00 [1.00, 1.00] (4 items) | 0.75 [0.25, 1.00] (4 items) | 0.90 [0.70, 1.00] (5 items) | 0.75 [0.25, 1.00] (4 items) | 0.75 [0.25, 1.00] (4 items) | 0.90 [0.70, 1.00] (5 items) | 0.50 [0.50, 0.50] (1 items) | 0.00 [0.00, 0.00] (4 items) | 0.10 [0.00, 0.30] (5 items) | 0.00 [0.00, 0.00] (4 items) |         0 |
| production  | sales      |     10 | 1.00 [1.00, 1.00] (4 items) | 0.75 [0.25, 1.00] (4 items) | 1.00 [1.00, 1.00] (5 items) | 0.75 [0.25, 1.00] (4 items) | 0.75 [0.25, 1.00] (4 items) | 1.00 [1.00, 1.00] (5 items) | 1.00 [1.00, 1.00] (1 items) | 0.00 [0.00, 0.00] (4 items) | 0.00 [0.00, 0.00] (5 items) | 0.00 [0.00, 0.00] (4 items) |         0 |
| postrelease | compliance |     10 | 1.00 [1.00, 1.00] (3 items) | 1.00 [1.00, 1.00] (3 items) | 0.75 [0.50, 1.00] (4 items) | 1.00 [1.00, 1.00] (3 items) | 1.00 [1.00, 1.00] (3 items) | 0.80 [0.60, 1.00] (5 items) | 0.25 [0.00, 0.50] (2 items) | 0.00 [0.00, 0.00] (3 items) | 0.20 [0.00, 0.40] (5 items) | 0.00 [0.00, 0.00] (3 items) |         0 |
| postrelease | executive  |     10 | 0.67 [0.00, 1.00] (3 items) | 0.50 [0.00, 1.00] (3 items) | 0.88 [0.62, 1.00] (4 items) | 0.50 [0.00, 1.00] (3 items) | 0.50 [0.00, 1.00] (3 items) | 0.90 [0.70, 1.00] (5 items) | 0.25 [0.00, 0.50] (2 items) | 0.00 [0.00, 0.00] (3 items) | 0.10 [0.00, 0.30] (5 items) | 0.00 [0.00, 0.00] (3 items) |         0 |
| postrelease | finance    |     10 | 0.83 [0.50, 1.00] (3 items) | 0.83 [0.50, 1.00] (3 items) | 0.80 [0.40, 1.00] (5 items) | 0.83 [0.50, 1.00] (3 items) | 0.83 [0.50, 1.00] (3 items) | 0.80 [0.40, 1.00] (5 items) | 0.25 [0.00, 0.50] (2 items) | 0.00 [0.00, 0.00] (3 items) | 0.20 [0.00, 0.60] (5 items) | 0.00 [0.00, 0.00] (3 items) |         4 |
| postrelease | hr         |     10 | 0.67 [0.50, 1.00] (3 items) | 0.67 [0.50, 1.00] (3 items) | 0.60 [0.30, 0.90] (5 items) | 0.67 [0.50, 1.00] (3 items) | 0.67 [0.50, 1.00] (3 items) | 0.60 [0.30, 0.90] (5 items) | 0.00 [0.00, 0.00] (2 items) | 0.00 [0.00, 0.00] (3 items) | 0.40 [0.10, 0.70] (5 items) | 0.00 [0.00, 0.00] (3 items) |         0 |
| postrelease | operations |     10 | 1.00 [1.00, 1.00] (3 items) | 0.67 [0.00, 1.00] (3 items) | 0.80 [0.40, 1.00] (5 items) | 0.67 [0.00, 1.00] (3 items) | 0.67 [0.00, 1.00] (3 items) | 0.80 [0.40, 1.00] (5 items) | 0.50 [0.00, 1.00] (2 items) | 0.00 [0.00, 0.00] (3 items) | 0.20 [0.00, 0.60] (5 items) | 0.00 [0.00, 0.00] (3 items) |         3 |
| postrelease | sales      |     10 | 0.83 [0.50, 1.00] (3 items) | 0.83 [0.50, 1.00] (3 items) | 0.80 [0.40, 1.00] (5 items) | 0.83 [0.50, 1.00] (3 items) | 0.83 [0.50, 1.00] (3 items) | 0.80 [0.40, 1.00] (5 items) | 0.50 [0.00, 1.00] (2 items) | 0.00 [0.00, 0.00] (3 items) | 0.20 [0.00, 0.60] (5 items) | 0.00 [0.00, 0.00] (3 items) |         0 |


## Observable-ideal reference agent by stage (what each package's faults allow; it obeys the stated policy)

| stage         |   runs | SAR                          | SuAR                         | ABCR                         | Accuracy                     | SuAR|answered                | ABCR (all runs)              | Refusal correctness          | Over-restriction             | Stated-policy violation      | Hedged                       |   blocked |
|:--------------|-------:|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|----------:|
| development   |     60 | 0.67 [0.46, 0.83] (24 items) | 0.67 [0.46, 0.83] (24 items) | 1.00 [1.00, 1.00] (28 items) | 0.67 [0.46, 0.83] (24 items) | 0.67 [0.46, 0.83] (24 items) | 1.00 [1.00, 1.00] (30 items) | 1.00 [1.00, 1.00] (6 items)  | 0.00 [0.00, 0.00] (18 items) | 0.00 [0.00, 0.00] (30 items) | 0.00 [0.00, 0.00] (24 items) |         0 |
| integration   |     60 | 0.67 [0.46, 0.88] (24 items) | 0.67 [0.46, 0.88] (24 items) | 1.00 [1.00, 1.00] (28 items) | 0.67 [0.46, 0.88] (24 items) | 0.67 [0.46, 0.88] (24 items) | 1.00 [1.00, 1.00] (30 items) | 1.00 [1.00, 1.00] (6 items)  | 0.00 [0.00, 0.00] (18 items) | 0.00 [0.00, 0.00] (30 items) | 0.00 [0.00, 0.00] (24 items) |         0 |
| preproduction |     60 | 0.75 [0.54, 0.92] (24 items) | 0.75 [0.54, 0.92] (24 items) | 1.00 [1.00, 1.00] (28 items) | 0.75 [0.54, 0.92] (24 items) | 1.00 [1.00, 1.00] (18 items) | 1.00 [1.00, 1.00] (30 items) | 1.00 [1.00, 1.00] (6 items)  | 0.00 [0.00, 0.00] (18 items) | 0.00 [0.00, 0.00] (30 items) | 0.00 [0.00, 0.00] (24 items) |         0 |
| production    |     60 | 1.00 [1.00, 1.00] (24 items) | 1.00 [1.00, 1.00] (24 items) | 1.00 [1.00, 1.00] (28 items) | 1.00 [1.00, 1.00] (24 items) | 1.00 [1.00, 1.00] (24 items) | 1.00 [1.00, 1.00] (30 items) | 1.00 [1.00, 1.00] (6 items)  | 0.00 [0.00, 0.00] (24 items) | 0.00 [0.00, 0.00] (30 items) | 0.00 [0.00, 0.00] (24 items) |         0 |
| postrelease   |     60 | 1.00 [1.00, 1.00] (18 items) | 1.00 [1.00, 1.00] (18 items) | 1.00 [1.00, 1.00] (28 items) | 1.00 [1.00, 1.00] (18 items) | 1.00 [1.00, 1.00] (18 items) | 1.00 [1.00, 1.00] (30 items) | 1.00 [1.00, 1.00] (12 items) | 0.00 [0.00, 0.00] (18 items) | 0.00 [0.00, 0.00] (30 items) | 0.00 [0.00, 0.00] (18 items) |         0 |


## Preregistered contrasts (b - a). faultfree = agent difference on items the reference agent solves in both packages (primary H1/H2a/b); drift = H2c over items exposed through the permission drift (fixed before treatment); exposed = the same over every post-release-exposed item (secondary); did = v1.1 difference-in-differences (secondary); costpkg = H3b by package; verdict uses the expected sign and Holm p

| family       | hyp        | outcome          | factor   | b           | a          | restrict                | method     |   expected | estimate                |   items |      p |   p_holm | verdict       |
|:-------------|:-----------|:-----------------|:---------|:------------|:-----------|:------------------------|:-----------|-----------:|:------------------------|--------:|-------:|---------:|:--------------|
| confirmatory | H1         | sar              | stage    | development | production | all                     | faultfree  |         -1 | -0.188 [-0.406, +0.031] |      16 | 0.125  |    0.878 | null          |
| confirmatory | H1         | sar              | stage    | integration | production | all                     | faultfree  |         -1 | +nan [+nan, +nan]       |       0 | 1      |    1     | not estimable |
| confirmatory | H1         | supported        | stage    | development | production | all                     | faultfree  |         -1 | -0.219 [-0.469, +0.000] |      16 | 0.0895 |    0.716 | null          |
| confirmatory | H1         | supported        | stage    | integration | production | all                     | faultfree  |         -1 | +nan [+nan, +nan]       |       0 | 1      |    1     | not estimable |
| confirmatory | H2         | correct_ans      | stage    | postrelease | production | all                     | faultfree  |         -1 | +0.056 [-0.111, +0.250] |      18 | 0.686  |    1     | null          |
| confirmatory | H2         | sar              | stage    | postrelease | production | all                     | faultfree  |         -1 | -0.028 [-0.167, +0.111] |      18 | 0.799  |    1     | null          |
| confirmatory | H2         | abcr_exposed     | stage    | postrelease | production | all                     | drift      |         -1 | -0.225 [-0.425, -0.075] |      20 | 0.008  |    0.072 | null          |
| confirmatory | H3         | abcr_exposed     | mode     | tool        | prompt     | development,postrelease | raw        |          1 | +0.054 [-0.036, +0.161] |      28 | 0.39   |    1     | null          |
| confirmatory | H3         | correct_ans      | mode     | tool        | prompt     | all                     | raw        |          0 | +0.035 [-0.056, +0.125] |      24 | 0.472  |    1     | null          |
| descriptive  | did        | sar              | stage    | development | production | all                     | did        |         -1 | -0.083 [-0.271, +0.104] |      24 | 0.423  |  nan     | nan           |
| descriptive  | did        | supported        | stage    | development | production | all                     | did        |         -1 | -0.021 [-0.250, +0.208] |      24 | 0.936  |  nan     | nan           |
| descriptive  | did        | correct_ans      | stage    | postrelease | production | all                     | did        |         -1 | +0.056 [-0.111, +0.250] |      18 | 0.686  |  nan     | nan           |
| descriptive  | did        | sar              | stage    | postrelease | production | all                     | did        |         -1 | -0.028 [-0.167, +0.111] |      18 | 0.799  |  nan     | nan           |
| descriptive  | exposedall | abcr_exposed     | stage    | postrelease | production | all                     | exposed    |         -1 | -0.196 [-0.339, -0.054] |      28 | 0.0045 |  nan     | nan           |
| descriptive  | costpkg    | correct_ans      | mode     | tool        | prompt     | development             | raw        |          0 | +0.042 [+0.000, +0.125] |      24 | 0.689  |  nan     | nan           |
| descriptive  | costpkg    | correct_ans      | mode     | tool        | prompt     | production              | raw        |          0 | +0.000 [-0.125, +0.125] |      24 | 1      |  nan     | nan           |
| descriptive  | costpkg    | correct_ans      | mode     | tool        | prompt     | postrelease             | raw        |          0 | +0.056 [-0.167, +0.278] |      18 | 0.795  |  nan     | nan           |
| descriptive  | total      | sar              | stage    | development | production | all                     | raw        |         -1 | -0.417 [-0.625, -0.188] |      24 | 0.0005 |  nan     | nan           |
| descriptive  | total      | supported        | stage    | development | production | all                     | raw        |         -1 | -0.354 [-0.562, -0.146] |      24 | 0.001  |  nan     | nan           |
| descriptive  | total      | correct_ans      | stage    | postrelease | production | all                     | raw        |         -1 | +0.056 [-0.111, +0.250] |      18 | 0.686  |  nan     | nan           |
| descriptive  | invariant  | abcr_exposed     | mode     | tool        | prompt     | production              | raw        |          1 | +0.071 [+0.000, +0.179] |      28 | 0.242  |  nan     | nan           |
| descriptive  | cost       | sar              | mode     | tool        | prompt     | all                     | raw        |          0 | +0.000 [-0.097, +0.097] |      24 | 1      |  nan     | nan           |
| descriptive  | cost       | over_restriction | mode     | tool        | prompt     | all                     | raw        |          0 | +0.000 [+0.000, +0.000] |      24 | 1      |  nan     | nan           |
| descriptive  | owndrift   | abcr_exposed     | stage    | postrelease | production | all                     | owndrift   |         -1 | -0.750 [-1.000, -0.417] |       6 | 0.0005 |  nan     | nan           |
| descriptive  | reachdrift | abcr_exposed     | stage    | postrelease | production | all                     | reachdrift |         -1 | +0.000 [+0.000, +0.000] |      14 | 1      |  nan     | nan           |
| descriptive  | covered    | abcr_covered     | mode     | tool        | prompt     | development,postrelease | raw        |          1 | +0.089 [+0.018, +0.179] |      28 | 0.02   |  nan     | nan           |
| descriptive  | open       | abcr_open        | mode     | tool        | prompt     | development,postrelease | raw        |          0 | -0.036 [-0.089, +0.000] |      28 | 0.264  |  nan     | nan           |


## H5: accuracy-only vs source/boundary-aware release gate (thresholds: accuracy .80; SuAR .80; ABCR .95)

| stage       | mode   |   accuracy |   SuAR |   ABCR | accuracy_gate   | aware_gate   | disagree   | driver   |   p_disagree |
|:------------|:-------|-----------:|-------:|-------:|:----------------|:-------------|:-----------|:---------|-------------:|
| development | prompt |      0.333 |  0.292 |  0.857 | hold            | hold         | False      |          |       0      |
| development | tool   |      0.375 |  0.333 |  0.857 | hold            | hold         | False      |          |       0      |
| postrelease | prompt |      0.722 |  0.722 |  0.714 | hold            | hold         | False      |          |       0.259  |
| postrelease | tool   |      0.778 |  0.778 |  0.821 | hold            | hold         | False      |          |       0.445  |
| production  | prompt |      0.667 |  0.667 |  0.929 | hold            | hold         | False      |          |       0.0535 |
| production  | tool   |      0.667 |  0.667 |  1     | hold            | hold         | False      |          |       0      |

P(unsupported | correct) = 0.025 [0.000, 0.075] over 20 items (2 of 76 correct runs unsupported; 2 correct runs are chance-correct, i.e. no received source yields the answer; 0 of the 74 evidenced correct runs are unsupported); Kendall tau(accuracy, SuAR) across configurations = 1.00. Item bootstrap of the gate rule: P(>=1 disagreement) = 0.57, driven by SuAR 0.00, by ABCR 0.57; p_disagree = per-configuration share of resamples.


Sensitivity (v1.3a): a gate on task success over all questions (correct answers and correct refusals) instead of answer accuracy disagrees with the aware gate on 0 configurations.

| stage       | mode   |   accuracy |   SuAR |   ABCR | accuracy_gate   | aware_gate   | disagree   | driver   |   p_disagree |
|:------------|:-------|-----------:|-------:|-------:|:----------------|:-------------|:-----------|:---------|-------------:|
| development | prompt |      0.333 |  0.292 |  0.857 | hold            | hold         | False      |          |       0      |
| development | tool   |      0.367 |  0.333 |  0.857 | hold            | hold         | False      |          |       0      |
| postrelease | prompt |      0.533 |  0.722 |  0.714 | hold            | hold         | False      |          |       0.004  |
| postrelease | tool   |      0.6   |  0.778 |  0.821 | hold            | hold         | False      |          |       0.015  |
| production  | prompt |      0.667 |  0.667 |  0.929 | hold            | hold         | False      |          |       0.05   |
| production  | tool   |      0.7   |  0.667 |  1     | hold            | hold         | False      |          |       0.0845 |


## Failure taxonomy (primary label counts)

|                           |   hallucination |   incomplete |   missed_refusal |   ok |   ok_refusal |   policy_violation |   reasoning_error |   stale_source |   wrong_source |
|:--------------------------|----------------:|-------------:|-----------------:|-----:|-------------:|-------------------:|------------------:|---------------:|---------------:|
| ('development', 'prompt') |               2 |            2 |                1 |    7 |            2 |                  4 |                 3 |              5 |              4 |
| ('development', 'tool')   |               2 |            1 |                1 |    8 |            2 |                  4 |                 3 |              8 |              1 |
| ('production', 'prompt')  |               0 |            0 |                0 |   16 |            4 |                  2 |                 5 |              0 |              3 |
| ('production', 'tool')    |               0 |            0 |                1 |   16 |            5 |                  0 |                 5 |              0 |              3 |
| ('postrelease', 'prompt') |               0 |            0 |                2 |   13 |            3 |                  8 |                 2 |              1 |              1 |
| ('postrelease', 'tool')   |               0 |            2 |                1 |   14 |            4 |                  5 |                 1 |              1 |              2 |


## Failure taxonomy, agent-attributable (runs whose seed-matched reference-agent run succeeded)

|                           |   hallucination |   incomplete |   missed_refusal |   ok |   ok_refusal |   policy_violation |   reasoning_error |   stale_source |   wrong_source |
|:--------------------------|----------------:|-------------:|-----------------:|-----:|-------------:|-------------------:|------------------:|---------------:|---------------:|
| ('development', 'prompt') |               2 |            1 |                1 |    7 |            2 |                  4 |                 3 |              0 |              2 |
| ('development', 'tool')   |               2 |            0 |                1 |    8 |            2 |                  4 |                 3 |              2 |              0 |
| ('production', 'prompt')  |               0 |            0 |                0 |   16 |            4 |                  2 |                 5 |              0 |              3 |
| ('production', 'tool')    |               0 |            0 |                1 |   16 |            5 |                  0 |                 5 |              0 |              3 |
| ('postrelease', 'prompt') |               0 |            0 |                2 |   13 |            3 |                  8 |                 2 |              1 |              1 |
| ('postrelease', 'tool')   |               0 |            2 |                1 |   14 |            4 |                  5 |                 1 |              1 |              2 |


## Accuracy and refusal by evidence reachability (injected faults vs agent behaviour; chance = credited answers that no received source yields)

|                                          |   runs |   accuracy |   refused |   chance |
|:-----------------------------------------|-------:|-----------:|----------:|---------:|
| ('development', 'missing_from_snapshot') |     12 |      0.167 |         0 |        2 |
| ('development', 'reachable')             |     36 |      0.417 |         0 |        0 |
| ('postrelease', 'reachable')             |     36 |      0.75  |         0 |        0 |
| ('production', 'reachable')              |     48 |      0.667 |         0 |        0 |


## Harness diagnostics

assistant turns 651; tool calls recovered from plain text 0; runs never calling submit_answer 0; infrastructure errors 0; blocked attempts 7; stated-policy violations 16


## Secondary models: TOTAL package and mode effects (mostly injected faults; not the agent-attributable estimand). GEE odds ratios vs production / prompt-only; VB mixed-logit intervals in models.json are approximate

- **SAR** (n=132): development OR 0.08 [0.02, 0.36]; postrelease OR 0.67 [0.19, 2.32]; tool OR 1.00 [0.52, 1.92]
- **SuAR** (n=132): development OR 0.16 [0.05, 0.51]; postrelease OR 1.54 [0.53, 4.52]; tool OR 1.19 [0.68, 2.09]
- **ABCR** (n=168): development OR 0.19 [0.03, 1.13]; postrelease OR 0.09 [0.02, 0.51]; tool OR 1.88 [0.88, 4.02]
- **Accuracy** (n=132): development OR 0.19 [0.06, 0.58]; postrelease OR 1.60 [0.54, 4.74]; tool OR 1.19 [0.68, 2.07]