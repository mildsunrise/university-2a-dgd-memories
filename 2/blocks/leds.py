# -*- coding: utf-8

ports = [
("show", "input", ur"Senyal que s'activa si s'ha de mostrar el resultat"),
("LED_GREEN[3..0]", "output", ur"LEDs verds de la placa"),
("LED_RED[3..0]", "output", ur"LEDs vermells de la placa"),
]

description = ur'''
Mostra el valor del senyal $show$ als LEDs de la placa. S'activen els LEDs
verds si $show$ està actiu, en cas contrari s'activen els LEDs vermells.
'''
