# Jennifer Quay Minnich

- **Location**: Miami, Florida. Works remote, EST
- **Phone**: 347-844-1684
- **Email**: quay@quay-cncpts.com
- **LinkedIn**: jennifer-quay-minnich

---

## Credentials
United States Citizen | Public Trust Clearance | 9+ yrs of Software Engineering

## Education
B.S., M.S. in Computer Science (Machine Learning focus)

---

## Technical Proficiency

- **Programming**: Python, SQL, Bash/Shell
- **ML Frameworks**: PyTorch, TensorFlow, Scikit-learn, XGBoost, Hugging Face, PEFT, LoRA
- **ML & Data Science**: Neural Networks, Model Evaluation, Drift Monitoring, ETL, Data Governance, Data Cleansing, Feature Engineering, Statistical Modeling, Training + Fine Tuning
- **LLMs**: OpenAI, Claude, Gemini, Llama, Fine-Tuning, Prompt Engineering, RAG, MCP
- **NLP & Retrieval**: LangChain, LlamaIndex, FAISS, BERT, Sentence Transformers
- **AI**: Agentic Systems, Governance, Red Team Testing, LLM Evaluation, Model Alignment, Responsible AI
- **Cloud & Infrastructure**: GCP (Vertex AI, BigQuery), AWS (Lambda, S3, SageMaker, Bedrock), Azure (ML Studio, Blob Storage, Functions), CUDA, Distributed Training
- **CI/CD & MLOps**: Git, GitHub Actions, Docker, Kubernetes, Weights & Biases, ML Flow
- **Visualization & Dashboarding**: Tableau, Power BI, Plotly/Dash, Matplotlib, Seaborn, Grafana

---

## Publication

**2026** | Minnich, Jennifer, Q., et al. | "Stream Recursion Model: A Novel LLM Architecture" | Submitted to ICML 2026. Research funded by Sandia National Labs (DOE). Under review.

---

## Experience

### ML/AI Engineer, Data Scientist III | Arch Systems Inc. | Nov 2024 - present
Baltimore, MD (Remote) | Federal contractor for HHS, USCIS, FEMA | Public Trust Clearance

- Designed crosswalk normalization layer consolidating 15 disparate software inventory sources into normalized PostgreSQL schema (42 tables, 10 views), enabling compliance gap analysis and cost savings identification across DHS.
- Developed model-agnostic SOP generator (JENNY) reducing LLM token costs by 88% through split-phase architecture: LLM handles text extraction, Python handles template mutation with 82-84 validation gates per document, 100% structural compliance.
- Produced enterprise governance analytics from consolidated TRM database, identifying $9M+ in combined savings across contract optimization and cloud idle resources for DHS.
- Conducted cross-model security evaluations comparing OpenAI and Anthropic architectures, developing comprehensive testing playbooks covering endpoint testing, persona validation, and jailbreak evaluation.
- Built Zendesk automation system routing 150 monthly helpdesk tickets across 7 categories using macros, triggers, and webhooks with AI assistant architecture for escalation.
- Evaluated enterprise AI platform viability across 100 pilot users for HHS-ACF, building automated pipeline processing millions of logs into Tableau dashboard with user behavior clustering and model utilization analysis.
- Developed AI Constitution Testing framework implementing 15+ testing strategies including constitutional AI alignment, red team datasets, and reusable evaluation templates for ACF child welfare policy compliance.

### Machine Learning Engineer | ICASA | Jan 2021 - Nov 2024
Socorro, NM (Remote) | Federal contractor for DOE, NM State Higher Education, NM Legislative Committee | Public Trust Clearance

- Co-authored novel LLM architecture (SRM) achieving GPT-2 performance at half the parameters by introducing learnable inter-stream communication, enabling scalable mechanistic interpretability. Submitted to ICML 2026, funded by Sandia National Labs/DOE.
- Built transformer-based NLP pipeline (DistilBERT, BERTopic, KeyBERT) analyzing 5k open-ended survey responses on food and housing insecurity, deployed as Kubernetes-hosted Dash dashboard.
- Fine-tuned Llama 2 for natural language to SQL generation against 14 years of state tax data, achieving 95% query accuracy across three benchmarked approaches (fine-tuned LLM, LangChain, LlamaIndex).
- Secured $1M state funding for healthcare workforce dashboard, building scalable Python data pipeline and Scikit-learn/XGBoost forecasting models predicting coverage gaps.
- Facilitated ML training series empowering cross-functional teams with end-to-end AI tools from data preparation through model deployment.

### Software Engineer, Data Scientist | Office of Institutional Research, NM Tech | Feb 2020 - Jan 2021
Socorro, NM (Remote) | NM State Higher Education contract

- Implemented scalable ETL processes consolidating large datasets from multiple sources, generating data-driven insights that influenced research funding allocation.
- Fine-tuned NLP models for text classification, NER, and sentiment analysis on institutional datasets.
- Built student reporting dashboards using Python (Pandas, Matplotlib, Seaborn) with statistical analysis methods driving actionable recommendations.

### Software Engineer, Data Analyst | Consumer 51 | Apr 2017 - Feb 2020
Philadelphia, PA (Remote) | International e-commerce and consumer technology consultant

- Developed full-stack web applications for enterprise e-commerce clients.
- Built automated data pipelines and interactive Tableau dashboards for consumer analytics.
- Engineered algorithmic trading toolkit integrating Robinhood API, federal economic data feeds, and backtesting engine.

### Founder, Principal Consultant | Quay Concepts | Jan 2017 - present
Remote

- Founded consulting practice specializing in making advanced analytics accessible to nontechnical stakeholders.
- Bridging the gap between technical and nontechnical stakeholders via collaborations, mentorships, and trainings.

---

## Notable Projects

### Data/AI Implementations - Federal Government

**2026 | DHS - USCIS TRM Enterprise Software & Cloud Governance Analytics**
- Produced enterprise governance analytics identifying $9M+ in combined savings across contract optimization ($7.5M) and cloud idle resources ($1.5M) for DHS.
- Demonstrated TRM value through OCR category analysis: 144 fragmented product names across 6 sources mapping to 2 DHS TRM records, revealing ungoverned spend and redundant AI acquisitions.
- Cross-referenced AI use case registry against active contracts, surfacing retired-status products with active spend.

**2026 | DHS - USCIS TRM Pipeline & Data Governance Standardization**
- Reformed DHS Technical Reference Model (TRM) pipeline by implementing data governance standards and metadata requirements for AI/ML software asset management.
- Consolidated multiple USCIS data sources and developed universal data dictionary standardizing cross-system terminology and schema.
- Standardized adjudication policy for AI/ML software requests within TRM framework.

**2026 | DHS - FEMA FIWA SOP Generator (JENNY)**
- Developed AI-powered SOP generation tool automating the creation of compliant Standard Operating Procedures from agency templates, unstructured text, and written instructions.
- Designed hybrid pipeline architecture limiting LLM usage to text extraction with human-in-the-loop review and Python-based template execution, reducing token costs by 88% compared to monolithic LLM generation.
- Benchmarked pipeline across multiple LLMs evaluating cost, latency, and accuracy to identify optimal model configuration.
- Validated 100% structural compliance against agency SOP templates with PII redaction.

**2026 | DHS - USCIS Internal Chatbot Security Evaluation**
- Conducted cross-model performance and security comparisons between OpenAI and Anthropic architectures based on mission requirements.
- Developed comprehensive testing playbook covering endpoint testing, persona validation, workspace security labels, and jailbreaking evaluation.
- Reformed demand management and software asset management processes for AI/ML requests based on evaluation findings.

**2026 | DHS - FEMA Ops Brief Generator**
- Automated weekly FEMA operational brief generation by building Python pipeline combining PDF class schedules, Excel Board workbook, and In-Processing schedule data from three source systems.
- Eliminated manual data compilation for operational reporting, standardizing field mapping across disparate source formats.

**2026 | ACF - OHS IT-AMS Helpdesk Automation**
- Built automation system in Zendesk using macros, triggers, and web hooks to route 150 monthly tickets across 7 categories.
- Automated live data dashboards and reporting.
- Designed AI assistant-style architectures integrating retrieval, evaluation, and dynamic prompt routing pipelines.

**2026 | ACF - OHS IT-AMS Data/AI Strategy**
- Developed current-to-future state strategy document and executive presentation for IT-AMS system modernization integrating advanced analytics, ML, and AI capabilities.
- Presented to executive leadership outlining implementation roadmap for transitioning legacy system to AI-enabled infrastructure.

**2025 | HHS - ACF AI Constitution Testing & Alignment Framework**
- Developed comprehensive testing framework evaluating LLM compliance with ACF mission requirements for child and family services.
- Conducted technical evaluation of enterprise testing platforms (Promptfoo, Deepeval) with Credal AI integration for HHS-ACF.
- Built compliant automated testing pipeline implementing 15+ testing strategies including constitutional AI alignment for ACF policy compliance.
- Generated red team test datasets using ACF-specific policy constraints and child safety requirements.
- Created reusable evaluation templates enabling rapid deployment across multiple federal use cases, reducing testing cycle time.

**2025 | ACF - OHS Digital Services Transition**
- Led modernization data analytics, reporting, and innovation strategy for ACF legacy IT-AMS system.
- Developed predictive analytics pipeline to forecast Head Start program compliance, risk, and funding allocation.
- Built FedRAMP automated real-time dashboards using Tableau and AWS, enabling executive-level decision-making.

**2025 | HHS-ACF Credal AI Platform Evaluation & Usage Analytics**
- Evaluated enterprise viability of Credal AI across 100 pilot users for ACF under the Chief AI Officer, analyzing volume metrics (DAU/WAU, session duration, API calls) and context patterns (use case mapping, copilot adoption, model utilization across GPT-4o/o1-mini/4o-mini).
- Engineered memory-optimized star schema via Tableau Hyper API, automating daily ingestion of millions of Credal AI logs with Python-based validation, cleaning, and statistical analysis pipeline.
- Applied user behavior clustering algorithms (k-means, hierarchical) to identify adoption patterns and segment user cohorts by engagement level and use case.
- Built automated Tableau dashboard providing executive-level insights for enterprise purchase decision.

**2025 | HHS-ACF Know Your Customer LLM Service Classification**
- Evaluated LLM effectiveness with analyzing and classifying services provided by ACF grantees.
- Cross model comparison analysis of accuracy and efficiency for returning services.
- Created strategic approach for scaling across ACF's thousands of grantees.

### FinTech Projects using Machine Learning

**2022 | Classification of Malicious Cyber Activity via Machine Learning**
- Developed feature engineering and encoding strategies, implementing Isolation Forest algorithms to categorize events as routine or anomalous.
- Evaluated model performance using Scikit-learn with dimensionality reduction (t-SNE), confusion matrices, and AUC-ROC analysis.

**2022 | Stock Bought Stock Trading Project**
- Engineered algorithmic trading toolkit integrating Robinhood API, federal economic data feeds, backtesting engine, and live execution with PyQt GUI.
- Leveraged correlative and predictive statistics to validate and optimize trading strategies.

### Higher Education & State Funded Data/AI Projects

**2024 | Cyber-Physical Sensing Research**
- Led cross-functional teams solving critical research problems in multi-modal sensing and unintended sensing domains.
- Implemented cloud-based machine learning tools with Python preprocessing and feature extraction.

**2024 | NM Higher Ed Basic Needs Analysis with NLP**
- Built transformer-based NLP pipeline (DistilBERT, BERTopic, KeyBERT) analyzing 5k open-ended survey responses on food and housing insecurity.
- Deployed as Kubernetes-hosted Dash dashboard with Docker containerization and Helm charts.
- Created real-time data exploration visualizations with Plotly and Dash.

**2024 | NM Higher Ed Student Reporting Dashboard**
- Comprehensive data analysis for thousands of students using Python, applying statistical methods (descriptive, regression, correlative).
- Generated actionable data-driven insights and visualizations that influenced research funding allocation.

**2023 | Healthcare Workforce Dashboard**
- $1M funded project to establish and maintain a state healthcare workforce dashboard.
- Designed scalable Python data pipeline ingesting large datasets from multiple sources.
- Built ML forecasting models (Scikit-learn, XGBoost) predicting healthcare coverage gaps.

### Research & Development

**2026 | Stream Recursion Model (SRM): A Novel LLM Architecture**
- Co-authored novel LLM architecture introducing stream-wise attention for learnable inter-stream communication, achieving GPT-2 performance at half the parameters (68M vs 124M). ICML 2026, funded by Sandia National Labs/DOE.
- Analysis revealed hub-like stream routing topology and specialized stream behavior, with top 9 of 32 streams accounting for 50% of causal impact through ablation studies.
- Trained three model variants (SRM-base, SRM-med, SRM-large up to 454M params) on OpenWebText using a single 4xL40s GPU cluster over ~1000 GPU hours.

**2025 | iHCD Human Centered Design Gen AI using RAG**
- Developed comprehensive data analysis system integrating multiple data sources using Python and GPT-4o.
- Engineered document processing pipeline using FAISS vector store and LangChain for efficient retrieval.
- Built intelligent prompt engineering system dynamically adapting analysis approaches based on query content.

**2023 | Analysis of GitHub Repositories using Neural Networks**
- Mined GBs of GitHub public user data into JSON format using Python (Pandas, NumPy).
- Built and trained TensorFlow neural network models profiling repository users.
- Predicted next user activity with high accuracy.

**2023 | Natural Language Interface for NM Tax Data**
- Fine-tuned Meta AI Llama 2 using HuggingFace and PyTorch, achieving 95% accuracy for NL-to-SQL generation.
- Implemented LlamaIndex and LangChain for optimized RAG.
- Deployed on GCP Vertex AI with MongoDB document store.

---

## References

**Jane Yang** | Chief Artificial Intelligence Officer, ACF Tech | Administration for Children and Families, US Department of Health and Human Services | jane.yang@acf.hhs.gov | (202) 545-4952

**Justin Hoffman** | Principal AI Data Scientist | Arch Systems | jhoffman@archsystemsinc.com | (210) 875-8278

---

## Education (Detail)

**2017-2022 | BS, MS Computer Science & Engineering** | New Mexico Institute of Mining & Technology
- 5yr accelerated BSCS/MSCS program
- Merit based CAHSI S-STEM scholar
- Tau Beta Pi Engineering Honors Society
