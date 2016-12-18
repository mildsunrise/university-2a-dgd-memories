# -*- coding: utf-8

ports = [
("ecnt", "input", ur"Habilitació del compte"),
("numx[3..0]", "output", ur"Nombre de sortida (BCD)"),
("tc", "output", ur"Sortida \emph{tail count}"),
("clk", "input", ur"Rellotge, flanc de pujada"),
("nrst", "input", ur"Reset asíncron, actiu baix"),
]

description = ur'''
Comptador BCD d'una xifra (ascendent cíclic).

El valor BCD de la sortida, inicialitzada a zero, s'incrementa en cada cicle de rellotge que sempre que $ecnt = 1$.
Quan la sortida arriba al valor 9, en el següent cicle s'estableix a 0 i es segueix incrementant de la mateixa forma.

La sortida $tc$ s'usa per encadenar comptadors.
'''

implementation = ur'''
Com en el comptador anterior, es fa servir el paquet \mintinline{vhdl}|numeric_std| i es defineix una senyal intermèdia
$n$ de tipus \mintinline{vhdl}|unsigned| de 4~bits. S'inicialitza en 0, i en arribar el flanc de rellotge i si $ecnt = 1$,
s'incrementa (si el seu valor és diferent de 9) o es reinicialitza a zero (cas contrari).

La senyal intermèdia es converteix a vector lògic i s'assigna a la sortida $numx$.
S'activa $tc$ si $ecnt = 1$ i la senyal intermèdia té el valor 9.
'''

timings = [
  {
    "scale": .7,
    "slices": [(0,14)],
    "force": True,
  }
]

# TODO: simulation
