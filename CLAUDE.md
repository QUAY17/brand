# Project Instructions

## Brand Voice

This project follows the brand voice guidelines in `.claude/brand-voice-guidelines.md`. All content generation -- README files, documentation, commit messages, PR descriptions, comments, and any user-facing text -- must follow those guidelines.

Key rules:
- Lead with outcomes and metrics, not process descriptions
- Use strong active verbs (built, deployed, reformed, architected) -- never "worked on", "helped with", "various"
- Name specific tools, frameworks, and architectural decisions -- no vague "AI solutions"
- No emojis in code or text
- Do not hallucinate metrics or fabricate claims. If a number is not in the guidelines or source material, do not invent one.

## Project Disclosure

Some projects have restricted disclosure levels. Before writing about any project publicly (README, LinkedIn, blog), check the **Project Disclosure Rules** table in the brand voice guidelines. Key restrictions:
- TRM Backend: HIGH-LEVEL ONLY. Can reference DHS/USCIS and architecture patterns. Cannot name internal systems (CARES, Mobius) or per-vendor cost breakdowns. $9M+ aggregate savings is approved.
- SRM Paper: Use "co-authored" for authorship. Do not specify author position.

## Resume Workflow

The resume source of truth is `resume/resume-source.md`. To generate LaTeX:

```
cd resume
python md_to_latex_resume.py --input resume-source.md --output jennifer.tex
```

When updating the resume:
1. Edit `resume-source.md` only
2. Run the converter to regenerate LaTeX
3. Apply brand voice guidelines to any new bullets

## Code Style

- Python: follow PEP 8, type hints preferred
- SQL: uppercase keywords, lowercase identifiers
- Documentation: concise, outcome-first, no filler
