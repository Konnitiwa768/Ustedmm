import svgwrite
import os

os.makedirs("letters", exist_ok=True)
WIDTH, HEIGHT = 100, 100
STROKE_WIDTH = 3

letters_lines = {
    'A': [[(20, 20), (80, 20), (50, 80)]],  # 三角形
    'B': [[(20, 20), (20, 80)], [(20, 50), (70, 65)]],
    'C': [[(80, 30), (30, 30), (20, 70)]],
    'D': [[(20, 20), (70, 50), (20, 80)]],
    'E': [[(80, 20), (20, 20), (20, 80), (80, 80)]],
    'F': [[(20, 20), (20, 80)], [(20, 50), (60, 50)]],
    'G': [[(80, 30), (30, 30), (30, 70), (80, 70)]],
    'H': [[(20, 20), (20, 80)], [(80, 20), (80, 80)], [(20, 50), (80, 50)]],
    'I': [[(50, 20), (50, 80)]],
    'J': [[(80, 20), (80, 60), (60, 80)]],
    'K': [[(20, 20), (20, 80)], [(20, 50), (80, 20)], [(20, 50), (80, 80)]],
    'L': [[(20, 20), (20, 80), (80, 80)]],
    'M': [[(20, 80), (50, 20), (80, 80)]],
    'N': [[(20, 80), (20, 20), (80, 80), (80, 20)]],
    'O': [[(30, 30), (70, 30), (70, 70), (30, 70), (30, 30)]],
    'P': [[(20, 80), (20, 20), (70, 35)]],
    'Q': [[(30, 30), (70, 30), (70, 70), (30, 70), (30, 30)], [(60, 60), (80, 80)]],
    'R': [[(20, 80), (20, 20), (70, 35)], [(20, 50), (80, 80)]],
    'S': [[(80, 20), (30, 20), (30, 50), (80, 50), (80, 80), (30, 80)]],
    'T': [[(20, 20), (80, 20)], [(50, 20), (50, 80)]],
    'U': [[(20, 20), (20, 70), (50, 80), (80, 70), (80, 20)]],
    'V': [[(20, 20), (50, 80), (80, 20)]],
    'W': [[(20, 20), (35, 80), (50, 60), (65, 80), (80, 20)]],
    'X': [[(20, 20), (80, 80)], [(80, 20), (20, 80)]],
    'Y': [[(20, 20), (50, 50)], [(80, 20), (50, 50), (50, 80)]],
    'Z': [[(20, 20), (80, 20), (20, 80), (80, 80)]],
}

for ch in letters_lines.keys():
    dwg = svgwrite.Drawing(filename=os.path.join("letters", f"{ch}.svg"), size=(WIDTH, HEIGHT))
    g = dwg.g(stroke="black", fill="none", stroke_width=STROKE_WIDTH)

    for line in letters_lines[ch]:
        for i in range(len(line) - 1):
            g.add(dwg.line(line[i], line[i + 1]))

    dwg.add(g)
    dwg.save()

print("✅ 完全オリジナル文字群を letters/ に保存しました。")
