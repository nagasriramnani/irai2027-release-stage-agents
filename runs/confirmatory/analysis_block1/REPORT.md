# Analysis of `qwen3-8b_confirmatory.jsonl`

Runs: 2400 (0 with unresolved infrastructure errors, excluded from inference); items: 120; model(s): ['qwen3:8b']; reference agent: observable-ideal

All intervals are item-cluster bootstrap 95% CIs (items weighted equally).


## Rates by stage x mode

| stage         | mode   |   runs | SAR                          | SuAR                         | ABCR                          | Accuracy                     | SuAR|answered                | ABCR (all runs)               | Refusal correctness          | Over-restriction             | Stated-policy violation       | Hedged                       |   blocked |
|:--------------|:-------|-------:|:-----------------------------|:-----------------------------|:------------------------------|:-----------------------------|:-----------------------------|:------------------------------|:-----------------------------|:-----------------------------|:------------------------------|:-----------------------------|----------:|
| development   | prompt |    240 | 0.61 [0.53, 0.71] (96 items) | 0.59 [0.50, 0.67] (96 items) | 0.88 [0.82, 0.93] (114 items) | 0.61 [0.52, 0.70] (96 items) | 0.61 [0.52, 0.71] (95 items) | 0.88 [0.83, 0.93] (120 items) | 0.54 [0.38, 0.71] (24 items) | 0.02 [0.00, 0.04] (78 items) | 0.00 [0.00, 0.01] (120 items) | 0.01 [0.00, 0.02] (96 items) |         0 |
| development   | tool   |    240 | 0.61 [0.53, 0.71] (96 items) | 0.58 [0.49, 0.67] (96 items) | 0.88 [0.83, 0.93] (114 items) | 0.60 [0.51, 0.69] (96 items) | 0.58 [0.49, 0.68] (96 items) | 0.89 [0.83, 0.93] (120 items) | 0.50 [0.33, 0.67] (24 items) | 0.01 [0.00, 0.03] (78 items) | 0.00 [0.00, 0.00] (120 items) | 0.01 [0.00, 0.03] (96 items) |         0 |
| integration   | prompt |    240 | 0.61 [0.52, 0.70] (96 items) | 0.61 [0.52, 0.70] (96 items) | 0.89 [0.83, 0.94] (112 items) | 0.63 [0.54, 0.72] (96 items) | 0.61 [0.52, 0.70] (96 items) | 0.90 [0.85, 0.95] (120 items) | 0.62 [0.44, 0.79] (24 items) | 0.01 [0.00, 0.02] (78 items) | 0.04 [0.01, 0.07] (120 items) | 0.00 [0.00, 0.00] (96 items) |         0 |
| integration   | tool   |    240 | 0.60 [0.51, 0.69] (96 items) | 0.58 [0.49, 0.67] (96 items) | 0.93 [0.88, 0.97] (112 items) | 0.61 [0.53, 0.70] (96 items) | 0.59 [0.49, 0.68] (96 items) | 0.93 [0.89, 0.97] (120 items) | 0.71 [0.54, 0.88] (24 items) | 0.01 [0.00, 0.02] (78 items) | 0.00 [0.00, 0.00] (120 items) | 0.00 [0.00, 0.00] (96 items) |         0 |
| preproduction | prompt |    240 | 0.79 [0.70, 0.86] (96 items) | 0.77 [0.69, 0.84] (96 items) | 0.75 [0.67, 0.82] (112 items) | 0.77 [0.69, 0.84] (96 items) | 0.77 [0.69, 0.84] (96 items) | 0.77 [0.70, 0.83] (120 items) | 0.06 [0.00, 0.15] (24 items) | 0.00 [0.00, 0.00] (84 items) | 0.33 [0.25, 0.40] (120 items) | 0.00 [0.00, 0.00] (96 items) |         0 |
| preproduction | tool   |    240 | 0.83 [0.76, 0.90] (96 items) | 0.79 [0.71, 0.86] (96 items) | 1.00 [1.00, 1.00] (112 items) | 0.81 [0.73, 0.88] (96 items) | 0.81 [0.73, 0.87] (95 items) | 1.00 [1.00, 1.00] (120 items) | 0.79 [0.65, 0.92] (24 items) | 0.01 [0.00, 0.02] (84 items) | 0.00 [0.00, 0.00] (120 items) | 0.00 [0.00, 0.00] (96 items) |         0 |
| production    | prompt |    240 | 0.93 [0.88, 0.97] (96 items) | 0.86 [0.79, 0.91] (96 items) | 0.79 [0.72, 0.86] (112 items) | 0.88 [0.82, 0.93] (96 items) | 0.86 [0.79, 0.91] (96 items) | 0.80 [0.74, 0.87] (120 items) | 0.08 [0.00, 0.21] (24 items) | 0.00 [0.00, 0.00] (96 items) | 0.20 [0.13, 0.26] (120 items) | 0.01 [0.00, 0.03] (96 items) |         0 |
| production    | tool   |    240 | 0.96 [0.92, 0.99] (96 items) | 0.88 [0.81, 0.92] (96 items) | 1.00 [1.00, 1.00] (112 items) | 0.89 [0.83, 0.93] (96 items) | 0.88 [0.82, 0.93] (96 items) | 1.00 [1.00, 1.00] (120 items) | 0.83 [0.69, 0.96] (24 items) | 0.01 [0.00, 0.02] (96 items) | 0.00 [0.00, 0.00] (120 items) | 0.01 [0.00, 0.02] (96 items) |         0 |
| postrelease   | prompt |    240 | 0.86 [0.80, 0.92] (84 items) | 0.79 [0.71, 0.86] (84 items) | 0.65 [0.57, 0.74] (108 items) | 0.81 [0.73, 0.88] (84 items) | 0.79 [0.71, 0.86] (84 items) | 0.69 [0.60, 0.76] (120 items) | 0.03 [0.00, 0.07] (36 items) | 0.00 [0.00, 0.00] (84 items) | 0.31 [0.24, 0.40] (120 items) | 0.00 [0.00, 0.00] (84 items) |         0 |
| postrelease   | tool   |    240 | 0.92 [0.86, 0.96] (84 items) | 0.85 [0.77, 0.92] (84 items) | 0.89 [0.83, 0.94] (108 items) | 0.86 [0.80, 0.92] (84 items) | 0.85 [0.77, 0.92] (84 items) | 0.90 [0.85, 0.95] (120 items) | 0.58 [0.43, 0.74] (36 items) | 0.00 [0.00, 0.00] (84 items) | 0.10 [0.05, 0.15] (120 items) | 0.00 [0.00, 0.00] (84 items) |         0 |


## Rates by profile

| profile    |   runs | SAR                          | SuAR                         | ABCR                         | Accuracy                     | SuAR|answered                | ABCR (all runs)              | Refusal correctness         | Over-restriction             | Stated-policy violation      | Hedged                       |   blocked |
|:-----------|-------:|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|----------:|
| compliance |    400 | 0.80 [0.68, 0.89] (16 items) | 0.73 [0.62, 0.82] (16 items) | 0.89 [0.83, 0.96] (20 items) | 0.74 [0.64, 0.82] (16 items) | 0.73 [0.62, 0.82] (16 items) | 0.89 [0.83, 0.96] (20 items) | 0.34 [0.11, 0.57] (6 items) | 0.00 [0.00, 0.00] (16 items) | 0.09 [0.04, 0.15] (20 items) | 0.02 [0.00, 0.04] (16 items) |         0 |
| executive  |    400 | 0.75 [0.65, 0.84] (16 items) | 0.72 [0.61, 0.82] (16 items) | 0.79 [0.65, 0.91] (18 items) | 0.74 [0.62, 0.84] (16 items) | 0.75 [0.63, 0.84] (16 items) | 0.85 [0.75, 0.93] (20 items) | 0.25 [0.05, 0.47] (6 items) | 0.03 [0.00, 0.06] (16 items) | 0.11 [0.05, 0.16] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| finance    |    400 | 0.76 [0.65, 0.86] (16 items) | 0.72 [0.58, 0.85] (16 items) | 0.90 [0.80, 0.97] (20 items) | 0.73 [0.59, 0.85] (16 items) | 0.72 [0.58, 0.85] (16 items) | 0.90 [0.80, 0.97] (20 items) | 0.43 [0.15, 0.68] (6 items) | 0.00 [0.00, 0.00] (16 items) | 0.09 [0.04, 0.15] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| hr         |    400 | 0.79 [0.71, 0.88] (16 items) | 0.74 [0.62, 0.84] (16 items) | 0.85 [0.74, 0.95] (19 items) | 0.77 [0.68, 0.85] (16 items) | 0.75 [0.62, 0.85] (16 items) | 0.86 [0.75, 0.95] (20 items) | 0.23 [0.07, 0.40] (6 items) | 0.00 [0.00, 0.00] (16 items) | 0.09 [0.04, 0.14] (20 items) | 0.00 [0.00, 0.01] (16 items) |         0 |
| operations |    400 | 0.76 [0.63, 0.87] (16 items) | 0.71 [0.54, 0.85] (16 items) | 0.89 [0.82, 0.96] (19 items) | 0.73 [0.58, 0.86] (16 items) | 0.71 [0.54, 0.85] (16 items) | 0.90 [0.83, 0.96] (20 items) | 0.41 [0.17, 0.62] (6 items) | 0.00 [0.00, 0.00] (16 items) | 0.09 [0.03, 0.15] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| sales      |    400 | 0.74 [0.63, 0.84] (16 items) | 0.73 [0.62, 0.83] (16 items) | 0.86 [0.77, 0.93] (19 items) | 0.75 [0.65, 0.83] (16 items) | 0.74 [0.62, 0.83] (16 items) | 0.86 [0.78, 0.94] (20 items) | 0.36 [0.14, 0.56] (6 items) | 0.01 [0.00, 0.02] (16 items) | 0.12 [0.06, 0.18] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |


## Rates by condition

| condition           |   runs | SAR                          | SuAR                         | ABCR                         | Accuracy                     | SuAR|answered                | ABCR (all runs)              | Refusal correctness          | Over-restriction             | Stated-policy violation      | Hedged                       |   blocked |
|:--------------------|-------:|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|----------:|
| authoritative       |    480 | 0.85 [0.80, 0.90] (24 items) | 0.82 [0.76, 0.87] (24 items) | 0.96 [0.92, 0.99] (24 items) | 0.82 [0.77, 0.88] (24 items) | 0.83 [0.78, 0.89] (24 items) | 0.96 [0.92, 0.99] (24 items) | 0.00 [0.00, 0.00] (3 items)  | 0.02 [0.00, 0.04] (24 items) | 0.05 [0.02, 0.09] (24 items) | 0.00 [0.00, 0.00] (24 items) |         0 |
| distractor          |    480 | 0.72 [0.60, 0.82] (24 items) | 0.67 [0.54, 0.79] (24 items) | 0.98 [0.95, 1.00] (23 items) | 0.72 [0.60, 0.81] (24 items) | 0.67 [0.54, 0.79] (24 items) | 0.98 [0.95, 1.00] (24 items) | 0.00 [0.00, 0.00] (3 items)  | 0.00 [0.00, 0.00] (24 items) | 0.03 [0.01, 0.06] (24 items) | 0.01 [0.00, 0.02] (24 items) |         0 |
| no_permitted_source |    480 | -                            | -                            | 0.57 [0.50, 0.65] (24 items) | -                            | -                            | 0.57 [0.50, 0.65] (24 items) | 0.51 [0.42, 0.60] (24 items) | -                            | 0.28 [0.25, 0.31] (24 items) | -                            |         0 |
| prohibited          |    480 | 0.81 [0.74, 0.87] (24 items) | 0.78 [0.70, 0.85] (24 items) | 0.90 [0.84, 0.96] (24 items) | 0.79 [0.72, 0.86] (24 items) | 0.78 [0.70, 0.86] (24 items) | 0.90 [0.84, 0.96] (24 items) | 0.00 [0.00, 0.00] (3 items)  | 0.00 [0.00, 0.01] (24 items) | 0.08 [0.04, 0.13] (24 items) | 0.00 [0.00, 0.01] (24 items) |         0 |
| stale               |    480 | 0.70 [0.61, 0.78] (24 items) | 0.64 [0.54, 0.74] (24 items) | 0.93 [0.82, 0.99] (20 items) | 0.64 [0.54, 0.74] (24 items) | 0.64 [0.54, 0.74] (24 items) | 0.97 [0.94, 0.99] (24 items) | 0.00 [0.00, 0.00] (3 items)  | 0.00 [0.00, 0.01] (24 items) | 0.04 [0.01, 0.07] (24 items) | 0.00 [0.00, 0.00] (24 items) |         0 |


## Rates by task_class

| task_class   |   runs | SAR                          | SuAR                         | ABCR                         | Accuracy                     | SuAR|answered                | ABCR (all runs)              | Refusal correctness          | Over-restriction             | Stated-policy violation      | Hedged                       |   blocked |
|:-------------|-------:|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|----------:|
| calculation  |    480 | 0.69 [0.60, 0.76] (24 items) | 0.59 [0.48, 0.70] (24 items) | 0.90 [0.83, 0.95] (23 items) | 0.61 [0.50, 0.71] (24 items) | 0.61 [0.49, 0.72] (24 items) | 0.90 [0.84, 0.95] (24 items) | 0.00 [0.00, 0.00] (4 items)  | 0.01 [0.00, 0.04] (24 items) | 0.10 [0.05, 0.15] (24 items) | 0.01 [0.00, 0.03] (24 items) |         0 |
| comparison   |    480 | 0.73 [0.62, 0.83] (24 items) | 0.66 [0.55, 0.76] (24 items) | 0.94 [0.90, 0.98] (24 items) | 0.72 [0.63, 0.79] (24 items) | 0.66 [0.55, 0.76] (24 items) | 0.94 [0.90, 0.98] (24 items) | 0.00 [0.00, 0.00] (4 items)  | 0.00 [0.00, 0.01] (24 items) | 0.05 [0.02, 0.09] (24 items) | 0.00 [0.00, 0.00] (24 items) |         0 |
| explanation  |    480 | 0.88 [0.83, 0.93] (24 items) | 0.87 [0.82, 0.92] (24 items) | 1.00 [1.00, 1.00] (20 items) | 0.87 [0.82, 0.92] (24 items) | 0.88 [0.83, 0.93] (24 items) | 1.00 [1.00, 1.00] (24 items) | -                            | 0.00 [0.00, 0.00] (24 items) | 0.01 [0.00, 0.03] (24 items) | 0.00 [0.00, 0.01] (24 items) |         0 |
| lookup       |    480 | 0.78 [0.70, 0.85] (24 items) | 0.78 [0.70, 0.85] (24 items) | 0.94 [0.85, 0.99] (24 items) | 0.78 [0.70, 0.85] (24 items) | 0.78 [0.70, 0.85] (24 items) | 0.97 [0.94, 0.99] (24 items) | 0.00 [0.00, 0.00] (4 items)  | 0.00 [0.00, 0.01] (24 items) | 0.04 [0.01, 0.08] (24 items) | 0.00 [0.00, 0.00] (24 items) |         0 |
| restricted   |    480 | -                            | -                            | 0.57 [0.50, 0.65] (24 items) | -                            | -                            | 0.57 [0.50, 0.65] (24 items) | 0.51 [0.42, 0.60] (24 items) | -                            | 0.28 [0.25, 0.31] (24 items) | -                            |         0 |


## Rates by format

| format   |   runs | SAR                          | SuAR                         | ABCR                         | Accuracy                     | SuAR|answered                | ABCR (all runs)              | Refusal correctness          | Over-restriction             | Stated-policy violation      | Hedged                       |   blocked |
|:---------|-------:|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|----------:|
| csv      |    720 | 0.77 [0.71, 0.83] (36 items) | 0.71 [0.64, 0.78] (36 items) | 0.96 [0.94, 0.99] (35 items) | 0.72 [0.65, 0.79] (36 items) | 0.72 [0.64, 0.79] (36 items) | 0.97 [0.94, 0.99] (36 items) | 0.00 [0.00, 0.00] (4 items)  | 0.00 [0.00, 0.01] (36 items) | 0.04 [0.02, 0.07] (36 items) | 0.00 [0.00, 0.00] (36 items) |         0 |
| doc      |    960 | 0.88 [0.83, 0.93] (24 items) | 0.87 [0.82, 0.92] (24 items) | 0.77 [0.70, 0.84] (44 items) | 0.87 [0.82, 0.92] (24 items) | 0.88 [0.83, 0.93] (24 items) | 0.79 [0.71, 0.86] (48 items) | 0.51 [0.42, 0.60] (24 items) | 0.00 [0.00, 0.00] (24 items) | 0.15 [0.11, 0.19] (48 items) | 0.00 [0.00, 0.01] (24 items) |         0 |
| json     |    720 | 0.69 [0.61, 0.76] (36 items) | 0.64 [0.55, 0.73] (36 items) | 0.88 [0.81, 0.94] (36 items) | 0.68 [0.59, 0.76] (36 items) | 0.65 [0.55, 0.74] (36 items) | 0.91 [0.86, 0.95] (36 items) | 0.00 [0.00, 0.00] (8 items)  | 0.01 [0.00, 0.03] (36 items) | 0.09 [0.05, 0.13] (36 items) | 0.01 [0.00, 0.02] (36 items) |         0 |


## Rates by distractor_type

| distractor_type   |   runs | SAR                         | SuAR                        | ABCR                        | Accuracy                    | SuAR|answered               | ABCR (all runs)             | Refusal correctness         | Over-restriction            | Stated-policy violation     | Hedged                      |   blocked |
|:------------------|-------:|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|:----------------------------|----------:|
| prior_period      |    180 | 0.86 [0.78, 0.94] (9 items) | 0.83 [0.77, 0.89] (9 items) | 0.95 [0.89, 1.00] (9 items) | 0.83 [0.77, 0.89] (9 items) | 0.83 [0.77, 0.89] (9 items) | 0.95 [0.89, 1.00] (9 items) | 0.00 [0.00, 0.00] (2 items) | 0.00 [0.00, 0.00] (9 items) | 0.05 [0.00, 0.11] (9 items) | 0.00 [0.00, 0.00] (9 items) |         0 |
| sister_scope      |    180 | 0.45 [0.28, 0.61] (9 items) | 0.37 [0.17, 0.57] (9 items) | 0.99 [0.97, 1.00] (9 items) | 0.50 [0.31, 0.68] (9 items) | 0.37 [0.17, 0.57] (9 items) | 0.99 [0.97, 1.00] (9 items) | 0.00 [0.00, 0.00] (1 items) | 0.00 [0.00, 0.00] (9 items) | 0.01 [0.00, 0.03] (9 items) | 0.02 [0.00, 0.05] (9 items) |         0 |


## Rates by prohibited_cue

|   prohibited_cue |   runs | SAR                          | SuAR                         | ABCR                         | Accuracy                     | SuAR|answered                | ABCR (all runs)              | Refusal correctness         | Over-restriction             | Stated-policy violation      | Hedged                       |   blocked |
|-----------------:|-------:|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|----------:|
|                0 |    240 | 0.80 [0.72, 0.87] (12 items) | 0.77 [0.65, 0.87] (12 items) | 0.86 [0.75, 0.95] (12 items) | 0.77 [0.65, 0.87] (12 items) | 0.78 [0.66, 0.87] (12 items) | 0.86 [0.75, 0.95] (12 items) | 0.00 [0.00, 0.00] (2 items) | 0.00 [0.00, 0.00] (12 items) | 0.12 [0.06, 0.19] (12 items) | 0.01 [0.00, 0.03] (12 items) |         0 |
|                1 |    240 | 0.81 [0.71, 0.92] (12 items) | 0.78 [0.67, 0.89] (12 items) | 0.95 [0.89, 1.00] (12 items) | 0.82 [0.74, 0.89] (12 items) | 0.79 [0.67, 0.89] (12 items) | 0.95 [0.89, 1.00] (12 items) | 0.00 [0.00, 0.00] (1 items) | 0.00 [0.00, 0.01] (12 items) | 0.05 [0.00, 0.10] (12 items) | 0.00 [0.00, 0.00] (12 items) |         0 |


## Rates by stage x profile

| stage         | profile    |   runs | SAR                          | SuAR                         | ABCR                         | Accuracy                     | SuAR|answered                | ABCR (all runs)              | Refusal correctness         | Over-restriction             | Stated-policy violation      | Hedged                       |   blocked |
|:--------------|:-----------|-------:|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|----------:|
| development   | compliance |     80 | 0.67 [0.47, 0.86] (16 items) | 0.52 [0.31, 0.72] (16 items) | 0.89 [0.74, 1.00] (20 items) | 0.52 [0.31, 0.72] (16 items) | 0.52 [0.31, 0.72] (16 items) | 0.89 [0.74, 1.00] (20 items) | 0.56 [0.12, 1.00] (4 items) | 0.00 [0.00, 0.00] (13 items) | 0.00 [0.00, 0.00] (20 items) | 0.05 [0.00, 0.12] (16 items) |         0 |
| development   | executive  |     80 | 0.55 [0.33, 0.73] (16 items) | 0.55 [0.33, 0.73] (16 items) | 0.84 [0.68, 1.00] (17 items) | 0.58 [0.34, 0.78] (16 items) | 0.61 [0.38, 0.81] (16 items) | 0.86 [0.71, 1.00] (20 items) | 0.44 [0.00, 0.88] (4 items) | 0.10 [0.02, 0.19] (13 items) | 0.00 [0.00, 0.00] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| development   | finance    |     80 | 0.62 [0.41, 0.84] (16 items) | 0.62 [0.41, 0.84] (16 items) | 0.91 [0.80, 1.00] (20 items) | 0.64 [0.44, 0.84] (16 items) | 0.62 [0.41, 0.84] (16 items) | 0.91 [0.80, 1.00] (20 items) | 0.69 [0.38, 1.00] (4 items) | 0.00 [0.00, 0.00] (13 items) | 0.00 [0.00, 0.00] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| development   | hr         |     80 | 0.66 [0.44, 0.84] (16 items) | 0.66 [0.44, 0.84] (16 items) | 0.82 [0.66, 0.95] (19 items) | 0.70 [0.48, 0.89] (16 items) | 0.66 [0.44, 0.84] (16 items) | 0.82 [0.68, 0.95] (20 items) | 0.12 [0.00, 0.38] (4 items) | 0.00 [0.00, 0.00] (13 items) | 0.00 [0.00, 0.00] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| development   | operations |     80 | 0.59 [0.34, 0.81] (16 items) | 0.56 [0.31, 0.78] (16 items) | 0.92 [0.84, 1.00] (19 items) | 0.59 [0.37, 0.78] (16 items) | 0.56 [0.31, 0.78] (16 items) | 0.93 [0.85, 1.00] (20 items) | 0.75 [0.50, 1.00] (4 items) | 0.00 [0.00, 0.00] (13 items) | 0.00 [0.00, 0.00] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| development   | sales      |     80 | 0.59 [0.38, 0.81] (16 items) | 0.59 [0.38, 0.81] (16 items) | 0.89 [0.75, 1.00] (19 items) | 0.59 [0.38, 0.81] (16 items) | 0.59 [0.38, 0.81] (16 items) | 0.90 [0.78, 1.00] (20 items) | 0.56 [0.12, 1.00] (4 items) | 0.00 [0.00, 0.00] (13 items) | 0.01 [0.00, 0.04] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| integration   | compliance |     80 | 0.66 [0.41, 0.88] (16 items) | 0.64 [0.41, 0.86] (16 items) | 1.00 [1.00, 1.00] (20 items) | 0.67 [0.44, 0.88] (16 items) | 0.64 [0.41, 0.86] (16 items) | 1.00 [1.00, 1.00] (20 items) | 0.88 [0.62, 1.00] (4 items) | 0.00 [0.00, 0.00] (13 items) | 0.00 [0.00, 0.00] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| integration   | executive  |     80 | 0.61 [0.36, 0.81] (16 items) | 0.61 [0.36, 0.81] (16 items) | 0.84 [0.68, 0.99] (17 items) | 0.61 [0.36, 0.81] (16 items) | 0.62 [0.41, 0.81] (16 items) | 0.86 [0.72, 0.99] (20 items) | 0.50 [0.00, 1.00] (4 items) | 0.04 [0.00, 0.12] (13 items) | 0.01 [0.00, 0.04] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| integration   | finance    |     80 | 0.55 [0.34, 0.73] (16 items) | 0.52 [0.30, 0.72] (16 items) | 0.93 [0.81, 1.00] (18 items) | 0.53 [0.31, 0.73] (16 items) | 0.52 [0.30, 0.72] (16 items) | 0.94 [0.82, 1.00] (20 items) | 0.69 [0.25, 1.00] (4 items) | 0.00 [0.00, 0.00] (13 items) | 0.01 [0.00, 0.04] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| integration   | hr         |     80 | 0.64 [0.42, 0.84] (16 items) | 0.62 [0.42, 0.81] (16 items) | 0.84 [0.68, 0.97] (19 items) | 0.69 [0.52, 0.86] (16 items) | 0.62 [0.42, 0.81] (16 items) | 0.85 [0.70, 0.97] (20 items) | 0.38 [0.00, 0.75] (4 items) | 0.00 [0.00, 0.00] (13 items) | 0.00 [0.00, 0.00] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| integration   | operations |     80 | 0.58 [0.33, 0.80] (16 items) | 0.58 [0.33, 0.80] (16 items) | 0.93 [0.86, 1.00] (19 items) | 0.58 [0.33, 0.80] (16 items) | 0.58 [0.33, 0.80] (16 items) | 0.94 [0.86, 1.00] (20 items) | 0.81 [0.56, 1.00] (4 items) | 0.00 [0.00, 0.00] (13 items) | 0.04 [0.00, 0.10] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| integration   | sales      |     80 | 0.61 [0.38, 0.81] (16 items) | 0.61 [0.38, 0.81] (16 items) | 0.91 [0.80, 0.99] (19 items) | 0.64 [0.42, 0.84] (16 items) | 0.61 [0.38, 0.81] (16 items) | 0.91 [0.82, 0.99] (20 items) | 0.75 [0.44, 1.00] (4 items) | 0.00 [0.00, 0.00] (13 items) | 0.05 [0.00, 0.11] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| preproduction | compliance |     80 | 0.83 [0.62, 0.97] (16 items) | 0.83 [0.62, 0.97] (16 items) | 0.88 [0.78, 0.96] (20 items) | 0.83 [0.62, 0.97] (16 items) | 0.83 [0.62, 0.97] (16 items) | 0.88 [0.78, 0.96] (20 items) | 0.38 [0.12, 0.50] (4 items) | 0.00 [0.00, 0.00] (14 items) | 0.17 [0.07, 0.28] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| preproduction | executive  |     80 | 0.83 [0.66, 0.97] (16 items) | 0.81 [0.64, 0.95] (16 items) | 0.85 [0.76, 0.96] (17 items) | 0.81 [0.64, 0.95] (16 items) | 0.81 [0.64, 0.95] (16 items) | 0.88 [0.79, 0.95] (20 items) | 0.31 [0.12, 0.50] (4 items) | 0.00 [0.00, 0.00] (14 items) | 0.17 [0.07, 0.26] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| preproduction | finance    |     80 | 0.80 [0.61, 0.97] (16 items) | 0.73 [0.50, 0.94] (16 items) | 0.89 [0.79, 0.97] (18 items) | 0.73 [0.50, 0.94] (16 items) | 0.73 [0.50, 0.94] (16 items) | 0.90 [0.81, 0.97] (20 items) | 0.62 [0.50, 0.75] (4 items) | 0.00 [0.00, 0.00] (14 items) | 0.15 [0.06, 0.25] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| preproduction | hr         |     80 | 0.83 [0.66, 0.98] (16 items) | 0.78 [0.58, 0.97] (16 items) | 0.88 [0.80, 0.96] (19 items) | 0.81 [0.64, 0.97] (16 items) | 0.78 [0.58, 0.97] (16 items) | 0.89 [0.80, 0.96] (20 items) | 0.38 [0.12, 0.62] (4 items) | 0.00 [0.00, 0.00] (14 items) | 0.15 [0.06, 0.25] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| preproduction | operations |     80 | 0.78 [0.56, 0.94] (16 items) | 0.75 [0.53, 0.91] (16 items) | 0.88 [0.79, 0.96] (19 items) | 0.78 [0.59, 0.94] (16 items) | 0.75 [0.53, 0.91] (16 items) | 0.89 [0.80, 0.96] (20 items) | 0.44 [0.31, 0.50] (4 items) | 0.00 [0.00, 0.00] (14 items) | 0.15 [0.05, 0.25] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| preproduction | sales      |     80 | 0.78 [0.59, 0.92] (16 items) | 0.77 [0.58, 0.91] (16 items) | 0.87 [0.78, 0.95] (19 items) | 0.77 [0.58, 0.91] (16 items) | 0.78 [0.59, 0.92] (16 items) | 0.88 [0.79, 0.95] (20 items) | 0.44 [0.31, 0.50] (4 items) | 0.02 [0.00, 0.05] (14 items) | 0.17 [0.09, 0.28] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| production    | compliance |     80 | 0.94 [0.81, 1.00] (16 items) | 0.84 [0.67, 0.97] (16 items) | 0.91 [0.82, 0.98] (20 items) | 0.86 [0.70, 0.97] (16 items) | 0.84 [0.67, 0.97] (16 items) | 0.91 [0.82, 0.98] (20 items) | 0.38 [0.12, 0.50] (4 items) | 0.00 [0.00, 0.00] (16 items) | 0.09 [0.02, 0.17] (20 items) | 0.03 [0.00, 0.09] (16 items) |         0 |
| production    | executive  |     80 | 0.94 [0.86, 1.00] (16 items) | 0.91 [0.81, 0.98] (16 items) | 0.85 [0.76, 0.96] (17 items) | 0.94 [0.86, 1.00] (16 items) | 0.91 [0.81, 0.98] (16 items) | 0.88 [0.79, 0.95] (20 items) | 0.25 [0.06, 0.44] (4 items) | 0.00 [0.00, 0.00] (16 items) | 0.12 [0.05, 0.21] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| production    | finance    |     80 | 0.94 [0.84, 1.00] (16 items) | 0.86 [0.67, 1.00] (16 items) | 0.90 [0.81, 0.99] (18 items) | 0.86 [0.67, 1.00] (16 items) | 0.86 [0.67, 1.00] (16 items) | 0.91 [0.82, 0.99] (20 items) | 0.69 [0.50, 0.94] (4 items) | 0.00 [0.00, 0.00] (16 items) | 0.09 [0.01, 0.17] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| production    | hr         |     80 | 0.98 [0.95, 1.00] (16 items) | 0.88 [0.72, 0.98] (16 items) | 0.89 [0.82, 0.97] (19 items) | 0.88 [0.72, 0.98] (16 items) | 0.88 [0.72, 0.98] (16 items) | 0.90 [0.80, 0.97] (20 items) | 0.38 [0.25, 0.50] (4 items) | 0.00 [0.00, 0.00] (16 items) | 0.10 [0.03, 0.20] (20 items) | 0.02 [0.00, 0.05] (16 items) |         0 |
| production    | operations |     80 | 0.94 [0.81, 1.00] (16 items) | 0.83 [0.64, 0.97] (16 items) | 0.91 [0.83, 0.97] (19 items) | 0.86 [0.70, 0.97] (16 items) | 0.83 [0.64, 0.97] (16 items) | 0.91 [0.82, 0.97] (20 items) | 0.56 [0.50, 0.69] (4 items) | 0.00 [0.00, 0.00] (16 items) | 0.09 [0.03, 0.17] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| production    | sales      |     80 | 0.92 [0.81, 1.00] (16 items) | 0.89 [0.77, 1.00] (16 items) | 0.89 [0.82, 0.97] (19 items) | 0.91 [0.81, 1.00] (16 items) | 0.90 [0.79, 1.00] (16 items) | 0.90 [0.80, 0.97] (20 items) | 0.50 [0.50, 0.50] (4 items) | 0.02 [0.00, 0.05] (16 items) | 0.10 [0.03, 0.20] (20 items) | 0.00 [0.00, 0.00] (16 items) |         0 |
| postrelease   | compliance |     80 | 0.91 [0.82, 1.00] (14 items) | 0.82 [0.64, 0.96] (14 items) | 0.80 [0.65, 0.93] (20 items) | 0.82 [0.64, 0.96] (14 items) | 0.82 [0.64, 0.96] (14 items) | 0.80 [0.65, 0.93] (20 items) | 0.25 [0.08, 0.42] (6 items) | 0.00 [0.00, 0.00] (14 items) | 0.20 [0.07, 0.35] (20 items) | 0.00 [0.00, 0.00] (14 items) |         0 |
| postrelease   | executive  |     80 | 0.89 [0.80, 0.96] (14 items) | 0.79 [0.61, 0.93] (14 items) | 0.72 [0.54, 0.85] (17 items) | 0.80 [0.62, 0.95] (14 items) | 0.79 [0.61, 0.93] (14 items) | 0.76 [0.61, 0.90] (20 items) | 0.25 [0.08, 0.42] (6 items) | 0.00 [0.00, 0.00] (14 items) | 0.24 [0.10, 0.39] (20 items) | 0.00 [0.00, 0.00] (14 items) |         0 |
| postrelease   | finance    |     80 | 0.93 [0.79, 1.00] (14 items) | 0.93 [0.79, 1.00] (14 items) | 0.79 [0.62, 0.93] (18 items) | 0.93 [0.79, 1.00] (14 items) | 0.93 [0.79, 1.00] (14 items) | 0.81 [0.66, 0.94] (20 items) | 0.38 [0.17, 0.58] (6 items) | 0.00 [0.00, 0.00] (14 items) | 0.19 [0.06, 0.34] (20 items) | 0.00 [0.00, 0.00] (14 items) |         0 |
| postrelease   | hr         |     80 | 0.89 [0.77, 1.00] (14 items) | 0.79 [0.62, 0.95] (14 items) | 0.79 [0.65, 0.92] (18 items) | 0.79 [0.62, 0.95] (14 items) | 0.79 [0.62, 0.95] (14 items) | 0.81 [0.68, 0.93] (20 items) | 0.33 [0.17, 0.50] (6 items) | 0.00 [0.00, 0.00] (14 items) | 0.19 [0.07, 0.33] (20 items) | 0.00 [0.00, 0.00] (14 items) |         0 |
| postrelease   | operations |     80 | 0.93 [0.79, 1.00] (14 items) | 0.82 [0.61, 1.00] (14 items) | 0.81 [0.68, 0.94] (17 items) | 0.86 [0.68, 1.00] (14 items) | 0.82 [0.61, 1.00] (14 items) | 0.84 [0.71, 0.95] (20 items) | 0.33 [0.17, 0.50] (6 items) | 0.00 [0.00, 0.00] (14 items) | 0.16 [0.05, 0.29] (20 items) | 0.00 [0.00, 0.00] (14 items) |         0 |
| postrelease   | sales      |     80 | 0.79 [0.59, 0.95] (14 items) | 0.79 [0.59, 0.95] (14 items) | 0.71 [0.53, 0.86] (18 items) | 0.82 [0.66, 0.95] (14 items) | 0.79 [0.59, 0.95] (14 items) | 0.74 [0.57, 0.88] (20 items) | 0.29 [0.12, 0.46] (6 items) | 0.00 [0.00, 0.00] (14 items) | 0.26 [0.12, 0.43] (20 items) | 0.00 [0.00, 0.00] (14 items) |         0 |


## Observable-ideal reference agent by stage (what each package's faults allow; it obeys the stated policy)

| stage         |   runs | SAR                          | SuAR                         | ABCR                          | Accuracy                     | SuAR|answered                | ABCR (all runs)               | Refusal correctness          | Over-restriction             | Stated-policy violation       | Hedged                       |   blocked |
|:--------------|-------:|:-----------------------------|:-----------------------------|:------------------------------|:-----------------------------|:-----------------------------|:------------------------------|:-----------------------------|:-----------------------------|:------------------------------|:-----------------------------|----------:|
| development   |    480 | 0.71 [0.62, 0.81] (96 items) | 0.71 [0.62, 0.81] (96 items) | 1.00 [1.00, 1.00] (114 items) | 0.71 [0.62, 0.81] (96 items) | 0.71 [0.62, 0.81] (96 items) | 1.00 [1.00, 1.00] (120 items) | 1.00 [1.00, 1.00] (24 items) | 0.00 [0.00, 0.00] (78 items) | 0.00 [0.00, 0.00] (120 items) | 0.00 [0.00, 0.00] (96 items) |         0 |
| integration   |    480 | 0.73 [0.65, 0.82] (96 items) | 0.73 [0.65, 0.82] (96 items) | 1.00 [1.00, 1.00] (112 items) | 0.73 [0.65, 0.82] (96 items) | 0.73 [0.65, 0.82] (96 items) | 1.00 [1.00, 1.00] (120 items) | 1.00 [1.00, 1.00] (24 items) | 0.00 [0.00, 0.00] (78 items) | 0.00 [0.00, 0.00] (120 items) | 0.00 [0.00, 0.00] (96 items) |         0 |
| preproduction |    480 | 0.88 [0.81, 0.94] (96 items) | 0.88 [0.81, 0.94] (96 items) | 1.00 [1.00, 1.00] (112 items) | 0.88 [0.81, 0.94] (96 items) | 1.00 [1.00, 1.00] (84 items) | 1.00 [1.00, 1.00] (120 items) | 1.00 [1.00, 1.00] (24 items) | 0.00 [0.00, 0.00] (84 items) | 0.00 [0.00, 0.00] (120 items) | 0.00 [0.00, 0.00] (96 items) |         0 |
| production    |    480 | 1.00 [1.00, 1.00] (96 items) | 1.00 [1.00, 1.00] (96 items) | 1.00 [1.00, 1.00] (112 items) | 1.00 [1.00, 1.00] (96 items) | 1.00 [1.00, 1.00] (96 items) | 1.00 [1.00, 1.00] (120 items) | 1.00 [1.00, 1.00] (24 items) | 0.00 [0.00, 0.00] (96 items) | 0.00 [0.00, 0.00] (120 items) | 0.00 [0.00, 0.00] (96 items) |         0 |
| postrelease   |    480 | 1.00 [1.00, 1.00] (84 items) | 1.00 [1.00, 1.00] (84 items) | 1.00 [1.00, 1.00] (108 items) | 1.00 [1.00, 1.00] (84 items) | 1.00 [1.00, 1.00] (84 items) | 1.00 [1.00, 1.00] (120 items) | 1.00 [1.00, 1.00] (36 items) | 0.00 [0.00, 0.00] (84 items) | 0.00 [0.00, 0.00] (120 items) | 0.00 [0.00, 0.00] (84 items) |         0 |


## Preregistered contrasts (b - a). faultfree = agent difference on items the reference agent solves in both packages (primary H1/H2a/b); drift = H2c over items exposed through the permission drift (fixed before treatment); exposed = the same over every post-release-exposed item (secondary); did = v1.1 difference-in-differences (secondary); costpkg = H3b by package; verdict uses the expected sign and Holm p

| family       | hyp        | outcome          | factor   | b           | a          | restrict                            | method     |   expected | estimate                |   items |      p |   p_holm | verdict   |
|:-------------|:-----------|:-----------------|:---------|:------------|:-----------|:------------------------------------|:-----------|-----------:|:------------------------|--------:|-------:|---------:|:----------|
| confirmatory | H1         | sar              | stage    | development | production | all                                 | faultfree  |         -1 | -0.078 [-0.138, -0.019] |      67 | 0.011  |   0.057  | null      |
| confirmatory | H1         | sar              | stage    | integration | production | all                                 | faultfree  |         -1 | -0.091 [-0.163, -0.025] |      69 | 0.008  |   0.056  | null      |
| confirmatory | H1         | supported        | stage    | development | production | all                                 | faultfree  |         -1 | -0.052 [-0.134, +0.026] |      67 | 0.217  |   0.652  | null      |
| confirmatory | H1         | supported        | stage    | integration | production | all                                 | faultfree  |         -1 | -0.033 [-0.109, +0.040] |      69 | 0.414  |   0.652  | null      |
| confirmatory | H2         | correct_ans      | stage    | postrelease | production | all                                 | faultfree  |         -1 | -0.045 [-0.092, +0.000] |      84 | 0.061  |   0.244  | null      |
| confirmatory | H2         | sar              | stage    | postrelease | production | all                                 | faultfree  |         -1 | -0.051 [-0.095, -0.012] |      84 | 0.0095 |   0.057  | null      |
| confirmatory | H2         | abcr_exposed     | stage    | postrelease | production | all                                 | drift      |         -1 | -0.274 [-0.402, -0.146] |      41 | 0.0005 |   0.0045 | supported |
| confirmatory | H3         | abcr_exposed     | mode     | tool        | prompt     | development,integration,postrelease | raw        |          1 | +0.087 [+0.057, +0.119] |     115 | 0.0005 |   0.0045 | supported |
| confirmatory | H3         | correct_ans      | mode     | tool        | prompt     | all                                 | raw        |          0 | +0.011 [-0.009, +0.031] |      96 | 0.305  |   0.652  | null      |
| descriptive  | did        | sar              | stage    | development | production | all                                 | did        |         -1 | -0.042 [-0.089, +0.003] |      96 | 0.07   | nan      | nan       |
| descriptive  | did        | sar              | stage    | integration | production | all                                 | did        |         -1 | -0.070 [-0.125, -0.023] |      96 | 0.004  | nan      | nan       |
| descriptive  | did        | supported        | stage    | development | production | all                                 | did        |         -1 | +0.003 [-0.065, +0.065] |      96 | 0.962  | nan      | nan       |
| descriptive  | did        | supported        | stage    | integration | production | all                                 | did        |         -1 | -0.005 [-0.065, +0.055] |      96 | 0.912  | nan      | nan       |
| descriptive  | did        | correct_ans      | stage    | postrelease | production | all                                 | did        |         -1 | -0.045 [-0.092, +0.000] |      84 | 0.061  | nan      | nan       |
| descriptive  | did        | sar              | stage    | postrelease | production | all                                 | did        |         -1 | -0.051 [-0.095, -0.012] |      84 | 0.0095 | nan      | nan       |
| descriptive  | exposedall | abcr_exposed     | stage    | postrelease | production | all                                 | exposed    |         -1 | -0.120 [-0.178, -0.067] |     108 | 0.0005 | nan      | nan       |
| descriptive  | costpkg    | correct_ans      | mode     | tool        | prompt     | development                         | raw        |          0 | -0.010 [-0.052, +0.026] |      96 | 0.731  | nan      | nan       |
| descriptive  | costpkg    | correct_ans      | mode     | tool        | prompt     | integration                         | raw        |          0 | -0.021 [-0.062, +0.021] |      96 | 0.394  | nan      | nan       |
| descriptive  | costpkg    | correct_ans      | mode     | tool        | prompt     | preproduction                       | raw        |          0 | +0.036 [-0.010, +0.083] |      96 | 0.154  | nan      | nan       |
| descriptive  | costpkg    | correct_ans      | mode     | tool        | prompt     | production                          | raw        |          0 | +0.005 [-0.026, +0.036] |      96 | 0.876  | nan      | nan       |
| descriptive  | costpkg    | correct_ans      | mode     | tool        | prompt     | postrelease                         | raw        |          0 | +0.054 [+0.018, +0.089] |      84 | 0.0055 | nan      | nan       |
| descriptive  | total      | sar              | stage    | development | production | all                                 | raw        |         -1 | -0.328 [-0.417, -0.240] |      96 | 0.0005 | nan      | nan       |
| descriptive  | total      | supported        | stage    | development | production | all                                 | raw        |         -1 | -0.284 [-0.378, -0.190] |      96 | 0.0005 | nan      | nan       |
| descriptive  | total      | correct_ans      | stage    | postrelease | production | all                                 | raw        |         -1 | -0.045 [-0.092, +0.000] |      84 | 0.061  | nan      | nan       |
| descriptive  | invariant  | abcr_exposed     | mode     | tool        | prompt     | production,preproduction            | raw        |          1 | +0.230 [+0.158, +0.306] |     112 | 0.0005 | nan      | nan       |
| descriptive  | cost       | sar              | mode     | tool        | prompt     | all                                 | raw        |          0 | +0.023 [+0.003, +0.045] |      96 | 0.0225 | nan      | nan       |
| descriptive  | cost       | over_restriction | mode     | tool        | prompt     | all                                 | raw        |          0 | +0.002 [-0.003, +0.008] |      96 | 0.523  | nan      | nan       |
| descriptive  | owndrift   | abcr_exposed     | stage    | postrelease | production | all                                 | owndrift   |         -1 | -0.854 [-1.000, -0.667] |      12 | 0.0005 | nan      | nan       |
| descriptive  | reachdrift | abcr_exposed     | stage    | postrelease | production | all                                 | reachdrift |         -1 | -0.034 [-0.095, +0.000] |      29 | 0.262  | nan      | nan       |
| descriptive  | covered    | abcr_covered     | mode     | tool        | prompt     | development,integration,postrelease | raw        |          1 | +0.093 [+0.064, +0.123] |     115 | 0.0005 | nan      | nan       |
| descriptive  | open       | abcr_open        | mode     | tool        | prompt     | development,integration,postrelease | raw        |          0 | -0.001 [-0.012, +0.009] |     115 | 0.757  | nan      | nan       |


## H6 (v1.4, pilot-derived, outside the Holm family): own re-classified dataset read, prompt-only, deny list by identifier with the label lagging minus labels synced: +0.125 [+0.000, +0.292], p = 0.232, sign-flip p = 0.500, 12 scenarios (2 non-zero); verdict null (null, inconclusive); read rate lagging 0.92, synced 0.79


## Stated-denied sources read, by how the deny reaches the agent (v1.4, descriptive)

| route      | description                                                                                | mode   |   rate |   lo |   hi |   scenarios |   runs |
|:-----------|:-------------------------------------------------------------------------------------------|:-------|-------:|-----:|-----:|------------:|-------:|
| Own        | identifier deny, label lags; targeted (post-release own re-classified dataset)             | prompt |   0.92 | 0.75 | 1.00 |          12 |     24 |
| Own        | identifier deny, label lags; targeted (post-release own re-classified dataset)             | tool   |   0.88 | 0.71 | 1.00 |          12 |     24 |
| Uat        | identifier deny, label permits; targeted (pre-production erroneous deny)                   | prompt |   1.00 | 1.00 | 1.00 |          12 |     24 |
| Uat        | identifier deny, label permits; targeted (pre-production erroneous deny)                   | tool   |   0.00 | 0.00 | 0.00 |          12 |     24 |
| Restricted | class deny on the label; targeted, no permitted source (production restricted questions)   | prompt |   0.88 | 0.75 | 0.98 |          24 |     48 |
| Restricted | class deny on the label; targeted, no permitted source (production restricted questions)   | tool   |   0.00 | 0.00 | 0.00 |          24 |     48 |
| Prohibited | class deny on the label; a permitted source also answers (production prohibited condition) | prompt |   0.10 | 0.02 | 0.23 |          24 |     48 |
| Prohibited | class deny on the label; a permitted source also answers (production prohibited condition) | tool   |   0.00 | 0.00 | 0.00 |          24 |     48 |


## H5: accuracy-only vs source/boundary-aware release gate (thresholds: accuracy .80; SuAR .80; ABCR .95)

| stage         | mode   |   accuracy |   SuAR |   ABCR | accuracy_gate   | aware_gate   | disagree   | driver    |   p_disagree |
|:--------------|:-------|-----------:|-------:|-------:|:----------------|:-------------|:-----------|:----------|-------------:|
| development   | prompt |      0.609 |  0.589 |  0.877 | hold            | hold         | False      |           |       0      |
| development   | tool   |      0.599 |  0.578 |  0.882 | hold            | hold         | False      |           |       0      |
| integration   | prompt |      0.63  |  0.609 |  0.893 | hold            | hold         | False      |           |       0      |
| integration   | tool   |      0.609 |  0.583 |  0.929 | hold            | hold         | False      |           |       0      |
| postrelease   | prompt |      0.81  |  0.792 |  0.653 | promote         | hold         | True       | SuAR+ABCR |       0.629  |
| postrelease   | tool   |      0.863 |  0.851 |  0.889 | promote         | hold         | True       | ABCR      |       0.962  |
| preproduction | prompt |      0.771 |  0.766 |  0.75  | hold            | hold         | False      |           |       0.25   |
| preproduction | tool   |      0.807 |  0.792 |  1     | promote         | hold         | True       | SuAR      |       0.156  |
| production    | prompt |      0.88  |  0.859 |  0.79  | promote         | hold         | True       | ABCR      |       0.995  |
| production    | tool   |      0.885 |  0.875 |  1     | promote         | promote      | False      |           |       0.0065 |

P(unsupported | correct) = 0.036 [0.011, 0.066] over 94 items (32 of 1393 correct runs unsupported; 6 correct runs are chance-correct, i.e. no received source yields the answer; 26 of the 1387 evidenced correct runs are unsupported); Kendall tau(accuracy, SuAR) across configurations = 0.98. Item bootstrap of the gate rule: P(>=1 disagreement) = 1.00, driven by SuAR 0.38, by ABCR 1.00; p_disagree = per-configuration share of resamples.


Sensitivity (v1.3a): a gate on task success over all questions (correct answers and correct refusals) instead of answer accuracy disagrees with the aware gate on 1 configurations.

| stage         | mode   |   accuracy |   SuAR |   ABCR | accuracy_gate   | aware_gate   | disagree   | driver   |   p_disagree |
|:--------------|:-------|-----------:|-------:|-------:|:----------------|:-------------|:-----------|:---------|-------------:|
| development   | prompt |      0.596 |  0.589 |  0.877 | hold            | hold         | False      |          |       0      |
| development   | tool   |      0.579 |  0.578 |  0.882 | hold            | hold         | False      |          |       0      |
| integration   | prompt |      0.629 |  0.609 |  0.893 | hold            | hold         | False      |          |       0      |
| integration   | tool   |      0.629 |  0.583 |  0.929 | hold            | hold         | False      |          |       0      |
| postrelease   | prompt |      0.575 |  0.792 |  0.653 | hold            | hold         | False      |          |       0      |
| postrelease   | tool   |      0.779 |  0.851 |  0.889 | hold            | hold         | False      |          |       0.2995 |
| preproduction | prompt |      0.629 |  0.766 |  0.75  | hold            | hold         | False      |          |       0      |
| preproduction | tool   |      0.804 |  0.792 |  1     | promote         | hold         | True       | SuAR     |       0.175  |
| production    | prompt |      0.721 |  0.859 |  0.79  | hold            | hold         | False      |          |       0.0235 |
| production    | tool   |      0.875 |  0.875 |  1     | promote         | promote      | False      |          |       0.0065 |


## Run-to-run consistency (pass^k: all repetitions succeed)

| stage         | mode   |   k |   mean Accuracy |   pass^k Accuracy |   mean SAR |   pass^k SAR |   mean ABCR |   pass^k ABCR |
|:--------------|:-------|----:|----------------:|------------------:|-----------:|-------------:|------------:|--------------:|
| development   | prompt |   2 |           0.609 |             0.531 |      0.615 |        0.542 |       0.877 |         0.833 |
| development   | tool   |   2 |           0.599 |             0.531 |      0.615 |        0.542 |       0.882 |         0.842 |
| integration   | prompt |   2 |           0.63  |             0.562 |      0.609 |        0.552 |       0.893 |         0.857 |
| integration   | tool   |   2 |           0.609 |             0.521 |      0.604 |        0.531 |       0.929 |         0.911 |
| preproduction | prompt |   2 |           0.771 |             0.708 |      0.786 |        0.74  |       0.75  |         0.696 |
| preproduction | tool   |   2 |           0.807 |             0.771 |      0.828 |        0.802 |       1     |         1     |
| production    | prompt |   2 |           0.88  |             0.823 |      0.927 |        0.906 |       0.79  |         0.768 |
| production    | tool   |   2 |           0.885 |             0.812 |      0.958 |        0.938 |       1     |         1     |
| postrelease   | prompt |   2 |           0.81  |             0.714 |      0.863 |        0.786 |       0.653 |         0.62  |
| postrelease   | tool   |   2 |           0.863 |             0.798 |      0.917 |        0.881 |       0.889 |         0.88  |


## Failure taxonomy (primary label counts)

|                             |   hedged_answer |   incomplete |   missed_refusal |   ok |   ok_refusal |   policy_violation |   reasoning_error |   safe_abstention |   stale_source |   stated_policy_violation |   unwarranted_refusal |   wrong_source |
|:----------------------------|----------------:|-------------:|-----------------:|-----:|-------------:|-------------------:|------------------:|------------------:|---------------:|--------------------------:|----------------------:|---------------:|
| ('development', 'prompt')   |               0 |            0 |                0 |  112 |           26 |                 28 |                 5 |                 2 |             56 |                         0 |                     3 |              8 |
| ('development', 'tool')     |               1 |            0 |                1 |  111 |           24 |                 27 |                 7 |                 0 |             58 |                         0 |                     2 |              9 |
| ('integration', 'prompt')   |               0 |            0 |                1 |  117 |           30 |                 24 |                 0 |                 0 |             59 |                         0 |                     1 |              8 |
| ('integration', 'tool')     |               0 |            0 |                1 |  112 |           34 |                 16 |                 4 |                 0 |             65 |                         0 |                     1 |              7 |
| ('preproduction', 'prompt') |               0 |            0 |                1 |  147 |            3 |                 56 |                 3 |                 0 |              0 |                        22 |                     0 |              8 |
| ('preproduction', 'tool')   |               0 |            0 |               10 |  152 |           38 |                  0 |                 7 |                 3 |              6 |                         0 |                     1 |             23 |
| ('production', 'prompt')    |               2 |            0 |                2 |  164 |            4 |                 47 |                13 |                 0 |              0 |                         0 |                     0 |              8 |
| ('production', 'tool')      |               1 |            1 |                7 |  168 |           40 |                  0 |                15 |                 0 |              1 |                         0 |                     1 |              6 |
| ('postrelease', 'prompt')   |               0 |            0 |                4 |  132 |            2 |                 75 |                12 |                 0 |              8 |                         0 |                     0 |              7 |
| ('postrelease', 'tool')     |               0 |            0 |                9 |  140 |           42 |                 24 |                11 |                 0 |              8 |                         0 |                     0 |              6 |


## Failure taxonomy, agent-attributable (runs whose seed-matched reference-agent run succeeded)

|                             |   hedged_answer |   incomplete |   missed_refusal |   ok |   ok_refusal |   policy_violation |   reasoning_error |   stale_source |   unwarranted_refusal |   wrong_source |
|:----------------------------|----------------:|-------------:|-----------------:|-----:|-------------:|-------------------:|------------------:|---------------:|----------------------:|---------------:|
| ('development', 'prompt')   |               0 |            0 |                0 |  112 |           26 |                 27 |                 5 |              6 |                     3 |              6 |
| ('development', 'tool')     |               1 |            0 |                1 |  111 |           24 |                 26 |                 7 |              8 |                     1 |              6 |
| ('integration', 'prompt')   |               0 |            0 |                1 |  117 |           30 |                 24 |                 0 |              8 |                     1 |              8 |
| ('integration', 'tool')     |               0 |            0 |                1 |  112 |           34 |                 16 |                 4 |             14 |                     1 |              7 |
| ('preproduction', 'prompt') |               0 |            0 |                1 |  147 |            3 |                 54 |                 3 |              0 |                     0 |              8 |
| ('preproduction', 'tool')   |               0 |            0 |               10 |  152 |           38 |                  0 |                 7 |              0 |                     1 |              8 |
| ('production', 'prompt')    |               2 |            0 |                2 |  164 |            4 |                 47 |                13 |              0 |                     0 |              8 |
| ('production', 'tool')      |               1 |            1 |                7 |  168 |           40 |                  0 |                15 |              1 |                     1 |              6 |
| ('postrelease', 'prompt')   |               0 |            0 |                4 |  132 |            2 |                 75 |                12 |              8 |                     0 |              7 |
| ('postrelease', 'tool')     |               0 |            0 |                9 |  140 |           42 |                 24 |                11 |              8 |                     0 |              6 |


## Accuracy and refusal by evidence reachability (injected faults vs agent behaviour; chance = credited answers that no received source yields)

|                                          |   runs |   accuracy |   refused |   chance |
|:-----------------------------------------|-------:|-----------:|----------:|---------:|
| ('development', 'missing_from_snapshot') |     72 |      0.014 |     0.028 |        1 |
| ('development', 'reachable')             |    312 |      0.74  |     0.016 |        0 |
| ('integration', 'old_version_served')    |     72 |      0     |     0     |        0 |
| ('integration', 'reachable')             |    312 |      0.763 |     0.006 |        3 |
| ('postrelease', 'reachable')             |    336 |      0.836 |     0     |        0 |
| ('preproduction', 'policy_denies')       |     48 |      0.042 |     0.062 |        2 |
| ('preproduction', 'reachable')           |    336 |      0.896 |     0.003 |        0 |
| ('production', 'reachable')              |    384 |      0.883 |     0.003 |        0 |


## Harness diagnostics

assistant turns 8660; tool calls recovered from plain text 934; runs never calling submit_answer 2; infrastructure errors 0; blocked attempts 0; stated-policy violations 234


## Secondary models: TOTAL package and mode effects (mostly injected faults; not the agent-attributable estimand). GEE odds ratios vs production / prompt-only; VB mixed-logit intervals in models.json are approximate

- **SAR** (n=1872): development OR 0.09 [0.04, 0.19]; integration OR 0.09 [0.04, 0.19]; postrelease OR 0.48 [0.27, 0.85]; preproduction OR 0.25 [0.13, 0.49]; tool OR 1.17 [1.02, 1.33]
- **SuAR** (n=1872): development OR 0.20 [0.12, 0.35]; integration OR 0.21 [0.12, 0.37]; postrelease OR 0.69 [0.48, 0.99]; preproduction OR 0.53 [0.35, 0.81]; tool OR 1.07 [0.95, 1.21]
- **ABCR** (n=2232): development OR 0.76 [0.42, 1.38]; integration OR 1.30 [0.64, 2.64]; postrelease OR 0.25 [0.15, 0.42]; preproduction OR 0.74 [0.60, 0.92]; tool OR 7.49 [4.79, 11.72]
- **Accuracy** (n=1872): development OR 0.19 [0.11, 0.34]; integration OR 0.21 [0.11, 0.37]; postrelease OR 0.67 [0.45, 0.99]; preproduction OR 0.49 [0.32, 0.75]; tool OR 1.07 [0.95, 1.20]