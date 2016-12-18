# -*- coding: utf-8

ports = [
("bcd", "input", ur"Senyal que s'activa si s'ha premut una xifra decimal"),
("ast", "input", ur"Senyal que s'activa si s'ha premut la tecla asterisc"),
("coi", "input", ur"Senyal que s'activa si s'ha premut la tecla coixinet"),
("ngtx", "input", ur"Indica que el nombre introduït és major que la solució (actiu baix)"),
("neqx", "input", ur"Indica que el nombre introduït coincideix amb la solució (actiu baix)"),
("nltx", "input", ur"Indica que el nombre introduït és menor que la solució (actiu baix)"),
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

simulation = ur'''
En aquesta simulació comprovem que les sortides es comporten correctament. Ens basem en una situació real que es donaria en el joc (p.e. no posariem les sortides $ngtx$, $netx$ o $nltx$ alhora).
'''
