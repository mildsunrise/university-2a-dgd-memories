# -*- coding: utf-8

ports = [
("sig", "input", ur"Signe a representar (1 $\rightarrow$ negatiu)"),
("ss[6..0]", "output", ur"Sortida pel display (set-segments, actiu baix)"),
]

description = ur'''
Representa el signe donat en un patró per a display set-segments actiu baix.
'''

implementation = ur'''
Tots els segments del display estan apagats, excepte el segment del mig, que
s'ilumina quan $sig = 1$. Per tant, com que son actius baixos, la sortida és
$(\overline{sig}, 1, 1, 1, 1, 1, 1)$.
'''
