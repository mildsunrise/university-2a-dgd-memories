# -*- coding: utf-8

ports = [
("show", "input", ur"Senyal que s'activa si s'ha de mostrar el resultat"),
("selop[1..0]", "input", ur"Índex d'operació que s'està efectuant"),
("LED_OP[3..0]", "output", ur"LEDs d'operació de la placa"),
("LED_GREEN[3..0]", "output", ur"LEDs verds de la placa"),
("LED_RED[3..0]", "output", ur"LEDs vermells de la placa"),
]

description = ur'''
Mostra el valor del senyal $show$ als LEDs de la placa. S'activen els LEDs
verds si $show$ està actiu, en cas contrari s'activen els LEDs vermells.

Addicionalment, s'activa el LED $LED\_OP_{3 - selop}$ per a indicar
la operació sel·leccionada.
'''

implementation = ur'''
Per a cada vector de LEDs, es retorna $0000$ o $1111$ depenent del valor
de $show$.
'''
