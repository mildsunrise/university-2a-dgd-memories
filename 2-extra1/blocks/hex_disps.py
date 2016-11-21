# -*- coding: utf-8

ports = [
("sigA", "input", ur"Signe del primer factor"),
("opA[3..0]", "input", ur"Mòdul del primer factor (BCD)"),
("sigB", "input", ur"Signe del segon factor"),
("opB[3..0]", "input", ur"Mòdul del segon factor (BCD)"),
("sigRes", "input", ur"Signe del resultat"),
("res[7..0]", "input", ur"Mòdul del resultat (BCD$^\dagger$)"),
("HEX7[6..0]", "output", ur"Sortida per al display~7 (set-segments)"),
("HEX6[6..0]", "output", ur"Sortida per al display~6 (set-segments)"),
("HEX5[6..0]", "output", ur"Sortida per al display~5 (set-segments)"),
("HEX4[6..0]", "output", ur"Sortida per al display~4 (set-segments)"),
("HEX3[6..0]", "output", ur"Sortida per al display~3 (set-segments)"),
("HEX2[6..0]", "output", ur"Sortida per al display~2 (set-segments)"),
("HEX1[6..0]", "output", ur"Sortida per al display~1 (set-segments)"),
("HEX0[6..0]", "output", ur"Sortida per al display~0 (set-segments)"),
]

description = ur'''
Converteix signe i mòdul dels factors i resultat a set-segments,
i els enruta als displays adequats de la placa.
'''

implementation = ur'''
Es fan servir instàncies de \textsf{BCD7seg} per convertir $opA$, $opB$
i les dues xifres de $res$ a set-segments. També s'utilizen instàncies
de \textsf{CA2\_SIG\_SS} per a convertir els tres signes a set-segments.

Finalment, s'assigna cada sortida set-segments al display adequat.
'''
