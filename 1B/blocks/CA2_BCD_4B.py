# -*- coding: utf-8

ports = [
("x[3..0]", "input", ur"Entrada (Ca2)"),
("bcd[3..0]", "output", ur"Mòdul (binari natural)"),
]

description = ur'''
Extractor de mòdul de Ca2 de 4~bits.

Calcula el valor absolut de l'entrada i el retorna al
bus de sortida en binari natural (o en BCD, perquè la sortida és de 4~bits i
mai serà major que 9).

Nota: La sortida es diu $bcd$ per consistència amb el bloc \textsf{CA2\_BCD\_8B}.
'''

implementation = ur'''
Si $x_3 = 0$, l'entrada és positiva i per tant no cal fer cap operació, es
retorna directament.

Per contra, si $x_3 = 1$ llavors s'ha de convertir en positiva negant bit a bit
i sumant 1 al resultat. La primera part es pot fer amb una \textsf{XOR}, la segona
es pot fer entrant el resultat a un sumador, amb l'altra entrada nula i carry
d'entrada $x_3$. La sortida d'aquest sumador és el mòdul que busquem.
'''
