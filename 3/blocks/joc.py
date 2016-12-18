# -*- coding: utf-8

ports = [
("nkey", "input", ur"Senyal que s'activa si s'ha premut una tecla (actiu baix)"),
("keycode[3..0]", "input", ur"Índex de la tecla que s'ha premut"),
("comp[2..0]", "output", ur"Sortida per als indicadors de l'estat del joc"),
("num[7..0]", "output", ur"Sortida pels displays (BCD)"),
("clk", "input", ur"Rellotge, flanc de pujada"),
("nrst", "input", ur"Reset asíncron, actiu baix"),
]

description = ur'''
% TODO
'''

implementation = ur'''
% TODO
'''

simulation = ur'''
Seria bastant complicat simular una partida real sencera del joc en una simulació així que hem agafat un valor molt alt i un altre molt baix per a comprovar que el bloc funciona com l'hem descrit.
'''
