# -*- coding: utf-8

ports = [
("a", "input", ur"Entrada 1"),
("b", "input", ur"Entrada 0"),
("s", "output", ur"Sortida"),
("ci", "input", ur"Carry d'entrada"),
("co", "output", ur"Carry de sortida"),
]

description = ur'''
Sumador de 1~bit amb carry.

Suma $a + b + ci$ i retorna el bit de menys pes a la sortida $s$, i el bit restant
al carry de sortida $co$.
'''

implementation = ur'''
'''
