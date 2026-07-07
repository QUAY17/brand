# Project Instructions

## On session start (read this first)

Before any content work, **read the `.claude/` directory and apply what's there** -- it is the source of truth for this repo's voice and disclosure rules:
- `.claude/brand-voice-guidelines.md` -- full voice, Terminology Guide, approved metrics, and the Project Disclosure Rules table
- `.claude/agents/` -- the `brand-voice-editor` (drafts/rewrites copy on-register) and `brand-voice-reviewer` (read-only pre-ship audit) subagents
- `.claude/output-styles/quay-brand-voice.md` -- the writing register for this repo

Do not generate or edit resume / LinkedIn / cover-letter / README / web copy without loading these first.

## Brand Voice

This project follows the brand voice guidelines in `.claude/brand-voice-guidelines.md`. All content generation -- README files, documentation, commit messages, PR descriptions, comments, and any user-facing text -- must follow those guidelines.

Key rules:
- Lead with outcomes and metrics, not process descriptions
- Use strong active verbs (built, deployed, reformed, architected) -- never "worked on", "helped with", "various"
- Name specific tools, frameworks, and architectural decisions -- no vague "AI solutions"
- No emojis in code or text
- Do not hallucinate metrics or fabricate claims. If a number is not in the guidelines or source material, do not invent one.

### Anti-jargon (this is the most common failure mode -- enforce it)

- **No keyword stacking.** Every tool or framework you name must connect to a decision or an outcome. A bullet that lists "Pinecone and Cosmos DB vector search with chunking, metadata filtering, reranking, and grounding" is a keyword dump -- rewrite it to say what it achieved.
- **Dense tool lists belong in the resume's Technical Proficiency section only**, never stacked inside prose bullets or the summary.
- **Apply the Jargon Test before writing any bullet:** could a non-technical hiring manager understand what was done and why it mattered? If it only parses for someone who already knows the work, rewrite it in plain language.
- **Understated register.** Secure confidence, not self-promotion -- let the work speak. No marketing adjectives ("innovative", "cutting-edge", "robust"/"scalable" without evidence), no filler endings ("enabling executive-level decision-making").
- When in doubt, prefer the register in the content master `resume/JENNIFER_QUAY_MINNICH_fin.md` -- that is the calibrated target.

## Project Disclosure

Some projects have restricted disclosure levels. Before writing about any project publicly (README, LinkedIn, blog), check the **Project Disclosure Rules** table in the brand voice guidelines. Key restrictions:
- TRM Backend: HIGH-LEVEL ONLY. Can reference DHS/USCIS and architecture patterns. Cannot name internal systems (CARES, Mobius) or per-vendor cost breakdowns. $9M+ aggregate savings is approved.
- SRM Paper: Use "co-authored" for authorship. Do not specify author position.

## Resume Workflow

The resume + cover letter are the **"Brass Sysbar" design** (Syne / Manrope / JetBrains Mono; brass + pilot-cyan). The design lives in the bound Claude Design project (reached via the `DesignSync` MCP, which only authorizes in Claude Code Web -- not a local VSCode session) and is exported into `resume/` (gitignored, local only):

- `resume/Resume - Brass Sysbar.dc.html` and `resume/Cover Letter - Brass Sysbar.dc.html` -- Design-Component sources; they need `resume/support.js` to render.
- Self-contained bundled `.html` exports (fonts embedded) for sending / printing.
- **`resume/JENNIFER_QUAY_MINNICH_fin.md`** -- the editable **content master** and source of record for the 3-page general resume. Edit content here.

Export to PDF with the toolbar's **Save / Print PDF** button -- keep the print dialog Margins at Default so the `@page` rules apply. The design is settled; **content is the only thing iterating.** Apply the brand voice guidelines to any new bullets and run the `brand-voice-reviewer` / `copy-editor` subagents before anything ships. There is no LaTeX/Markdown converter pipeline (the old `resume-source.md` plus the `md_to_latex_resume.py` / `md_to_docx_resume.py` converters were retired).

The earlier **"Hairline Pilot"** design (Inter / IBM Plex Mono, pilot-cyan + gold, 7 sections) is **retired** -- archived at `resume/_hairline-pilot-retired/`. Do not build off it.

## Subagents & Output Style

- **Output style `quay-brand-voice`** (`.claude/output-styles/quay-brand-voice.md`) -- sets the writing register for this repo. Activate with `/output-style quay-brand-voice` when doing content work.
- **`brand-voice-editor`** (`.claude/agents/`) -- rewrites draft copy to brand voice and strips jargon. Use it for any resume/LinkedIn/cover-letter/README copy.
- **`brand-voice-reviewer`** (`.claude/agents/`) -- read-only audit of copy against the guidelines and disclosure rules; flags jargon stacking, missing metrics, and disclosure leaks. Run it before anything ships.
- **`copy-editor`** (`.claude/agents/`) -- line-level copy editing AFTER brand voice: tense consistency, plain-English grammar, parallelism, and clarity. Does not change facts, metrics, register, or disclosure. Run it as the final mechanical pass before a resume/letter ships.

## Code Style

- Python: follow PEP 8, type hints preferred
- SQL: uppercase keywords, lowercase identifiers
- Documentation: concise, outcome-first, no filler
