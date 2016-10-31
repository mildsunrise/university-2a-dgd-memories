# -*- coding: utf-8

top_level = True

ports = [
("SW[17..14]", "input", ur"Switches on s'introdueix el primer factor en Ca2"),
("SW[13..10]", "input", ur"Switches on s'introdueix el segon factor en Ca2"),
("HEX7[6..0]", "output", ur"Display set-segments 7"),
("HEX6[6..0]", "output", ur"Display set-segments 6"),
("HEX5[6..0]", "output", ur"Display set-segments 5"),
("HEX4[6..0]", "output", ur"Display set-segments 4"),
("HEX3[6..0]", "output", ur"Display set-segments 3"),
("HEX2[6..0]", "output", ur"Display set-segments 2"),
("HEX1[6..0]", "output", ur"Display set-segments 1"),
("HEX0[6..0]", "output", ur"Display set-segments 0"),
]

description = ur'''
Disseny a carregar a la placa FPGA.

Visualitza els dos factors en format signe -- modul habitual, en els displays
7--6 i 5--4 respectivament. Multiplica els dos factors i visualitza el resultat
amb la mateixa representació, en els displays 2--0. El display restant està
sempre apagat.
'''

implementation = ur'''
Ambdues entrades es porten cap a blocs \textsf{CA2\_4A8} per a convertir-les a
Ca2 abans d'operar. Llavors, es fan entrar a un bloc \textsf{MULT\_8x8}.

Finalment, les entrades es porten també a blocs \textsf{CA2\_SS\_4B} i llavors
als displays corresponents. La sortida es porta a un bloc \textsf{CA2\_SS\_8B}
i als displays corresponents.
'''
