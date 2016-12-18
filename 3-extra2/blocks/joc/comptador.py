# -*- coding: utf-8

ports = [
("ecnt", "input", ur"Habilitació del compte"),
("numx[11..0]", "output", ur"Nombre de sortida (BCD, tres xifres)"),
("clk", "input", ur"Rellotge, flanc de pujada"),
("nrst", "input", ur"Reset asíncron, actiu baix"),
]

description = ur'''
Comptador BCD de tres xifres (ascendent cíclic).

El valor BCD de la sortida, inicialitzada a zero, s'incrementa en cada cicle de rellotge que sempre que $ecnt = 1$.
Quan la sortida arriba al valor 999, en el següent cicle s'estableix a 0 i es segueix incrementant de la mateixa forma.
'''

implementation = ur'''
Com que el codi es feia engorrós per a tres xifres, hem decidit implementar-lo
encadenant tres comptadors d'una xifra (instàncies del bloc \textsf{comptador\_single}).

Per consistència, el \emph{tail count} no s'exporta.
'''

# TODO: simulation
