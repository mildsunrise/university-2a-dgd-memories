# -*- coding: utf-8

ports = [
("a[7..0]", "input", ur"Primer factor"),
("b[7..0]", "input", ur"Segon factor"),
("z[7..0]", "output", ur"Producte"),
]

description = ur'''
Multiplicador de busos de 8~bits.

Multiplica els dos factors (en Ca2 o binari natural), i retorna els 8 bits de menor pes del resultat en la sortida $z$.
'''

implementation = ur'''
S'implementa mitjançant 8~blocs \textsf{MULT\_ACC} encadenant carry, cadascun multiplica $a$ per un bit de $b$ i retorna un bit a la sortida. El carry sortint
es descarta.
'''
