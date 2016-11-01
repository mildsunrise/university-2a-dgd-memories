# -*- coding: utf-8

top_level = True

ports = [
("SW[17..14]", "input", ur"Switches on s'introdueix el primer factor en Ca2"),
("SW[13..10]", "input", ur"Switches on s'introdueix el segon factor en Ca2"),
("SW[9..8]", "input", ur"Switches on s'introdueix la operació a realitzar"),
("HEX7[6..0]", "output", ur"Display set-segments 7"),
("HEX6[6..0]", "output", ur"Display set-segments 6"),
("HEX5[6..0]", "output", ur"Display set-segments 5"),
("HEX4[6..0]", "output", ur"Display set-segments 4"),
("HEX3[6..0]", "output", ur"Display set-segments 3"),
("HEX2[6..0]", "output", ur"Display set-segments 2"),
("HEX1[6..0]", "output", ur"Display set-segments 1"),
("HEX0[6..0]", "output", ur"Display set-segments 0"),
("LED_RED[6]", "output", ur"LED d'alarma"),
]

description = ur'''
Disseny a carregar a la placa FPGA.

Visualitza els dos factors en format signe -- modul habitual, en els displays
7--6 i 5--4 respectivament. Executa la operació demanada pels bits $SW_{9..8}$ amb
els dos factors introduïts, i mostra el resultat als displays 2--0. El display
restant està sempre apagat.

$LED\_RED_6$ s'encén quan s'activa el bit d'alarma de la calculadora.
'''

implementation = ur'''
Ambdues entrades, i els switches de selecció es porten al bloc \textsf{Calculadora}.

Finalment, les entrades es porten també a blocs \textsf{CA2\_SS\_4B} i llavors
als displays corresponents. La sortida es porta a un bloc \textsf{CA2\_SS\_8B}
i als displays corresponents. El bit d'alarma ($r$) es porta a $LED\_RED_6$.
'''
