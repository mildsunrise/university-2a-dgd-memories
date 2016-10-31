# -*- coding: utf-8

ports = [
("a[3..0]", "input", ur"Bus d'entrada 1"),
("b[3..0]", "input", ur"Bus d'entrada 0"),
("sel", "input", ur"Bit de selecció"),
("z[3..0]", "output", ur"Bus de sortida"),
]

description = ur'''
Multiplexor de 2 entrades per busos de 4~bits.

Estableix el bus de sortida $z$ al bus d'entrada $b$ si $sel = 0$,
o al bus de sortida $a$ si $sel = 1$.
'''

implementation = ur'''
Implementació feta fent servir quatre multiplexors 2:1 d'un bit,
un per a cada un dels quatre bits del bus.
'''

simulation = ur'''
Escollim que les entrades i la sortida siguin \textsf{unsigned\_decimal} ja que visualment es més sencill observar errors. Esperem que la sortida es comporti adecuadament.
'''

