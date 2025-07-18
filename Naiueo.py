import svgwrite
import os

output_dir = "parallel_letters"
os.makedirs(output_dir, exist_ok=True)

WIDTH, HEIGHT = 100, 100
STROKE_WIDTH = 4
all_chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!?:;.,'\"")

def draw_parallel_letter(dwg, char):
    g = dwg.g(stroke="black", fill="none", stroke_width=STROKE_WIDTH)

    # === パラレルワールド風の文字デザイン例 ===
    if char == 'A':
        g.add(dwg.path(d="M 20,90 L 50,10 L 80,90 L 50,70 Z"))
    elif char == 'B':
        g.add(dwg.path(d="M 20,10 L 20,90 Q 80,40 20,60 Q 80,80 20,90"))
    elif char == 'C':
        g.add(dwg.path(d="M 80,20 Q 40,10 20,50 Q 40,90 80,80 Q 70,70 65,65"))
    elif char == 'D':
        g.add(dwg.path(d="M 20,10 L 20,90 Q 90,50 20,10"))
    elif char == 'E':
        g.add(dwg.path(d="M 80,10 L 20,10 L 20,90 L 80,90 M 20,50 L 60,50"))
    elif char == 'F':
        g.add(dwg.path(d="M 20,10 L 20,90 M 20,10 L 80,10 M 20,50 L 60,50"))
    elif char == 'G':
        g.add(dwg.path(d="M 80,20 Q 30,0 20,50 Q 40,90 80,80 L 60,60"))
    elif char == 'H':
        g.add(dwg.path(d="M 20,10 L 20,90 M 80,10 L 80,90 M 20,50 L 80,50"))
    elif char == 'I':
        g.add(dwg.path(d="M 50,10 L 50,90 M 30,10 L 70,10 M 30,90 L 70,90"))
    elif char == 'J':
        g.add(dwg.path(d="M 70,10 L 70,70 Q 60,100 30,80"))
    elif char == 'K':
        g.add(dwg.path(d="M 20,10 L 20,90 M 20,50 L 80,10 M 20,50 L 80,90"))
    elif char == 'L':
        g.add(dwg.path(d="M 20,10 L 20,90 L 80,90"))
    elif char == 'M':
        g.add(dwg.path(d="M 20,90 L 20,10 L 50,60 L 80,10 L 80,90"))
    elif char == 'N':
        g.add(dwg.path(d="M 20,90 L 20,10 L 80,90 L 80,10"))
    elif char == 'O':
        g.add(dwg.path(d="M 50,10 Q 90,50 50,90 Q 10,50 50,10 Z"))
    elif char == 'P':
        g.add(dwg.path(d="M 20,10 L 20,90 M 20,10 Q 80,30 20,50"))
    elif char == 'Q':
        g.add(dwg.circle(center=(50, 50), r=35))
        g.add(dwg.line((50, 50), (90, 90)))
    elif char == 'R':
        g.add(dwg.path(d="M 20,10 L 20,90 M 20,10 Q 80,30 20,50 L 80,90"))
    elif char == 'S':
        g.add(dwg.path(d="M 80,20 Q 50,0 20,30 Q 50,50 20,70 Q 50,90 80,80"))
    elif char == 'T':
        g.add(dwg.path(d="M 50,10 L 50,90 M 20,10 L 80,10"))
    elif char == 'U':
        g.add(dwg.path(d="M 20,10 L 20,60 Q 50,90 80,60 L 80,10"))
    elif char == 'V':
        g.add(dwg.path(d="M 20,10 L 50,90 L 80,10"))
    elif char == 'W':
        g.add(dwg.path(d="M 20,10 L 35,90 L 50,30 L 65,90 L 80,10"))
    elif char == 'X':
        g.add(dwg.path(d="M 20,20 L 80,80 M 80,20 L 20,80"))
    elif char == 'Y':
        g.add(dwg.path(d="M 20,10 L 50,50 L 80,10 M 50,50 L 50,90"))
    elif char == 'Z':
        g.add(dwg.path(d="M 20,10 L 80,10 L 20,90 L 80,90"))

    # 小文字 a-z（それぞれ独自デザイン）
    elif char == 'a':
        g.add(dwg.path(d="M 50,70 Q 30,50 50,30 Q 70,50 50,70 Z"))
    elif char == 'b':
        g.add(dwg.path(d="M 30,10 L 30,90 Q 70,60 30,50"))
    elif char == 'c':
        g.add(dwg.path(d="M 70,40 Q 30,10 20,50 Q 40,90 70,70"))
    elif char == 'd':
        g.add(dwg.path(d="M 70,10 L 70,90 Q 30,60 70,50"))
    elif char == 'e':
        g.add(dwg.path(d="M 30,50 Q 50,30 70,50 Q 50,70 30,50"))
    elif char == 'f':
        g.add(dwg.path(d="M 50,10 L 50,90 M 30,40 L 70,40"))
    elif char == 'g':
        g.add(dwg.circle(center=(50, 50), r=20))
        g.add(dwg.path(d="M 60,60 Q 80,90 50,110"))
    elif char == 'h':
        g.add(dwg.path(d="M 30,10 L 30,90 M 30,60 Q 70,40 70,90"))
    elif char == 'i':
        g.add(dwg.circle(center=(50, 25), r=5))
        g.add(dwg.line((50, 40), (50, 90)))
    elif char == 'j':
        g.add(dwg.circle(center=(60, 25), r=5))
        g.add(dwg.path(d="M 60,40 L 60,100 Q 50,110 40,90"))
    elif char == 'k':
        g.add(dwg.path(d="M 30,10 L 30,90 M 30,60 L 70,30 M 30,60 L 70,90"))
    elif char == 'l':
        g.add(dwg.path(d="M 50,10 L 50,90"))
    elif char == 'm':
        g.add(dwg.path(d="M 20,60 L 20,90 M 20,60 Q 40,40 40,60 L 40,90 M 40,60 Q 60,40 60,60 L 60,90"))
    elif char == 'n':
        g.add(dwg.path(d="M 30,60 L 30,90 M 30,60 Q 70,40 70,90"))
    elif char == 'o':
        g.add(dwg.circle(center=(50, 70), r=20))
    elif char == 'p':
        g.add(dwg.path(d="M 30,40 L 30,110 Q 70,80 30,60"))
    elif char == 'q':
        g.add(dwg.path(d="M 70,40 L 70,110 Q 30,80 70,60"))
    elif char == 'r':
        g.add(dwg.path(d="M 30,60 L 30,90 M 30,60 Q 60,40 60,60"))
    elif char == 's':
        g.add(dwg.path(d="M 70,60 Q 50,40 30,60 Q 50,80 70,70"))
    elif char == 't':
        g.add(dwg.path(d="M 50,10 L 50,90 M 30,30 L 70,30"))
    elif char == 'u':
        g.add(dwg.path(d="M 30,60 L 30,90 Q 50,110 70,90 L 70,60"))
    elif char == 'v':
        g.add(dwg.path(d="M 30,60 L 50,90 L 70,60"))
    elif char == 'w':
        g.add(dwg.path(d="M 20,60 L 35,90 L 50,60 L 65,90 L 80,60"))
    elif char == 'x':
        g.add(dwg.path(d="M 30,60 L 70,90 M 70,60 L 30,90"))
    elif char == 'y':
        g.add(dwg.path(d="M 30,60 L 50,90 L 70,60 M 50,90 L 50,110"))
    elif char == 'z':
        g.add(dwg.path(d="M 30,60 L 70,60 L 30,90 L 70,90"))

    # 記号（パラレル風）
    elif char == '!':
        g.add(dwg.path(d="M 50,20 L 50,70"))
        g.add(dwg.circle(center=(50, 85), r=5))
    elif char == '?':
        g.add(dwg.path(d="M 30,30 Q 50,10 70,30 Q 70,50 50,60 L 50,70"))
        g.add(dwg.circle(center=(50, 85), r=5))
    elif char == ':':
        g.add(dwg.circle(center=(50, 30), r=5))
        g.add(dwg.circle(center=(50, 70), r=5))
    elif char == ';':
        g.add(dwg.circle(center=(50, 30), r=5))
        g.add(dwg.path(d="M 50,70 Q 45,85 55,95"))
    elif char == '.':
        g.add(dwg.circle(center=(50, 85), r=5))
    elif char == ',':
        g.add(dwg.path(d="M 50,80 Q 45,90 55,100"))
    elif char == "'":
        g.add(dwg.line((50, 20), (50, 40)))
    elif char == '"':
        g.add(dwg.line((40, 20), (40, 40)))
        g.add(dwg.line((60, 20), (60, 40)))

    dwg.add(g)

# 書き出し処理
for ch in all_chars:
    fname = ch if ch.isalnum() else f"symbol_{ord(ch)}"
    filepath = os.path.join(output_dir, f"{fname}.svg")
    dwg = svgwrite.Drawing(filepath, size=(WIDTH, HEIGHT), viewBox="0 0 100 100")
    draw_parallel_letter(dwg, ch)
    dwg.save()

print("✅ パラレル風アルファベット 66文字を完全に描画し出力しました。")
