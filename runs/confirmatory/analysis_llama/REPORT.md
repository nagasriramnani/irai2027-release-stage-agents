# Analysis of `llama3.1-8b_confirmatory.jsonl`, `llama3.1-8b_confirmatory_b2.jsonl`, `llama3.1-8b_confirmatory_b3.jsonl`, `llama3.1-8b_confirmatory_b4.jsonl`, `llama3.1-8b_confirmatory_b5.jsonl`, `llama3.1-8b_confirmatory_b6.jsonl`

Runs: 4320 (0 with unresolved infrastructure errors, excluded from inference); items: 720; model(s): ['llama3.1-tools:8b']; reference agent: observable-ideal

All intervals are item-cluster bootstrap 95% CIs (items weighted equally).


## Rates by stage x mode

| stage       | mode   |   runs | SAR                           | SuAR                          | ABCR                          | Accuracy                      | SuAR|answered                 | ABCR (all runs)               | Refusal correctness           | Over-restriction              | Stated-policy violation       | Hedged                        |   blocked |
|:------------|:-------|-------:|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|----------:|
| development | prompt |    720 | 0.49 [0.45, 0.53] (576 items) | 0.37 [0.33, 0.41] (576 items) | 0.87 [0.84, 0.89] (667 items) | 0.43 [0.39, 0.47] (576 items) | 0.40 [0.35, 0.44] (539 items) | 0.88 [0.85, 0.90] (720 items) | 0.35 [0.28, 0.44] (144 items) | 0.03 [0.01, 0.05] (468 items) | 0.02 [0.01, 0.03] (720 items) | 0.00 [0.00, 0.00] (576 items) |         0 |
| development | tool   |    720 | 0.50 [0.46, 0.54] (576 items) | 0.35 [0.32, 0.39] (576 items) | 0.89 [0.86, 0.91] (667 items) | 0.41 [0.38, 0.45] (576 items) | 0.37 [0.34, 0.41] (545 items) | 0.89 [0.87, 0.92] (720 items) | 0.32 [0.24, 0.40] (144 items) | 0.02 [0.01, 0.03] (468 items) | 0.00 [0.00, 0.00] (720 items) | 0.00 [0.00, 0.00] (576 items) |         2 |
| production  | prompt |    720 | 0.84 [0.81, 0.87] (576 items) | 0.61 [0.57, 0.65] (576 items) | 0.86 [0.84, 0.89] (664 items) | 0.62 [0.59, 0.66] (576 items) | 0.61 [0.57, 0.65] (575 items) | 0.87 [0.85, 0.90] (720 items) | 0.29 [0.22, 0.37] (144 items) | 0.00 [0.00, 0.00] (576 items) | 0.13 [0.10, 0.15] (720 items) | 0.00 [0.00, 0.00] (576 items) |         0 |
| production  | tool   |    720 | 0.86 [0.83, 0.89] (576 items) | 0.61 [0.57, 0.64] (576 items) | 1.00 [1.00, 1.00] (664 items) | 0.63 [0.59, 0.66] (576 items) | 0.61 [0.57, 0.65] (574 items) | 1.00 [1.00, 1.00] (720 items) | 0.56 [0.48, 0.64] (144 items) | 0.00 [0.00, 0.01] (576 items) | 0.00 [0.00, 0.00] (720 items) | 0.00 [0.00, 0.00] (576 items) |         1 |
| postrelease | prompt |    720 | 0.88 [0.86, 0.91] (504 items) | 0.65 [0.61, 0.69] (504 items) | 0.72 [0.69, 0.76] (654 items) | 0.67 [0.63, 0.71] (504 items) | 0.65 [0.61, 0.69] (503 items) | 0.75 [0.72, 0.78] (720 items) | 0.12 [0.08, 0.16] (216 items) | 0.00 [0.00, 0.01] (504 items) | 0.25 [0.22, 0.28] (720 items) | 0.00 [0.00, 0.00] (504 items) |         0 |
| postrelease | tool   |    720 | 0.86 [0.83, 0.89] (504 items) | 0.64 [0.60, 0.68] (504 items) | 0.88 [0.86, 0.91] (654 items) | 0.65 [0.61, 0.69] (504 items) | 0.64 [0.60, 0.68] (504 items) | 0.89 [0.87, 0.91] (720 items) | 0.31 [0.24, 0.37] (216 items) | 0.00 [0.00, 0.00] (504 items) | 0.11 [0.09, 0.13] (720 items) | 0.00 [0.00, 0.00] (504 items) |        25 |


## Rates by profile

| profile    |   runs | SAR                          | SuAR                         | ABCR                          | Accuracy                     | SuAR|answered                | ABCR (all runs)               | Refusal correctness          | Over-restriction             | Stated-policy violation       | Hedged                       |   blocked |
|:-----------|-------:|:-----------------------------|:-----------------------------|:------------------------------|:-----------------------------|:-----------------------------|:------------------------------|:-----------------------------|:-----------------------------|:------------------------------|:-----------------------------|----------:|
| compliance |    720 | 0.77 [0.72, 0.82] (96 items) | 0.59 [0.51, 0.67] (96 items) | 0.88 [0.85, 0.92] (116 items) | 0.62 [0.54, 0.70] (96 items) | 0.60 [0.52, 0.67] (96 items) | 0.89 [0.86, 0.92] (120 items) | 0.22 [0.13, 0.31] (36 items) | 0.01 [0.00, 0.02] (96 items) | 0.08 [0.06, 0.11] (120 items) | 0.00 [0.00, 0.00] (96 items) |         3 |
| executive  |    720 | 0.62 [0.56, 0.67] (96 items) | 0.46 [0.39, 0.53] (96 items) | 0.82 [0.77, 0.87] (102 items) | 0.53 [0.46, 0.60] (96 items) | 0.47 [0.40, 0.54] (96 items) | 0.85 [0.81, 0.89] (120 items) | 0.24 [0.16, 0.31] (36 items) | 0.02 [0.01, 0.03] (96 items) | 0.10 [0.07, 0.13] (120 items) | 0.00 [0.00, 0.00] (96 items) |         1 |
| finance    |    720 | 0.77 [0.71, 0.82] (96 items) | 0.52 [0.45, 0.60] (96 items) | 0.89 [0.85, 0.93] (117 items) | 0.54 [0.46, 0.62] (96 items) | 0.53 [0.45, 0.61] (96 items) | 0.90 [0.86, 0.93] (120 items) | 0.29 [0.19, 0.38] (36 items) | 0.01 [0.00, 0.02] (96 items) | 0.08 [0.05, 0.10] (120 items) | 0.00 [0.00, 0.00] (96 items) |         8 |
| hr         |    720 | 0.78 [0.74, 0.83] (96 items) | 0.57 [0.49, 0.64] (96 items) | 0.85 [0.81, 0.89] (112 items) | 0.60 [0.52, 0.67] (96 items) | 0.57 [0.49, 0.64] (96 items) | 0.87 [0.83, 0.90] (120 items) | 0.10 [0.05, 0.15] (36 items) | 0.00 [0.00, 0.00] (96 items) | 0.09 [0.07, 0.12] (120 items) | 0.00 [0.00, 0.00] (96 items) |         0 |
| operations |    720 | 0.73 [0.68, 0.78] (96 items) | 0.53 [0.45, 0.60] (96 items) | 0.88 [0.85, 0.91] (117 items) | 0.56 [0.48, 0.63] (96 items) | 0.55 [0.47, 0.62] (96 items) | 0.88 [0.85, 0.91] (120 items) | 0.31 [0.21, 0.41] (36 items) | 0.01 [0.00, 0.03] (96 items) | 0.08 [0.05, 0.10] (120 items) | 0.00 [0.00, 0.00] (96 items) |         3 |
| sales      |    720 | 0.71 [0.66, 0.76] (96 items) | 0.50 [0.43, 0.58] (96 items) | 0.88 [0.84, 0.92] (115 items) | 0.53 [0.45, 0.60] (96 items) | 0.51 [0.44, 0.59] (96 items) | 0.89 [0.86, 0.93] (120 items) | 0.29 [0.19, 0.38] (36 items) | 0.00 [0.00, 0.01] (96 items) | 0.07 [0.05, 0.09] (120 items) | 0.00 [0.00, 0.00] (96 items) |        13 |


## Rates by condition

| condition           |   runs | SAR                           | SuAR                          | ABCR                          | Accuracy                      | SuAR|answered                 | ABCR (all runs)               | Refusal correctness           | Over-restriction              | Stated-policy violation       | Hedged                        |   blocked |
|:--------------------|-------:|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|----------:|
| authoritative       |    864 | 0.79 [0.75, 0.84] (144 items) | 0.56 [0.50, 0.62] (144 items) | 0.94 [0.91, 0.97] (134 items) | 0.59 [0.52, 0.65] (144 items) | 0.57 [0.51, 0.63] (144 items) | 0.95 [0.94, 0.97] (144 items) | 0.00 [0.00, 0.00] (18 items)  | 0.00 [0.00, 0.01] (144 items) | 0.04 [0.02, 0.06] (144 items) | 0.00 [0.00, 0.00] (144 items) |         1 |
| distractor          |    864 | 0.64 [0.58, 0.69] (144 items) | 0.49 [0.42, 0.55] (144 items) | 0.96 [0.94, 0.97] (132 items) | 0.54 [0.47, 0.60] (144 items) | 0.50 [0.43, 0.56] (144 items) | 0.96 [0.94, 0.98] (144 items) | 0.00 [0.00, 0.00] (18 items)  | 0.01 [0.00, 0.02] (144 items) | 0.03 [0.02, 0.05] (144 items) | 0.00 [0.00, 0.00] (144 items) |         0 |
| no_permitted_source |    864 | -                             | -                             | 0.61 [0.58, 0.65] (144 items) | -                             | -                             | 0.61 [0.58, 0.65] (144 items) | 0.36 [0.32, 0.40] (144 items) | -                             | 0.25 [0.23, 0.27] (144 items) | -                             |        27 |
| prohibited          |    864 | 0.80 [0.76, 0.83] (144 items) | 0.57 [0.51, 0.63] (144 items) | 0.92 [0.90, 0.95] (144 items) | 0.60 [0.53, 0.66] (144 items) | 0.58 [0.51, 0.64] (144 items) | 0.92 [0.90, 0.95] (144 items) | 0.00 [0.00, 0.00] (18 items)  | 0.01 [0.00, 0.02] (144 items) | 0.06 [0.04, 0.08] (144 items) | 0.00 [0.00, 0.00] (144 items) |         0 |
| stale               |    864 | 0.69 [0.66, 0.72] (144 items) | 0.50 [0.44, 0.55] (144 items) | 0.94 [0.90, 0.97] (125 items) | 0.53 [0.47, 0.59] (144 items) | 0.50 [0.45, 0.56] (144 items) | 0.96 [0.94, 0.97] (144 items) | 0.00 [0.00, 0.00] (18 items)  | 0.01 [0.00, 0.02] (144 items) | 0.04 [0.02, 0.06] (144 items) | 0.00 [0.00, 0.00] (144 items) |         0 |


## Rates by task_class

| task_class   |   runs | SAR                           | SuAR                          | ABCR                          | Accuracy                      | SuAR|answered                 | ABCR (all runs)               | Refusal correctness           | Over-restriction              | Stated-policy violation       | Hedged                        |   blocked |
|:-------------|-------:|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|----------:|
| calculation  |    864 | 0.67 [0.62, 0.71] (144 items) | 0.11 [0.07, 0.15] (144 items) | 0.91 [0.88, 0.94] (140 items) | 0.12 [0.08, 0.16] (144 items) | 0.11 [0.08, 0.16] (144 items) | 0.93 [0.91, 0.95] (144 items) | 0.00 [0.00, 0.00] (24 items)  | 0.02 [0.01, 0.03] (144 items) | 0.06 [0.04, 0.08] (144 items) | 0.00 [0.00, 0.00] (144 items) |         1 |
| comparison   |    864 | 0.70 [0.65, 0.75] (144 items) | 0.54 [0.48, 0.60] (144 items) | 0.91 [0.88, 0.94] (140 items) | 0.66 [0.60, 0.72] (144 items) | 0.54 [0.48, 0.60] (144 items) | 0.92 [0.89, 0.95] (144 items) | 0.00 [0.00, 0.00] (24 items)  | 0.00 [0.00, 0.00] (144 items) | 0.07 [0.05, 0.09] (144 items) | 0.00 [0.00, 0.00] (144 items) |         0 |
| explanation  |    864 | 0.81 [0.77, 0.84] (144 items) | 0.73 [0.68, 0.77] (144 items) | 1.00 [1.00, 1.00] (113 items) | 0.73 [0.68, 0.78] (144 items) | 0.73 [0.68, 0.77] (144 items) | 1.00 [1.00, 1.00] (144 items) | -                             | 0.00 [0.00, 0.00] (144 items) | 0.00 [0.00, 0.00] (144 items) | 0.00 [0.00, 0.00] (144 items) |         0 |
| lookup       |    864 | 0.74 [0.70, 0.78] (144 items) | 0.74 [0.69, 0.78] (144 items) | 0.94 [0.92, 0.97] (142 items) | 0.74 [0.70, 0.78] (144 items) | 0.76 [0.71, 0.80] (144 items) | 0.95 [0.93, 0.97] (144 items) | 0.00 [0.00, 0.00] (24 items)  | 0.01 [0.01, 0.02] (144 items) | 0.05 [0.03, 0.06] (144 items) | 0.00 [0.00, 0.00] (144 items) |         0 |
| restricted   |    864 | -                             | -                             | 0.61 [0.58, 0.65] (144 items) | -                             | -                             | 0.61 [0.58, 0.65] (144 items) | 0.36 [0.32, 0.40] (144 items) | -                             | 0.25 [0.23, 0.27] (144 items) | -                             |        27 |


## Rates by format

| format   |   runs | SAR                           | SuAR                          | ABCR                          | Accuracy                      | SuAR|answered                 | ABCR (all runs)               | Refusal correctness           | Over-restriction              | Stated-policy violation       | Hedged                        |   blocked |
|:---------|-------:|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|----------:|
| csv      |   1296 | 0.76 [0.73, 0.79] (216 items) | 0.46 [0.41, 0.52] (216 items) | 0.95 [0.93, 0.97] (211 items) | 0.49 [0.43, 0.54] (216 items) | 0.47 [0.42, 0.52] (216 items) | 0.96 [0.94, 0.97] (216 items) | 0.00 [0.00, 0.00] (30 items)  | 0.01 [0.00, 0.02] (216 items) | 0.04 [0.03, 0.05] (216 items) | 0.00 [0.00, 0.00] (216 items) |         0 |
| doc      |   1728 | 0.81 [0.77, 0.84] (144 items) | 0.73 [0.68, 0.77] (144 items) | 0.78 [0.75, 0.81] (257 items) | 0.73 [0.68, 0.78] (144 items) | 0.73 [0.68, 0.77] (144 items) | 0.80 [0.78, 0.83] (288 items) | 0.36 [0.32, 0.40] (144 items) | 0.00 [0.00, 0.00] (144 items) | 0.12 [0.11, 0.14] (288 items) | 0.00 [0.00, 0.00] (144 items) |        27 |
| json     |   1296 | 0.65 [0.61, 0.69] (216 items) | 0.46 [0.41, 0.51] (216 items) | 0.90 [0.87, 0.92] (211 items) | 0.52 [0.47, 0.57] (216 items) | 0.47 [0.42, 0.52] (216 items) | 0.91 [0.89, 0.93] (216 items) | 0.00 [0.00, 0.00] (42 items)  | 0.01 [0.01, 0.02] (216 items) | 0.07 [0.06, 0.09] (216 items) | 0.00 [0.00, 0.00] (216 items) |         1 |


## Rates by distractor_type

| distractor_type   |   runs | SAR                          | SuAR                         | ABCR                         | Accuracy                     | SuAR|answered                | ABCR (all runs)              | Refusal correctness         | Over-restriction             | Stated-policy violation      | Hedged                       |   blocked |
|:------------------|-------:|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|----------:|
| prior_period      |    324 | 0.79 [0.73, 0.85] (54 items) | 0.57 [0.47, 0.67] (54 items) | 0.94 [0.91, 0.98] (54 items) | 0.59 [0.48, 0.70] (54 items) | 0.58 [0.47, 0.68] (54 items) | 0.94 [0.91, 0.98] (54 items) | 0.00 [0.00, 0.00] (9 items) | 0.01 [0.00, 0.02] (54 items) | 0.05 [0.02, 0.08] (54 items) | 0.00 [0.00, 0.00] (54 items) |         0 |
| sister_scope      |    324 | 0.38 [0.30, 0.47] (54 items) | 0.23 [0.16, 0.32] (54 items) | 0.95 [0.92, 0.98] (52 items) | 0.33 [0.25, 0.42] (54 items) | 0.25 [0.17, 0.33] (54 items) | 0.95 [0.92, 0.98] (54 items) | 0.00 [0.00, 0.00] (9 items) | 0.01 [0.00, 0.03] (54 items) | 0.05 [0.02, 0.08] (54 items) | 0.00 [0.00, 0.00] (54 items) |         0 |


## Rates by prohibited_cue

|   prohibited_cue |   runs | SAR                          | SuAR                         | ABCR                         | Accuracy                     | SuAR|answered                | ABCR (all runs)              | Refusal correctness         | Over-restriction             | Stated-policy violation      | Hedged                       |   blocked |
|-----------------:|-------:|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|:----------------------------|:-----------------------------|:-----------------------------|:-----------------------------|----------:|
|                0 |    432 | 0.76 [0.70, 0.81] (72 items) | 0.56 [0.47, 0.64] (72 items) | 0.91 [0.87, 0.94] (72 items) | 0.60 [0.52, 0.69] (72 items) | 0.57 [0.48, 0.65] (72 items) | 0.91 [0.87, 0.94] (72 items) | 0.00 [0.00, 0.00] (9 items) | 0.01 [0.00, 0.03] (72 items) | 0.06 [0.04, 0.09] (72 items) | 0.00 [0.00, 0.00] (72 items) |         0 |
|                1 |    432 | 0.83 [0.78, 0.88] (72 items) | 0.58 [0.49, 0.68] (72 items) | 0.94 [0.91, 0.97] (72 items) | 0.59 [0.49, 0.68] (72 items) | 0.58 [0.49, 0.68] (72 items) | 0.94 [0.91, 0.97] (72 items) | 0.00 [0.00, 0.00] (9 items) | 0.00 [0.00, 0.01] (72 items) | 0.05 [0.03, 0.08] (72 items) | 0.00 [0.00, 0.00] (72 items) |         0 |


## Rates by stage x profile

| stage       | profile    |   runs | SAR                          | SuAR                         | ABCR                          | Accuracy                     | SuAR|answered                | ABCR (all runs)               | Refusal correctness          | Over-restriction             | Stated-policy violation       | Hedged                       |   blocked |
|:------------|:-----------|-------:|:-----------------------------|:-----------------------------|:------------------------------|:-----------------------------|:-----------------------------|:------------------------------|:-----------------------------|:-----------------------------|:------------------------------|:-----------------------------|----------:|
| development | compliance |    240 | 0.59 [0.49, 0.68] (96 items) | 0.45 [0.35, 0.55] (96 items) | 0.92 [0.87, 0.96] (113 items) | 0.49 [0.39, 0.58] (96 items) | 0.47 [0.38, 0.57] (92 items) | 0.92 [0.87, 0.96] (120 items) | 0.44 [0.27, 0.62] (24 items) | 0.03 [0.00, 0.06] (78 items) | 0.01 [0.00, 0.02] (120 items) | 0.00 [0.00, 0.00] (96 items) |         0 |
| development | executive  |    240 | 0.36 [0.28, 0.45] (96 items) | 0.27 [0.19, 0.35] (96 items) | 0.81 [0.74, 0.88] (99 items)  | 0.38 [0.30, 0.47] (96 items) | 0.29 [0.21, 0.39] (92 items) | 0.85 [0.78, 0.90] (120 items) | 0.33 [0.17, 0.50] (24 items) | 0.05 [0.02, 0.09] (78 items) | 0.01 [0.00, 0.02] (120 items) | 0.00 [0.00, 0.00] (96 items) |         0 |
| development | finance    |    240 | 0.58 [0.49, 0.68] (96 items) | 0.39 [0.30, 0.49] (96 items) | 0.92 [0.87, 0.96] (115 items) | 0.42 [0.33, 0.52] (96 items) | 0.40 [0.32, 0.49] (93 items) | 0.92 [0.87, 0.96] (120 items) | 0.48 [0.29, 0.67] (24 items) | 0.02 [0.00, 0.05] (78 items) | 0.01 [0.00, 0.02] (120 items) | 0.00 [0.00, 0.00] (96 items) |         1 |
| development | hr         |    240 | 0.54 [0.44, 0.64] (96 items) | 0.40 [0.30, 0.49] (96 items) | 0.87 [0.81, 0.93] (109 items) | 0.47 [0.38, 0.57] (96 items) | 0.40 [0.31, 0.52] (94 items) | 0.88 [0.82, 0.94] (120 items) | 0.00 [0.00, 0.00] (24 items) | 0.00 [0.00, 0.00] (78 items) | 0.00 [0.00, 0.00] (120 items) | 0.00 [0.00, 0.00] (96 items) |         0 |
| development | operations |    240 | 0.47 [0.38, 0.56] (96 items) | 0.36 [0.27, 0.45] (96 items) | 0.87 [0.81, 0.92] (117 items) | 0.42 [0.33, 0.52] (96 items) | 0.40 [0.31, 0.49] (91 items) | 0.87 [0.82, 0.92] (120 items) | 0.44 [0.27, 0.62] (24 items) | 0.05 [0.01, 0.10] (78 items) | 0.01 [0.00, 0.03] (120 items) | 0.00 [0.00, 0.00] (96 items) |         1 |
| development | sales      |    240 | 0.43 [0.34, 0.52] (96 items) | 0.30 [0.22, 0.39] (96 items) | 0.87 [0.82, 0.93] (114 items) | 0.35 [0.27, 0.43] (96 items) | 0.31 [0.22, 0.40] (96 items) | 0.88 [0.82, 0.93] (120 items) | 0.33 [0.17, 0.54] (24 items) | 0.00 [0.00, 0.00] (78 items) | 0.01 [0.00, 0.03] (120 items) | 0.00 [0.00, 0.00] (96 items) |         0 |
| production  | compliance |    240 | 0.87 [0.81, 0.93] (96 items) | 0.65 [0.57, 0.74] (96 items) | 0.92 [0.89, 0.96] (113 items) | 0.67 [0.58, 0.77] (96 items) | 0.65 [0.57, 0.74] (96 items) | 0.93 [0.90, 0.96] (120 items) | 0.27 [0.17, 0.40] (24 items) | 0.00 [0.00, 0.00] (96 items) | 0.07 [0.04, 0.10] (120 items) | 0.00 [0.00, 0.00] (96 items) |         0 |
| production  | executive  |    240 | 0.72 [0.65, 0.80] (96 items) | 0.56 [0.47, 0.65] (96 items) | 0.88 [0.84, 0.92] (99 items)  | 0.61 [0.52, 0.70] (96 items) | 0.56 [0.47, 0.65] (96 items) | 0.90 [0.87, 0.94] (120 items) | 0.40 [0.29, 0.52] (24 items) | 0.00 [0.00, 0.00] (96 items) | 0.10 [0.06, 0.13] (120 items) | 0.00 [0.00, 0.00] (96 items) |         0 |
| production  | finance    |    240 | 0.85 [0.79, 0.91] (96 items) | 0.57 [0.48, 0.67] (96 items) | 0.94 [0.91, 0.97] (112 items) | 0.58 [0.49, 0.67] (96 items) | 0.58 [0.48, 0.67] (96 items) | 0.95 [0.92, 0.97] (120 items) | 0.50 [0.38, 0.60] (24 items) | 0.01 [0.00, 0.03] (96 items) | 0.05 [0.03, 0.08] (120 items) | 0.00 [0.00, 0.00] (96 items) |         0 |
| production  | hr         |    240 | 0.92 [0.87, 0.96] (96 items) | 0.66 [0.57, 0.74] (96 items) | 0.93 [0.89, 0.96] (109 items) | 0.66 [0.57, 0.74] (96 items) | 0.66 [0.57, 0.74] (96 items) | 0.93 [0.90, 0.96] (120 items) | 0.25 [0.15, 0.35] (24 items) | 0.00 [0.00, 0.00] (96 items) | 0.07 [0.04, 0.10] (120 items) | 0.00 [0.00, 0.00] (96 items) |         0 |
| production  | operations |    240 | 0.89 [0.83, 0.95] (96 items) | 0.60 [0.51, 0.69] (96 items) | 0.95 [0.93, 0.98] (117 items) | 0.61 [0.52, 0.70] (96 items) | 0.60 [0.51, 0.69] (96 items) | 0.95 [0.93, 0.98] (120 items) | 0.56 [0.42, 0.69] (24 items) | 0.00 [0.00, 0.00] (96 items) | 0.05 [0.02, 0.07] (120 items) | 0.00 [0.00, 0.00] (96 items) |         0 |
| production  | sales      |    240 | 0.86 [0.79, 0.92] (96 items) | 0.60 [0.52, 0.70] (96 items) | 0.95 [0.93, 0.98] (114 items) | 0.62 [0.53, 0.71] (96 items) | 0.61 [0.53, 0.70] (96 items) | 0.95 [0.93, 0.98] (120 items) | 0.58 [0.46, 0.71] (24 items) | 0.00 [0.00, 0.00] (96 items) | 0.05 [0.02, 0.07] (120 items) | 0.00 [0.00, 0.00] (96 items) |         1 |
| postrelease | compliance |    240 | 0.89 [0.83, 0.95] (84 items) | 0.71 [0.62, 0.81] (84 items) | 0.82 [0.76, 0.88] (114 items) | 0.73 [0.64, 0.83] (84 items) | 0.71 [0.62, 0.81] (84 items) | 0.83 [0.77, 0.88] (120 items) | 0.18 [0.08, 0.28] (36 items) | 0.00 [0.00, 0.00] (84 items) | 0.17 [0.12, 0.23] (120 items) | 0.00 [0.00, 0.00] (84 items) |         3 |
| postrelease | executive  |    240 | 0.80 [0.72, 0.87] (84 items) | 0.60 [0.50, 0.69] (84 items) | 0.76 [0.69, 0.83] (99 items)  | 0.64 [0.55, 0.73] (84 items) | 0.60 [0.50, 0.69] (84 items) | 0.80 [0.75, 0.86] (120 items) | 0.22 [0.12, 0.33] (36 items) | 0.00 [0.00, 0.00] (84 items) | 0.20 [0.14, 0.25] (120 items) | 0.00 [0.00, 0.00] (84 items) |         1 |
| postrelease | finance    |    240 | 0.89 [0.83, 0.95] (84 items) | 0.62 [0.52, 0.72] (84 items) | 0.82 [0.76, 0.88] (112 items) | 0.63 [0.53, 0.73] (84 items) | 0.62 [0.52, 0.72] (84 items) | 0.83 [0.77, 0.88] (120 items) | 0.21 [0.11, 0.31] (36 items) | 0.00 [0.00, 0.00] (84 items) | 0.17 [0.12, 0.23] (120 items) | 0.00 [0.00, 0.00] (84 items) |         7 |
| postrelease | hr         |    240 | 0.93 [0.88, 0.97] (84 items) | 0.67 [0.57, 0.76] (84 items) | 0.77 [0.70, 0.83] (110 items) | 0.67 [0.57, 0.76] (84 items) | 0.67 [0.57, 0.76] (84 items) | 0.79 [0.72, 0.85] (120 items) | 0.12 [0.06, 0.19] (36 items) | 0.00 [0.00, 0.00] (84 items) | 0.21 [0.15, 0.28] (120 items) | 0.00 [0.00, 0.00] (84 items) |         0 |
| postrelease | operations |    240 | 0.85 [0.77, 0.92] (84 items) | 0.63 [0.53, 0.74] (84 items) | 0.81 [0.75, 0.87] (108 items) | 0.64 [0.54, 0.74] (84 items) | 0.63 [0.53, 0.74] (84 items) | 0.83 [0.77, 0.88] (120 items) | 0.28 [0.17, 0.40] (36 items) | 0.00 [0.00, 0.00] (84 items) | 0.17 [0.12, 0.23] (120 items) | 0.00 [0.00, 0.00] (84 items) |         2 |
| postrelease | sales      |    240 | 0.86 [0.79, 0.93] (84 items) | 0.62 [0.52, 0.73] (84 items) | 0.83 [0.78, 0.89] (111 items) | 0.64 [0.54, 0.74] (84 items) | 0.62 [0.52, 0.73] (84 items) | 0.85 [0.79, 0.90] (120 items) | 0.25 [0.15, 0.35] (36 items) | 0.01 [0.00, 0.02] (84 items) | 0.15 [0.10, 0.21] (120 items) | 0.00 [0.00, 0.00] (84 items) |        12 |


## Rates by block

|   block |   runs | SAR                          | SuAR                         | ABCR                          | Accuracy                     | SuAR|answered                | ABCR (all runs)               | Refusal correctness          | Over-restriction             | Stated-policy violation       | Hedged                       |   blocked |
|--------:|-------:|:-----------------------------|:-----------------------------|:------------------------------|:-----------------------------|:-----------------------------|:------------------------------|:-----------------------------|:-----------------------------|:------------------------------|:-----------------------------|----------:|
|       1 |    720 | 0.73 [0.68, 0.78] (96 items) | 0.51 [0.43, 0.58] (96 items) | 0.84 [0.80, 0.89] (115 items) | 0.54 [0.46, 0.61] (96 items) | 0.51 [0.44, 0.59] (96 items) | 0.86 [0.82, 0.89] (120 items) | 0.23 [0.15, 0.31] (36 items) | 0.00 [0.00, 0.01] (96 items) | 0.10 [0.07, 0.13] (120 items) | 0.00 [0.00, 0.00] (96 items) |         4 |
|       2 |    720 | 0.76 [0.71, 0.80] (96 items) | 0.54 [0.46, 0.62] (96 items) | 0.86 [0.82, 0.90] (115 items) | 0.57 [0.49, 0.65] (96 items) | 0.55 [0.47, 0.62] (96 items) | 0.88 [0.85, 0.91] (120 items) | 0.24 [0.16, 0.33] (36 items) | 0.01 [0.00, 0.01] (96 items) | 0.09 [0.06, 0.11] (120 items) | 0.00 [0.00, 0.00] (96 items) |         8 |
|       3 |    720 | 0.75 [0.69, 0.79] (96 items) | 0.55 [0.47, 0.63] (96 items) | 0.88 [0.85, 0.92] (110 items) | 0.58 [0.50, 0.66] (96 items) | 0.55 [0.47, 0.63] (96 items) | 0.89 [0.86, 0.93] (120 items) | 0.25 [0.16, 0.34] (36 items) | 0.01 [0.00, 0.01] (96 items) | 0.08 [0.06, 0.10] (120 items) | 0.00 [0.00, 0.00] (96 items) |         3 |
|       4 |    720 | 0.73 [0.67, 0.78] (96 items) | 0.54 [0.46, 0.61] (96 items) | 0.88 [0.84, 0.92] (114 items) | 0.58 [0.50, 0.65] (96 items) | 0.55 [0.47, 0.62] (96 items) | 0.89 [0.86, 0.93] (120 items) | 0.25 [0.16, 0.34] (36 items) | 0.01 [0.00, 0.02] (96 items) | 0.07 [0.05, 0.10] (120 items) | 0.00 [0.00, 0.00] (96 items) |         3 |
|       5 |    720 | 0.71 [0.65, 0.77] (96 items) | 0.52 [0.44, 0.59] (96 items) | 0.88 [0.84, 0.92] (112 items) | 0.56 [0.49, 0.64] (96 items) | 0.53 [0.45, 0.61] (96 items) | 0.89 [0.85, 0.92] (120 items) | 0.21 [0.13, 0.29] (36 items) | 0.02 [0.00, 0.03] (96 items) | 0.08 [0.06, 0.10] (120 items) | 0.00 [0.00, 0.00] (96 items) |         6 |
|       6 |    720 | 0.70 [0.65, 0.75] (96 items) | 0.52 [0.45, 0.59] (96 items) | 0.86 [0.82, 0.90] (113 items) | 0.54 [0.46, 0.61] (96 items) | 0.53 [0.45, 0.60] (96 items) | 0.88 [0.84, 0.91] (120 items) | 0.26 [0.17, 0.36] (36 items) | 0.01 [0.00, 0.02] (96 items) | 0.08 [0.06, 0.11] (120 items) | 0.00 [0.00, 0.00] (96 items) |         4 |


## Observable-ideal reference agent by stage (what each package's faults allow; it obeys the stated policy)

| stage         |   runs | SAR                           | SuAR                          | ABCR                          | Accuracy                      | SuAR|answered                 | ABCR (all runs)               | Refusal correctness           | Over-restriction              | Stated-policy violation       | Hedged                        |   blocked |
|:--------------|-------:|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|:------------------------------|----------:|
| development   |   1440 | 0.73 [0.70, 0.77] (576 items) | 0.73 [0.70, 0.77] (576 items) | 1.00 [1.00, 1.00] (667 items) | 0.73 [0.70, 0.77] (576 items) | 0.73 [0.70, 0.77] (576 items) | 1.00 [1.00, 1.00] (720 items) | 1.00 [1.00, 1.00] (144 items) | 0.00 [0.00, 0.00] (468 items) | 0.00 [0.00, 0.00] (720 items) | 0.00 [0.00, 0.00] (576 items) |         0 |
| integration   |   1440 | 0.74 [0.71, 0.78] (576 items) | 0.74 [0.71, 0.78] (576 items) | 1.00 [1.00, 1.00] (664 items) | 0.74 [0.71, 0.78] (576 items) | 0.74 [0.71, 0.78] (576 items) | 1.00 [1.00, 1.00] (720 items) | 1.00 [1.00, 1.00] (144 items) | 0.00 [0.00, 0.00] (468 items) | 0.00 [0.00, 0.00] (720 items) | 0.00 [0.00, 0.00] (576 items) |         0 |
| preproduction |   1440 | 0.88 [0.85, 0.90] (576 items) | 0.88 [0.85, 0.90] (576 items) | 1.00 [1.00, 1.00] (664 items) | 0.88 [0.85, 0.90] (576 items) | 1.00 [1.00, 1.00] (504 items) | 1.00 [1.00, 1.00] (720 items) | 1.00 [1.00, 1.00] (144 items) | 0.00 [0.00, 0.00] (504 items) | 0.00 [0.00, 0.00] (720 items) | 0.00 [0.00, 0.00] (576 items) |         0 |
| production    |   1440 | 1.00 [1.00, 1.00] (576 items) | 1.00 [1.00, 1.00] (576 items) | 1.00 [1.00, 1.00] (664 items) | 1.00 [1.00, 1.00] (576 items) | 1.00 [1.00, 1.00] (576 items) | 1.00 [1.00, 1.00] (720 items) | 1.00 [1.00, 1.00] (144 items) | 0.00 [0.00, 0.00] (576 items) | 0.00 [0.00, 0.00] (720 items) | 0.00 [0.00, 0.00] (576 items) |         0 |
| postrelease   |   1440 | 1.00 [1.00, 1.00] (504 items) | 1.00 [1.00, 1.00] (504 items) | 1.00 [1.00, 1.00] (654 items) | 1.00 [1.00, 1.00] (504 items) | 1.00 [1.00, 1.00] (504 items) | 1.00 [1.00, 1.00] (720 items) | 1.00 [1.00, 1.00] (216 items) | 0.00 [0.00, 0.00] (504 items) | 0.00 [0.00, 0.00] (720 items) | 0.00 [0.00, 0.00] (504 items) |         0 |


## Preregistered contrasts (b - a). faultfree = agent difference on items the reference agent solves in both packages (primary H1/H2a/b); drift = H2c over items exposed through the permission drift (fixed before treatment); exposed = the same over every post-release-exposed item (secondary); did = v1.1 difference-in-differences (secondary); costpkg = H3b by package; verdict uses the expected sign and Holm p

| family       | hyp        | outcome          | factor   | b           | a          | restrict                | method     |   expected | estimate                |   items |      p |   p_holm | verdict       |
|:-------------|:-----------|:-----------------|:---------|:------------|:-----------|:------------------------|:-----------|-----------:|:------------------------|--------:|-------:|---------:|:--------------|
| confirmatory | H1         | sar              | stage    | development | production | all                     | faultfree  |         -1 | -0.167 [-0.213, -0.121] |     423 | 0.0005 |   0.0045 | supported     |
| confirmatory | H1         | sar              | stage    | integration | production | all                     | faultfree  |         -1 | +nan [+nan, +nan]       |       0 | 1      |   1      | not estimable |
| confirmatory | H1         | supported        | stage    | development | production | all                     | faultfree  |         -1 | -0.125 [-0.170, -0.080] |     423 | 0.0005 |   0.0045 | supported     |
| confirmatory | H1         | supported        | stage    | integration | production | all                     | faultfree  |         -1 | +nan [+nan, +nan]       |       0 | 1      |   1      | not estimable |
| confirmatory | H2         | correct_ans      | stage    | postrelease | production | all                     | faultfree  |         -1 | +0.024 [-0.003, +0.052] |     504 | 0.103  |   0.517  | null          |
| confirmatory | H2         | sar              | stage    | postrelease | production | all                     | faultfree  |         -1 | +0.010 [-0.017, +0.036] |     504 | 0.489  |   1      | null          |
| confirmatory | H2         | abcr_exposed     | stage    | postrelease | production | all                     | drift      |         -1 | -0.246 [-0.293, -0.200] |     285 | 0.0005 |   0.0045 | supported     |
| confirmatory | H3         | abcr_exposed     | mode     | tool        | prompt     | development,postrelease | raw        |          1 | +0.085 [+0.068, +0.102] |     679 | 0.0005 |   0.0045 | supported     |
| confirmatory | H3         | correct_ans      | mode     | tool        | prompt     | all                     | raw        |          0 | -0.010 [-0.025, +0.005] |     576 | 0.204  |   0.816  | null          |
| descriptive  | did        | sar              | stage    | development | production | all                     | did        |         -1 | -0.090 [-0.128, -0.053] |     576 | 0.0005 | nan      | nan           |
| descriptive  | did        | supported        | stage    | development | production | all                     | did        |         -1 | +0.021 [-0.022, +0.064] |     576 | 0.372  | nan      | nan           |
| descriptive  | did        | correct_ans      | stage    | postrelease | production | all                     | did        |         -1 | +0.024 [-0.003, +0.052] |     504 | 0.103  | nan      | nan           |
| descriptive  | did        | sar              | stage    | postrelease | production | all                     | did        |         -1 | +0.010 [-0.017, +0.036] |     504 | 0.489  | nan      | nan           |
| descriptive  | exposedall | abcr_exposed     | stage    | postrelease | production | all                     | exposed    |         -1 | -0.128 [-0.153, -0.103] |     654 | 0.0005 | nan      | nan           |
| descriptive  | costpkg    | correct_ans      | mode     | tool        | prompt     | development             | raw        |          0 | -0.014 [-0.038, +0.010] |     576 | 0.286  | nan      | nan           |
| descriptive  | costpkg    | correct_ans      | mode     | tool        | prompt     | production              | raw        |          0 | +0.003 [-0.023, +0.030] |     576 | 0.83   | nan      | nan           |
| descriptive  | costpkg    | correct_ans      | mode     | tool        | prompt     | postrelease             | raw        |          0 | -0.022 [-0.046, +0.002] |     504 | 0.078  | nan      | nan           |
| descriptive  | total      | sar              | stage    | development | production | all                     | raw        |         -1 | -0.356 [-0.402, -0.312] |     576 | 0.0005 | nan      | nan           |
| descriptive  | total      | supported        | stage    | development | production | all                     | raw        |         -1 | -0.245 [-0.288, -0.204] |     576 | 0.0005 | nan      | nan           |
| descriptive  | total      | correct_ans      | stage    | postrelease | production | all                     | raw        |         -1 | +0.024 [-0.003, +0.052] |     504 | 0.103  | nan      | nan           |
| descriptive  | invariant  | abcr_exposed     | mode     | tool        | prompt     | production              | raw        |          1 | +0.137 [+0.111, +0.164] |     664 | 0.0005 | nan      | nan           |
| descriptive  | cost       | sar              | mode     | tool        | prompt     | all                     | raw        |          0 | +0.003 [-0.013, +0.019] |     576 | 0.713  | nan      | nan           |
| descriptive  | cost       | over_restriction | mode     | tool        | prompt     | all                     | raw        |          0 | -0.003 [-0.008, +0.002] |     576 | 0.282  | nan      | nan           |
| descriptive  | owndrift   | abcr_exposed     | stage    | postrelease | production | all                     | owndrift   |         -1 | -0.833 [-0.896, -0.764] |      72 | 0.0005 | nan      | nan           |
| descriptive  | reachdrift | abcr_exposed     | stage    | postrelease | production | all                     | reachdrift |         -1 | -0.047 [-0.073, -0.023] |     213 | 0.0005 | nan      | nan           |
| descriptive  | covered    | abcr_covered     | mode     | tool        | prompt     | development,postrelease | raw        |          1 | +0.096 [+0.081, +0.113] |     679 | 0.0005 | nan      | nan           |
| descriptive  | open       | abcr_open        | mode     | tool        | prompt     | development,postrelease | raw        |          0 | -0.010 [-0.020, -0.001] |     679 | 0.035  | nan      | nan           |


## Sensitivity: design cell as the cluster (blocks are instances of one 120-cell design)

| hyp   | outcome      | b           | method    |   expected |      diff |        lo |        hi |      p |   items |   nonzero |   p_signflip |   p_holm | verdict       |
|:------|:-------------|:------------|:----------|-----------:|----------:|----------:|----------:|-------:|--------:|----------:|-------------:|---------:|:--------------|
| H1    | sar          | development | faultfree |         -1 |  -0.174   |  -0.233   |  -0.115   | 0.0005 |      94 |        74 |        0     |   0.0045 | supported     |
| H1    | sar          | integration | faultfree |         -1 | nan       | nan       | nan       | 1      |       0 |       nan |      nan     |   1      | not estimable |
| H1    | supported    | development | faultfree |         -1 |  -0.127   |  -0.181   |  -0.0729  | 0.0005 |      94 |        65 |        1e-05 |   0.0045 | supported     |
| H1    | supported    | integration | faultfree |         -1 | nan       | nan       | nan       | 1      |       0 |       nan |      nan     |   1      | not estimable |
| H2    | correct_ans  | postrelease | faultfree |         -1 |   0.0207  |  -0.00539 |   0.0477  | 0.123  |      96 |        51 |        0.133 |   0.615  | null          |
| H2    | sar          | postrelease | faultfree |         -1 |   0.0105  |  -0.0153  |   0.0373  | 0.449  |      96 |        46 |        0.454 |   1      | null          |
| H2    | abcr_exposed | postrelease | drift     |         -1 |  -0.232   |  -0.29    |  -0.176   | 0.0005 |      85 |        50 |        0     |   0.0045 | supported     |
| H3    | abcr_exposed | tool        | raw       |          1 |   0.0797  |   0.051   |   0.111   | 0.0005 |     120 |        41 |        0     |   0.0045 | supported     |
| H3    | correct_ans  | tool        | raw       |          0 |  -0.00955 |  -0.0249  |   0.00579 | 0.218  |      96 |        65 |        0.237 |   0.874  | null          |

Verdicts that change: none


## H6 (v1.4, pilot-derived, outside the Holm family): own re-classified dataset read, prompt-only, deny list by identifier with the label lagging minus labels synced: +0.653 [+0.556, +0.750], p = 0.000, sign-flip p = 0.000, 72 scenarios (47 non-zero); verdict supported (supported, compatible with >= SESOI); read rate lagging 0.79, synced 0.14


## Stated-denied sources read, by how the deny reaches the agent (v1.4, descriptive)

| route      | description                                                                                | mode   |   rate |     lo |     hi |   scenarios |   runs |
|:-----------|:-------------------------------------------------------------------------------------------|:-------|-------:|-------:|-------:|------------:|-------:|
| Own        | identifier deny, label lags; targeted (post-release own re-classified dataset)             | prompt |   0.83 |   0.75 |   0.92 |          72 |     72 |
| Own        | identifier deny, label lags; targeted (post-release own re-classified dataset)             | tool   |   0.85 |   0.76 |   0.93 |          72 |     72 |
| Uat        | identifier deny, label permits; targeted (pre-production erroneous deny)                   | prompt | nan    | nan    | nan    |           0 |      0 |
| Uat        | identifier deny, label permits; targeted (pre-production erroneous deny)                   | tool   | nan    | nan    | nan    |           0 |      0 |
| Restricted | class deny on the label; targeted, no permitted source (production restricted questions)   | prompt |   0.60 |   0.52 |   0.68 |         144 |    144 |
| Restricted | class deny on the label; targeted, no permitted source (production restricted questions)   | tool   |   0.00 |   0.00 |   0.00 |         144 |    144 |
| Prohibited | class deny on the label; a permitted source also answers (production prohibited condition) | prompt |   0.03 |   0.00 |   0.06 |         144 |    144 |
| Prohibited | class deny on the label; a permitted source also answers (production prohibited condition) | tool   |   0.00 |   0.00 |   0.00 |         144 |    144 |


## H5: accuracy-only vs source/boundary-aware release gate (thresholds: accuracy .80; SuAR .80; ABCR .95)

| stage       | mode   |   accuracy |   SuAR |   ABCR | accuracy_gate   | aware_gate   | disagree   | driver   |   p_disagree |
|:------------|:-------|-----------:|-------:|-------:|:----------------|:-------------|:-----------|:---------|-------------:|
| development | prompt |      0.429 |  0.372 |  0.868 | hold            | hold         | False      |          |            0 |
| development | tool   |      0.415 |  0.354 |  0.888 | hold            | hold         | False      |          |            0 |
| postrelease | prompt |      0.671 |  0.651 |  0.725 | hold            | hold         | False      |          |            0 |
| postrelease | tool   |      0.649 |  0.637 |  0.881 | hold            | hold         | False      |          |            0 |
| production  | prompt |      0.623 |  0.609 |  0.863 | hold            | hold         | False      |          |            0 |
| production  | tool   |      0.627 |  0.606 |  1     | hold            | hold         | False      |          |            0 |

P(unsupported | correct) = 0.065 [0.048, 0.085] over 442 items (104 of 1871 correct runs unsupported; 37 correct runs are chance-correct, i.e. no received source yields the answer; 67 of the 1834 evidenced correct runs are unsupported); Kendall tau(accuracy, SuAR) across configurations = 0.87. Item bootstrap of the gate rule: P(>=1 disagreement) = 0.00, driven by SuAR 0.00, by ABCR 0.00; p_disagree = per-configuration share of resamples.


Sensitivity (v1.3a): a gate on task success over all questions (correct answers and correct refusals) instead of answer accuracy disagrees with the aware gate on 0 configurations.

| stage       | mode   |   accuracy |   SuAR |   ABCR | accuracy_gate   | aware_gate   | disagree   | driver   |   p_disagree |
|:------------|:-------|-----------:|-------:|-------:|:----------------|:-------------|:-----------|:---------|-------------:|
| development | prompt |      0.414 |  0.372 |  0.868 | hold            | hold         | False      |          |            0 |
| development | tool   |      0.396 |  0.354 |  0.888 | hold            | hold         | False      |          |            0 |
| postrelease | prompt |      0.504 |  0.651 |  0.725 | hold            | hold         | False      |          |            0 |
| postrelease | tool   |      0.546 |  0.637 |  0.881 | hold            | hold         | False      |          |            0 |
| production  | prompt |      0.557 |  0.609 |  0.863 | hold            | hold         | False      |          |            0 |
| production  | tool   |      0.614 |  0.606 |  1     | hold            | hold         | False      |          |            0 |


## Failure taxonomy (primary label counts)

|                           |   hallucination |   incomplete |   missed_refusal |   ok |   ok_refusal |   policy_violation |   reasoning_error |   safe_abstention |   stale_source |   unsupported_correct |   unwarranted_refusal |   wrong_source |
|:--------------------------|----------------:|-------------:|-----------------:|-----:|-------------:|-------------------:|------------------:|------------------:|---------------:|----------------------:|----------------------:|---------------:|
| ('development', 'prompt') |              21 |           18 |               24 |  214 |           51 |                 88 |                68 |                 4 |            177 |                     2 |                    14 |             39 |
| ('development', 'tool')   |              20 |           19 |               35 |  204 |           46 |                 76 |                80 |                 4 |            189 |                     4 |                     9 |             34 |
| ('production', 'prompt')  |               0 |            1 |               15 |  351 |           42 |                 91 |               132 |                 0 |              4 |                     0 |                     0 |             84 |
| ('production', 'tool')    |               0 |            1 |               62 |  349 |           81 |                  0 |               149 |                 0 |              6 |                     0 |                     2 |             70 |
| ('postrelease', 'prompt') |               0 |            0 |               19 |  328 |           25 |                180 |               117 |                 0 |             17 |                     0 |                     1 |             33 |
| ('postrelease', 'tool')   |               0 |            2 |               79 |  321 |           66 |                 78 |               111 |                 0 |             23 |                     0 |                     0 |             40 |


## Failure taxonomy, agent-attributable (runs whose seed-matched reference-agent run succeeded)

|                           |   hallucination |   incomplete |   missed_refusal |   ok |   ok_refusal |   policy_violation |   reasoning_error |   stale_source |   unsupported_correct |   unwarranted_refusal |   wrong_source |
|:--------------------------|----------------:|-------------:|-----------------:|-----:|-------------:|-------------------:|------------------:|---------------:|----------------------:|----------------------:|---------------:|
| ('development', 'prompt') |              20 |           11 |               24 |  214 |           51 |                 87 |                68 |             50 |                     2 |                    10 |             30 |
| ('development', 'tool')   |              19 |           13 |               35 |  202 |           46 |                 75 |                79 |             62 |                     4 |                     8 |             24 |
| ('production', 'prompt')  |               0 |            1 |               15 |  351 |           42 |                 91 |               132 |              4 |                     0 |                     0 |             84 |
| ('production', 'tool')    |               0 |            1 |               62 |  349 |           81 |                  0 |               149 |              6 |                     0 |                     2 |             70 |
| ('postrelease', 'prompt') |               0 |            0 |               19 |  328 |           25 |                180 |               117 |             17 |                     0 |                     1 |             33 |
| ('postrelease', 'tool')   |               0 |            2 |               79 |  321 |           66 |                 78 |               111 |             23 |                     0 |                     0 |             40 |


## Accuracy and refusal by evidence reachability (injected faults vs agent behaviour; chance = credited answers that no received source yields)

|                                          |   runs |   accuracy |   refused |   chance |
|:-----------------------------------------|-------:|-----------:|----------:|---------:|
| ('development', 'missing_from_snapshot') |    216 |      0.06  |     0.037 |       13 |
| ('development', 'reachable')             |    936 |      0.505 |     0.025 |        9 |
| ('postrelease', 'reachable')             |   1008 |      0.66  |     0.001 |        8 |
| ('production', 'reachable')              |   1152 |      0.625 |     0.002 |        7 |


## Harness diagnostics

assistant turns 14803; tool calls recovered from plain text 13; runs never calling submit_answer 2; infrastructure errors 0; blocked attempts 28; stated-policy violations 361


## Secondary models: TOTAL package and mode effects (mostly injected faults; not the agent-attributable estimand). GEE odds ratios vs production / prompt-only; VB mixed-logit intervals in models.json are approximate

- **SAR** (n=3312): development OR 0.16 [0.12, 0.21]; postrelease OR 1.15 [0.91, 1.45]; tool OR 1.02 [0.92, 1.12]
- **SuAR** (n=3312): development OR 0.25 [0.20, 0.32]; postrelease OR 1.20 [0.99, 1.44]; tool OR 0.93 [0.85, 1.02]
- **ABCR** (n=3970): development OR 0.45 [0.34, 0.59]; postrelease OR 0.21 [0.17, 0.27]; tool OR 3.58 [2.94, 4.36]
- **Accuracy** (n=3312): development OR 0.32 [0.25, 0.41]; postrelease OR 1.21 [1.01, 1.46]; tool OR 0.94 [0.86, 1.03]