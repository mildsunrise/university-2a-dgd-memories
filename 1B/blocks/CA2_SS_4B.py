# -*- coding: utf-8

ports = [
("x[3..0]", "input", ur"Entrada (Ca2)"),
("hex0[6..0]", "output", ur"Primer display en ordre lèxic (set-segments actiu baix, signe)"),
("hex1[6..0]", "output", ur"Segon display en ordre lèxic (set-segments actiu baix, unitats)"),
]

description = ur'''
Formatejador de Ca2 4~bits en set-segments.

Donat un valor en complement a 2 de 4~bits, el representa en format signe --
mòdul decimal habitual en 2 displays set-segments $hex0$ i $hex1$.

Nota: Contràriament a la placa, les sortides set-segments estan numerades
en ordre lèxic ($hex0$ ha d'anar al display de l'esquerra).
'''

implementation = ur'''
En primer lloc, el signe $x_3$ es fa entrar al bloc \textsf{CA2\_SIG\_SS} i la
representació resultant es retorna a $hex0$. Llavors, s'utilitza el bloc
\textsf{CA2\_BCD\_4B} per a obtenir el mòdul de $x$. Aquest mòdul ja és una xifra
BCD vàlida, que es converteix a set-segments amb \textsf{BCD7seg} i es retorna a
$hex1$.
'''
