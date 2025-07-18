import svgwrite
import os

# 出力フォルダ
output_dir = "letters"
os.makedirs(output_dir, exist_ok=True)

# SVGサイズ
WIDTH, HEIGHT = 100, 100
STROKE_WIDTH = 4

# 全対象文字
all_chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!?:;.,'\"")

def draw_letter(dwg, char):
    g = dwg.g(stroke="black", fill="none", stroke_width=STROKE_WIDTH)

    # === 大文字 A-Z ===
    if char == 'A':
        g.add(dwg.line((50, 10), (20, 90)))
        g.add(dwg.line((50, 10), (80, 90)))
        g.add(dwg.line((35, 55), (65, 55)))
    elif char == 'B':
        g.add(dwg.line((20, 10), (20, 90)))
        g.add(dwg.path(d="M 20,10 Q 70,30 20,50"))
        g.add(dwg.path(d="M 20,50 Q 70,70 20,90"))
    elif char == 'C':
        g.add(dwg.path(d="M 80,20 Q 40,10 20,50 Q 40,90 80,80"))
    elif char == 'D':
        g.add(dwg.line((20, 10), (20, 90)))
        g.add(dwg.path(d="M 20,10 Q 90,50 20,90"))
    elif char == 'E':
        g.add(dwg.line((80, 10), (20, 10)))
        g.add(dwg.line((20, 10), (20, 90)))
        g.add(dwg.line((20, 50), (60, 50)))
        g.add(dwg.line((20, 90), (80, 90)))
    elif char == 'F':
        g.add(dwg.line((20, 10), (20, 90)))
        g.add(dwg.line((20, 10), (80, 10)))
        g.add(dwg.line((20, 50), (60, 50)))
    elif char == 'G':
        g.add(dwg.path(d="M 80,20 Q 40,10 20,50 Q 40,90 80,80"))
        g.add(dwg.line((60, 60), (80, 60)))
    elif char == 'H':
        g.add(dwg.line((20, 10), (20, 90)))
        g.add(dwg.line((80, 10), (80, 90)))
        g.add(dwg.line((20, 50), (80, 50)))
    elif char == 'I':
        g.add(dwg.line((50, 10), (50, 90)))
        g.add(dwg.line((30, 10), (70, 10)))
        g.add(dwg.line((30, 90), (70, 90)))
    elif char == 'J':
        g.add(dwg.line((50, 10), (50, 80)))
        g.add(dwg.path(d="M 50,80 Q 50,95 20,80"))
    elif char == 'K':
        g.add(dwg.line((20, 10), (20, 90)))
        g.add(dwg.line((20, 50), (80, 10)))
        g.add(dwg.line((20, 50), (80, 90)))
    elif char == 'L':
        g.add(dwg.line((20, 10), (20, 90)))
        g.add(dwg.line((20, 90), (80, 90)))
    elif char == 'M':
        g.add(dwg.line((20, 90), (20, 10)))
        g.add(dwg.line((20, 10), (50, 50)))
        g.add(dwg.line((50, 50), (80, 10)))
        g.add(dwg.line((80, 10), (80, 90)))
    elif char == 'N':
        g.add(dwg.line((20, 90), (20, 10)))
        g.add(dwg.line((20, 10), (80, 90)))
        g.add(dwg.line((80, 90), (80, 10)))
    elif char == 'O':
        g.add(dwg.circle(center=(50, 50), r=35))
    elif char == 'P':
        g.add(dwg.line((20, 10), (20, 90)))
        g.add(dwg.path(d="M 20,10 Q 80,30 20,50"))
    elif char == 'Q':
        g.add(dwg.circle(center=(50, 50), r=35))
        g.add(dwg.line((65, 65), (90, 90)))
    elif char == 'R':
        g.add(dwg.line((20, 10), (20, 90)))
        g.add(dwg.path(d="M 20,10 Q 80,30 20,50"))
        g.add(dwg.line((20, 50), (80, 90)))
    elif char == 'S':
        g.add(dwg.path(d="M 80,20 Q 40,10 30,40 Q 20,70 60,80 Q 80,85 80,90"))
    elif char == 'T':
        g.add(dwg.line((50, 10), (50, 90)))
        g.add(dwg.line((20, 10), (80, 10)))
    elif char == 'U':
        g.add(dwg.path(d="M 20,10 L 20,60 Q 50,90 80,60 L 80,10"))
    elif char == 'V':
        g.add(dwg.line((20, 10), (50, 90)))
        g.add(dwg.line((80, 10), (50, 90)))
    elif char == 'W':
        g.add(dwg.line((20, 10), (35, 90)))
        g.add(dwg.line((35, 90), (50, 10)))
        g.add(dwg.line((50, 10), (65, 90)))
        g.add(dwg.line((65, 90), (80, 10)))
    elif char == 'X':
        g.add(dwg.line((20, 20), (80, 80)))
        g.add(dwg.line((80, 20), (20, 80)))
    elif char == 'Y':
        g.add(dwg.line((20, 10), (50, 50)))
        g.add(dwg.line((80, 10), (50, 50)))
        g.add(dwg.line((50, 50), (50, 90)))
    elif char == 'Z':
        g.add(dwg.line((20, 10), (80, 10)))
        g.add(dwg.line((80, 10), (20, 90)))
        g.add(dwg.line((20, 90), (80, 90)))

    # === 小文字 a-z ===
    elif char == 'a':
        g.add(dwg.circle(center=(50, 50), r=20))
        g.add(dwg.line((70, 50), (70, 90)))
    elif char == 'b':
        g.add(dwg.line((30, 10), (30, 90)))
        g.add(dwg.circle(center=(50, 60), r=20))
    elif char == 'c':
        g.add(dwg.path(d="M 70,30 Q 40,10 20,50 Q 40,90 70,70"))
    elif char == 'd':
        g.add(dwg.line((70, 10), (70, 90)))
        g.add(dwg.circle(center=(50, 60), r=20))
    elif char == 'e':
        g.add(dwg.path(d="M 70,50 Q 40,30 30,50 Q 40,70 70,50"))
    elif char == 'f':
        g.add(dwg.line((50, 10), (50, 90)))
        g.add(dwg.line((30, 30), (70, 30)))
    elif char == 'g':
        g.add(dwg.circle(center=(50, 50), r=20))
        g.add(dwg.line((60, 60), (70, 100)))
    elif char == 'h':
        g.add(dwg.line((30, 10), (30, 90)))
        g.add(dwg.line((30, 60), (70, 60)))
        g.add(dwg.line((70, 60), (70, 90)))
    elif char == 'i':
        g.add(dwg.line((50, 40), (50, 90)))
        g.add(dwg.circle(center=(50, 25), r=5))
    elif char == 'j':
        g.add(dwg.line((50, 40), (50, 90)))
        g.add(dwg.path(d="M 50,90 Q 40,100 30,90"))
        g.add(dwg.circle(center=(50, 25), r=5))
    elif char == 'k':
        g.add(dwg.line((30, 10), (30, 90)))
        g.add(dwg.line((30, 60), (70, 30)))
        g.add(dwg.line((30, 60), (70, 90)))
    elif char == 'l':
        g.add(dwg.line((50, 10), (50, 90)))
    elif char == 'm':
        g.add(dwg.line((20, 60), (20, 90)))
        g.add(dwg.line((20, 60), (40, 60)))
        g.add(dwg.line((40, 60), (40, 90)))
        g.add(dwg.line((40, 60), (60, 60)))
        g.add(dwg.line((60, 60), (60, 90)))
    elif char == 'n':
        g.add(dwg.line((30, 60), (30, 90)))
        g.add(dwg.line((30, 60), (70, 60)))
        g.add(dwg.line((70, 60), (70, 90)))
    elif char == 'o':
        g.add(dwg.circle(center=(50, 70), r=20))
    elif char == 'p':
        g.add(dwg.line((30, 40), (30, 110)))
        g.add(dwg.circle(center=(50, 60), r=20))
    elif char == 'q':
        g.add(dwg.line((70, 40), (70, 110)))
        g.add(dwg.circle(center=(50, 60), r=20))
    elif char == 'r':
        g.add(dwg.line((30, 60), (30, 90)))
        g.add(dwg.line((30, 60), (60, 60)))
    elif char == 's':
        g.add(dwg.path(d="M 70,60 Q 50,40 30,60 Q 50,80 70,70"))
    elif char == 't':
        g.add(dwg.line((50, 10), (50, 90)))
        g.add(dwg.line((30, 30), (70, 30)))
    elif char == 'u':
        g.add(dwg.path(d="M 30,60 L 30,90 Q 50,110 70,90 L 70,60"))
    elif char == 'v':
        g.add(dwg.line((30, 60), (50, 90)))
        g.add(dwg.line((70, 60), (50, 90)))
    elif char == 'w':
        g.add(dwg.line((20, 60), (35, 90)))
        g.add(dwg.line((35, 90), (50, 60)))
        g.add(dwg.line((50, 60), (65, 90)))
        g.add(dwg.line((65, 90), (80, 60)))
    elif char == 'x':
        g.add(dwg.line((30, 60), (70, 90)))
        g.add(dwg.line((70, 60), (30, 90)))
    elif char == 'y':
        g.add(dwg.line((30, 60), (50, 90)))
        g.add(dwg.line((70, 60), (50, 90)))
        g.add(dwg.line((50, 90), (50, 110)))
    elif char == 'z':
        g.add(dwg.line((30, 60), (70, 60)))
        g.add(dwg.line((70, 60), (30, 90)))
        g.add(dwg.line((30, 90), (70, 90)))

    # === 記号 ===
    elif char == '!':
        g.add(dwg.line((50, 20), (50, 70)))
        g.add(dwg.circle(center=(50, 85), r=3))
    elif char == '?':
        g.add(dwg.path(d="M 30,30 Q 50,10 70,30 Q 70,50 50,60 Q 50,65 50,70"))
        g.add(dwg.circle(center=(50, 85), r=3))
    elif char == ':':
        g.add(dwg.circle(center=(50, 30), r=4))
        g.add(dwg.circle(center=(50, 70), r=4))
    elif char == ';':
        g.add(dwg.circle(center=(50, 30), r=4))
        g.add(dwg.path(d="M 50,65 Q 45,80 55,90"))
    elif char == '.':
        g.add(dwg.circle(center=(50, 85), r=4))
    elif char == ',':
        g.add(dwg.path(d="M 50,80 Q 45,90 55,95"))
    elif char == "'":
        g.add(dwg.line((50, 20), (50, 40)))
    elif char == '"':
        g.add(dwg.line((40, 20), (40, 40)))
        g.add(dwg.line((60, 20), (60, 40)))

    dwg.add(g)

# 各文字を個別にファイル出力
for ch in all_chars:
    fname = ch if ch.isalnum() else f"symbol_{ord(ch)}"
    filename = os.path.join(output_dir, f"{fname}.svg")
    dwg = svgwrite.Drawing(filename, size=(WIDTH, HEIGHT), viewBox="0 0 100 100")
    draw_letter(dwg, ch)
    dwg.save()

print("✅ 全66文字のSVGを完全に出力しました。")
