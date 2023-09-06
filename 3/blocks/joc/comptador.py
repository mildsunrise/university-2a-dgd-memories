# -*- coding: utf-8

ports = [
("ecnt", "input", r"Habilitació del compte"),
("numx[7..0]", "output", r"Nombre de sortida (BCD, dos xifres)"),
("clk", "input", r"Rellotge, flanc de pujada"),
("nrst", "input", r"Reset asíncron, actiu baix"),
]

description = r'''
Comptador BCD de dues xifres (ascendent cíclic).

El valor BCD de la sortida, inicialitzada a zero, s'incrementa en cada cicle de rellotge que sempre que $ecnt = 1$.
Quan la sortida arriba al valor 99, en el següent cicle s'estableix a 0 i es segueix incrementant de la mateixa forma.
'''

timings = [
  {
    "scale": 1.1,
    "slices": [ (0,9), (52,9) ],
  }
]

implementation = r'''
En aquest cas hem optat per a fer servir el paquet \mintinline{vhdl}|numeric_std|, l'ús del qual
es recomana sobre \mintinline{vhdl}|std_logic_unsigned| i \mintinline{vhdl}|std_logic_signed|.

Per conveniència es defineixen dos senyals intermèdies de tipus \mintinline{vhdl}|unsigned|
de quatre bits, $n1$ i $n0$, on s'emmagatzemen les dues xifres del comptador.
Dins el \mintinline{vhdl}|process| es comprova el valor de $ecnt$ i s'incrementa $n0$ si
el seu valor és diferent a nou. En cas contari es posa a zero i s'incrementa $n1$ si el
seu valor és diferent a nou (sino, es posa també a zero).
'''

simulation = r'''
Ja que resultaria molt laboriós comprovar una simulació exhaustiva, agafem una mostra que ensenyi els canvis més significatius, que son els canvi de 9 a 0 de les unitats i el canvi de \texttt{0x99} a \texttt{0x00}. Per això hem agafat els nombres entre 85 i 11 del següent cicle. La sortida $numx$ es mostra en hexadecimal per simplicitat. També ens assegurem que el \emph{count enable} realitzi la seva funció.
'''
