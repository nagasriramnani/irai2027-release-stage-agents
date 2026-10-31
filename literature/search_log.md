# Literature search log

- **Paper:** Release-Stage Effects on AI Agent Answer Reliability Across Business Simulation Profiles (IRAI 2027)
- **Search date:** 2026-10-30 (all agents ran on this date)
- **Agents:** 9 topic sweeps + 1 citation auditor per topic, 3 independent novelty challengers, 1 lead-author consolidation pass (this file)

## Engines and databases

- **Discovery:** a general web search engine (the `WebSearch` tool, US index), in standard and "extended" modes. A shared budget of 200 searches per run was exhausted in every topic agent and in the novelty agents. Queries marked FAILED, BLOCKED or NOT RUN below were not executed.
- **Verification (direct page fetch, `WebFetch`):**
  - arXiv abstract and HTML pages
  - ACL Anthology
  - Proceedings: PMLR, NeurIPS, ICLR, AAAI OJS, NDSS
  - mlanthology.org, Crossref DOI metadata, DBLP keys surfaced via Semantic Scholar
  - Official pages: neurips.cc, icml.cc, iclr.cc
  - Standards and policy: NIST nvlpubs, the EU AI Act Service Desk, Microsoft Learn (for ISO 42001)
  - Venue and tooling: IEEE Author Center, IEEE PDF eXpress, CTAN, the IRAI 2026/2027 sites, IES ITeN
  - Authors' GitHub READMEs, used for venue claims only
- **Blocked or unavailable:** OpenReview (browser check), ACM DL (403), iso.org (Cloudflare 403), IEEE Xplore (HTTP 418), the COLM site (404). IEEE Xplore therefore was **not** searched systematically; see the follow-ups below.

## Inclusion and exclusion rules

1. **Source type:** peer-reviewed venue, or an arXiv preprint (flagged as such in `references.bib`).
2. **Years:** 2017-2026.
3. **Relevance:** at least two of our design dimensions: role profiles, heterogeneous sources, access control, source appropriateness, evidence support, staleness/drift, release stages, enforcement ablation, abstention.
4. **Verification:** title, every author, venue, year and every number quoted in a summary checked on a primary page. Corrected entries keep a note.

Documented exceptions:
- Methodology classics outside 2017-2026: Artstein & Poesio 2008; Sculley et al. 2015.
- Statistics and evaluation-methodology references, and governance documents: NIST AI 100-1 and AI 600-1, EU AI Act Art. 72, ISO/IEC 42001. These are kept to justify methods and framing even when they touch only one design dimension.
- Venue and policy web pages: section 9 of the bib, for authors only, not for citation.

Exclusion criteria:
- Not verifiable on a primary page within budget.
- Superseded by a peer-reviewed version (kept the later one).
- Duplicate key or title.
- Weaker fit than an included work covering the same point.

## Counts

| Stage | Count |
|---|---|
| Logged query/fetch entries, all agents (below) | 254 (245 executed; 9 failed/blocked/not run) |
| Citation records returned verified by topic auditors | 136 |
| ... unique after dedup (5 same-key repeats + 3 alias keys merged) | 128 |
| Novelty-report closest works rated high/medium and not already kept | 8 |
| ... verified by me and added (`[NEW]` in bib) | 7 |
| ... excluded after verification | 1 (GuardianAgentBench) |
| **Final `references.bib` entries** | **136** = 120 scholarly (peer-reviewed or arXiv) + 4 standards/regulation + 12 venue/policy pages; the 136th, the Llama 3 report (`grattafiori2024llama3`), was added on 31 Oct 2026 for the replication model |
| Citations dropped by the auditor (list D) | 0 |
| Candidates seen but not included (listed below; excludes the 4 aliases) | 57 |
| Rows in `related_work_matrix.csv` | 33 related benchmarks/studies + "This work" |
| Distinct references cited in `related_work.tex` / `related_work_table.tex` | 35 / 8 (all 8 table keys also cited in the text) |

Duplicates merged (kept key, then dropped key):
- `sanyal2026orgaccess` (EMNLP 2026) replaces `sanyal2025orgaccess` (arXiv). The EMNLP author list adds Dhruv Kumar.
- `jayaraman2025permllm` replaces `jayaraman2025permissioned`.
- `song2025trustscore` replaces `song2025trustalign` (same ICLR 2025 paper).
- `huang2026crmarenapro` replaces `huang2025crmarenapro` (novelty-report alias, TMLR version kept).
- Same key in several topic lists, merged into one entry each: `vishwakarma2025enterprisebench`, `yao2025taubench`, `shi2025progent`, `chen2024rgb`, `sun2026enterpriseragbench`.

## Queries run

### Topic 1: enterprise agent benchmarks (18)
- EnterpriseBench LLM agents enterprise benchmark role-based access
- CRMArena-Pro confidentiality awareness LLM agents arXiv
- TheAgentCompany benchmarking LLM agents consequential real world tasks
- tau-bench tool-agent-user interaction benchmark ICLR 2025
- "CRMArena-Pro" accepted conference 2025 OR 2026 aclanthology OR openreview
- CRMArena: Understanding the Capacity of LLM Agents to Perform Professional CRM Tasks NAACL 2025
- WorkBench dataset LLM agents workplace setting Olly Styles COLM 2024
- WorkArena++ compositional planning knowledge work NeurIPS 2024 datasets benchmarks
- permission-aware retrieval augmented generation benchmark enterprise access control LLM agent 2025 (extended)
- tau2-bench dual-control conversational agents benchmark arXiv 2506.07982
- benchmark LLM agent enterprise role-based access control confidential information leakage multi-user 2025 arXiv (extended)
- enterprise agent benchmark 2026 arXiv heterogeneous data sources tables APIs documents LLM agents (extended)
- benchmark enterprise RAG agent access control OR permissions role-aware answers unauthorized documents evaluation 2026 arXiv (extended)
- WorkArena how capable are web agents at solving common knowledge work tasks ICML 2024
- OfficeBench benchmarking language agents across multiple applications office automation
- openreview TMLR CRMArena-Pro Holistic Assessment of LLM Agents
- WorkBench Styles COLM 2024 openreview conference on language modeling
- WebFetch: aclanthology 2025.emnlp-main.466; arXiv 2505.18878, 2608.19235, 2607.25765, 2610.27911, 2606.23654, 2605.05253, 2405.00823, 2607.05318; neurips.cc poster 121705; proceedings.neurips.cc WorkArena++; mlanthology WorkArena ICML 2024; ICLR 2025 tau-bench proceedings; eprints.gla.ac.uk 329746

### Topic 2: access control and RAG leakage (18)
- permission-aware retrieval-augmented generation access control LLM arXiv (extended)
- Zeng 2024 "The Good and The Bad: Exploring Privacy Issues in Retrieval-Augmented Generation"
- "Permissioned LLMs" access control language models arXiv
- PrivacyLens evaluating privacy norm awareness language models in action NeurIPS 2024
- AgentDAM privacy leakage evaluation autonomous web agents
- ConfAIde "Can LLMs Keep a Secret" contextual integrity ICLR 2024
- role-based access control LLM agent enterprise benchmark leakage unauthorized data 2025 (extended)
- multi-tenant RAG knowledge base access control leakage evaluation benchmark 2025 2026 arXiv (extended)
- "Enterprise AI Must Enforce Participant-Aware Access Control" authors
- Progent programmable privilege control LLM agents arXiv
- SudoLM learning access control of parametric knowledge authorization alignment
- enterprise agent benchmark access permissions document-level ACL retrieval LLM evaluation 2026 (extended)
- "access control" "retrieval-augmented generation" unauthorized documents leakage evaluation prompt-based enforcement vs filtering (extended)
- "Follow My Instruction and Spill the Beans" datastore leakage RAG ICLR 2025
- AgentLeak benchmark privacy leakage multi-agent LLM systems
- [FAILED: budget exhausted] arXiv 2025 RAG role-based access control metadata filtering permission leakage experiment
- [FAILED: budget exhausted] LLM agent data minimization contextual integrity tool-use benchmark enterprise 2025 2026
- WebFetch: arXiv 2505.19165, 2509.14608, 2605.05287, 2604.12177, 2609.02095, 2506.23139, 2610.30193, 2505.08728, 2602.11510, 2504.11703, 2503.09780, 2310.17884, 2409.00138, 2402.17840; ACL Anthology 2024.findings-acl.267, 2025.acl-long.1318, 2025.ijcnlp-long.29, 2026.acl-industry.103; NeurIPS 2025 PermLLM proceedings page

### Topic 3: agent policy enforcement (24)
- CaMeL Defeating Prompt Injections by Design arXiv
- Progent programmable privilege control LLM agents
- AgentSpec customizable runtime enforcement safe reliable LLM agents ICSE
- GuardAgent safeguard LLM agents guard agent knowledge-enabled reasoning ICML 2025
- ShieldAgent shielding agents via verifiable safety policy reasoning ICML 2025
- IsolateGPT execution isolation architecture LLM-based agentic systems NDSS 2025
- FIDES Securing AI Agents with Information-Flow Control arXiv 2025
- Conseca contextual agent security policy for every purpose HotOS 2025
- The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions Wallace arXiv 2404.13208
- AgentDojo dynamic environment evaluate prompt injection attacks defenses LLM agents NeurIPS 2024 Datasets Benchmarks
- InjecAgent benchmarking indirect prompt injections tool-integrated LLM agents Findings ACL 2024
- ST-WebAgentBench benchmark evaluating safety trustworthiness web agents policy compliance
- tau-bench benchmark tool-agent-user interaction real-world domains ICLR 2025 policy
- LLM agent role-based access control enterprise permissions benchmark prompt instructions insufficient 2025 (extended)
- Control Illusion failure of instruction hierarchies in large language models
- Permissioned LLMs enforcing access control in large language models arXiv
- Design Patterns for Securing LLM Agents against Prompt Injections Beurer-Kellner
- "prompt-based" versus "tool-level" enforcement access control LLM agent data leakage evaluation 2026 (extended)
- Defeating Prompt Injections by Design CaMeL Debenedetti accepted conference 2025 OR 2026 proceedings
- Progent Programmable Privilege Control for LLM Agents accepted proceedings 2026
- "An Evaluation of Data Leakage Risks in Tool-Using LLM Agents in Realistic Scenarios"
- tau-bench Yao Shinn Razavi Narasimhan ICLR 2025 openreview
- permission-aware retrieval augmented generation agent access control leakage unauthorized documents benchmark 2025 2026 (extended)
- WebFetch: arXiv 2503.18813, 2504.11703, 2505.23643, 2501.17070, 2503.18666, 2406.12045, 2506.08837, 2601.11893, 2606.22916, 2605.28071, 2609.26682; ACL Anthology 2026.emnlp-main.1700, 2025.emnlp-main.466, 2026.realm-1.75; AAAI OJS 40339; NeurIPS 2024 D&B and NeurIPS 2025 proceedings; mlanthology ICML 2025 GuardAgent/ShieldAgent; iclr.cc 2026 poster 10009904; Princeton record for tau-bench; NDSS IsolateGPT page

### Topic 4: attribution and groundedness (21)
- Measuring Attribution in Natural Language Generation Models Rashkin Computational Linguistics AIS
- Enabling Large Language Models to Generate Text with Citations ALCE EMNLP 2023 Gao
- AttributionBench how hard is automatic attribution evaluation ACL Findings 2024
- Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse Trust-Score ICLR 2025
- Correctness is not Faithfulness in RAG Attributions Wallat
- Evaluating Verifiability in Generative Search Engines Liu Zhang Liang Findings EMNLP 2023
- RAGTruth hallucination corpus trustworthy retrieval-augmented language models ACL 2024
- ARES automated evaluation framework retrieval-augmented generation NAACL 2024 Saad-Falcon
- RAGAS automated evaluation of retrieval augmented generation EACL 2024 demo Es
- FActScore fine-grained atomic evaluation of factual precision EMNLP 2023 Min
- TRUE: Re-evaluating factual consistency evaluation NAACL 2022 Honovich
- 2025 benchmark citation faithfulness RAG attribution evaluation agents tool outputs supported claims (extended)
- enterprise RAG groundedness evaluation access control permissions citations benchmark 2025 (extended)
- CiteEval principle-driven citation evaluation source attribution ACL 2025
- "Attribute or Abstain" large language models long document assistants EMNLP 2024
- attribution citation evaluation LLM answers over tables structured data cell-level attribution benchmark (extended)
- MiniCheck efficient fact-checking of LLMs on grounding documents EMNLP 2024 Tang
- FaithEval ICLR 2025 contextual faithfulness
- LLM agent answers grounded in tool outputs attribution evaluation citations unsupported claims benchmark 2026 (extended)
- correct answer but unsupported by retrieved context RAG parametric knowledge groundedness gap accuracy vs attribution 2025 (extended)
- WebFetch: arXiv 2609.22537, 2605.06635, 2608.11584, 2602.15769, 2602.13059, 2606.07783, 2607.20527, 2609.18154, 2409.11242 (abs + html v4); TU Delft record for Wallat et al.; ACL Anthology 2025.findings-acl.875, 2024.acl-long.585, 2025.acl-long.1574, 2022.naacl-main.287

### Topic 5: stale, conflicting and distracting knowledge (20)
- FreshLLMs refreshing large language models with search engine augmentation FreshQA ACL Findings 2024
- ClashEval quantifying the tug-of-war between LLM internal prior and external evidence NeurIPS 2024
- Knowledge Conflicts for LLMs: A Survey Xu EMNLP 2024
- Large Language Models Can Be Easily Distracted by Irrelevant Context Shi ICML 2023
- The Power of Noise: Redefining Retrieval for RAG Systems Cuconasu SIGIR 2024
- Lost in the Middle: How Language Models Use Long Contexts TACL 2024 Liu
- RealTime QA: What's the Answer Right Now? NeurIPS 2023 Datasets Benchmarks Kasai
- temporal RAG benchmark outdated documents versioned knowledge base LLM 2025 arXiv (extended)
- retrieval-augmented generation robustness knowledge base updates document drift evaluation 2025 (extended)
- inter-context knowledge conflict RAG benchmark conflicting retrieved documents 2025 ACL EMNLP (extended)
- Benchmarking Large Language Models in Retrieval-Augmented Generation RGB noise robustness negative rejection AAAI 2024 Chen
- Retrieval-Augmented Generation with Conflicting Evidence MADAM-RAG RAMDocs Wang Bansal 2025
- Adaptive Chameleon or Stubborn Sloth knowledge conflicts ICLR 2024 Xie
- Making Retrieval-Augmented Language Models Robust to Irrelevant Context Yoran ICLR 2024
- FaithEval can your language model stay faithful to context unanswerable inconsistent counterfactual ICLR 2025
- "Retrieval-Augmented Generation with Conflicting Evidence" COLM 2025
- enterprise RAG stale outdated policy documents benchmark agent conflicting versions 2026 (extended)
- DRAGged into Conflicts detecting addressing conflicting sources search-augmented LLMs CONFLICTS benchmark
- Sufficient Context: A New Lens on Retrieval Augmented Generation Systems ICLR 2025 Joren
- WebFetch: ACL Anthology 2024.findings-acl.813, 2025.acl-long.301, 2025.findings-emnlp.466; arXiv 2510.08109, 2608.08512, 2609.11572, 2605.05253, 2504.13079, 2604.05096, 2302.00093, 2401.14887, 2207.13332, 2410.03727

### Topic 6: abstention and refusal (18)
- Know Your Limits: A Survey of Abstention in Large Language Models Wen TACL
- AbstentionBench reasoning LLMs fail on unanswerable questions 2025
- XSTest test suite exaggerated safety behaviours NAACL 2024
- OR-Bench over-refusal benchmark large language models ICML 2025
- UAEval4RAG unanswerability evaluation retrieval augmented generation ACL 2025
- Trust-Align measuring and enhancing trustworthiness of LLMs in RAG grounded attributions learning to refuse ICLR 2025
- RefusalBench selective refusal grounded language models RAG 2025 (extended)
- Benchmarking large language models in retrieval-augmented generation negative rejection RGB AAAI 2024
- Sufficient Context: A New Lens on Retrieval Augmented Generation Systems ICLR 2025 selective generation
- ToolBeHonest unsolvable tasks tool-augmented LLM hallucination benchmark EMNLP 2024
- ToolBeHonest aclanthology 2024.emnlp-main
- When2Call when to call tools abstain benchmark NAACL 2025
- LLM agents abstention over-refusal tool-use benchmark 2026 arXiv (extended)
- permission-aware RAG access control refusal over-restriction enterprise LLM assistant evaluation (extended)
- "over-refusal" OR "overcautious" retrieval-augmented generation safety refusal benign queries contexts 2025
- Selective Question Answering under Domain Shift Kamath Jia Liang ACL 2020 aclanthology
- "Don't Hallucinate, Abstain" identifying LLM knowledge gaps multi-LLM collaboration ACL 2024 aclanthology
- WebFetch: arXiv 2607.10059, 2606.28733, 2608.01358, 2605.09480, 2510.10390, 2412.12300v3; ACL Anthology 2025.acl-long.415, 2025.findings-acl.1243, 2024.naacl-long.301, 2024.emnlp-main.637, 2024.acl-long.786; PMLR v267/cui25a; ICLR proceedings (Trust-Align, Sufficient Context); mlanthology NeurIPS 2025 AbstentionBench; neurips.cc/virtual/2025/122468

### Topic 7: LLMOps and release lifecycle (22)
- "How is ChatGPT's behavior changing over time" Chen Zaharia Zou Harvard Data Science Review
- The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction Breck IEEE Big Data 2017
- Paleyes Urma Lawrence "Challenges in Deploying Machine Learning: A Survey of Case Studies" ACM Computing Surveys
- evaluation-driven development LLM agents process model reference architecture arXiv 2024
- AgentOps taxonomy observability LLM agents Dong Lu Zhu arXiv
- Sculley "Hidden Technical Debt in Machine Learning Systems" NeurIPS 2015 proceedings
- NIST AI 600-1 Generative Artificial Intelligence Profile July 2024 pre-deployment testing post-deployment monitoring
- empirical study LLM agent reliability staging vs production deployment environment gap evaluation 2025 (extended)
- "Is My Prompt Getting Worse" regression testing evolving LLM APIs Ma Yang Kastner CAIN 2024
- LLM agent continuous evaluation pre-deployment vs post-deployment empirical comparison offline online evaluation gap 2025 arXiv (extended)
- EU AI Act Regulation (EU) 2024/1689 Article 72 post-market monitoring EUR-Lex
- ISO/IEC 42001:2023 artificial intelligence management system iso.org
- Shankar Garcia Hellerstein Parameswaran Operationalizing Machine Learning interview study staging canary
- empirical study testing practices LLM applications open-source agent projects 2025 arXiv
- agent behavior drift after model update silent update tool-using agent regression evaluation 2026 arXiv (extended)
- Kreuzberger Kuhl Hirschl MLOps Overview Definition Architecture IEEE Access
- "A Survey on AgentOps" categorization challenges future directions arXiv 2025
- shadow deployment OR canary release LLM application evaluation empirical RAG production monitoring arXiv (extended)
- Raji Smart Closing the AI accountability gap end-to-end internal algorithmic auditing FAT* 2020
- hdsr.mitpress.mit.edu How Is ChatGPT's Behavior Changing Over Time volume 6 issue 2 doi
- NIST AI 100-1 AI RMF 1.0 January 2023 doi TEVV lifecycle
- WebFetch: arXiv 2411.13768v3, 2512.04123, 2601.06112, 2601.17292, 2601.22025, 2509.19185, 2411.05285, 2011.09926; research.google ML Test Score page; nvlpubs.nist.gov NIST.AI.600-1.pdf and NIST.AI.100-1.pdf; ai-act-service-desk.ec.europa.eu Article 72

### Topic 8: evaluation methodology and statistics (23)
- "Adding Error Bars to Evals" statistical approach language model evaluations Miller arXiv
- "AI Agents That Matter" Kapoor Stroebl Narayanan TMLR
- BetterBench assessing AI benchmarks best practices NeurIPS 2024 Reuel
- HiBayES hierarchical Bayesian modeling framework AI evaluation statistics
- "Measuring what Matters" construct validity large language model benchmarks Bean 2025
- "Establishing Best Practices for Building Rigorous Agentic Benchmarks" Agentic Benchmark Checklist
- non-determinism of "deterministic" LLM settings temperature zero repeated runs accuracy variation Atil
- "Judging the Judges" evaluating alignment and vulnerabilities in LLMs-as-judges Thakur
- "LLMs instead of Human Judges" large scale empirical study 20 NLP evaluation tasks JUDGE-BENCH ACL 2025
- "Don't use the CLT in LLM evals with fewer than a few hundred datapoints" Bowyer ICML 2025
- tinyBenchmarks evaluating LLMs with fewer examples item response theory Polo ICML 2024
- tinyBenchmarks Maia Polo Weber Choshen Sun Xu Yurochkin proceedings.mlr.press v235
- "Towards Inferential Reproducibility of Machine Learning Research" linear mixed effects models ICLR 2023 Hagmann Riezler
- "Quantifying Variance in Evaluation Benchmarks" Madaan seed variance LLM
- Zheng "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" NeurIPS 2023 Datasets and Benchmarks proceedings
- "Preregistering NLP research" van Miltenburg van der Lee Krahmer NAACL 2021
- AI agent reliability repeated runs consistency benchmark 2026 arXiv reliability agents pass^k variance across trials (extended)
- "Towards a Science of AI Agent Reliability" Rabanser
- validity of synthetic data benchmarks LLM-generated evaluation data reliability synthetic benchmark comparison human-written 2025 (extended)
- "Signal and Noise" framework reducing uncertainty language model evaluation Heineman NeurIPS 2025
- generalized linear mixed model LLM evaluation item random effects benchmark mixed-effects logistic regression language models evaluation (extended)
- "Evaluation Examples are not Equally Informative" How should that change NLP leaderboards Rodriguez ACL 2021 item response theory
- Artstein Poesio "Inter-coder agreement for computational linguistics" Computational Linguistics 2008 (budget exhausted; confirmed by direct fetch of ACL Anthology J08-4004)

### Topic 9: venue and policy (30)
- WebFetch https://irai2027.ieee-ies.org/for_authors/
- WebSearch: IEEE International Conference on Responsible Artificial Intelligence IRAI 2026 IES
- WebFetch https://irai2026.ieee-ies.org/
- WebFetch https://irai2026.ieee-ies.org/for_authors/
- WebFetch https://irai2027.ieee-ies.org/
- WebSearch (extended): "Responsible Artificial Intelligence" IRAI 2026 proceedings ieeexplore.ieee.org
- WebFetch https://irai2026.ieee-ies.org/about/index.html
- WebFetch https://iten.ieee-ies.org/events/2026/2026-irai-2026-1st-ieee-international-conference-on-responsible-artificial-intelligence/
- WebFetch https://irai2026.ieee-ies.org/program/index.html (program not rendered)
- WebFetch https://confcomm.ieee-ies.org/share/IRAI26/schedule (JS-only, no titles)
- WebFetch https://irai2026.ieee-ies.org/program/technical_tracks/index.html
- WebSearch: IEEE author center guidelines artificial intelligence generated text disclosure acknowledgments
- WebSearch: IEEE conference policy preprint arXiv posting author center "preprint"
- WebFetch https://conferences.ieeeauthorcenter.ieee.org/author-ethics/guidelines-and-policies/submission-policies/
- WebFetch https://conferences.ieeeauthorcenter.ieee.org/get-published/post-your-paper/
- WebFetch https://conferences.ieeeauthorcenter.ieee.org/write-your-paper/authoring-tools-and-templates/
- WebSearch: IEEE PDF eXpress conference author create PDF check compliance Xplore conference ID
- WebFetch https://conferences.ieeeauthorcenter.ieee.org/prepare-your-paper-for-publication/meet-ieee-xplore-requirements/
- WebFetch https://www.ieee.org/conferences/publishing/templates.html (empty render)
- WebSearch: IEEEtran LaTeX conference template CTAN conference mode
- WebFetch https://ieee-pdf-express.org/
- WebFetch https://ieee-pdf-express.org/External/UsingIEEEPDFeXpress
- WebFetch https://ctan.org/pkg/ieeetran
- WebFetch https://open.ieee.org/author-guidelines-for-artificial-intelligence-ai-generated-text/
- [NOT RUN: budget exhausted] WebSearch (extended): "2026 IEEE International Conference on Responsible Artificial Intelligence (IRAI)"
- WebFetch https://irai2026.ieee-ies.org/news_and_updates/index.html
- WebFetch https://irai2026.ieee-ies.org/registration/index.html
- WebFetch https://ieeexplore.ieee.org/xpl/conhome.jsp (HTTP 418)
- WebFetch https://irai2027.ieee-ies.org/program/technical_tracks/index.html
- WebFetch https://irai2026.ieee-ies.org/for_authors/IRAI2026-CFP.pdf (binary PDF, not parsed)

### Novelty challenger 1 (20)
- LLM agent evaluation across deployment stages staging production pre-production reliability (extended)
- RAG system evaluation lifecycle development staging production LLMOps arXiv
- enterprise RAG access control permission-aware retrieval benchmark LLM agent leakage (extended)
- EnterpriseBench LLM agents enterprise environment access control benchmark
- CRMArena-Pro confidentiality awareness LLM agents business scenarios
- ST-WebAgentBench policy compliance enterprise web agents safety trustworthiness
- evaluation-driven development LLM agents lifecycle offline online evaluation process model arXiv
- regression testing LLM applications model version updates behavioral change prompts arXiv
- document drift permission drift RAG agent post-deployment monitoring evaluation stale documents (extended)
- prompt-based access control vs enforced tool-level access control LLM agent RAG comparison leakage evaluation 2025 (extended)
- "Securing the Agent" vendor-neutral multitenant enterprise retrieval tool use arXiv 2605.05287
- AgentOps taxonomy observability LLM agents lifecycle arXiv
- empirical study gap between pre-deployment evaluation and production behavior LLM agents release gating (extended)
- configuration variants same LLM agent reliability benchmark retrieval settings system prompt guardrails factorial experiment enterprise
- arXiv 2026 benchmark LLM agent staging production environment configuration drift evaluation (extended)
- RAG access control benchmark role-based permissions unauthorized document disclosure evaluation arXiv 2025 2026 (extended)
- continuous integration deployment pipeline LLM-based application evaluation quality gates empirical study arXiv
- [BLOCKED: budget exhausted] benchmark RAG outdated stale documents conflicting versions enterprise knowledge base
- [BLOCKED: budget exhausted] tau-bench tool-agent-user interaction benchmark ICLR 2025
- WebFetch: arXiv 2605.23950, 2509.10769, 2609.21267, 2506.00964, 2601.06112, 2603.15676, 2603.27355, 2410.06703, 2411.13768, 2506.03401, 2512.20535, 2605.26269; aclanthology 2025.emnlp-main.466; mlanthology TMLR CRMArena-Pro; icml.cc/virtual/2026/77896; caisconf.org CAIS 2026 program

### Novelty challenger 2 (11)
- role-based access control LLM agent benchmark enterprise permissions
- enterprise RAG permission-aware benchmark access control leakage evaluation arXiv 2025
- benchmark LLM agent enterprise confidential information need-to-know access boundaries retrieval citation
- EnterpriseBench LLM agents enterprise environment access control persona benchmark 2025
- CRMArena-Pro confidentiality awareness LLM agents business roles benchmark
- benchmark agent stale outdated conflicting documents source authority enterprise RAG citation correctness
- RBAC RAG benchmark role-aware retrieval leakage unauthorized documents answer grounding evaluation 2026
- prompt-based policy instructions versus tool-level enforcement LLM agent access control compliance empirical comparison
- LLM agent evaluation across deployment stages development staging production drift permission changes empirical study
- [NOT RUN: budget exhausted] benchmark permission-aware retrieval agent per-user ground truth unauthorized document disclosure citation faithfulness enterprise multi-tenant
- WebFetch: aclanthology 2026.emnlp-main.1700, 2025.emnlp-main.466, 2025.ijcnlp-long.29; arXiv 2605.08761, 2604.21308, 2506.00964, 2607.27353 (abs+html), 2608.11584, 2605.18414, 2606.28061, 2609.09853, 2605.05253, 2505.18878, 2411.13768, 2512.20535; snu.elsevierpure.com Permission-Aware RAG (IEEE Access)

### Novelty challenger 3 (17)
- permission-aware RAG evaluation access control leakage prompt-only vs retrieval filtering LLM (extended)
- enterprise copilot oversharing benchmark LLM agent access control 2025 arXiv (extended)
- role-based access control LLM benchmark system prompt instructions leak restricted data evaluation arXiv 2025 (extended)
- "source appropriateness" OR "supported answer rate" OR "access-boundary compliance" LLM agent evaluation (extended)
- LLM agent evaluation deployment stages development staging production drift permission changes benchmark reliability (extended)
- tool-level access control enforcement vs system prompt policy LLM agents empirical comparison leakage enterprise data (extended)
- arXiv access control retrieval-augmented generation benchmark unauthorized document leakage role permissions evaluation 2025 2026 (extended)
- Microsoft 365 Copilot oversharing study permissions sensitive data exposure enterprise assistant research paper
- enterprise LLM agent benchmark stale documents distractor sources citation support grounded answers permissions finance HR synthetic (extended)
- Namboothiri 2026 retrieve-then-filter unauthorized context access control RAG arXiv (extended) -- paper not found
- LLM agent policy compliance system prompt policy versus runtime enforcement compared benchmark violation rate arXiv 2025 2026 (extended)
- contextual integrity enterprise agent benchmark role-based permissions tool access filtering mitigation compared leakage rate 2026 (extended)
- Retrieval Pivot Thornton 2026 / AC-RAG fine-grained authorization arXiv
- PiSAs benchmark cross-user data spillage shared agentic systems Gupta 2026
- [NOT RUN: budget exhausted] permission drift / access drift RAG agent evaluation
- [NOT RUN: budget exhausted] IEEE Xplore RBAC RAG enterprise LLM leakage 2025
- WebFetch: arXiv 2607.27353 (+HTML), 2602.16708 (+v2 HTML), 2510.07642, 2606.17114, 2604.21308, 2505.19165, 2509.14608, 2510.27287, 2605.08761, 2607.05318, 2604.12177, 2605.05501, 2608.28502, 2608.17148, 2512.20535, 2505.22860, 2411.13768; ACL Anthology 2026.acl-industry.103

### Lead-author consolidation pass (this session) (12)
- WebFetch arxiv.org/abs/2506.00964 (ACCESS DENIED INC; journal-ref Findings ACL 2025 pp. 13221-13240)
- WebFetch arxiv.org/abs/2607.27353 (LayerRAG-Bench)
- WebFetch arxiv.org/abs/2602.16708 (current title "Formal Policy Enforcement for Agentic Systems")
- WebFetch arxiv.org/abs/2602.16708v2 (v2 title "Policy Compiler for Secure Agentic Systems"; 48% to 93%)
- WebFetch arxiv.org/abs/2510.07642 (Role-Conditioned Refusals)
- WebFetch arxiv.org/abs/2605.18414 (Prompts Don't Protect; EMNLP 2026 Industry accepted)
- WebFetch icml.cc/virtual/2026/77896 (GuardianAgentBench: **workshop** poster; incomplete author list)
- WebFetch openreview.net/forum?id=dhs7mrXglf (blocked by browser check)
- WebFetch arxiv.org/abs/2603.15676 (Maiorano, quality gate)
- WebFetch arxiv.org/abs/2603.27355 (Maiorano, readiness harness)
- WebFetch aclanthology.org/2026.realm-1.75/ (Baek et al.: REALM 2026, Budapest, Oct 2026, pp. 1074-1096)
- [BLOCKED: budget exhausted] WebSearch: GuardianAgentBench "Where Agents Fail and How to Guard Them" arXiv

## Dropped or excluded citations, with reasons

The auditor dropped none (list D was empty). The items below were seen during the search but are **not** in `references.bib`.

**Dropped after verification (1)**
- GuardianAgentBench (Naik et al., ICML 2026): the novelty report called it a main-conference paper. The ICML page shows a workshop poster ("Failure Modes in Agentic AI"), the author list renders incompletely, and OpenReview was blocked. It is not needed for H3, which is covered by PCAS, Prompts Don't Protect and Arceo & Narsing.

**Merged duplicates or aliases (4)**
- `sanyal2025orgaccess`, `jayaraman2025permissioned`, `song2025trustalign`, `huang2025crmarenapro`; see Counts above.

**Not verified within budget (17)**
- AppWorld; Spider 2.0; AssistantBench; OfficeBench (arXiv:2407.19056)
- Provably Secure RAG (2508.01084); ACM SAC '25 RAG access control (DOI 10.1145/3672608.3707848, 403)
- Secure-RAG review (2603.21654); SoK on RAG privacy (2601.03979); Permit (2605.09480)
- PACE; AgentFlow (2608.22868); AgentSecBench (2605.26269)
- Agent Gym (2608.15591); Agent System Operations (2606.01581); A Survey on AgentOps (2508.02121); interview study 2410.12071
- Namboothiri 2026 retrieve-then-filter (not found)

**Verified or seen but excluded as weaker fit or out of scope (29)**
- EnterpriseClawBench (2606.23654; data withheld); DataSpace (2608.03451); Data Agent Benchmark (2603.20576)
- Ahmed 2026 framework paper (2608.19235)
- PhantomPolicy / Wu & Gong (2604.12177); RAG protection survey (2610.30193); Securing RAG (2505.08728)
- HERB (2506.23139); READY (2609.02095)
- AgentGuard ABAC (2605.28071); IGAC (2606.22916); Baracaldo (2609.26682)
- MAGIC (Findings EMNLP 2025); DRAGged into Conflicts (2506.08500); TimelyRAG (2609.11572)
- Adaptive Chameleon or Stubborn Sloth (ICLR 2024); Yoran et al. (ICLR 2024)
- HopRefusalBench (2608.01358)
- Shankar et al. (2209.09125); Raji et al. (FAT* 2020); Kreuzberger et al. (IEEE Access 2023)
- Signal and Noise (NeurIPS 2025); Madaan et al. (2406.10229); tinyBenchmarks (ICML 2024)
- Noise Floor Audit (2608.22331); Beyond pass@1 (2603.29231)
- ToolBeHonest; "Don't Hallucinate, Abstain"; MiniCheck: searched, not retained

**Named in novelty verdicts but not among the rated closest works, so not added (10)**
- AgentArch (2509.10769); harness-induced variance, Zhang et al. (2605.23950); She & Lin (2609.21267); RAGOps (2506.03401)
- EntCollabBench (2605.08761); ToolPrivacyBench (2606.28061); ARBITER (2512.20535)
- SOCpilot (2605.05501); Leong 2026 (2608.28502)
- Permission-Aware RAG (IEEE Access 2025, DOI 10.1109/ACCESS.2025.3628960)

## Recommended follow-up searches (before June 2027)

1. **IEEE Xplore** (not reachable this session): "permission-aware RAG", "RBAC LLM", "enterprise LLM access control". Verify Permission-Aware RAG (IEEE Access 2025), which would be an IEEE-venue cite.
2. **Permission/access drift in RAG agents.** This query never ran in any agent.
3. **H1 confound framing.** Verify Zhang et al. (2605.23950, harness variance) and AgentArch (2509.10769).
4. **Additional RBAC-RAG baselines.** Verify ARBITER (2512.20535), EntCollabBench (2605.08761) and ToolPrivacyBench (2606.28061).
5. **Re-check preprint venues:**
   - LayerRAG-Bench, PCAS, Progent, CaMeL, FIDES, Maiorano x2
   - EvidenT and Prompts Don't Protect (EMNLP 2026 Industry: swap in ACL Anthology entries)
   - Pan et al. 2026 (PMLR pages)
   - TheAgentCompany track
   - ISO 42001 catalogue page
