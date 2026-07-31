import datetime
import os

with open("ascii_face.txt", "r", encoding="utf-8") as file:
    lines = [line.rstrip('\n') for line in file.readlines()]

max_len = max(len(line) for line in lines)

svg_elements = ""
y_position = 20

speed = 0.1

for i, line in enumerate(lines):
    padded_line = line.ljust(max_len)
    safe_line = padded_line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    
    delay = i * speed
    svg_elements += f'<text x="50%" y="{y_position}" text-anchor="middle" class="ascii-line" style="animation-delay: {delay}s;">{safe_line}</text>\n'
    y_position += 12

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
y_position += 20
status_delay = len(lines) * speed + 0.5

svg_elements += f'<text x="50%" y="{y_position}" text-anchor="middle" class="status" style="animation-delay: {status_delay}s;">>> System Update: {current_time} | Latest Launch: KippQuiz</text>'

total_height = y_position + 20

svg_content = f"""<svg width="800" height="{total_height}" xmlns="http://www.w3.org/2000/svg">
    <style>
        .ascii-line {{
            font-family: 'Courier New', monospace;
            font-size: 10px;
            fill: #c9d1d9;
            white-space: pre;
            opacity: 0;
            animation: fadeIn 0.1s forwards;
        }}
        .status {{
            font-family: 'Courier New', monospace;
            font-size: 12px;
            fill: #58a6ff;
            opacity: 0;
            animation: fadeIn 1s forwards;
        }}
        @keyframes fadeIn {{
            to {{ opacity: 1; }}
        }}
    </style>
    
    <rect width="100%" height="100%" fill="#0d1117" rx="10" />
    
    {svg_elements}
</svg>"""

with open("profile_art.svg", "w", encoding="utf-8") as file:
    file.write(svg_content)

print("SVG erfolgreich generiert, zentriert und verlangsamt!")