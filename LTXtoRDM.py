import re

def latex_to_markdown(latex_content):
    # En-tête README avec titre
    title_match = re.search(r'\\bfseries\s+(.+?)\\par', latex_content)
    title = f"# {title_match.group(1)}" if title_match else "# Projet"

    # Auteurs
    authors = re.findall(r'\\large\s+Réalisé par\s*:\\\\\s*(.*?)\\par', latex_content, re.DOTALL)
    authors_md = ""
    if authors:
        names = authors[0].strip().split('\\\\')
        authors_md += "**Réalisé par :**\n" + "\n".join(f"- {n.strip()}" for n in names)

    # Encadrant
    encadrant = re.findall(r'Encadré par\s*:\s*Professeur (.+?)\\par', latex_content)
    encadrant_md = f"\n\n**Encadré par :** Professeur {encadrant[0]}" if encadrant else ""

    # Supprimer les commandes inutiles
    content = re.sub(r'\\(documentclass|usepackage|geometry|setlength|titlepage|vspace\*?|begin|end|center|tableofcontents|newpage|document)\{[^}]*\}', '', latex_content)
    content = re.sub(r'\\(vspace\*?\{.*?\}|par|bfseries|large|textbf\{(.*?)\}|tiny|textit\{(.*?)\})', lambda m: f"**{m.group(2) or m.group(3) or ''}**", content)
    content = re.sub(r'\\section\{(.+?)\}', r'\n## \1\n', content)
    content = re.sub(r'\\subsection\{(.+?)\}', r'\n### \1\n', content)
    content = re.sub(r'\\subsubsection\{(.+?)\}', r'\n#### \1\n', content)
    content = re.sub(r'\\paragraph\{(.+?)\}', r'\n**\1** ', content)

    # Listes
    content = re.sub(r'\\begin\{itemize\}.*?\\end\{itemize\}', lambda m: re.sub(r'\\item\s*(.*?)\n?', r'- \1\n', m.group(0), flags=re.DOTALL), content, flags=re.DOTALL)
    content = content.replace(r'\item', '-')

    # Tableaux simples
    content = re.sub(r'\\begin\{tabular\}\{[^\}]+\}', '', content)
    content = re.sub(r'\\end\{tabular\}', '', content)
    content = re.sub(r'\\hline', '', content)
    content = re.sub(r'\s*\|\s*', ' | ', content)
    content = re.sub(r'([^\|]+)\n', r'\1  ', content)
    content = re.sub(r'(.*?)\n(.*?)\n(.*?)\n', lambda m: f"{m.group(1)}\n{re.sub('[^|]+', '---', m.group(1))}\n{m.group(2)}\n", content)

    # Nettoyage final
    content = re.sub(r'\\[a-z]+\s*', '', content)  # toutes commandes restantes
    content = re.sub(r'\n{2,}', '\n\n', content).strip()

    # Assemble le README
    readme = f"{title}\n\n{authors_md}{encadrant_md}\n\n{content}"
    return readme


# Utilisation
with open("pfm_raid.tex", "r", encoding="utf-8") as f:
    latex_code = f.read()

markdown_readme = latex_to_markdown(latex_code)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(markdown_readme)

print("README.md généré avec succès.")
