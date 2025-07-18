import svgwrite
import os

output_dir = "letters"
os.makedirs(output_dir, exist_ok=True)

WIDTH, HEIGHT = 100, 100
STROKE_WIDTH = 3

all_chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!?:;.,'\"")

def draw_letter(dwg, ch):
    g = dwg.g(stroke="black", fill="none", stroke_width=STROKE_WIDTH)

    # 大文字パラレルアルファベット風
    if ch == 'A':
        g.add(dwg.line((30, 85), (45, 20)))
        g.add(dwg.line((45, 20), (70, 85)))
        g.add(dwg.line((38, 55), (62, 55)))
    elif ch == 'B':
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.path(d="M30,20 C60,20 65,40 30,50"))
        g.add(dwg.path(d="M30,50 C65,60 60,80 30,80"))
    elif ch == 'C':
        g.add(dwg.path(d="M70,25 C30,10 20,50 40,75"))
    elif ch == 'D':
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.path(d="M30,20 C75,30 75,70 30,80"))
    elif ch == 'E':
        g.add(dwg.line((70, 20), (30, 20)))
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.line((40, 50), (65, 50)))
        g.add(dwg.line((30, 80), (70, 80)))
    elif ch == 'F':
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.line((30, 20), (70, 20)))
        g.add(dwg.line((35, 50), (65, 50)))
    elif ch == 'G':
        g.add(dwg.path(d="M65,75 C25,80 30,40 65,45"))
        g.add(dwg.line((65, 45), (65, 65)))
    elif ch == 'H':
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.line((70, 20), (70, 80)))
        g.add(dwg.line((30, 50), (70, 50)))
    elif ch == 'I':
        g.add(dwg.line((50, 20), (50, 80)))
        g.add(dwg.line((35, 20), (65, 20)))
        g.add(dwg.line((35, 80), (65, 80)))
    elif ch == 'J':
        g.add(dwg.line((50, 20), (50, 70)))
        g.add(dwg.path(d="M50,70 C45,80 30,75 30,65"))
    elif ch == 'K':
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.line((30, 50), (65, 30)))
        g.add(dwg.line((30, 50), (65, 75)))
    elif ch == 'L':
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.line((30, 80), (70, 80)))
    elif ch == 'M':
        g.add(dwg.line((30, 80), (30, 20)))
        g.add(dwg.line((30, 20), (50, 50)))
        g.add(dwg.line((50, 50), (70, 20)))
        g.add(dwg.line((70, 20), (70, 80)))
    elif ch == 'N':
        g.add(dwg.line((30, 80), (30, 20)))
        g.add(dwg.line((30, 20), (70, 80)))
        g.add(dwg.line((70, 80), (70, 20)))
    elif ch == 'O':
        g.add(dwg.circle(center=(50, 50), r=32))
        g.add(dwg.line((50, 20), (50, 80)))
    elif ch == 'P':
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.path(d="M30,20 C70,20 70,50 30,50"))
    elif ch == 'Q':
        g.add(dwg.circle(center=(50, 50), r=32))
        g.add(dwg.line((60, 70), (80, 90)))
    elif ch == 'R':
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.path(d="M30,20 C70,20 70,50 30,50"))
        g.add(dwg.line((40, 50), (75, 80)))
    elif ch == 'S':
        g.add(dwg.path(d="M70,20 C35,20 30,40 60,50 C90,60 35,80 30,80"))
    elif ch == 'T':
        g.add(dwg.line((50, 20), (50, 80)))
        g.add(dwg.line((30, 20), (70, 20)))
    elif ch == 'U':
        g.add(dwg.path(d="M30,20 L30,65 C40,90 60,90 70,65 L70,20"))
    elif ch == 'V':
        g.add(dwg.line((30, 20), (50, 80)))
        g.add(dwg.line((70, 20), (50, 80)))
    elif ch == 'W':
        g.add(dwg.line((25, 20), (40, 80)))
        g.add(dwg.line((40, 80), (55, 20)))
        g.add(dwg.line((55, 20), (70, 80)))
        g.add(dwg.line((70, 80), (85, 20)))
    elif ch == 'X':
        g.add(dwg.line((30, 30), (70, 70)))
        g.add(dwg.line((70, 30), (30, 70)))
    elif ch == 'Y':
        g.add(dwg.line((30, 20), (50, 50)))
        g.add(dwg.line((70, 20), (50, 50)))
        g.add(dwg.line((50, 50), (50, 80)))
    elif ch == 'Z':
        g.add(dwg.line((30, 20), (70, 20)))
        g.add(dwg.line((70, 20), (30, 80)))
        g.add(dwg.line((30, 80), (70, 80)))

    # 小文字パラレルアルファベット風
    elif ch == 'a':
        g.add(dwg.circle(center=(50, 60), r=18))
        g.add(dwg.line((68, 60), (68, 90)))
    elif ch == 'b':
        g.add(dwg.line((30, 30), (30, 90)))
        g.add(dwg.path(d="M30,50 C60,40 60,80 30,70"))
    elif ch == 'c':
        g.add(dwg.path(d="M65,40 C40,30 30,70 60,70"))
    elif ch == 'd':
        g.add(dwg.line((70, 30), (70, 90)))
        g.add(dwg.path(d="M70,50 C40,40 40,80 70,70"))
    elif ch == 'e':
        g.add(dwg.path(d="M65,60 C40,40 35,60 60,65 C65,70 35,75 65,65"))
    elif ch == 'f':
        g.add(dwg.line((50, 20), (50, 80)))
        g.add(dwg.line((30, 35), (65, 35)))
    elif ch == 'g':
        g.add(dwg.circle(center=(50, 60), r=18))
        g.add(dwg.line((62, 65), (70, 100)))
    elif ch == 'h':
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.line((30, 60), (60, 60)))
        g.add(dwg.line((60, 60), (60, 90)))
    elif ch == 'i':
        g.add(dwg.line((50, 50), (50, 90)))
        g.add(dwg.circle(center=(50, 35), r=4))
    elif ch == 'j':
        g.add(dwg.line((50, 50), (50, 90)))
        g.add(dwg.path(d="M50,90 C45,100 35,95 35,85"))
        g.add(dwg.circle(center=(50, 35), r=4))
    elif ch == 'k':
        g.add(dwg.line((30, 20), (30, 90)))
        g.add(dwg.line((30, 60), (65, 40)))
        g.add(dwg.line((30, 60), (65, 90)))
    elif ch == 'l':
        g.add(dwg.line((50, 20), (50, 90)))
    elif ch == 'm':
        g.add(dwg.line((20, 60), (20, 90)))
        g.add(dwg.line((20, 60), (40, 60)))
        g.add(dwg.line((40, 60), (40, 90)))
        g.add(dwg.line((40, 60), (60, 60)))
        g.add(dwg.line((60, 60), (60, 90)))
    elif ch == 'n':
        g.add(dwg.line((30, 60), (30, 90)))
        g.add(dwg.line((30, 60), (65, 60)))
        g.add(dwg.line((65, 60), (65, 90)))
    elif ch == 'o':
        g.add(dwg.circle(center=(50, 70), r=20))
    elif ch == 'p':
        g.add(dwg.line((30, 50), (30, 110)))
        g.add(dwg.circle(center=(50, 70), r=18))
    elif ch == 'q':
        g.add(dwg.line((70, 50), (70, 110)))
        g.add(dwg.circle(center=(50, 70), r=18))
    elif ch == 'r':
        g.add(dwg.line((30, 60), (30, 90)))
        g.add(dwg.line((30, 60), (60, 60)))
    elif ch == 's':
        g.add(dwg.path(d="M65,70 C50,50 30,65 60,80"))
    elif ch == 't':
        g.add(dwg.line((50, 30), (50, 90)))
        g.add(dwg.line((30, 45), (70, 45)))
    elif ch == 'u':
        g.add(dwg.path(d="M30,60 L30,90 C50,110 65,90 65,60"))
    elif ch == 'v':
        g.add(dwg.line((30, 60), (50, 90)))
        g.add(dwg.line((65, 60), (50, 90)))
    elif ch == 'w':
        g.add(dwg.line((20, 60), (35, 90)))
        g.add(dwg.line((35, 90), (50, 65)))
        g.add(dwg.line((50, 65), (65, 90)))
        g.add(dwg.line((65, 90), (80, 60)))
    elif ch == 'x':
        g.add(dwg.line((30, 65), (70, 90)))
        g.add(dwg.line((70, 65), (30, 90)))
    elif ch == 'y':
        g.add(dwg.line((30, 60), (50, 90)))
        g.add(dwg.line((70, 60), (50, 90)))
        g.add(dwg.line((50, 90), (50, 110)))
    elif ch == 'z':
        g.add(dwg.line((30, 60), (70, 60)))
        g.add(dwg.line((70, 60), (30, 90)))
        g.add(dwg.line((30, 90), (70, 90)))

    # 記号パラレル風
    elif ch == '!':
        g.add(dwg.line((50, 25), (50, 65)))
        g.add(dwg.circle(center=(50, 80), r=3))
    elif ch == '?':
        g.add(dwg.path(d="M35,30 C50,10 70,30 50,50"))
        g.add(dwg.path(d="M50,50 L50,60"))
        g.add(dwg.circle(center=(50, 75), r=4))
    elif ch == ':':
        g.add(dwg.circle(center=(50, 35), r=5))
        g.add(dwg.circle(center=(50, 65), r=5))
    elif ch == ';':
        g.add(dwg.circle(center=(50, 35), r=5))
        g.add(dwg.path(d="M50,65 Q45,75 55,85"))
    elif ch == '.':
        g.add(dwg.circle(center=(50, 80), r=5))
    elif ch == ',':
        g.add(dwg.path(d="M50,75 Q45,85 55,95"))
    elif ch == "'":
        g.add(dwg.line((50, 20), (50, 40)))
    elif ch == '"':
        g.add(dwg.line((40, 20), (40, 40)))
        g.add(dwg.line((60, 20), (60, 40)))

    dwg.add(g)

for ch in all_chars:
    fname = ch if ch.isalnum() else f"symbol_{ord(ch)}"
    filename = os.path.join(output_dir, f"{fname}.svg")
    dwg = svgwrite.Drawing(filename, size=(WIDTH, HEIGHT), viewBox="0 0 100 100")
    draw_letter(dwg, ch)
    dwg.save()

print("✅ 対応しないがアルファベットっぽい独自字形をstroke3_letters_parallel/にすべて保存しました。")
