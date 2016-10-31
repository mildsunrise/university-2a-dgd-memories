# -*- coding: utf-8

ports = [
("CA2[7..0]", "input", ur"Entrada (Ca2)"),
("BCD[7..0]", "output", ur"Mòdul (BCD)"),
]

description = ur'''
Extractor de mòdul de Ca2 de 8~bits.

Calcula el valor absolut de l'entrada, \emph{que ha d'estar en el rang
$\left[-56, 64\right]$}, i el retorna al bus de sortida en BCD de dues xifres.
'''

unspecs = ur'''
La sortida no està definida si $CA2$ està fora del rang $\left[-56, 64\right]$.
'''

implementation = ur'''
Implementat mitjançant la taula de veritat.
'''
