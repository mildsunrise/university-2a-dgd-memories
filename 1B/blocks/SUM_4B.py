# -*- coding: utf-8

ports = [
("A[3..0]", "input", ur"Bus d'entrada 1"),
("B[3..0]", "input", ur"Bus d'entrada 0"),
("S[3..0]", "output", ur"Bus de sortida"),
("CI", "input", ur"Carry d'entrada"),
("CO", "output", ur"Carry de sortida"),
]

description = ur'''
Sumador de 4~bits amb carry.

Suma els busos $A$ i $B$ amb el carry d'entrada $CI$ i retorna els 4 bits de menys
pes al bus de sortida $S$, i el bit restant al carry de sortida $CO$.
'''

implementation = ur'''
S'implementa mitjançant 4~sumadors de 1~bit (\textsf{SUM\_1B}) encadenant carry,
cadascun suma $A_i$ amb $B_i$ i es retorna la sortida en $S_i$.
'''
