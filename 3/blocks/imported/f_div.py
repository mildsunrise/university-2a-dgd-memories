# -*- coding: utf-8

ports = [
("clkin", "input", r"Rellotge d'entrada, flanc de pujada"),
("clkout", "output", r"Rellotge de sortida, flanc de pujada"),
("nrst", "input", r"Reset asíncron, actiu baix"),
]

description = r'''
Divisor de freqüència per 65536.

Genera a $clkout$ un rellotge de freqüència $f_s / 65536$, on $f_s$
és la freqüència del rellotge d'entrada $clkin$.
'''
