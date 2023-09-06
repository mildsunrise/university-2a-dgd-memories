# -*- coding: utf-8

ports = [
("row[3..0]", "output", r"Pins de fila del teclat"),
("col[3..0]", "input", r"Pins de columna del teclat"),
("nkey", "output", r"Senyal que s'activa si s'ha premut una tecla (actiu baix)"),
("keycode[3..0]", "output", r"Índex de la tecla que s'ha premut"),
("clk", "input", r"Rellotge, flanc de pujada"),
("nrst", "input", r"Reset asíncron, actiu baix"),
]

description = r'''
Escàner de pulsacions en un \emph{crossbar switch} de 4 per 4.

Sondeja la matriu de tecles i activa la sortida $nkey$ quan una tecla es pulsa
(la sortida es desactiva en el següent cicle de rellotge encara que la tecla
segueixi premuda). La sortida $keycode$ indica l'index de la tecla.
'''
