import fontforge

font = fontforge.font()
font.fontname = "OtherworldAlt"
font.fullname = "Otherworld Alternate Font"
font.familyname = "OtherworldAlt"
font.encoding = "UnicodeFull"

default_width = 700

# A
g = font.createChar(ord('A'), 'A')
p = g.glyphPen()
p.moveTo((300, 700))
p.lineTo((100, 0))
p.lineTo((200, 0))
p.lineTo((275, 350))
p.lineTo((325, 350))
p.lineTo((400, 0))
p.lineTo((500, 0))
p.lineTo((300, 700))
p.closePath()
g.width = default_width

# B
g = font.createChar(ord('B'), 'B')
p = g.glyphPen()
p.moveTo((100, 0))
p.lineTo((100, 700))
p.lineTo((350, 700))
p.curveTo((450, 700), (450, 600), (350, 600))
p.lineTo((350, 550))
p.curveTo((450, 550), (450, 400), (350, 400))
p.lineTo((100, 400))
p.lineTo((350, 400))
p.curveTo((450, 400), (450, 200), (350, 200))
p.lineTo((350, 100))
p.curveTo((450, 100), (450, 0), (350, 0))
p.lineTo((100, 0))
p.closePath()
g.width = default_width

# C
g = font.createChar(ord('C'), 'C')
p = g.glyphPen()
p.moveTo((450, 600))
p.curveTo((350, 700), (150, 700), (100, 500))
p.lineTo((100, 200))
p.curveTo((150, 0), (350, 0), (450, 100))
p.lineTo((400, 200))
p.curveTo((300, 100), (200, 100), (150, 300))
p.lineTo((150, 400))
p.curveTo((200, 600), (300, 600), (400, 500))
p.closePath()
g.width = default_width

# D
g = font.createChar(ord('D'), 'D')
p = g.glyphPen()
p.moveTo((100, 0))
p.lineTo((100, 700))
p.lineTo((350, 700))
p.curveTo((475, 700), (500, 600), (475, 500))
p.lineTo((475, 200))
p.curveTo((500, 100), (475, 0), (350, 0))
p.closePath()
g.width = default_width

# E
g = font.createChar(ord('E'), 'E')
p = g.glyphPen()
p.moveTo((450, 700))
p.lineTo((100, 700))
p.lineTo((100, 0))
p.lineTo((450, 0))
p.lineTo((450, 100))
p.lineTo((200, 100))
p.lineTo((200, 300))
p.lineTo((400, 300))
p.lineTo((400, 400))
p.lineTo((200, 400))
p.lineTo((200, 600))
p.lineTo((450, 600))
p.closePath()
g.width = default_width

# F
g = font.createChar(ord('F'), 'F')
p = g.glyphPen()
p.moveTo((100, 700))
p.lineTo((100, 0))
p.lineTo((450, 0))
p.lineTo((450, 100))
p.lineTo((200, 100))
p.lineTo((200, 300))
p.lineTo((400, 300))
p.lineTo((400, 400))
p.lineTo((200, 400))
p.lineTo((200, 600))
p.lineTo((100, 600))
p.closePath()
g.width = default_width

# G
g = font.createChar(ord('G'), 'G')
p = g.glyphPen()
p.moveTo((450, 600))
p.curveTo((350, 700), (150, 700), (100, 500))
p.lineTo((100, 200))
p.curveTo((150, 0), (350, 0), (450, 100))
p.lineTo((400, 200))
p.lineTo((400, 350))
p.lineTo((300, 350))
p.lineTo((300, 300))
p.lineTo((350, 300))
p.lineTo((350, 200))
p.curveTo((300, 100), (200, 100), (150, 300))
p.lineTo((150, 400))
p.curveTo((200, 600), (300, 600), (400, 500))
p.closePath()
g.width = default_width

# H
g = font.createChar(ord('H'), 'H')
p = g.glyphPen()
p.moveTo((100, 0))
p.lineTo((100, 700))
p.lineTo((200, 700))
p.lineTo((200, 400))
p.lineTo((400, 400))
p.lineTo((400, 700))
p.lineTo((500, 700))
p.lineTo((500, 0))
p.lineTo((400, 0))
p.lineTo((400, 300))
p.lineTo((200, 300))
p.lineTo((200, 0))
p.closePath()
g.width = default_width

# I
g = font.createChar(ord('I'), 'I')
p = g.glyphPen()
p.moveTo((300, 0))
p.lineTo((300, 700))
p.lineTo((400, 700))
p.lineTo((400, 0))
p.closePath()
g.width = default_width

# J
g = font.createChar(ord('J'), 'J')
p = g.glyphPen()
p.moveTo((400, 700))
p.lineTo((400, 100))
p.curveTo((400, 50), (350, 0), (300, 0))
p.curveTo((200, 0), (150, 100), (150, 200))
p.lineTo((150, 300))
p.lineTo((250, 300))
p.lineTo((250, 200))
p.curveTo((250, 150), (300, 100), (350, 100))
p.lineTo((350, 700))
p.closePath()
g.width = default_width

# K
g = font.createChar(ord('K'), 'K')
p = g.glyphPen()
p.moveTo((100, 0))
p.lineTo((100, 700))
p.lineTo((200, 700))
p.lineTo((350, 400))
p.lineTo((500, 700))
p.lineTo((600, 700))
p.lineTo((400, 400))
p.lineTo((600, 0))
p.lineTo((500, 0))
p.lineTo((350, 300))
p.lineTo((200, 0))
p.closePath()
g.width = default_width

# L
g = font.createChar(ord('L'), 'L')
p = g.glyphPen()
p.moveTo((100, 700))
p.lineTo((100, 0))
p.lineTo((500, 0))
p.lineTo((500, 100))
p.lineTo((200, 100))
p.lineTo((200, 700))
p.closePath()
g.width = default_width

# M
g = font.createChar(ord('M'), 'M')
p = g.glyphPen()
p.moveTo((100, 0))
p.lineTo((100, 700))
p.lineTo((250, 700))
p.lineTo((350, 300))
p.lineTo((450, 700))
p.lineTo((600, 700))
p.lineTo((600, 0))
p.lineTo((500, 0))
p.lineTo((500, 600))
p.lineTo((350, 100))
p.lineTo((200, 600))
p.lineTo((200, 0))
p.closePath()
g.width = default_width

# N
g = font.createChar(ord('N'), 'N')
p = g.glyphPen()
p.moveTo((100, 0))
p.lineTo((100, 700))
p.lineTo((200, 700))
p.lineTo((500, 200))
p.lineTo((500, 700))
p.lineTo((600, 700))
p.lineTo((600, 0))
p.lineTo((500, 0))
p.lineTo((200, 500))
p.lineTo((200, 0))
p.closePath()
g.width = default_width

# O
g = font.createChar(ord('O'), 'O')
p = g.glyphPen()
p.moveTo((300, 700))
p.curveTo((500, 700), (600, 500), (600, 300))
p.curveTo((600, 100), (500, 0), (300, 0))
p.curveTo((100, 0), (0, 100), (0, 300))
p.curveTo((0, 500), (100, 700), (300, 700))
p.closePath()
g.width = default_width

# P
g = font.createChar(ord('P'), 'P')
p = g.glyphPen()
p.moveTo((100, 0))
p.lineTo((100, 700))
p.lineTo((350, 700))
p.curveTo((450, 700), (450, 600), (350, 600))
p.curveTo((450, 600), (450, 400), (350, 400))
p.lineTo((100, 400))
p.closePath()
g.width = default_width

# Q
g = font.createChar(ord('Q'), 'Q')
p = g.glyphPen()
p.moveTo((300, 700))
p.curveTo((500, 700), (600, 500), (600, 300))
p.curveTo((600, 100), (500, 0), (300, 0))
p.curveTo((100, 0), (0, 100), (0, 300))
p.curveTo((0, 500), (100, 700), (300, 700))
p.closePath()
p.moveTo((450, 150))
p.lineTo((600, 0))
g.width = default_width

# R
g = font.createChar(ord('R'), 'R')
p = g.glyphPen()
p.moveTo((100, 0))
p.lineTo((100, 700))
p.lineTo((350, 700))
p.curveTo((450, 700), (450, 600), (350, 600))
p.curveTo((450, 600), (450, 400), (350, 400))
p.lineTo((100, 400))
p.lineTo((500, 0))
p.lineTo((400, 0))
p.closePath()
g.width = default_width

# S
g = font.createChar(ord('S'), 'S')
p = g.glyphPen()
p.moveTo((450, 600))
p.curveTo((350, 700), (150, 700), (100, 600))
p.curveTo((0, 500), (150, 400), (350, 400))
p.curveTo((450, 400), (600, 300), (500, 200))
p.curveTo((400, 100), (150, 100), (100, 0))
p.curveTo((0, -100), (450, -100), (450, 600))
p.closePath()
g.width = default_width

# T
g = font.createChar(ord('T'), 'T')
p = g.glyphPen()
p.moveTo((100, 700))
p.lineTo((600, 700))
p.lineTo((600, 600))
p.lineTo((400, 600))
p.lineTo((400, 0))
p.lineTo((300, 0))
p.lineTo((300, 600))
p.lineTo((100, 600))
p.closePath()
g.width = default_width

# U
g = font.createChar(ord('U'), 'U')
p = g.glyphPen()
p.moveTo((100, 700))
p.lineTo((100, 200))
p.curveTo((100, 100), (200, 0), (300, 0))
p.curveTo((400, 0), (500, 100), (500, 200))
p.lineTo((500, 700))
p.closePath()
g.width = default_width

# V
g = font.createChar(ord('V'), 'V')
p = g.glyphPen()
p.moveTo((100, 700))
p.lineTo((300, 0))
p.lineTo((500, 700))
p.closePath()
g.width = default_width

# W
g = font.createChar(ord('W'), 'W')
p = g.glyphPen()
p.moveTo((100, 700))
p.lineTo((225, 0))
p.lineTo((350, 400))
p.lineTo((475, 0))
p.lineTo((600, 700))
p.closePath()
g.width = default_width

# X
g = font.createChar(ord('X'), 'X')
p = g.glyphPen()
p.moveTo((100, 700))
p.lineTo((500, 0))
p.closePath()  # まず1つ目の輪郭を閉じる
p.moveTo((500, 700))
p.lineTo((100, 0))
p.closePath()
g.width = default_width

# Y
g = font.createChar(ord('Y'), 'Y')
p = g.glyphPen()
p.moveTo((100, 700))
p.lineTo((300, 400))
p.lineTo((300, 0))
p.closePath()  # まず1つ目の輪郭を閉じる
p.moveTo((500, 700))
p.lineTo((300, 400))
p.closePath()
g.width = default_width

# Z
g = font.createChar(ord('Z'), 'Z')
p = g.glyphPen()
p.moveTo((100, 700))
p.lineTo((500, 700))
p.lineTo((100, 0))
p.lineTo((500, 0))
p.closePath()
g.width = default_width

# 小文字 a-z を続けます

# a
g = font.createChar(ord('a'), 'a')
p = g.glyphPen()
p.moveTo((450, 400))
p.curveTo((450, 600), (300, 700), (200, 600))
p.curveTo((100, 500), (150, 300), (300, 300))
p.curveTo((400, 300), (450, 350), (450, 400))
p.closePath()
g.width = default_width

# b
g = font.createChar(ord('b'), 'b')
p = g.glyphPen()
p.moveTo((150, 0))
p.lineTo((150, 700))
p.lineTo((350, 700))
p.curveTo((450, 700), (450, 600), (350, 600))
p.curveTo((450, 600), (450, 400), (350, 400))
p.lineTo((150, 400))
p.closePath()
g.width = default_width

# c
g = font.createChar(ord('c'), 'c')
p = g.glyphPen()
p.moveTo((400, 500))
p.curveTo((300, 700), (150, 700), (100, 500))
p.curveTo((100, 300), (150, 100), (300, 100))
p.curveTo((400, 100), (450, 300), (400, 500))
p.closePath()
g.width = default_width

# d
g = font.createChar(ord('d'), 'd')
p = g.glyphPen()
p.moveTo((450, 0))
p.lineTo((450, 700))
p.lineTo((250, 700))
p.curveTo((150, 700), (150, 600), (250, 600))
p.curveTo((150, 600), (150, 400), (250, 400))
p.lineTo((450, 400))
p.closePath()
g.width = default_width

# e
g = font.createChar(ord('e'), 'e')
p = g.glyphPen()
p.moveTo((400, 400))
p.curveTo((350, 500), (150, 500), (150, 350))
p.curveTo((150, 300), (350, 300), (400, 350))
p.lineTo((400, 400))
p.closePath()
g.width = default_width

# f
g = font.createChar(ord('f'), 'f')
p = g.glyphPen()
p.moveTo((400, 700))
p.lineTo((300, 700))
p.lineTo((300, 0))
p.lineTo((400, 0))
p.lineTo((400, 100))
p.lineTo((350, 100))
p.lineTo((350, 300))
p.lineTo((400, 300))
p.closePath()
g.width = default_width

# g
g = font.createChar(ord('g'), 'g')
p = g.glyphPen()
p.moveTo((350, 400))
p.curveTo((450, 400), (450, 600), (350, 600))
p.curveTo((250, 600), (250, 400), (350, 400))
p.moveTo((450, 0))
p.lineTo((450, 100))
p.lineTo((150, 100))
p.curveTo((100, 100), (100, 0), (150, 0))
p.lineTo((450, 0))
p.closePath()
g.width = default_width

# h
g = font.createChar(ord('h'), 'h')
p = g.glyphPen()
p.moveTo((150, 0))
p.lineTo((150, 700))
p.lineTo((250, 700))
p.lineTo((250, 400))
p.lineTo((400, 400))
p.lineTo((400, 700))
p.lineTo((500, 700))
p.lineTo((500, 0))
p.lineTo((400, 0))
p.lineTo((400, 350))
p.lineTo((250, 350))
p.lineTo((250, 0))
p.closePath()
g.width = default_width

# i
g = font.createChar(ord('i'), 'i')
p = g.glyphPen()
p.moveTo((250, 0))
p.lineTo((250, 700))
p.lineTo((350, 700))
p.lineTo((350, 0))
p.closePath()
p.moveTo((250, 750))
p.lineTo((250, 800))
p.lineTo((350, 800))
p.lineTo((350, 750))
p.closePath()
g.width = default_width

# j
g = font.createChar(ord('j'), 'j')
p = g.glyphPen()
p.moveTo((350, 0))
p.lineTo((350, 700))
p.lineTo((250, 700))
p.lineTo((250, 0))
p.curveTo((250, -100), (350, -100), (400, 0))
p.closePath()
p.moveTo((250, 750))
p.lineTo((250, 800))
p.lineTo((350, 800))
p.lineTo((350, 750))
p.closePath()
g.width = default_width

# k
g = font.createChar(ord('k'), 'k')
p = g.glyphPen()
p.moveTo((150, 0))
p.lineTo((150, 700))
p.lineTo((250, 700))
p.lineTo((350, 450))
p.lineTo((450, 700))
p.lineTo((550, 700))
p.lineTo((350, 400))
p.lineTo((550, 0))
p.lineTo((450, 0))
p.lineTo((350, 350))
p.lineTo((250, 0))
p.closePath()
g.width = default_width

# l
g = font.createChar(ord('l'), 'l')
p = g.glyphPen()
p.moveTo((300, 0))
p.lineTo((300, 700))
p.lineTo((400, 700))
p.lineTo((400, 0))
p.closePath()
g.width = default_width

# m
g = font.createChar(ord('m'), 'm')
p = g.glyphPen()
p.moveTo((150, 400))
p.lineTo((150, 700))
p.lineTo((250, 700))
p.lineTo((250, 500))
p.lineTo((350, 700))
p.lineTo((450, 500))
p.lineTo((450, 700))
p.lineTo((550, 700))
p.lineTo((550, 400))
p.lineTo((450, 400))
p.lineTo((450, 600))
p.lineTo((350, 400))
p.lineTo((250, 600))
p.lineTo((250, 400))
p.closePath()
g.width = default_width

# n
g = font.createChar(ord('n'), 'n')
p = g.glyphPen()
p.moveTo((150, 400))
p.lineTo((150, 700))
p.lineTo((250, 700))
p.lineTo((350, 400))
p.lineTo((350, 700))
p.lineTo((450, 700))
p.lineTo((450, 400))
p.lineTo((350, 400))
p.lineTo((350, 600))
p.lineTo((250, 400))
p.lineTo((250, 600))
p.lineTo((150, 400))
p.closePath()
g.width = default_width

# o
g = font.createChar(ord('o'), 'o')
p = g.glyphPen()
p.moveTo((300, 400))
p.curveTo((450, 400), (450, 600), (300, 600))
p.curveTo((150, 600), (150, 400), (300, 400))
p.closePath()
g.width = default_width

# p
g = font.createChar(ord('p'), 'p')
p = g.glyphPen()
p.moveTo((150, 0))
p.lineTo((150, 700))
p.lineTo((350, 700))
p.curveTo((450, 700), (450, 600), (350, 600))
p.curveTo((450, 600), (450, 400), (350, 400))
p.lineTo((150, 400))
p.closePath()
p.moveTo((150, 400))
p.lineTo((150, 0))
p.closePath()
g.width = default_width

# q
g = font.createChar(ord('q'), 'q')
p = g.glyphPen()
p.moveTo((450, 0))
p.lineTo((450, 700))
p.lineTo((250, 700))
p.curveTo((150, 700), (150, 600), (250, 600))
p.curveTo((150, 600), (150, 400), (250, 400))
p.lineTo((450, 400))
p.closePath()
p.moveTo((450, 400))
p.lineTo((450, 0))
p.closePath()
g.width = default_width

# r
g = font.createChar(ord('r'), 'r')
p = g.glyphPen()
p.moveTo((150, 400))
p.lineTo((150, 700))
p.lineTo((250, 700))
p.lineTo((350, 400))
p.closePath()
g.width = default_width

# s
g = font.createChar(ord('s'), 's')
p = g.glyphPen()
p.moveTo((450, 600))
p.curveTo((350, 700), (150, 700), (100, 600))
p.curveTo((100, 500), (350, 400), (450, 400))
p.curveTo((550, 400), (500, 300), (400, 300))
p.curveTo((350, 300), (150, 200), (100, 100))
p.curveTo((100, 0), (350, 0), (450, 100))
p.closePath()
g.width = default_width

# t
g = font.createChar(ord('t'), 't')
p = g.glyphPen()
p.moveTo((350, 700))
p.lineTo((350, 300))
p.lineTo((250, 300))
p.lineTo((250, 0))
p.lineTo((350, 0))
p.lineTo((350, 300))
p.lineTo((450, 300))
p.lineTo((450, 700))
p.closePath()
g.width = default_width

# u
g = font.createChar(ord('u'), 'u')
p = g.glyphPen()
p.moveTo((150, 700))
p.lineTo((150, 300))
p.curveTo((150, 100), (350, 100), (350, 300))
p.lineTo((350, 700))
p.closePath()
g.width = default_width

# v
g = font.createChar(ord('v'), 'v')
p = g.glyphPen()
p.moveTo((150, 700))
p.lineTo((300, 0))
p.lineTo((450, 700))
p.closePath()
g.width = default_width

# w
g = font.createChar(ord('w'), 'w')
p = g.glyphPen()
p.moveTo((150, 700))
p.lineTo((225, 0))
p.lineTo((300, 400))
p.lineTo((375, 0))
p.lineTo((450, 700))
p.closePath()
g.width = default_width

# x
g = font.createChar(ord('x'), 'x')
p = g.glyphPen()
p.moveTo((150, 700))
p.lineTo((450, 0))
p.moveTo((450, 700))
p.lineTo((150, 0))
p.closePath()
g.width = default_width

# y
g = font.createChar(ord('y'), 'y')
p = g.glyphPen()
p.moveTo((150, 700))
p.lineTo((300, 400))
p.lineTo((300, 0))
p.lineTo((450, 0))
p.lineTo((450, 400))
p.lineTo((300, 700))
p.closePath()
g.width = default_width

# z
g = font.createChar(ord('z'), 'z')
p = g.glyphPen()
p.moveTo((150, 700))
p.lineTo((450, 700))
p.lineTo((150, 0))
p.lineTo((450, 0))
p.closePath()
g.width = default_width

# 記号

# .
g = font.createChar(ord('.'), '.')
p = g.glyphPen()
p.moveTo((275, 100))
p.lineTo((325, 100))
p.lineTo((325, 150))
p.lineTo((275, 150))
p.closePath()
g.width = 400

# ,
g = font.createChar(ord(','), ',')
p = g.glyphPen()
p.moveTo((275, 150))
p.lineTo((325, 150))
p.lineTo((300, 50))
p.closePath()
g.width = 400

# ;
g = font.createChar(ord(';'), ';')
p = g.glyphPen()
p.moveTo((275, 200))
p.lineTo((325, 200))
p.lineTo((300, 100))
p.closePath()
p.moveTo((275, 100))
p.lineTo((325, 100))
p.lineTo((325, 150))
p.lineTo((275, 150))
p.closePath()
g.width = 400

# :
g = font.createChar(ord(':'), ':')
p = g.glyphPen()
p.moveTo((275, 100))
p.lineTo((325, 100))
p.lineTo((325, 150))
p.lineTo((275, 150))
p.closePath()
p.moveTo((275, 250))
p.lineTo((325, 250))
p.lineTo((325, 300))
p.lineTo((275, 300))
p.closePath()
g.width = 400

# "
g = font.createChar(ord('"'), '"')
p = g.glyphPen()
p.moveTo((200, 600))
p.lineTo((275, 700))
p.lineTo((350, 600))
p.closePath()
p.moveTo((400, 600))
p.lineTo((475, 700))
p.lineTo((550, 600))
p.closePath()
g.width = 600

# '
g = font.createChar(ord("'"), "'")
p = g.glyphPen()
p.moveTo((300, 600))
p.lineTo((350, 700))
p.lineTo((400, 600))
p.closePath()
g.width = 400

# !
g = font.createChar(ord('!'), '!')
p = g.glyphPen()
p.moveTo((325, 0))
p.lineTo((375, 0))
p.lineTo((375, 600))
p.lineTo((325, 600))
p.closePath()
p.moveTo((325, 700))
p.lineTo((375, 700))
p.lineTo((375, 750))
p.lineTo((325, 750))
p.closePath()
g.width = 400

# ?
g = font.createChar(ord('?'), '?')
p = g.glyphPen()
p.moveTo((350, 700))
p.curveTo((300, 750), (250, 700), (250, 650))
p.lineTo((250, 600))
p.lineTo((300, 550))
p.lineTo((350, 600))
p.lineTo((350, 650))
p.lineTo((300, 700))
p.closePath()
p.moveTo((325, 0))
p.lineTo((375, 0))
p.lineTo((375, 50))
p.lineTo((325, 50))
p.closePath()
g.width = 400

# フォント生成
font.generate("OtherworldAlt-Full.ttf")
print("✅ フォント生成完了: OtherworldAlt-Full.ttf")
