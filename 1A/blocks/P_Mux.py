# -*- coding: utf-8

top_level = True

ports = [
("SW[17..14]", "input", ur"Switches on s'introdueix la segona xifra BCD"),
("SW[13..10]", "input", ur"Switches on s'introdueix la primera xifra BCD"),
("SW[0]", "input", ur"Switch on s'introdueix el bit de selecció"),
("HEX6[6..0]", "output", ur"Display set-segments 6"),
("HEX4[6..0]", "output", ur"Display set-segments 4"),
("HEX0[6..0]", "output", ur"Display set-segments 0"),
]

description = ur'''
Disseny a carregar a la placa FPGA.

Visualitza la primera entrada i la segona entrada (en BCD) als displays~4 i 6,
respectivament. Si $SW_0$ està desactivat, visualitza la primera entrada al
display~0; si està activat, visualitza la segona entrada al display~0.
'''

unspecs = ur'''
La sortida està inespecificada si $SW_{17..4}$ o bé $SW_{13..10}$ no tenen valors
vàlids en BCD.
'''

implementation = ur'''
La primera entrada es porta cap al primer conversor BCD a set-segments, i cap a l'entrada 0 d'un multiplexor 2:1. La segona entrada es porta a un segon conversor set-segments, i a l'entrada 1 del multiplexor.

Finalment, la sortida del multiplexor es porta a un tercer conversor BCD a set-segments. Les sortides dels tres conversors es porten als displays 4, 6 i 0 respectivament.
'''
