# Jennifer Quay Minnich / Quay Concepts Brand Voice Guidelines

## Generation Metadata
- Created: 2026-03-29
- Version: 3
- Sources: Resume (LaTeX), SRM paper (ICML 2026 submission), CARES TRM Data Analysis II, CARES TRM OCR Tool Analysis, Credal AI Usage Analytics Project Scope, GitHub (QUAY17), GitHub (archsystemsinc-com), Gmail correspondence, career context
- Documents processed: 5 (resume, SRM paper, TRM analysis, OCR analysis, Credal scope)
- Overall confidence: High

---

## Executive Summary

Jennifer Quay Minnich is an ML/AI Engineer and Data Scientist with 9+ years shipping production systems across federal government (DHS, HHS, DOE), higher education, and private sector. She holds a BS and MS in Computer Science (ML focus), Public Trust clearance, and is co-author of a novel LLM architecture (Stream Recursion Model) submitted to ICML 2026 and funded by Sandia National Labs/DOE.

Her work spans three distinct modes that few engineers cover simultaneously:

**Research**: Co-authored SRM, a novel LLM architecture that achieves GPT-2 performance at half the parameters (68M vs 124M) by introducing learnable inter-stream communication. The architecture is inherently interpretable -- stream ablation studies, hub-like routing topology analysis, and KL divergence measurements for representational drift. This is not applied ML; this is fundamental architecture research at the ICML level.

**Production AI systems**: JENNY (model-agnostic document generator, 88% token cost reduction, 100% compliance validation), AI Constitution Testing framework (15+ testing strategies for federal child welfare policy), cross-model security evaluations (OpenAI vs Anthropic), Credal AI platform evaluation (100 users, millions of logs, user behavior clustering).

**Data governance and infrastructure**: TRM database consolidating 15 source systems into 42-table PostgreSQL schema, producing $9M+ in identified savings. OCR governance analysis revealing 144 fragmented product names across 6 sources. Crosswalk normalization enabling compliance gap, spend, and redundancy analysis previously impossible at DHS.

Her consulting entity, Quay Concepts, extends the same ethos: measurable outcomes, shipped systems, no wasted words.

The voice across all content should communicate: I do the research, I build the system, I produce the governance analytics, and I present to leadership. That combination at $160k+ is rare.

---

## Visual Identity

### Color Palette

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| **Primary** | Orange | `#E07020` | Logo only -- reserved exclusively for the QUAY wordmark |
| **Accent** | Gold | `#C9A84C` | Highlight stat text, link hovers, data callouts |
| **Background** | Charcoal | `#2F3136` | Primary background for web, presentations, and brand assets |
| **Text (primary)** | Light gray | `#E4E6E9` | Body text on dark backgrounds |
| **Text (secondary)** | Gray | `#B0B5BC` | Taglines, supporting text |
| **Text (tertiary)** | Dim gray | `#7A8290` | Labels, metadata, footer text |
| **Ambient: Purple** | Deep purple | `#3D1A6E` to `#2A1250` | Two-tone glow (bottom-left) |
| **Ambient: Blue** | Electric blue | `#1D4ED8` to `#162E6E` | Two-tone glow (right, mid-height) |
| **Ambient: Gold** | Dark gold | `#B8891A` to `#7A5C12` | Two-tone glow (bottom-center) |
| **Ambient: Magenta** | Purple-magenta | `#5B21B6` to `#3B1578` | Two-tone glow (top-left) |
| **Ambient: Navy** | Deep navy | `#152D55` to `#0E1F3A` | Two-tone glow (top-right) |

### Color Rules

- Orange is **exclusively** for the QUAY wordmark. No other element on the page uses orange.
- Gold (`#C9A84C`) is the secondary accent for all interactive and highlight elements.
- The ambient glow uses five orbs creating an aurora effect that evokes the original Quay Concepts abstract imagery. Each orb uses a two-tone radial gradient for depth. CSS `filter: blur(50px)` on desktop, `blur(40px)` on mobile. Orbs are sized in `vw` units so they scale with viewport.
- Glow orbs drift slowly (14-20s cycles) with subtle translate and scale transforms. Purple and magenta are pulled back in opacity; blue and gold are boosted for color contrast.

### Typography

| Element | Font | Weight | Notes |
|---------|------|--------|-------|
| Logo (Quay) | Orbitron | 400 (Light) | Title case. Matches the original geometric wordmark. |
| Tagline | Inter | 300 (Light) | Title case. Letter-spacing: 0.25em. Not uppercase. |
| Highlight labels | Inter | 400 | CSS uppercase, letter-spacing: 0.3em |
| Highlight stats | Inter | 500 (Medium) | CSS uppercase, letter-spacing: 0.08em, gold accent color |
| Links | Inter | 400 | CSS uppercase, letter-spacing: 0.2em |

### Design Principles

- **One screen, no scroll**: The site fits entirely in a single viewport. `overflow: hidden` on html/body. No navigation, no sections, no pages.
- **Logo-forward**: Quay in Orbitron dominates the visual hierarchy. Title case (not all caps). Everything else supports it.
- **Ambient glow**: Five drifting radial gradient orbs (purple, blue, gold, magenta, navy) spread across the full viewport create depth and life. Sized in `vw` units for responsive scaling. Low blur for visible ripple edges.
- **Rotating highlights**: Key stats cycle with a slide-up/slide-out animation. Each has a single past-tense verb label (Published, Saved, Patented, Cut, Cleared, Shipped, Built, Deployed) above an uppercase gold stat line.
- **Minimal**: No images, no icons, no borders, no cards. Just type, color, and light.
- **Favicon**: Orbitron Q glyph path in orange on charcoal with ambient gradient background. SVG format.
- **LinkedIn profile image**: Quay wordmark (Orbitron glyph paths, title case) with tagline on ambient gradient background. "Designing Intelligence" left-aligned, "Developing the Future" right-aligned under the logo.

---

## We Are / We Are Not

| We Are | We Are Not |
|--------|------------|
| **Impact-driven** -- every claim ties to a measurable outcome or shipped system | **Vague** -- we never say "helped improve" without saying by how much |
| **Technically deep** -- we know the architecture, the tradeoffs, and the failure modes | **Jargon-stuffing** -- depth means understanding, not keyword dumps |
| **Direct** -- we get to the point in the first sentence | **Blunt or cold** -- directness includes professionalism and warmth |
| **Versatile** -- we move from research papers to production pipelines to executive presentations | **Scattered** -- versatility is deliberate range, not lack of focus |
| **Credible** -- clearance, publications, federal clients, named references | **Self-promotional** -- the work speaks; we do not oversell |
| **Builder** -- we ship things that people use and that change processes | **Theoretical** -- research matters, but only if it reaches production |

### Voice Attributes Detail

#### Impact-driven
- **What it means**: Every bullet, every claim, every project description anchors to a concrete result -- cost reduction, accuracy improvement, compliance metric, funding secured, process reformed.
- **How it shows up**: Lead with the outcome, then explain the method. "Reduced token costs by 88% by designing hybrid pipeline architecture" not "Designed a pipeline that was more cost efficient."
- **What to avoid**: Passive language, missing metrics, "contributed to" without specifics.

#### Technically deep
- **What it means**: Demonstrate that you understand the system end-to-end -- from data governance to model architecture to deployment infrastructure.
- **How it shows up**: Name specific tools, frameworks, and architectural decisions. "Implemented FAISS vector store with LangChain retrieval" not "used AI search."
- **What to avoid**: Listing tools without context. Every tool mentioned should connect to a decision or outcome.

#### Direct
- **What it means**: Respect the reader's time. First sentence carries the weight. Say what you did, not what it sounds like you did.
- **How it shows up**: Short email signatures. No preamble in cover letters. Resume bullets that start with the strongest verb. Plain language over jargon -- always. If a sentence reads like a consulting slide deck, rewrite it until a person would actually say it out loud.
- **What to avoid**: Filler phrases like "I am writing to express my interest in..." or "I believe I would be a great fit." Jargon-stacked sentences that sound impressive but communicate nothing. Modifier pileups ("comprehensive automated real-time scalable"). Trailing filler ("enabling executive-level decision-making").
- **The rule**: If you strip out all the adjectives and buzzwords and the sentence says nothing, the sentence was never saying anything. Start over.

#### Versatile
- **What it means**: The ability to operate across the full stack of data/ML/AI work -- from ETL and data governance through model training to executive dashboards.
- **How it shows up**: Resume sections and project descriptions that demonstrate range without repetition. Each role or project highlights a different facet.
- **What to avoid**: Making it look like you cannot decide what you want to be. Frame versatility as deliberate capability, not career drift.

#### Credible
- **What it means**: Public Trust clearance, ICML publication, named federal clients (HHS, DHS, USCIS, FEMA), named references at the Chief AI Officer level.
- **How it shows up**: State credentials upfront. Reference specific agencies and programs by name. Include the publication with venue and status.
- **What to avoid**: Over-explaining credentials. "Public Trust Clearance" speaks for itself.

#### Builder
- **What it means**: You do not just analyze or advise -- you build the system, deploy the pipeline, and automate the workflow. Your GitHub proves it.
- **How it shows up**: Strong action verbs: built, developed, deployed, automated, reformed, architected. Project descriptions that describe what was shipped. Public repos with real code.
- **What to avoid**: Consultant-speak that is all strategy and no execution.

---

## Brand Personality

- **Archetype**: The Senior Engineer Who Ships -- technically rigorous, outcome-obsessed, no-nonsense but approachable.
- **If this brand were a person**: Someone who shows up to the meeting with the dashboard already built, the metrics already pulled, and a one-page recommendation ready. Gives you the answer first, then the reasoning if you want it.
- **Core values expressed in voice**: Accountability, precision, speed, impact, accessibility (making technical work understandable to leadership).

---

## Messaging Framework

### Primary Value Proposition
ML/AI engineer who publishes novel architecture research (ICML) AND ships production systems for federal agencies -- with the data governance chops to identify $9M+ in savings from the same database she designed.

### Key Message Pillars

1. **Research-to-Production**
   - Core idea: I co-author ICML papers on novel LLM architectures AND build the SOP generators, testing frameworks, and governance databases that federal agencies use daily. Same person.
   - When to use: Resume summary, cover letters, LinkedIn headline/about, consulting proposals
   - Example phrasing: "From ICML architecture research to deployed federal AI systems"
   - Evidence: SRM paper (GPT-2 performance at half the parameters), JENNY (88% token cost reduction), TRM (15 sources consolidated)

2. **Measurable Impact**
   - Core idea: Every project has numbers. $9M+ savings identified. 88% token cost reduction. 100% compliance validation. 95% NL-to-SQL accuracy. 100 pilot users evaluated. 15 source systems consolidated.
   - When to use: Resume bullets, case studies, interview responses, proposal ROI sections
   - Example phrasing: "Identified $9M+ in cost savings by cross-referencing AI use case registry against active contracts through the TRM I built"

3. **Federal AI Governance**
   - Core idea: Public Trust cleared, experienced navigating FedRAMP, responsible AI, constitutional AI alignment, red team testing, software asset management policy, and agency-specific compliance. I do not just build AI; I govern it.
   - When to use: Federal job applications, cleared positions, GovCon proposals, AI governance roles
   - Example phrasing: "Built the AI Constitution Testing framework, the TRM governance database, and the cross-model security evaluations -- all for the same set of federal agencies"
   - Evidence: TRM + CARES analysis, AI Constitution Testing, chatbot security evaluations, OCR governance analysis

4. **Full-Stack Data/AI**
   - Core idea: End-to-end ownership from crosswalk normalization and data governance through model training and LLM architecture research to executive Tableau dashboards and stakeholder presentations.
   - When to use: Roles that need breadth, consulting pitches, LinkedIn content
   - Example phrasing: "I designed the 42-table schema, wrote the 13 data loaders, produced the governance analytics, and presented the $9M savings to leadership"
   - Evidence: TRM backend (data engineering), SRM (research), JENNY (applied AI), Credal evaluation (analytics + dashboards), Ops Brief generator (automation)

### Competitive Positioning
- vs. Pure Data Scientists: I also design the database schema, build the ETL, and deploy the models. The TRM is 42 tables and 13 loaders that I architected.
- vs. Pure ML Engineers: I also publish architecture research. SRM is an ICML submission, not a fine-tuning exercise.
- vs. Pure Software Engineers: I bring ML/AI depth from LLM architecture (SRM) through applied NLP (Basic Needs) to production deployment (JENNY, TRM).
- vs. AI Researchers: I also ship production systems. JENNY runs at FEMA. The TRM runs at USCIS. The Credal evaluation informed a real enterprise purchase decision.
- vs. AI Governance/Policy people: I do not just write frameworks -- I build the testing pipelines, the compliance databases, and the security evaluation playbooks. Then I present to the Chief AI Officer.
- vs. Status Quo (staying at current comp): ICML co-author + Public Trust + federal production AI + data governance architecture + $9M savings identification. That combination does not exist at $140k.

---

## Tone-by-Context Matrix

| Context | Formality | Energy | Technical Depth | Key Principle |
|---------|-----------|--------|-----------------|---------------|
| Resume bullets | High | Medium | High | Outcome first, method second |
| Cover letter | Medium-High | Medium | Medium | Why this role, why me, one paragraph max per point |
| LinkedIn post | Medium | Medium-High | Medium | Share insight or lesson, not self-congratulation |
| LinkedIn profile/about | Medium | Medium | Medium-High | Narrative arc from education through current impact |
| GitHub README | Medium | Low-Medium | High | What it does, how to run it, what problem it solves |
| Recruiter email | Low-Medium | Medium | Low | Direct, short, state availability and rate/expectations |
| Consulting proposal | High | Medium | High | Problem-solution-outcome with metrics |
| Portfolio/case study | Medium-High | Medium | High | Walk through the technical decisions and results |
| Interview prep | Medium | High | High | STAR format but lead with the result |
| Cold outreach (job) | Medium | High | Low-Medium | Hook with strongest credential, ask for 15 minutes |
| Slack/internal comms | Low | Medium | Varies | Brief, action-oriented, no ceremony |

### Context-Specific Guidelines

#### Resume Bullets
- Start with a strong past-tense verb (Reformed, Developed, Architected, Built, Deployed, Automated, Benchmarked)
- Include a metric or measurable outcome whenever possible
- Name the specific technology, framework, or platform
- Keep to 1-2 lines max per bullet
- Do not start multiple bullets with the same verb in a single role

#### GitHub READMEs
- First line: one sentence saying what the project does and the key result
- Include a "Quick Start" or "How to Run" section
- Link to the publication or paper if applicable
- Architecture diagram or pipeline overview if the project has multiple components
- Do not include badges or shields unless they convey real information (build status, coverage)

#### Compensation & Work Arrangement

- **Remote only. No exceptions.**
- **$80/hr+ W2 / $160k+ FTE base.** This is the floor, not the target.
- Titles: ML/AI Engineer, Senior Data Scientist. Will consider AI Engineer, LLM Engineer, Principal Data Scientist.
- Do not engage with roles below the floor. A polite "that's below my range" is sufficient.
- Do not negotiate against yourself. State the number, let them respond.
- Context: ICML co-author + Public Trust + 9+ years production software + federal AI governance + $9M savings identification. That combination commands this rate.

#### Recruiter/Job Search Emails
- Keep to 3-5 sentences max
- State role interest, availability, and comp expectations clearly
- Sign off with: "Best, Jennifer Minnich / quay-cncpts.com / 347.844.1684"
- Do not attach resume unless asked -- offer to send it

#### Gmail Filter Strategy

Two filters route recruiter email. YES = auto-reply. NO = archive silently.

**YES filter** -- remote + right title:
- Has the words: `remote (ML OR "machine learning" OR "AI engineer" OR "data scientist" OR "agentic" OR "LLM")`
- Action: Keep in Inbox, label `Jobs`, send template "Recruiter Auto-Reply"

**NO filter** -- onsite/hybrid/wrong title:
- Has the words: `onsite OR hybrid OR "on-site" OR "in-office" OR "in office" OR subject:("data mining" OR ".net" OR "graphic designer" OR "data entry" OR "business analyst" OR "QA" OR "devops")`
- Action: Skip Inbox, Mark as read

**NO filter** -- LinkedIn automated digests:
- From: `jobs-noreply@linkedin.com OR jobalerts-noreply@linkedin.com OR messages-noreply@linkedin.com`
- Action: Skip Inbox, Mark as read

**Recruiter Auto-Reply Template** (saved in Gmail with resume PDF attached):
```
Jennifer Minnich | ML/AI Engineer | ICML 2026 Co-Author
Remote Only | $80/hr+ W2 / $160k+ FTE | No exceptions

If this role fits, send the JD and rate to quay@quay-cncpts.com.

Best,
Jennifer Minnich
quay-cncpts.com | 347.844.1684
```

#### LinkedIn Posts
- Lead with a concrete observation or lesson from real work
- No hashtag spam -- 3 max if any
- Do not post "excited to announce" style content
- Share technical insights that demonstrate expertise without being a tutorial

#### Consulting Proposals (Quay Concepts)
- Frame around client's problem first, not your capabilities
- Include a "What You Get" section with specific deliverables
- Reference similar past work with metrics
- Keep scope tight and timeline concrete

---

## Terminology Guide

### Must-Use Terms
| Term | Usage | Instead Of | Example |
|------|-------|------------|---------|
| shipped / deployed | When describing production work | "worked on", "helped with" | "Shipped AI-powered SOP generation tool" |
| reformed / architected | When describing systemic change | "improved", "updated" | "Reformed TRM pipeline data governance standards" |
| pipeline | For data/ML workflows | "process", "system" (when vague) | "Built compliant automated testing pipeline" |
| model-agnostic | When describing flexible AI systems | "works with different models" | "Model-agnostic document generator" |

### Preferred Terms
| Term | Usage | Example |
|------|-------|---------|
| production | Deployed, live systems | "Moved model to production on AWS" |
| end-to-end | Full ownership from data to deployment | "End-to-end ML pipeline ownership" |
| cross-model comparison | When evaluating multiple LLMs | "Cross-model performance comparison" |
| hybrid architecture | When combining multiple approaches | "Hybrid pipeline limiting LLM usage to extraction" |
| human-in-the-loop | When describing AI+human review systems | "Human-in-the-loop review pipeline" |

### Avoid These Terms
| Term | Reason | Alternative |
|------|--------|-------------|
| passionate about | Overused, says nothing | Show passion through the work described |
| leveraged (as filler) | Only use when it genuinely means "used as leverage" | "Used", "Applied", "Implemented" |
| utilize | Pretentious synonym for "use" | "Use" |
| synergy / synergize | Corporate filler | Describe the actual collaboration |
| helped / assisted | Diminishes ownership | "Led", "Built", "Developed" |
| various | Vague | Name the specific things |
| cutting-edge | Overused buzzword | Name the specific technology or approach |
| rock star / ninja / guru | Unprofessional | Senior Engineer, Principal, Lead |
| comprehensive | Filler -- everything claims to be comprehensive | Describe what it actually covers |
| advanced analytics | Vague buzzword | Name the specific method (clustering, forecasting, etc.) |
| innovative / innovation | Says nothing -- the work should show it | Describe what was new and why it mattered |
| robust / scalable (without evidence) | Empty modifiers | State the actual scale or resilience metric |
| integrating [buzzword] capabilities | Jargon padding | Say what the system does in plain language |
| enabling [stakeholder]-level [noun] | Filler ending for bullets | End with the actual outcome or cut the sentence shorter |
| dynamic [anything] | Almost always meaningless | Say what changes and why |

### Never-Use Terms
| Term | Reason |
|------|--------|
| "just a" (self-diminishing) | Undermines authority |
| "I think maybe" (hedging) | State positions with confidence |
| "detail-oriented" (resume cliche) | Show detail through specific metrics instead |
| emojis in professional content | Per personal preference -- no emojis in code or text |

---

## Language That Works

### Top Phrases
1. **"Reformed [X] by implementing [Y]"** -- Shows systemic change, not just task completion
2. **"Reduced [metric] by [X]% compared to [baseline]"** -- Quantified improvement with context
3. **"Built [system] enabling [stakeholder] to [action]"** -- Connects technical work to business value
4. **"Cross-model comparison of [X] evaluating [metrics]"** -- Shows rigor in AI evaluation work
5. **"Validated 100% [compliance/accuracy] against [standard]"** -- Shows precision and standards adherence

### Strong Opening Lines (by context)
- **Resume summary**: "ML/AI Engineer and ICML co-author with 9+ years shipping production AI systems and data governance infrastructure across DHS, HHS, and DOE. Public Trust clearance."
- **Cover letter**: "I co-authored a novel LLM architecture submitted to ICML, built the AI governance database that identified $9M+ in savings for DHS, and shipped the SOP generator that reduced FEMA's token costs by 88%. Same year."
- **LinkedIn about**: "I publish LLM architecture research (ICML 2026) and ship production AI systems for federal agencies. Currently building AI governance infrastructure for DHS and HHS."
- **Recruiter reply**: "Interested. Looking for $160k+ base, remote, ML/AI engineering or senior data science. ICML co-author, Public Trust, 9+ years federal AI."
- **GitHub bio**: "ML/AI Engineer. ICML 2026 co-author. Research-to-production."

---

## Language to Avoid

### Anti-Patterns
1. **"Responsible for [X]"** -- Problem: passive, describes a job description not an accomplishment. Better: "[Verb] [X], resulting in [Y]"
2. **"Helped improve [X]"** -- Problem: diminishes ownership and lacks specificity. Better: "Improved [X] by [metric] through [method]"
3. **"Worked on various projects"** -- Problem: vague, no signal. Better: Name the projects and outcomes.
4. **"I am a highly motivated professional"** -- Problem: tells instead of shows. Better: Let the ICML paper and federal clients speak for themselves.
5. **Long paragraphs in emails to recruiters** -- Problem: recruiters skim. Better: 3-5 sentences, state what you want, move on.
6. **Jargon stacking** -- Problem: stringing together buzzwords that sound technical but say nothing. "Designed AI assistant-style architectures integrating retrieval, evaluation, and dynamic prompt routing pipelines" is meaningless. Better: Say what the system does and who uses it. "Built automated ticket routing with AI-assisted escalation."
7. **Filler endings** -- Problem: bullets that trail off into "enabling executive-level decision-making" or "driving actionable insights." If you cannot name the specific decision or insight, cut the ending.
8. **Modifier stacking** -- Problem: "comprehensive automated real-time scalable" before a noun. Pick the one that matters most. If none of them add information, drop them all.

### The Jargon Test

Before publishing any bullet or sentence, apply this test: **Could a non-technical hiring manager understand what you did and why it mattered?** If the sentence only makes sense to someone who already knows the work, rewrite it. Being technical means naming specific tools and decisions -- not stacking abstractions.

- Bad: "Designed AI assistant-style architectures integrating retrieval, evaluation, and dynamic prompt routing pipelines"
- Good: "Built automated ticket routing with AI-assisted escalation for 150 monthly helpdesk requests"
- Bad: "Developed comprehensive data analysis system integrating multiple data sources"
- Good: "Built RAG-based analysis system combining survey data with GPT-4o for design research"

---

## Content Examples

### Resume Bullet -- Good
"Designed hybrid pipeline architecture limiting LLM usage to text extraction with human-in-the-loop review and Python-based template execution, reducing token costs by 88% compared to monolithic LLM generation."

Why it works: Specific architecture decision, names the tradeoff, quantified result with comparison baseline.

### Resume Bullet -- Bad
"Worked on developing AI solutions for the federal government to help automate various processes."

Why it fails: "Worked on", "help", "various", no metric, no specific agency, no specific technology.

### GitHub README -- Good
"JENNY is a model-agnostic Intelligent Document Generator that reduces monolithic LLM token usage by 88%. Published: 'Efficiency by Design: Reducing AI Cost Through Smart Architecture.'"

Why it works: Says what it does, quantifies the result, links to the published work.

### Recruiter Email -- Good
"Hi Mayson, Can you send over JDs here? I am FTE and more responsive via email/text."

Why it works: Direct, states preference, no wasted words.

### Recruiter Email -- Bad
"Dear Hiring Manager, I hope this email finds you well. I wanted to reach out because I came across your posting and I believe my background in artificial intelligence and machine learning would make me a strong candidate."

Why it fails: Generic, slow to the point, "I believe", no specific hook.

---

## Open Questions for Team Discussion

### High Priority
1. **Quay Concepts vs. Personal Brand separation**
   - What was found: Resume uses personal name, consulting entity is Quay Concepts. Email signature references quay-cncpts.com. Invoices go through Quay Concepts to Arch Systems via RockGap.
   - Agent recommendation: One unified voice. Quay Concepts is the business entity for contracting. The brand is Jennifer Quay Minnich. Consulting proposals use slightly higher formality but same voice attributes.
   - Status: RECOMMENDATION APPLIED -- awaiting your confirmation.

2. **Target role title positioning**
   - What was found: You span ML Engineer, Data Scientist, Data Engineer, Software Engineer. With the SRM paper, "ML/AI Engineer" is clearly the strongest lead. The data governance work (TRM, CARES analytics) adds a unique dimension that pure ML titles don't capture.
   - Agent recommendation: Lead with "ML/AI Engineer" for job search. For roles that emphasize governance or data architecture, lead with the TRM work. "Data Scientist" as secondary for analytics-heavy roles (like the Credal evaluation). "Software Engineer" only appears when the role specifically requires it.
   - Suggested headline hierarchy: ML/AI Engineer > Data Scientist > (Data Engineer and Software Engineer are capabilities, not titles)
   - Status: RECOMMENDATION APPLIED -- awaiting your confirmation.

3. **LinkedIn profile update**
   - Status: BLOCKED -- cannot access LinkedIn directly. When ready, use `/brand-voice:enforce-voice` to generate on-brand LinkedIn headline, about, and experience sections from these guidelines.

### Medium Priority
4. **TRM disclosure boundaries**
   - RESOLVED: $9M+ aggregate savings figure is confirmed safe for public use. Context: potential savings identified in a 12-month period from mapping disparate data sources into a consolidated database. Do not break down by specific source (contract vs cloud vs idle). Do not name internal system names (CARES, Mobius) or per-vendor figures externally. Architecture pattern (crosswalk normalization, 15 sources, 42 tables) is safe to describe.

5. **SRM authorship positioning**
   - RESOLVED: Use "co-author" consistently. Do not specify author position or get into granular authorship details. The contribution speaks for itself: novel architecture, GPT-2 at half the parameters, ICML venue, Sandia/DOE funded.

---

## Project Portfolio -- Brand Messaging by Project

Each project below includes the real technical scope (from source code and READMEs), the brand-voice-aligned messaging for different contexts, and disclosure guidance.

### JENNY -- Intelligent Document Generator
- **Repo**: github.com/QUAY17/JENNY (public, MIT)
- **Disclosure level**: Full -- public repo with published research
- **What it actually does**: Model-agnostic SOP generator that converts draft documents into federally compliant formatted output. Two-phase architecture: LLM extracts structured content (title, purpose, scope, steps, images, hyperlinks), then deterministic Python pipeline handles template mutation with 82-84 validation gates. Processes both .docx and .pdf. Flask backend, React frontend.
- **Key metrics**: 88% token cost reduction vs monolithic LLM, 100% structural compliance across all tested SOPs (82-84 checks each), 15-25x cost reduction over LLM-heavy approaches
- **Resume bullet (high-level)**: "Developed model-agnostic document generator reducing LLM token costs by 88% through split-phase architecture separating text extraction from deterministic template execution."
- **Resume bullet (detailed)**: "Architected two-phase SOP generator: LLM handles content extraction, Python pipeline handles template mutation with 82-84 validation gates per document, achieving 100% structural compliance and 15-25x cost reduction over monolithic approaches."
- **LinkedIn post angle**: The architectural insight -- most LLM cost comes from using the model for work that deterministic code does better. Show the split-phase decision.
- **Interview talking point**: "I looked at where the LLM was actually needed vs where Python could do the job. Turns out only about 12% of the pipeline needs an LLM. That architectural decision saved 88% on token costs."

### AIEA CIS TRM Backend -- Technology Reference Model Database
- **Repo**: archsystemsinc-com (employer org, likely private)
- **Disclosure level**: HIGH-LEVEL ONLY -- can reference DHS/USCIS, describe the problem and architecture pattern, but do not name specific internal systems (CARES, Mobius) or data volumes by source
- **What it actually does**: Consolidated 15 disparate software inventory, licensing, approval, security, and cloud service data sources into a normalized PostgreSQL schema with 42 tables and 10 views. Includes crosswalk normalization layer, 5-criteria scoring matrix, LLM-generated product knowledge base, redundancy detection, compliance gap analysis, and cloud cost tracking. 13 data loaders with dry-run support. Docker-containerized.
- **Key metrics**: 15 source systems consolidated, 42 tables, 10 analytical views, 5-criteria scoring framework, dual-source validation (LLM-generated KB cross-referenced against SME reports)
- **Resume bullet (safe for public)**: "Consolidated 15 disparate software inventory and licensing data sources into a normalized PostgreSQL schema enabling compliance gap analysis, license optimization, and enterprise software reduction decisions for DHS."
- **Resume bullet (alternate angle)**: "Designed crosswalk normalization layer mapping messy multi-source data to canonical golden records, supporting a 5-criteria scoring framework for software consolidation prioritization across DHS."
- **LinkedIn post angle**: The data governance problem -- when an enterprise has 15 different systems tracking software and none of them agree. How crosswalk normalization creates a single source of truth.
- **Interview talking point**: "The core challenge was that 15 different systems all had different names for the same software. I built a crosswalk normalization layer that maps every messy source record to a canonical golden record, with confidence scoring and validation. That unlocked every downstream analysis -- compliance gaps, license waste, redundancy detection."

### Basic-Needs-Evaluation-Using-NLP -- Survey Analysis Platform
- **Repo**: github.com/QUAY17/Basic-Needs-Evaluation-Using-NLP (public)
- **Disclosure level**: Full -- public repo
- **What it actually does**: Six-stage NLP pipeline analyzing ~5k open-ended survey responses about food and housing insecurity across New Mexico higher education. DistilBERT for sentiment, BERTopic with SentenceTransformer embeddings for topic discovery, KeyBERT for keyword extraction with domain boosting. Dash web dashboard containerized with Docker, deployed to Kubernetes via Helm charts. Institution-level and faculty/staff/student segmentation.
- **Key metrics**: ~5k survey responses processed, 5 core survey questions analyzed, multi-model pipeline (DistilBERT + BERTopic + KeyBERT), Kubernetes deployment
- **Resume bullet**: "Built transformer-based NLP pipeline (DistilBERT, BERTopic, KeyBERT) analyzing 5k open-ended survey responses on food and housing insecurity, deployed as Kubernetes-hosted Dash dashboard for state higher education stakeholders."
- **LinkedIn post angle**: Applied NLP for policy impact -- using transformer models to surface themes from thousands of open-ended survey responses that would take humans months to read.
- **Interview talking point**: "This wasn't a sentiment analysis toy project. State legislators needed to understand what 5,000 students were saying about food and housing insecurity to make funding decisions. I built the pipeline that turned unstructured text into actionable themes."

### Using-Natural-Language-to-Generate-Complex-SQL -- NL-to-SQL Chatbot
- **Repo**: github.com/QUAY17/Using-Natural-Language-to-Generate-Complex-SQL (public, GPL-3.0)
- **Disclosure level**: Full -- public repo
- **What it actually does**: Three implementation approaches for converting natural language to SQL against New Mexico gross receipt tax data (2009-2023): (1) Fine-tuned Llama 2 on paired NL/SQL datasets, (2) LangChain with local LlamaCpp and custom prompt templates, (3) LlamaIndex NLSQLTableQueryEngine with token cost tracking. Targets 85%+ accuracy for correct query generation. Deployed on GCP Vertex AI with MongoDB document store.
- **Key metrics**: 95% accuracy rate (from resume), 3 implementation approaches benchmarked, 14 years of tax data (2009-2023), GCP/Vertex AI deployment
- **Resume bullet**: "Fine-tuned Llama 2 for natural language to SQL generation against 14 years of state tax data, achieving 95% query accuracy. Benchmarked three approaches (fine-tuned LLM, LangChain, LlamaIndex) and deployed via GCP Vertex AI."
- **LinkedIn post angle**: The comparison between fine-tuning, LangChain, and LlamaIndex for NL-to-SQL -- what worked, what didn't, and why the choice depends on query complexity.
- **Interview talking point**: "I didn't just pick a framework and ship it. I built three different approaches -- fine-tuned Llama 2, LangChain, and LlamaIndex -- benchmarked them all on the same tax dataset, and deployed the winner on Vertex AI. That kind of rigorous comparison is how I make architecture decisions."

### Stock-Bought -- Algorithmic Trading Toolkit
- **Repo**: github.com/QUAY17/Stock-Bought (public, MIT)
- **Disclosure level**: Full -- public repo
- **What it actually does**: Python trading toolkit built as a Robinhood API extension. Backtesting engine with visual output, federal economic data integration, financial analysis functions (technical + fundamental), live algorithm execution, PyQt GUI with 2FA. 97 commits, 28 files.
- **Key metrics**: 97 commits, backtesting + live execution, Robinhood API integration, federal data integration
- **Resume bullet**: "Engineered algorithmic trading toolkit integrating Robinhood API, federal economic data feeds, and backtesting engine, enabling automated strategy validation and live execution."
- **Note**: This is earlier work (pre-ML career pivot). Position as evidence of full-stack Python capability and FinTech domain exposure, not as a headline project.

### Latent-App -- Music Player
- **Repo**: github.com/QUAY17/Latent-App (public, MIT)
- **Disclosure level**: Full -- public repo
- **What it actually does**: Full-screen cinematic music player. React/Vite frontend, Three.js with custom GLSL shaders for WebGL fluid effects, YouTube IFrame API for streaming, Framer Motion animations. DJ Mode (manual) and Playlist Mode (auto-advance). Vercel deployment.
- **Note**: This is a creative/side project. Position as evidence of frontend capability and design sensibility, not as a career-defining project. Good for showing range in interviews ("I also build things for fun").

### Stream Recursion Model (SRM) -- ICML 2026
- **Repo**: Likely ICASA org or private
- **Disclosure level**: Full -- paper submitted to ICML, anonymized for review but content is shareable
- **What it actually does**: Novel LLM architecture that modifies the Hierarchical Reasoning Model (HRM) to expose internal computational structure while remaining scalable. SRM organizes computation into multiple interacting latent streams updated through recursive refinement. Key innovation: a learnable "communication layer" (stream-wise attention) that enables streams to selectively translate information between each other, solving HRM's stream scaling limitation. Achieves GPT-2 comparable performance on a per-parameter basis with half the parameters (68M vs 124M for SRM-base). Trained on a single 4xL40s GPU cluster over 2 months (~1000 GPU hours). Analysis reveals hub-like stream topology, specialized stream behavior, and structured routing patterns -- opening avenues for mechanistic interpretability at scale.
- **Key metrics**: SRM-base matches GPT-2 at 68M params (vs 124M) with 7x compute time; SRM-med outperforms GPT-2 at similar param count (134M) with 6x compute; SRM-large (454M params) demonstrates continued scaling; trained on ~5B tokens from OpenWebText
- **Technical depth**: Stream-wise attention (learned Q/K/V per stream), RMSNorm update function, post-root architecture following GPT-NeoX, ABCABC step-group ordering, limited backpropagation through last 4 layers, KL divergence analysis for representational drift, stream ablation studies showing top 9 streams account for 50% of causal impact
- **Resume bullet (lead with contribution)**: "Co-authored novel LLM architecture (SRM) achieving GPT-2 performance at half the parameters by introducing learnable inter-stream communication, enabling scalable mechanistic interpretability. Submitted to ICML 2026, funded by Sandia National Labs/DOE."
- **Resume bullet (interpretability angle)**: "Developed Stream Recursion Model introducing stream-wise attention for inter-stream communication in recurrent LLM architectures, with analysis revealing hub-like routing topology and specialized stream behavior. ICML 2026 submission."
- **LinkedIn post angle**: The core insight -- vanilla transformers have massive parameter redundancy. By organizing computation into streams that learn how to communicate, you can match GPT-2 with half the parameters. That's not just efficiency; it's interpretability.
- **Interview talking point**: "The problem with HRM was that streams couldn't scale -- they communicated by just adding their states together, which doesn't translate information between streams. We introduced stream-wise attention, where each stream learns its own Q/K/V weights for a learned communication function. SRM-base matches GPT-2 at 68M parameters versus 124M. More importantly, the architecture is inherently interpretable -- we can analyze routing patterns, identify hub streams, and measure per-stream causal contribution through ablation. That's the future of trustworthy AI."

### CARES TRM Data Analysis Reports -- DHS/USCIS Governance Analytics
- **Disclosure level**: HIGH-LEVEL ONLY -- can reference DHS/USCIS and describe the analytical approach, but do not name specific cost figures, system names, or contract details
- **What it actually does**: Comprehensive enterprise software and cloud governance analytics produced entirely from the TRM database. Phase 2 analysis covers spend analysis ($55M+ cloud spend across providers), cost savings identification ($9M+ combined savings opportunity), compliance risk (prohibited/divest software still deployed), FY26 contract analysis (99 contracts, expiration windows), cloud cost attribution per system, and system dependency mapping. OCR-specific analysis demonstrates TRM's value as a governance tool by surfacing fragmented sourcing across 144 product names mapping to only 2 DHS TRM records, identifying $696K in potentially unnecessary contracts by cross-referencing AI use case registry (retired status) against active contracts, and revealing ungoverned cloud spend.
- **Key metrics**: 15 source systems consolidated, $9M+ savings identified, 144 OCR product names normalized, cross-referencing AI use case registry against contracts for savings
- **Resume bullet (governance angle)**: "Produced enterprise software governance analytics from consolidated TRM database, identifying $9M+ in cost savings across contract optimization and cloud idle resources for DHS."
- **Resume bullet (data engineering angle)**: "Designed crosswalk normalization chain mapping 144 fragmented product names across 6 source systems to canonical DHS TRM records, enabling compliance gap, spend, and redundancy analysis previously impossible."
- **Interview talking point**: "The OCR analysis is a good example of why the TRM matters. We found 144 different names for OCR products across source systems, mapping to just 2 records in the DHS catalog. Three deployed AI use cases were each acquired independently using different platforms with no shared infrastructure. That kind of fragmentation is invisible without a normalized data model."

### FEMA Ops Brief Generator -- Automated Operational Reporting
- **Disclosure level**: HIGH-LEVEL ONLY -- can reference FEMA and describe the automation approach
- **What it actually does**: Python-based automated report generator that creates weekly operational briefs by combining data from three sources: PDF class schedules, Board workbook (XLSM), and In-Processing schedules. Extracts and joins data across sources to produce formatted operational briefs.
- **Resume bullet**: "Automated weekly FEMA operational brief generation by building Python pipeline combining PDF, Excel, and scheduling data from three source systems into formatted reports."
- **Note**: This is a data engineering/automation project, not ML. Position as evidence of practical pipeline building and stakeholder-facing deliverable automation.

### Credal AI Usage Analytics -- Enterprise AI Platform Evaluation
- **Disclosure level**: HIGH-LEVEL ONLY -- can reference ACF/HHS and the analytical approach
- **What it actually does**: 6-week pilot evaluation of Credal AI platform across 100 users for HHS-ACF. Volume metrics (DAU/WAU, session counts, API call distribution, peak usage, week-over-week growth). Context analysis (use case mapping, copilot adoption, prompt categorization, model usage patterns including 4o/o1-mini/4o-mini/o3). User behavior clustering (k-means, hierarchical). Automated data pipeline from Credal API to Tableau with daily refreshes. Memory-optimized star schema via Hyper API. Python scripts for log collection, validation, cleaning, and statistical analysis. All code delivered via private GitHub repository.
- **Key metrics**: 100 pilot users, millions of logs processed, daily automated refreshes, star schema optimization via Hyper API, multiple model comparison (GPT-4o, o1-mini, 4o-mini)
- **Resume bullet (analytics angle)**: "Evaluated enterprise AI platform viability across 100 pilot users for HHS-ACF, building automated pipeline processing millions of logs into Tableau dashboard with user behavior clustering and model utilization analysis to inform purchase decision."
- **Resume bullet (data engineering angle)**: "Engineered memory-optimized star schema via Tableau Hyper API, automating daily ingestion of millions of Credal AI logs with Python-based validation, cleaning, and statistical analysis pipeline."
- **Interview talking point**: "The Chief AI Officer needed to decide whether to buy Credal AI enterprise-wide. I built the analytics that answered that question -- 100 users, millions of logs, automated daily refreshes, user behavior clustering to identify adoption patterns, and model comparison across GPT-4o and the o-series models. The dashboard went from raw API logs to executive-ready insights."

---

## Project Disclosure Rules

When generating content that references projects, always check the disclosure level:

| Disclosure Level | What You Can Say | What You Cannot Say |
|-----------------|-----------------|---------------------|
| **Full** | Architecture, tools, metrics, agency names, data volumes, everything in the public README | N/A -- it's public |
| **High-level only** | Problem domain, architecture patterns, general metrics, agency names (DHS, USCIS) | Specific internal system names, exact data volumes by source, internal tool names |
| **Pending** | What's on the resume already | Nothing beyond the resume until the source material is shared |

---

## Data Gaps & Recommendations

- [x] SRM paper -- DONE. Full paper analyzed. Resume bullets rewritten to lead with novel contribution (GPT-2 at half params via stream-wise attention).
- [x] Credal AI project scope -- DONE. Specific metrics (100 users, k-means clustering, Hyper API, multi-model comparison) incorporated.
- [x] TRM governance analytics -- DONE. CARES Data Analysis II and OCR Tool Analysis incorporated. $9M+ savings, crosswalk normalization, governance insights.
- [x] FEMA Ops Brief -- DONE. Added as data engineering/automation project.
- [ ] ICASA/Sandia org GitHub repos: Any public repos from DOE-funded work would add to portfolio
- [ ] LinkedIn profile content: Need current headline/about to rewrite with brand voice
- [ ] quay-cncpts.com website content: Should align with these guidelines
- [ ] AI Constitution Testing artifacts: The testing framework and red team datasets are referenced but not seen -- shareable deliverables would strengthen the governance pillar
- [ ] Zendesk automation details: Know the high-level (macros, triggers, webhooks, 150 tickets/7 categories) but specific architecture docs would add depth
- [ ] SRM author position: Needed to calibrate how aggressively to lead with the publication
