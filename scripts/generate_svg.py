import datetime
import os

with open("ascii_face.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

svg_elements = ""
y_position = 20

for i, line in enumerate(lines):
    safe_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").rstrip()
    
    delay = i * 0.03
    svg_elements += f'<text x="10" y="{y_position}" class="ascii-line" style="animation-delay: {delay}s;">{safe_line}</text>\n'
    y_position += 12  

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
y_position += 20
svg_elements += f'<text x="10" y="{y_position}" class="status">>> System Update: {current_time} | Latest Launch: KippQuiz</text>'

total_height = y_position + 20

svg_content = f"""<svg width="800" height="{total_height}" xmlns="http://www.w3.org/2000/svg">
    <style>
        .ascii-line {{
            font-family: 'Courier New', monospace;
            font-size: 10px;
            fill: #c9d1d9; /* Helles GitHub-Grau */
            white-space: pre;
            opacity: 0;
            animation: fadeIn 0.1s forwards;
        }}
        .status {{
            font-family: 'Courier New', monospace;
            font-size: 12px;
            fill: #58a6ff; /* GitHub-Blau */
            opacity: 0;
            animation: fadeIn 1s forwards;
            animation-delay: {len(lines) * 0.03 + 0.5}s; /* Erscheint ganz am Schluss */
        }}
        @keyframes fadeIn {{
            to {{ opacity: 1; }}
        }}
    </style>
    
    <!-- Transparenter oder dunkler Hintergrund -->
    <rect width="100%" height="100%" fill="#0d1117" rx="10" />
    
    {svg_elements}
</svg>"""

with open("profile_art.svg", "w", encoding="utf-8") as file:
    file.write(svg_content)

print("SVG erfolgreich generiert!")