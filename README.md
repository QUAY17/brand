# Brand

Personal brand hub for Jennifer Quay Minnich. Single source of truth for resume, cover letters, LinkedIn content, website copy, and brand messaging.

## Structure

```
resume/           Resume source (Markdown) + LaTeX and DOCX generators
cover-letters/    Tailored cover letters
linkedin/         LinkedIn profile and post drafts
website/          Website copy for quay-cncpts.com
messaging/        Brand positioning and talking points
.claude/          Brand voice guidelines
```

## Resume Workflow

The resume source of truth is `resume/resume-source.md`. Generate both output formats:

```bash
cd resume
python md_to_latex_resume.py   # -> jennifer.tex
python md_to_docx_resume.py    # -> jennifer.docx
pdflatex jennifer.tex          # -> jennifer.pdf
```

## Brand Voice

All content follows `.claude/brand-voice-guidelines.md`. Key rules: lead with outcomes, use strong active verbs, name specific tools and frameworks, no filler.
