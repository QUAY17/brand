# Jennifer Quay Minnich

- **Location**: Miami, Florida
- **Email**: quay@quay-cncpts.com
- **LinkedIn**: jennifer-quay-minnich
- **Phone**: 347-844-1684 (text)

---

## Summary

Senior AI & Data Engineer | International Conference on Machine Learning (ICML) 2026 co-author | 9+ years shipping production software, from SaaS to AI | developed AI and data systems for DHS, HHS, and DOE | designed data architecture, PostgreSQL governance databases, and the retrieval layer powering RAG knowledge platforms | led technical direction across public and private platforms | Public Trust clearance

## Credentials
United States Citizen | Public Trust Clearance | 9+ yrs of Software Engineering

## Education
B.S., M.S. in Computer Science, Machine Learning focus

---

## Technical Proficiency

- **Languages**: Python, SQL, Bash/Shell
- **ML & Deep Learning**: PyTorch, scikit-learn, Pandas, NumPy, TensorFlow, XGBoost, Hugging Face
- **LLMs & Frameworks**: Claude, OpenAI, LangChain, LangGraph, LangSmith, MCP, fine-tuning open-source LLMs (LLaMA)
- **RAG & LLM Evaluation**: RAG, semantic search over vector DBs, prompt engineering, model evaluation, accuracy optimization, hallucination evaluation (semantic similarity), LLM-as-a-judge groundedness, token-cost reduction
- **Data & Storage**: PostgreSQL, MongoDB, Databricks, BigQuery, Pinecone, Elasticsearch, FAISS
- **Data Engineering & Pipelines**: custom Python ETL, data ingestion & throughput, pipeline orchestration, schema validation, data quality, medallion lakehouse, crosswalk normalization, data governance
- **Cloud**: Azure (OpenAI, AI Foundry, ML Studio), AWS (Bedrock, SageMaker, Lambda, S3), GCP (Vertex AI), cost optimization
- **MLOps & Deployment**: Docker, Kubernetes, FastAPI, Git/GitHub Actions, Jenkins, Harness, MLflow, Weights & Biases; model versioning, drift monitoring, red-teaming, alignment, responsible AI
- **Full-Stack & Visualization**: Node.js, React, Three.js/WebGL, REST APIs, Tableau, Power BI, Grafana

---

## Publication

**2026** | Minnich, Jennifer Q. (co-author) | "Stream Recursion Model: A Novel LLM Architecture" | Submitted to ICML 2026. An interpretable architecture that matches GPT-2 performance at half the parameters via recursively refined latent streams. Research funded by Sandia National Labs (DOE). Under review.

---

## Experience

### Senior AI & Data Engineer | Arch Systems Inc. | Nov 2024 - present
Baltimore, MD (Remote) | Federal contractor

- Architected the enterprise AI application that consolidated disparate USCIS IT systems into one platform - identifying $9M+ in savings through its Technical Reference Module governance layer.
- Built JENNY, a split-phase document generator that cut LLM token cost 88% and per-document cost 15-25x. Winner, 2026 FORUM Innovation Award.
- Set the data architecture and design-review standards across two federal platforms and mentored the engineers building them.
- Built LLM security and compliance testing for federal AI systems - cross-model evaluation (OpenAI vs Anthropic), jailbreak resilience, and 15+ red-team strategies against agency policy and compliance boundaries.

### Machine Learning Engineer | ICASA (NMT) | Jan 2022 - Nov 2024
Socorro, NM (Remote) | Federal contractor for DOE | Institutional research and development

- Co-authored a novel LLM architecture (Stream Recursion Model) submitted to ICML 2026, funded by Sandia National Labs/DOE. Splitting computation across interacting latent streams makes each stream's dynamics, causal contribution, and routing directly measurable - exposing the model's internal reasoning where transformers stay a black box.
- Secured $1M in funding for the Healthcare Workforce Dashboard by building a single source-of-truth database (10+ state and regional data systems, plus market-analysis data) and analyzing statewide coverage gaps.
- Turned thousands of open-ended survey responses on food and housing insecurity into statewide policy and budget decisions, building the pre-LLM transformer NLP pipeline that surfaced the themes.
- Built a natural-language-to-SQL chatbot at 92.5% accuracy over historical state tax and financial data, letting users query and understand complex data in plain language.
- Ran an internal ML/AI training series for engineering and analytics teams, standardizing how the org builds and evaluates LLM tooling.

### Data Scientist | ICASA (NMT) | Feb 2020 - Jan 2022
Socorro, NM (Remote) | Federal contractor for DOE | Institutional research and development

- Hired full-time after internship on the strength of early ML and AI research traction.
- Built graph neural networks modeling relationships between GitHub events to predict next-event activity.
- Built the Computer Science department reporting tool that analyzed enrollment and funding allocation with statistical and ML methods.


### Software Engineer | Consumer 51 | Apr 2017 - Feb 2020
Philadelphia, PA (Remote) | International consumer technology consultant

- Shipped full-stack web applications (Python, JavaScript, SQL) for enterprise e-commerce clients across international markets.
- Built consumer analytics dashboards in Tableau tracking sales and behavior patterns across multiple product lines.
- Engineered an algorithmic trading toolkit integrating Robinhood API, federal economic data feeds, and a backtesting engine.

### Founder, Principal Consultant | Quay Concepts | Jan 2017 - present
Remote

- Founded a consulting practice offering AI/ML services, analytics acceleration, and full-stack web development.
- Built interactive React/WebGL prototypes, SVG visuals, and design systems, and reviewed UI/UX assets and UI kits for AI products.

---

## Notable Projects

### Data/AI Implementations - Federal Government

**2026 | U.S. Army HAWKEYE-DQ - Data-Quality Error Bot (IPPS-A)**
- Architected a medallion lakehouse (Bronze/Silver/Gold) that lands raw Army HR and pay data exactly as received, then validates it - catching defects before they reach downstream systems.
- Designed a two-track validation flow that quarantines untrustworthy rows and flags fixable ones, then routes each defect to an owner with a recommended fix.
- Built the ingestion and validation pipeline across 40+ Army data interfaces (~25 inbound, ~17 outbound) in PostgreSQL with custom Python ETL and full source/load lineage - automated schema validation held the data error rate to 0.015%.

**2026 | DHS-USCIS Technology Reference Model (TRM)**
- Built the TRM in PostgreSQL - consolidated ~20 disparate data sources into a normalized 45-table schema fed by an ETL pipeline (APIs, scripts, manual extracts) with a crosswalk normalization layer resolving each source to canonical master records.
- Generalized the crosswalk into Temper, reusable normalization IP - a resolver with a built-in audit trail that makes every record match traceable and defensible.
- Produced the governance analytics behind the $9M+ in savings ($7.5M contract consolidation + reduction, $1.5M cloud idle).
- Standardized how DHS approves AI/ML software for use, aligning the TRM's review criteria to FEAF and NIST.

**2026 | DHS-USCIS Enterprise AI Architecture**
- Unified idea and demand management, the Technology Reference Model, budgeting, analytics, and dashboards into one enterprise platform, replacing disparate IT inventory systems and disconnected operational pipelines.
- Built the data and ML pipelines feeding 5 production models, cutting downstream model drift and accelerating deployment 25%.

**2026 | DHS-FEMA FIWA SOP Generator (JENNY)**
- Split the pipeline so the LLM only extracts content while deterministic Python handles template execution; benchmarked across multiple LLMs for cost, latency, and accuracy.
- Validated 100% structural compliance against agency SOP templates across 82-84 gates per document, with PII redaction.

**2025 | HHS - ACF AI Constitution Testing & Alignment Framework**
- Developed an endpoint-testing framework that evaluates agentic LLMs against ACF mission requirements (the 'Constitution') for child and family services.
- Evaluated LLM testing platforms (Promptfoo, Deepeval) against ACF's compliance needs and recommended the integration path.
- Built the automated testing pipeline behind it - 15+ strategies and ACF-specific red-team datasets probing each model endpoint for policy and child-safety compliance.

**2025 | HHS-ACF Credal AI Usage Analytics**
- Built the real-time ETL pipeline feeding an executive Tableau dashboard - a memory-optimized star schema (Tableau Hyper API) that ingested and validated millions of platform logs as they streamed in.
- Analyzed both structured usage and unstructured prompt text - k-means and hierarchical clustering on user cohorts, plus topic modeling and semantic-similarity analysis of user prompts.

### FinTech Projects using Machine Learning

**2022 | Stock Bought Stock Trading Project**
- Engineered an algorithmic trading toolkit (Robinhood API, federal economic data, backtesting, live execution via PyQt), tuning strategies with correlation and regression analysis over historical market data.

### Higher Education & State Funded Data/AI Projects

**2024 | NM Higher Ed Basic Needs Analysis with NLP**
- Evaluated student food- and housing-insecurity survey data with a transformer-based NLP pipeline - DistilBERT sentiment, BERTopic topic modeling, KeyBERT keyword extraction.
- Deployed as a containerized Kubernetes dashboard (Docker, Helm) with FastAPI-served drill-down exploration of keywords and themes.

**2023 | Natural Language Interface for NM Tax Data**
- Fine-tuned Llama 2 (HuggingFace, PyTorch) for NL-to-SQL at 92.5% accuracy.


### Research & Development

**2026 | Stream Recursion Model (SRM): A Novel LLM Architecture**
- Co-authored SRM, an interpretable LLM architecture that organizes computation into interacting latent streams updated through recursive refinement, exposing internal structure - stream dynamics, causal contribution, and routing.
- A practical foundation for scalable mechanistic interpretability - analysis shows consistent, structured specialization across streams. ICML 2026 (under review); funded by Sandia National Labs/DOE.

### Additional Projects (full summaries on request)

---

## References

**Justin Hoffman** | Director of AI Software Engineering | Arch Systems Inc., Federal Contractor | jhoffman@archsystemsinc.com | (210) 875-8278


**Jane Yang** | Chief Artificial Intelligence Officer, ACF Tech | Administration for Children and Families, US Department of Health and Human Services | jane.yang@acf.hhs.gov | (202) 545-4952
---

## Education (Detail)

**2017-2022 | BS, MS Computer Science & Engineering** | New Mexico Institute of Mining & Technology
- 5yr accelerated BSCS/MSCS program
- Merit based CAHSI S-STEM scholar
- Tau Beta Pi Engineering Honors Society
