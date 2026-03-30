#!/usr/bin/env python3
"""
md_to_latex_resume.py
Converts resume-source.md into jennifer.tex (moderncv format).

Usage:
    python md_to_latex_resume.py                          # reads resume-source.md, writes jennifer.tex
    python md_to_latex_resume.py --input my.md --output out.tex
    python md_to_latex_resume.py --dry-run                # prints LaTeX to stdout without writing

The Markdown file is the single source of truth.
Edit the Markdown, run this script, compile the LaTeX.
"""

import argparse
import re
import sys
from pathlib import Path


def escape_latex(text: str) -> str:
    """Escape special LaTeX characters in text."""
    replacements = [
        ("&", r"\&"),
        ("%", r"\%"),
        ("$", r"\$"),
        ("#", r"\#"),
        ("_", r"\_"),
        ("{", r"\{"),
        ("}", r"\}"),
        ("~", r"\textasciitilde{}"),
        ("^", r"\textasciicircum{}"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def parse_markdown(md_path: str) -> dict:
    """Parse the resume Markdown into structured sections."""
    with open(md_path, "r") as f:
        lines = f.readlines()

    resume = {
        "name_first": "",
        "name_last": "",
        "location": "",
        "phone": "",
        "email": "",
        "linkedin": "",
        "summary": "",
        "credentials": "",
        "education_summary": "",
        "technical": [],
        "publication": "",
        "experience": [],
        "notable_projects": {},
        "references": [],
        "education_detail": [],
    }

    current_section = None
    current_subsection = None
    current_entry = None
    current_project = None
    i = 0

    while i < len(lines):
        line = lines[i].rstrip()

        # Top-level name
        if line.startswith("# ") and not line.startswith("## "):
            parts = line[2:].strip().split()
            if len(parts) >= 2:
                resume["name_first"] = " ".join(parts[:-1])
                resume["name_last"] = parts[-1]
            i += 1
            continue

        # Contact info
        if line.startswith("- **Location**:"):
            resume["location"] = line.split(":", 1)[1].strip()
        elif line.startswith("- **Phone**:"):
            resume["phone"] = line.split(":", 1)[1].strip()
        elif line.startswith("- **Email**:"):
            resume["email"] = line.split(":", 1)[1].strip()
        elif line.startswith("- **LinkedIn**:"):
            resume["linkedin"] = line.split(":", 1)[1].strip()

        # Sections
        if line.startswith("## "):
            section_name = line[3:].strip()
            current_section = section_name
            current_subsection = None
            current_entry = None
            current_project = None
            i += 1
            continue

        if line.startswith("### ") and current_section == "Notable Projects":
            current_subsection = line[4:].strip()
            if current_subsection not in resume["notable_projects"]:
                resume["notable_projects"][current_subsection] = []
            i += 1
            continue

        if line.startswith("### ") and current_section == "Experience":
            # Parse experience entry: ### Title | Company | Dates
            header = line[4:].strip()
            parts = [p.strip() for p in header.split("|")]
            entry = {
                "title": parts[0] if len(parts) > 0 else "",
                "company": parts[1] if len(parts) > 1 else "",
                "dates": parts[2] if len(parts) > 2 else "",
                "location": "",
                "detail": "",
                "clearance": "",
                "bullets": [],
            }
            # Next line should have location info
            if i + 1 < len(lines):
                next_line = lines[i + 1].rstrip()
                if next_line and not next_line.startswith("#") and not next_line.startswith("-"):
                    entry["location"] = next_line.strip()
                    i += 1
                    # Check for another detail line
                    if i + 1 < len(lines):
                        next_line2 = lines[i + 1].rstrip()
                        if next_line2 and not next_line2.startswith("#") and not next_line2.startswith("-"):
                            entry["detail"] = next_line2.strip()
                            i += 1
            current_entry = entry
            resume["experience"].append(entry)
            i += 1
            continue

        # Skip separator lines
        if line.strip() == "---":
            i += 1
            continue

        # Summary
        if current_section == "Summary" and line.strip() and not line.startswith("#"):
            resume["summary"] = line.strip()

        # Credentials
        if current_section == "Credentials" and line.strip():
            resume["credentials"] = line.strip()

        # Education summary
        if current_section == "Education" and line.strip() and not line.startswith("#"):
            if not resume["education_summary"]:
                resume["education_summary"] = line.strip()

        # Technical proficiency
        if current_section == "Technical Proficiency" and line.startswith("- **"):
            match = re.match(r"- \*\*(.+?)\*\*:\s*(.+)", line)
            if match:
                resume["technical"].append((match.group(1), match.group(2)))

        # Publication
        if current_section == "Publication" and line.strip() and not line.startswith("#") and line.strip() != "---":
            resume["publication"] = line.strip()

        # Experience bullets
        if current_section == "Experience" and current_entry and line.startswith("- "):
            current_entry["bullets"].append(line[2:].strip())

        # Notable projects
        if current_section == "Notable Projects":
            if line.startswith("**") and "|" in line:
                # Project header: **Year | Title**
                match = re.match(r"\*\*(.+?)\s*\|\s*(.+?)\*\*", line)
                if match:
                    current_project = {
                        "year": match.group(1).strip(),
                        "title": match.group(2).strip(),
                        "bullets": [],
                    }
                    if current_subsection and current_subsection in resume["notable_projects"]:
                        resume["notable_projects"][current_subsection].append(current_project)
            elif line.startswith("- ") and current_project:
                current_project["bullets"].append(line[2:].strip())

        # References
        if current_section == "References" and line.startswith("**"):
            resume["references"].append(line.strip())

        # Education detail
        if current_section == "Education (Detail)" and line.strip() and not line.startswith("#"):
            if line.startswith("**"):
                resume["education_detail"].append({"header": line.strip(), "bullets": []})
            elif line.startswith("- ") and resume["education_detail"]:
                resume["education_detail"][-1]["bullets"].append(line[2:].strip())

        i += 1

    return resume


def generate_latex(resume: dict) -> str:
    """Generate moderncv LaTeX from parsed resume data."""
    esc = escape_latex

    tex = []
    tex.append(r"\documentclass[10pt,a4paper,sans]{moderncv}")
    tex.append(r"\moderncvstyle{classic}")
    tex.append(r"\moderncvcolor{orange}")
    tex.append(r"\usepackage[scale=.93]{geometry}")
    tex.append(r"\usepackage{lastpage}")
    tex.append(r"\usepackage{fancyhdr}")
    tex.append(r"\usepackage{amssymb}")
    tex.append(r"\usepackage{verbatim}")
    tex.append(r"\pagestyle{fancy}")
    tex.append(r"\cfoot{\thepage\ of \pageref{LastPage}}")
    tex.append("")

    # Personal data
    tex.append(rf"\name{{{esc(resume['name_first'])}}}{{{esc(resume['name_last'])}}}")
    tex.append(rf"\address{{{esc(resume['location'])}}}")
    tex.append(rf"\phone{{{resume['phone']}}}")
    tex.append(rf"\social[linkedin]{{{resume['linkedin']}}}")
    tex.append(rf"\email{{{resume['email']}}}")
    tex.append(r"\renewcommand*{\bibliographyitemlabel}{[\arabic{enumiv}]}")
    tex.append("")
    tex.append(r"\begin{document}")
    tex.append(r"\makecvtitle")
    tex.append("")

    # Summary
    if resume["summary"]:
        # Replace | with centered dot, escape text but not the LaTeX commands
        parts = [esc(p.strip()) for p in resume["summary"].split("|")]
        summary_line = r" $\cdot$ ".join(parts)
        tex.append(r"\noindent")
        tex.append(rf"{summary_line}")
        tex.append(r"\vspace{6pt}")
        tex.append("")

    # Credentials
    if resume["credentials"]:
        parts = [esc(p.strip()) for p in resume["credentials"].split("|")]
        cred_line = r" $\cdot$ ".join(parts)
        tex.append(r"\noindent")
        tex.append(rf"\textbf{{Clearance \& Credentials:}} {cred_line}")
        tex.append("")

    # Education summary
    if resume["education_summary"]:
        tex.append(r"\noindent")
        tex.append(rf"\textbf{{Education:}} {esc(resume['education_summary'])}")
        tex.append(r"\vspace{4pt}")
        tex.append("")

    # Technical proficiency
    if resume["technical"]:
        tex.append(r"\section{Technical Proficiency}")
        tex.append(r"\noindent")
        for idx, (category, items) in enumerate(resume["technical"]):
            # Split on commas but preserve commas inside parentheses
            parts = re.split(r",\s*(?![^()]*\))", items)
            items_formatted = r" $\cdot$ ".join(esc(p.strip()) for p in parts)
            if idx > 0:
                tex.append(r"\newline \noindent")
            tex.append(rf"\textbf{{{esc(category)}:}} {items_formatted}")
        tex.append("")

    # Publication
    if resume["publication"]:
        tex.append(r"\section{Publication}")
        pub = resume["publication"]
        # Parse: **Year** | Author | "Title" | Venue
        match = re.match(r"\*\*(\d{4})\*\*\s*\|\s*(.+?)\s*\|\s*\"(.+?)\"\s*\|\s*(.+)", pub)
        if match:
            year, author, title, venue = match.groups()
            tex.append(
                rf'\cventry{{{year}}}{{{esc(author)}}}{{"{esc(title)}"}}'
                rf"{{\newline {esc(venue)}}}{{}}{{}}{{}}"
            )
        else:
            tex.append(rf"\cvitem{{}}{{{esc(pub)}}}")
        tex.append("")

    # Experience
    if resume["experience"]:
        tex.append(r"\section{Experience}")
        for entry in resume["experience"]:
            # Parse dates for cventry
            title = esc(entry["title"])
            company = esc(entry["company"])
            dates = esc(entry["dates"])
            location = esc(entry["location"]) if entry["location"] else ""
            detail = esc(entry["detail"]) if entry["detail"] else ""

            # Build location string
            loc_parts = []
            if location:
                loc_parts.append(location)
            loc_str = r"\newline ".join(loc_parts)
            if detail:
                loc_str = loc_str + r"\newline " + detail if loc_str else detail

            tex.append(r"\vspace{4pt}")
            tex.append(
                rf"\cventry{{{dates}}}{{{title}}}{{{company}}}{{{loc_str}}}{{}}{{"
            )

            if entry["bullets"]:
                tex.append(r"\begin{itemize}")
                for bullet in entry["bullets"]:
                    tex.append(rf"    \item {esc(bullet)}")
                tex.append(r"\end{itemize}")

            tex.append("}")
            tex.append("")

    # Notable Projects
    if resume["notable_projects"]:
        tex.append(r"\section{Notable Projects}")
        tex.append(r"\vspace{2pt}")
        for subsection, projects in resume["notable_projects"].items():
            tex.append(rf"\subsection{{{esc(subsection)}}}")
            for project in projects:
                tex.append(
                    rf"\cventry{{{esc(project['year'])}}}{{{esc(project['title'])}}}{{}}{{}}{{}}{{"
                )
                if project["bullets"]:
                    tex.append(r"    \begin{itemize}")
                    for bullet in project["bullets"]:
                        tex.append(rf"        \item {esc(bullet)}")
                    tex.append(r"    \end{itemize}")
                tex.append("}")
                tex.append(r"\vspace{6pt}")
            tex.append("")

    # References
    if resume["references"]:
        tex.append(r"\section{References}")
        for ref in resume["references"]:
            # Parse: **Name** | Title | Org | email | phone
            ref_clean = ref.replace("**", "")
            parts = [p.strip() for p in ref_clean.split("|")]
            if len(parts) >= 5:
                name = parts[0]
                title = parts[1]
                org = parts[2]
                email = parts[3]
                phone = parts[4]
                tex.append(
                    rf"\cventry{{{esc(name)}}}{{{esc(title)}}}"
                    rf"{{\newline {esc(org)}}}{{}}{{}}{{"
                )
                tex.append(r"    \begin{itemize}")
                tex.append(rf"        \item {esc(email)}")
                tex.append(rf"        \item {esc(phone)}")
                tex.append(r"    \end{itemize}")
                tex.append("}")
            tex.append("")

    # Education detail
    if resume["education_detail"]:
        tex.append(r"\section{Education}")
        for edu in resume["education_detail"]:
            header = edu["header"].replace("**", "")
            # Parse: Year | Degree | School
            parts = [p.strip() for p in header.split("|")]
            if len(parts) >= 3:
                year = parts[0]
                degree = parts[1]
                school = parts[2]
                tex.append(
                    rf"\cventry{{{esc(year)}}}{{{esc(degree)}}}"
                    rf"{{\newline {esc(school)}}}{{}}{{}}{{"
                )
                if edu["bullets"]:
                    tex.append(r"    \begin{itemize}")
                    for bullet in edu["bullets"]:
                        tex.append(rf"        \item {esc(bullet)}")
                    tex.append(r"    \end{itemize}")
                tex.append("}")
        tex.append("")

    tex.append(r"\end{document}")
    return "\n".join(tex)


def main():
    parser = argparse.ArgumentParser(
        description="Convert resume Markdown to moderncv LaTeX"
    )
    parser.add_argument(
        "--input", default="resume-source.md", help="Input Markdown file"
    )
    parser.add_argument(
        "--output", default="jennifer.tex", help="Output LaTeX file"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print LaTeX to stdout without writing",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: {input_path} not found", file=sys.stderr)
        sys.exit(1)

    resume = parse_markdown(str(input_path))
    latex = generate_latex(resume)

    if args.dry_run:
        print(latex)
    else:
        output_path = Path(args.output)
        output_path.write_text(latex)
        print(f"Generated {output_path} from {input_path}")
        print(f"  Sections: {len(resume['experience'])} experience entries, "
              f"{sum(len(v) for v in resume['notable_projects'].values())} projects")


if __name__ == "__main__":
    main()
