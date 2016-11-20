# -*- coding: utf-8

ports = [
("bcd", "input", ur"Senyal que s'activa si s'ha premut una xifra decimal"),
("ast", "input", ur"Senyal que s'activa si s'ha premut la tecla asterisc"),
("coi", "input", ur"Senyal que s'activa si s'ha premut la tecla coixinet"),
("intro", "output", ur"Senyal que s'activa si s'ha d'emmagatzemar una xifra nova"),
("show", "output", ur"Senyal que s'activa si s'ha de mostrar el resultat"),
("clk", "input", ur"Rellotge, flanc de pujada"),
("nrst", "input", ur"Reset asíncron, actiu baix"),
]

description = ur'''
Bloc de control d'estat per al multiplicador.

El senyal $show$ indica si el multiplicador està en mode visualització o introducció,
i el senyal $intro$ s'activa quan el multiplicador està en mode introducció i l'usuari
prem una xifra decimal.
'''

unspecs = ur'''
El comportament del bloc no està definit si més d'una entrada està activa a la vegada.
'''
