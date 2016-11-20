# -*- coding: utf-8

ports = [
("CA2[7..0]", "input", ur"Entrada (Ca2)"),
("BCD[7..0]", "output", ur"Mòdul (BCD)"),
]

description = ur'''
Extractor de mòdul de Ca2 de 8~bits.

Calcula el valor absolut de l'entrada, i el retorna al bus de sortida en BCD de dues xifres.
'''

unspecs = ur'''
La sortida no està definida si el valor de l'entrada no és producte de dos
enters en el rang $\left[0, 9\right]$, o bé suma de dos enters en el rang
$\left[-9, 9\right]$.
'''

implementation = ur'''
Implementat mitjançant la taula de veritat.
'''

# TODO
