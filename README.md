# Brand

Personal brand hub — resume, LinkedIn content, cover letters, website copy, and brand messaging.

## Structure

```
.claude/                  Brand voice guidelines (auto-loaded by Claude Code)
CLAUDE.md                 Project instructions for Claude Code
resume/                   Resume source (markdown) + LaTeX converter
linkedin/                 LinkedIn profile rewrites and post drafts
cover-letters/            Tailored cover letters
website/                  Website copy and content
messaging/                Brand positioning, talking points, elevator pitches
```

## Brand Voice

All content follows the guidelines in `.claude/brand-voice-guidelines.md`. Claude Code enforces these automatically.

## Resume Workflow

```bash
cd resume
# edit resume-source.md, then:
python md_to_latex_resume.py --input resume-source.md --output jennifer.tex
pdflatex jennifer.tex
```
