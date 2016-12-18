# -*- coding: utf-8

ports = [
("ecnt", "input", ur"Habilitació del compte"),
("numx[7..0]", "output", ur"Nombre de sortida (BCD, dos xifres)"),
("clk", "input", ur"Rellotge, flanc de pujada"),
("nrst", "input", ur"Reset asíncron, actiu baix"),
]

timings = [
  {
    "scale": 1.1,
    "slices": [ (0,9), (52,9) ],
  }
]

simulation = ur'''
Ja que resultaria molt laboriós fer una simulació exhaustiva, agafem una mostra que ensenyi els canvis més significatius, que son els canvi de 9 a 0 de les unitats i el canvi de \texttt{0x99} a \texttt{0x00}. Per això hem agafat els nombres entre 85 i 11 del següent cicle. La sortida $numx$ es mostra en hexadecimal per simplicitat. També ens assegurem que el \emph{count enable} realitzi la seva funció.
'''
