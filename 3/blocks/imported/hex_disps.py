# -*- coding: utf-8

ports = [
("num7[3..0]", "input", r"Xifra a mostrar al display~7 (BCD)"),
("num6[3..0]", "input", r"Xifra a mostrar al display~6 (BCD)"),
("num5[3..0]", "input", r"Xifra a mostrar al display~5 (BCD)"),
("num4[3..0]", "input", r"Xifra a mostrar al display~4 (BCD)"),
("num3[3..0]", "input", r"Xifra a mostrar al display~3 (BCD)"),
("num2[3..0]", "input", r"Xifra a mostrar al display~2 (BCD)"),
("num1[3..0]", "input", r"Xifra a mostrar al display~1 (BCD)"),
("num0[3..0]", "input", r"Xifra a mostrar al display~0 (BCD)"),
("HEX7[6..0]", "output", r"Sortida per al display~7 (set-segments)"),
("HEX6[6..0]", "output", r"Sortida per al display~6 (set-segments)"),
("HEX5[6..0]", "output", r"Sortida per al display~5 (set-segments)"),
("HEX4[6..0]", "output", r"Sortida per al display~4 (set-segments)"),
("HEX3[6..0]", "output", r"Sortida per al display~3 (set-segments)"),
("HEX2[6..0]", "output", r"Sortida per al display~2 (set-segments)"),
("HEX1[6..0]", "output", r"Sortida per al display~1 (set-segments)"),
("HEX0[6..0]", "output", r"Sortida per al display~0 (set-segments)"),
]

description = r'''
Converteix les xifres d'entrada a set-segments per a cada display de la placa.
'''

implementation = r'''
Es fa servir una instància de \textsf{BCD7seg} per convertir cada $num_i$ a
set-segments, i es retorna a $HEX_i$.
'''
