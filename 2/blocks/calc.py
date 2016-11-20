# -*- coding: utf-8

top_level = True

ports = [
("OSC_50", "input", ur"Rellotge a \SI{50}{\mega\hertz} intern"),
("KEY[0]", "input", ur"Tecla~0 de la placa (actiu baix)"),
("COL[3..0]", "input", ur"Pins de columna del teclat"),
("ROW[3..0]", "output", ur"Pins de fila del teclat"),
("LED_GREEN[7..0]", "output", ur"LEDs verds de la placa"),
("LED_RED[7..0]", "output", ur"LEDs vermells de la placa"),
("HEX7[6..0]", "output", ur"Display set-segments~7"),
("HEX6[6..0]", "output", ur"Display set-segments~6"),
("HEX5[6..0]", "output", ur"Display set-segments~5"),
("HEX4[6..0]", "output", ur"Display set-segments~4"),
("HEX3[6..0]", "output", ur"Display set-segments~3"),
("HEX2[6..0]", "output", ur"Display set-segments~2"),
("HEX1[6..0]", "output", ur"Display set-segments~1"),
("HEX0[6..0]", "output", ur"Display set-segments~0"),
]

description = ur'''
Disseny a carregar a la placa FPGA.

Implementa un multiplicador BCD, controlat pel teclat connectat a la placa.
Els dos factors es mostren a $HEX6$ i $HEX4$ respectivament, i el resultat
a $HEX1$ i $HEX0$.

El disseny es pot resetejar prement la tecla~0 de la placa.
'''
