import svgwrite
import os

output_dir = "letters"
os.makedirs(output_dir, exist_ok=True)

WIDTH, HEIGHT = 100, 100
STROKE_WIDTH = 3

# ほんの少しだけアルファベット感を残しつつも
# 完全オリジナル形で各文字を直線・多角形で定義する

def draw_letter(dwg, ch):
    g = dwg.g(stroke="black", fill="none", stroke_width=STROKE_WIDTH)

    if ch == 'A':
        # 縦長の四角形に斜めをほんの少し入れるだけで、
        # ただの三角ではない形
        g.add(dwg.line((30, 80), (30, 20)))
        g.add(dwg.line((30, 20), (70, 30)))
        g.add(dwg.line((70, 30), (70, 80)))
        g.add(dwg.line((30, 50), (70, 60)))
    elif ch == 'B':
        # 大きい長方形＋中を斜め線で2分割
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.line((30, 20), (70, 20)))
        g.add(dwg.line((70, 20), (70, 80)))
        g.add(dwg.line((70, 80), (30, 80)))
        g.add(dwg.line((30, 50), (70, 50)))
        g.add(dwg.line((30, 20), (70, 80)))
    elif ch == 'C':
        # L字を横長にずらして2本重ねただけ
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.line((30, 20), (70, 20)))
        g.add(dwg.line((30, 80), (70, 80)))
        g.add(dwg.line((70, 20), (70, 40)))
    elif ch == 'D':
        # 大きめ長方形＋中に小さい斜め長方形
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.line((30, 20), (70, 20)))
        g.add(dwg.line((70, 20), (70, 80)))
        g.add(dwg.line((70, 80), (30, 80)))
        g.add(dwg.line((45, 35), (65, 45)))
        g.add(dwg.line((65, 45), (45, 65)))
        g.add(dwg.line((45, 65), (65, 75)))
    elif ch == 'E':
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.line((30, 20), (70, 20)))
        g.add(dwg.line((30, 50), (60, 50)))
        g.add(dwg.line((30, 80), (70, 80)))
    elif ch == 'F':
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.line((30, 20), (70, 20)))
        g.add(dwg.line((30, 50), (60, 50)))
    elif ch == 'G':
        # 開いた四角＋中にL字
        g.add(dwg.line((30, 20), (70, 20)))
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.line((30, 80), (70, 80)))
        g.add(dwg.line((70, 80), (70, 50)))
        g.add(dwg.line((50, 50), (70, 50)))
        g.add(dwg.line((50, 50), (50, 65)))
    elif ch == 'H':
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.line((70, 20), (70, 80)))
        g.add(dwg.line((30, 50), (70, 60)))
    elif ch == 'I':
        g.add(dwg.line((50, 20), (50, 80)))
        g.add(dwg.line((40, 20), (60, 20)))
        g.add(dwg.line((40, 80), (60, 80)))
    elif ch == 'J':
        g.add(dwg.line((50, 20), (50, 70)))
        g.add(dwg.line((50, 70), (40, 80)))
        g.add(dwg.line((40, 80), (30, 70)))
    elif ch == 'K':
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.line((30, 50), (70, 30)))
        g.add(dwg.line((30, 50), (70, 70)))
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
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.line((70, 20), (70, 80)))
        g.add(dwg.line((30, 20), (70, 80)))
        g.add(dwg.line((30, 80), (70, 20)))
    elif ch == 'P':
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.line((30, 20), (70, 40)))
        g.add(dwg.line((70, 40), (30, 50)))
    elif ch == 'Q':
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.line((70, 20), (70, 80)))
        g.add(dwg.line((30, 20), (70, 80)))
        g.add(dwg.line((30, 80), (70, 20)))
        g.add(dwg.line((60, 60), (80, 80)))
    elif ch == 'R':
        g.add(dwg.line((30, 20), (30, 80)))
        g.add(dwg.line((30, 20), (70, 40)))
        g.add(dwg.line((30, 50), (70, 80)))
    elif ch == 'S':
        g.add(dwg.line((70, 20), (30, 50)))
        g.add(dwg.line((30, 50), (70, 80)))
    elif ch == 'T':
        g.add(dwg.line((50, 20), (50, 80)))
        g.add(dwg.line((30, 20), (70, 20)))
    elif ch == 'U':
        g.add(dwg.line((30, 20), (30, 70)))
        g.add(dwg.line((30, 70), (50, 80)))
        g.add(dwg.line((50, 80), (70, 70)))
        g.add(dwg.line((70, 70), (70, 20)))
    elif ch == 'V':
        g.add(dwg.line((30, 20), (50, 80)))
        g.add(dwg.line((70, 20), (50, 80)))
    elif ch == 'W':
        g.add(dwg.line((20, 20), (35, 80)))
        g.add(dwg.line((35, 80), (50, 40)))
        g.add(dwg.line((50, 40), (65, 80)))
        g.add(dwg.line((65, 80), (80, 20)))
    elif ch == 'X':
        g.add(dwg.line((30, 20), (70, 80)))
        g.add(dwg.line((70, 20), (30, 80)))
    elif ch == 'Y':
        g.add(dwg.line((30, 20), (50, 50)))
        g.add(dwg.line((70, 20), (50, 50)))
        g.add(dwg.line((50, 50), (50, 80)))
    elif ch == 'Z':
        g.add(dwg.line((30, 20), (70, 20)))
        g.add(dwg.line((70, 20), (30, 80)))
        g.add(dwg.line((30, 80), (70, 80)))

    # 小文字は大文字をベースに縮小・上下ずらしのようなイメージで別形状に
    elif ch == 'a':
        g.add(dwg.line((35, 80), (35, 50)))
        g.add(dwg.line((35, 50), (65, 50)))
        g.add(dwg.line((65, 50), (65, 80)))
        g.add(dwg.line((65, 80), (35, 80)))
        g.add(dwg.line((50, 50), (50, 80)))
    elif ch == 'b':
        g.add(dwg.line((35, 40), (35, 90)))
        g.add(dwg.line((35, 40), (65, 40)))
        g.add(dwg.line((65, 40), (65, 90)))
        g.add(dwg.line((65, 90), (35, 90)))
        g.add(dwg.line((35, 65), (65, 65)))
    elif ch == 'c':
        g.add(dwg.line((65, 40), (35, 40)))
        g.add(dwg.line((35, 40), (35, 80)))
        g.add(dwg.line((35, 80), (65, 80)))
    elif ch == 'd':
        g.add(dwg.line((65, 40), (65, 90)))
        g.add(dwg.line((65, 40), (35, 40)))
        g.add(dwg.line((35, 40), (35, 90)))
        g.add(dwg.line((35, 90), (65, 90)))
        g.add(dwg.line((35, 65), (65, 65)))
    elif ch == 'e':
        g.add(dwg.line((65, 40), (35, 40)))
        g.add(dwg.line((35, 40), (35, 90)))
        g.add(dwg.line((35, 65), (65, 65)))
        g.add(dwg.line((65, 90), (35, 90)))
    elif ch == 'f':
        g.add(dwg.line((50, 40), (50, 90)))
        g.add(dwg.line((50, 40), (35, 40)))
        g.add(dwg.line((50, 65), (70, 65)))
    elif ch == 'g':
        g.add(dwg.line((35, 50), (65, 50)))
        g.add(dwg.line((65, 50), (65, 90)))
        g.add(dwg.line((65, 90), (35, 90)))
        g.add(dwg.line((35, 90), (35, 75)))
        g.add(dwg.line((35, 75), (65, 75)))
    elif ch == 'h':
        g.add(dwg.line((35, 40), (35, 90)))
        g.add(dwg.line((65, 40), (65, 90)))
        g.add(dwg.line((35, 65), (65, 65)))
    elif ch == 'i':
        g.add(dwg.line((50, 40), (50, 90)))
        g.add(dwg.line((50, 40), (50, 45)))
    elif ch == 'j':
        g.add(dwg.line((50, 40), (50, 90)))
        g.add(dwg.line((50, 90), (40, 100)))
        g.add(dwg.line((50, 40), (50, 45)))
    elif ch == 'k':
        g.add(dwg.line((35, 40), (35, 90)))
        g.add(dwg.line((65, 40), (35, 65)))
        g.add(dwg.line((35, 65), (65, 90)))
    elif ch == 'l':
        g.add(dwg.line((50, 40), (50, 90)))
    elif ch == 'm':
        g.add(dwg.line((35, 65), (35, 90)))
        g.add(dwg.line((35, 65), (50, 75)))
        g.add(dwg.line((50, 75), (65, 65)))
        g.add(dwg.line((65, 65), (65, 90)))
    elif ch == 'n':
        g.add(dwg.line((35, 65), (35, 90)))
        g.add(dwg.line((35, 65), (65, 90)))
        g.add(dwg.line((65, 90), (65, 65)))
    elif ch == 'o':
        g.add(dwg.line((35, 50), (65, 50)))
        g.add(dwg.line((35, 50), (35, 90)))
        g.add(dwg.line((65, 50), (65, 90)))
        g.add(dwg.line((35, 90), (65, 90)))
    elif ch == 'p':
        g.add(dwg.line((35, 40), (35, 90)))
        g.add(dwg.line((35, 40), (65, 40)))
        g.add(dwg.line((65, 40), (65, 65)))
        g.add(dwg.line((65, 65), (35, 65)))
    elif ch == 'q':
        g.add(dwg.line((65, 40), (65, 90)))
        g.add(dwg.line((65, 40), (35, 40)))
        g.add(dwg.line((35, 40), (35, 65)))
        g.add(dwg.line((35, 65), (65, 65)))
    elif ch == 'r':
        g.add(dwg.line((35, 65), (35, 90)))
        g.add(dwg.line((35, 65), (65, 90)))
    elif ch == 's':
        g.add(dwg.line((65, 50), (35, 65)))
        g.add(dwg.line((35, 65), (65, 80)))
    elif ch == 't':
        g.add(dwg.line((50, 40), (50, 90)))
        g.add(dwg.line((35, 65), (65, 65)))
    elif ch == 'u':
        g.add(dwg.line((35, 50), (35, 90)))
        g.add(dwg.line((35, 90), (65, 90)))
        g.add(dwg.line((65, 90), (65, 50)))
    elif ch == 'v':
        g.add(dwg.line((35, 50), (50, 90)))
        g.add(dwg.line((65, 50), (50, 90)))
    elif ch == 'w':
        g.add(dwg.line((30, 50), (40, 90)))
        g.add(dwg.line((40, 90), (50, 65)))
        g.add(dwg.line((50, 65), (60, 90)))
        g.add(dwg.line((60, 90), (70, 50)))
    elif ch == 'x':
        g.add(dwg.line((35, 65), (65, 90)))
        g.add(dwg.line((65, 65), (35, 90)))
    elif ch == 'y':
        g.add(dwg.line((35, 50), (50, 90)))
        g.add(dwg.line((65, 50), (50, 90)))
        g.add(dwg.line((50, 90), (50, 110)))
    elif ch == 'z':
        g.add(dwg.line((35, 65), (65, 65)))
        g.add(dwg.line((65, 65), (35, 90)))
        g.add(dwg.line((35, 90), (65, 90)))

    # 記号は全部四角・斜線・縦横線のみで独自デザイン
    elif ch == '!':
        g.add(dwg.line((50, 20), (50, 70)))
        g.add(dwg.line((50, 80), (50, 90)))
    elif ch == '?':
        g.add(dwg.line((35, 30), (65, 30)))
        g.add(dwg.line((65, 30), (50, 60)))
        g.add(dwg.line((50, 60), (35, 90)))
        g.add(dwg.line((50, 90), (50, 100)))
    elif ch == ':':
        g.add(dwg.line((50, 40), (50, 50)))
        g.add(dwg.line((50, 70), (50, 80)))
    elif ch == ';':
        g.add(dwg.line((50, 40), (50, 50)))
        g.add(dwg.line((50, 70), (50, 90)))
        g.add(dwg.line((45, 90), (55, 95)))
    elif ch == '.':
        g.add(dwg.line((50, 90), (50, 95)))
        g.add(dwg.line((45, 95), (55, 95)))
    elif ch == ',':
        g.add(dwg.line((50, 90), (50, 100)))
        g.add(dwg.line((45, 100), (55, 110)))
    elif ch == '\'':
        g.add(dwg.line((55, 20), (55, 50)))
    elif ch == '"':
        g.add(dwg.line((45, 20), (45, 50)))
        g.add(dwg.line((55, 20), (55, 50)))
    else:
        # 対応なければ何も描かない（空白）
        pass
    return g


def main():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!?:;.,'\""
    for ch in letters:
        dwg = svgwrite.Drawing(filename=os.path.join(output_dir, f"{ch}.svg"), size=(WIDTH, HEIGHT))
        dwg.add(draw_letter(dwg, ch))
        dwg.save()

if __name__ == "__main__":
    main()
