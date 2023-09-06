# -*- coding: utf-8

ports = [
("num[3..0]", "input", r"Xifra a convertir (BCD)"),
("HEX[6..0]", "output", r"Sortida pel display (set-segments, actiu baix)"),
]

description = r'''
Converteix la xifra BCD donada en un patró per a un display set-segments actiu baix
que la representi adequadament.
'''

unspecs = r'''
La sortida està inespecificada si $num$ no representa una xifra BCD vàlida.
'''

implementation = r'''
Implementat a partir de la taula de veritat. Per conveniència, es força la sortida
$1111111$ (display apagat) per als valors inespecificats.
'''
