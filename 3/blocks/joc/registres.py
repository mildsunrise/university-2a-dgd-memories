# -*- coding: utf-8

ports = [
("eshft", "input", ur"Habilitació d'emmagatzemament"),
("keycode[3..0]", "input", ur"Xifra que s'està introduint (BCD)"),
("num[7..0]", "output", ur"Nombre enmagatzemat (BCD, dos xifres)"),
("clk", "input", ur"Rellotge, flanc de pujada"),
("nrst", "input", ur"Reset asíncron, actiu baix"),
]

description = ur'''
% TODO
'''

implementation = ur'''
% TODO
Dos biestables D amb habilitació de càrrega encadenats, de forma similar a un \emph{shift
register}. Les sortides dels biestables es retornen en ordre a $opA$ i $opB$.
'''
