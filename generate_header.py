import os

def generate_header_svg(title, filename):
    text_width = len(title) * 10 + 15
    
    svg_content = f"""<svg width="620" height="40" viewBox="0 0 620 40" xmlns="http://www.w3.org/2000/svg">
    <style>
        .header-text {{
            font-family: 'JetBrains Mono', 'Courier New', monospace;
            font-size: 16px;
            fill: #7d8590;
            font-weight: bold;
        }}
        .header-line {{
            stroke: #30363d;
            stroke-width: 1;
        }}
    </style>
    
    <text x="0" y="25" class="header-text">{title}</text>
    <line x1="{text_width}" y1="21" x2="620" y2="21" class="header-line" />
</svg>"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"✅ {filename} erfolgreich generiert!")

def main():
    headers = [
        ("about", "hd-about.svg"),
        ("stack", "hd-stack.svg"),
        ("projects", "hd-projects.svg"),
        ("stats", "hd-stats.svg")
    ]

    for title, filename in headers:
        generate_header_svg(title, filename)

if __name__ == "__main__":
    main()