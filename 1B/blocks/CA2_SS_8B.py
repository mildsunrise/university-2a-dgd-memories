# -*- coding: utf-8

ports = [
("x[7..0]", "input", ur"Entrada (Ca2)"),
("hex0[6..0]", "output", ur"Primer display en ordre lèxic (set-segments actiu baix, signe)"),
("hex1[6..0]", "output", ur"Segon display en ordre lèxic (set-segments actiu baix, desenes)"),
("hex2[6..0]", "output", ur"Tercer display en ordre lèxic (set-segments actiu baix, unitats)"),
]

description = ur'''
Formatejador de Ca2 8~bits en set-segments.

Donat un valor en complement a 2 de 8~bits, el representa en format signe --
mòdul decimal habitual en 3 displays set-segments $hex0$, $hex1$ i $hex2$.

Nota: Els displays estan numerats en ordre lèxic ($hex0$ és el de l'esquerra).
'''

unspecs = ur'''
A causa de \textsf{CA2\_BCD\_8B}, les sortides $hex1$ i $hex2$ són indefinides
quan $x$ està fora del rang $\left[-56, 64\right]$.
'''

implementation = ur'''
En primer lloc, el signe $x_3$ es fa entrar al bloc \textsf{CA2\_SIG\_SS} i la
representació resultant es retorna a $hex0$. Llavors, s'utilitza el bloc
\textsf{CA2\_BCD\_8B} per a obtenir el mòdul de $x$ en BCD. Cada una de les dues
xifres del mòdul es converteix a set-segments i es retorna a $hex1$ i $hex2$
respectivament.
'''
