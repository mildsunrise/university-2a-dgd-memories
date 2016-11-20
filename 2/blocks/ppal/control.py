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

implementation = ur'''
Es tracta d'una màquina de Mealy amb diagrama d'estats:

% TODO

Quan arriba el flanc de rellotge, es força l'estat \mintinline{vhdl}|st_show| si $ast$ és
actiu, o l'estat \mintinline{vhdl}|st_intro| si $coi$ és actiu.

La sortida $show$ indica l'estat actual de la màquina, i la sortida $intro$ és activa
només quan $bcd$ és activa i ens trobem en l'estat \mintinline{vhdl}|st_intro|.
'''
