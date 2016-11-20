# -*- coding: utf-8

ports = [
("clkin", "input", ur"Rellotge d'entrada, flanc de pujada"),
("clkout", "output", ur"Rellotge de sortida, flanc de pujada"),
("nrst", "input", ur"Reset asíncron, actiu baix"),
]

description = ur'''
Divisor de freqüència per 65536.

Genera a $clkout$ un rellotge de freqüència $f_s / 65536$, on $f_s$
és la freqüència del rellotge d'entrada $clkin$.
'''
