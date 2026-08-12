from pathlib import Path

output = Path("assets/ascii.svg")

svg = """<svg xmlns="http://www.w3.org/2000/svg" width="700" height="400">
<rect width="100%" height="100%" fill="#0d1117"/>

<text x="30" y="50"
      fill="#00ff88"
      font-family="monospace"
      font-size="18">
  $ whoami
</text>

<text x="30" y="90"
      fill="#ffffff"
      font-family="monospace"
      font-size="16">
  Tushar Bhatt
</text>

<text x="30" y="120"
      fill="#8b949e"
      font-family="monospace"
      font-size="14">
  CSE • AI/ML Developer
</text>

<text x="30" y="180"
      fill="#00ff88"
      font-family="monospace"
      font-size="18">
  $ status
</text>

<text x="30" y="220"
      fill="#ffffff"
      font-family="monospace"
      font-size="14">
  Building intelligent systems...
</text>

<text x="30" y="250"
      fill="#ffffff"
      font-family="monospace"
      font-size="14">
  Exploring AI • Web • Automation
</text>

<text x="30" y="320"
      fill="#00ff88"
      font-family="monospace"
      font-size="18">
  $ 
  <animate
    attributeName="opacity"
    values="1;0;1"
    dur="1s"
    repeatCount="indefinite"/>
</text>
</svg>
"""

output.write_text(svg, encoding="utf-8")
print(f"Generated {output}")