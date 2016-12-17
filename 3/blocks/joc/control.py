# -*- coding: utf-8

ports = [
("bcd", "input", ur"Senyal que s'activa si s'ha premut una xifra decimal"),
("ast", "input", ur"Senyal que s'activa si s'ha premut la tecla asterisc"),
("coi", "input", ur"Senyal que s'activa si s'ha premut la tecla coixinet"),
("ngtx", "input", ur"Indica que la solució és major que el nombre introduït (actiu baix)"),
("neqx", "input", ur"Indica que la solució és igual al nombre introduït (actiu baix)"),
("nltx", "input", ur"Indica que la solució és menor que el nombre introduït (actiu baix)"),
("eshft", "output", ur"Senyal que s'activa quan s'ha d'enregistrar la xifra premuda"),
("ecnt", "output", ur"Senyal que d'habilitació del comptador"),
("comp[2..0]", "output", ur"Sortida per als indicadors de l'estat del joc"),
("clk", "input", ur"Rellotge, flanc de pujada"),
("nrst", "input", ur"Reset asíncron, actiu baix"),
]

description = ur'''
% TODO
'''

unspecs = ur'''
El comportament del bloc no està definit si més d'una de les entrades $bcd, ast, coi$ està activa a la vegada.
El comportament del bloc no està definit si cap de les entrades $ngtx, neqx, nltx$ està activa, o més d'una ho està.
'''

implementation = ur'''
% TODO
'''
