# -*- coding: utf-8

ports = [
("num[3..0]", "input", ur"Xifra a convertir (BCD)"),
("HEX[6..0]", "output", ur"Sortida pel display (set-segments, actiu baix)"),
]

description = ur'''
Converteix la xifra BCD donada en un patró per a un display set-segments actiu baix
que la representi adequadament.
'''

unspecs = ur'''
La sortida està inespecificada si $num$ no representa una xifra BCD vàlida.
'''

implementation = ur'''
Implementat a partir de la taula de veritat. Per conveniència, es força la sortida
$1111111$ (display apagat) per als valors inespecificats.
'''
