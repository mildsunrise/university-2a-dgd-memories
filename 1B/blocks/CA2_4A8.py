# -*- coding: utf-8

ports = [
("a[3..0]", "input", ur"Entrada (Ca2 4~bits)"),
("z[7..0]", "output", ur"Sortida (Ca2 8~bits)"),
]

description = ur'''
Canviador de mida del codi, de Ca2 4~bits a Ca2 8~bits.

Expressa el valor de l'entrada (complement a 2 amb 4~bits) en el codi
de sortida (complement a 2 amb 8~bits).
'''

implementation = ur'''
Només cal fer una extensió de signe; l'entrada es copia directament als 4~bits
de menys pes de la sortida, i els 4~bits restants s'emplenen amb el signe (o sigui,
$a_3$).
'''
