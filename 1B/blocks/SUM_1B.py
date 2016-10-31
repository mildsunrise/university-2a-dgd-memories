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

simulation = ur'''
Esperem que la sortida $s$ es comporti com una \textsf{XOR} per a $ci = 0$ i com una \textsf{XNOR} per a $Ci = 1$. També que $co$ sigui 1 quan existeixen almenys dos 1 a les entrades $a$, $b$ i $ci$.
'''
