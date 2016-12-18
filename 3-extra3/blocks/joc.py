# -*- coding: utf-8

ports = [
("nkey", "input", ur"Senyal que s'activa si s'ha premut una tecla (actiu baix)"),
("keycode[3..0]", "input", ur"Índex de la tecla que s'ha premut"),
("comp[2..0]", "output", ur"Sortida per als indicadors de l'estat del joc"),
("num[11..0]", "output", ur"Sortida pels displays (BCD)"),
("clk", "input", ur"Rellotge, flanc de pujada"),
("nrst", "input", ur"Reset asíncron, actiu baix"),
]

description = ur'''
Implementa la funcionalitat del joc.

Inicialment, el joc es troba en estat de repós. Quan l'usuari prem \texttt{\#},
el joc genera internament un nombre (suposadament aleatori) i comença la partida.
L'usuari prem els dígits per a introduir un nombre als visualitzadors. Quan es prem \texttt{*},
el joc compara el nombre introduït amb la solució, i mostra el resultat de la comparació
a l'usuari. Si el nombre introduït coincidia amb la solució, la partida es finalitza
i es torna a l'estat de repós.

A més, mentre hi ha una partida iniciada, l'usuari pot premer una lletra; llavors
el teclat es bloqueja i es visualitza la solució en comptes del nombre introduït. Quan
es torna a premer una lletra, es visualitza el nombre anterior i la partida continua
com abans. És possible premer \texttt{\#} per reiniciar mentre s'està visualitzant
la solució.
'''

implementation = ur'''
La implementació és la mateixa que en la secció anterior, però ara \textsf{keygroup} té
una sortida més que es porta a l'entrada corresponent de \textsf{control}. Aquest bloc
també té una sortida nova, $show$.

Quan aquest senyal és actiu, la sortida $num$ no s'assigna a la sortida de \textsf{registres}
sino a la de \textsf{comptador}, per tal de visualitzar la solució del joc.
'''

timings = [
  {
    "scale": .7,
    "force": True,
    "slices": [(0,16)],
  }
]

simulation = ur'''
Introduint comandes simulant una partida real del joc. En aquest cas ens centrem que el funcionament de la trampa sigui el correcte.
'''
