# -*- coding: utf-8

ports = [
("A[7..0]", "input", ur"Bus d'entrada 1"),
("B[7..0]", "input", ur"Bus d'entrada 0"),
("S[7..0]", "output", ur"Bus de sortida"),
("CI", "input", ur"Carry d'entrada"),
("CO", "output", ur"Carry de sortida"),
]

description = ur'''
Sumador de 8~bits amb carry.

Suma els busos $A$ i $B$ amb el carry d'entrada $CI$ i retorna els 8 bits de menys
pes al bus de sortida $S$, i el bit restant al carry de sortida $CO$.
'''

implementation = ur'''
S'implementa mitjançant 8~sumadors de 1~bit (\textsf{SUM\_1B}) encadenant carry,
cadascun suma $A_i$ amb $B_i$ i es retorna la sortida en $S_i$.
'''

simulation = ur'''
Per a fer la simulació hem optat per agafar com a format dels busos d'entrada i sortida \textsf{unsigned\_decimal}, ja que ens ha semblat el format més còmode per identificar possibles errors. Esperem que $S$ ens doni el valor de la suma $A+B+CI$ si el resultat es troba dins de rang ($A+B < 256$) i $\left(A+B\right)-256$ quan la suma surti de rang, i que $CO$ s'activi quan pertoqui.
'''
