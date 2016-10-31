# -*- coding: utf-8

ports = [
("a[7..0]", "input", ur"Primer factor"),
("b", "input", ur"Segon factor"),
("z[7..0]", "output", ur"Producte"),
]

description = ur'''
Multiplicador de 8~bits per 1~bit.

Multiplica els primer factor, de 8~bits, pel segon factor d'un bit i retorna el resultat a la sortida.
'''

implementation = ur'''
Si $b = 0$, sabem que el resultat és $00000000$. Però si $b = 1$, la sortida és
idèntica a $a$. Per tant, només cal aplicar un AND entre cada bit de $a$ i el
bit $b$.
'''
