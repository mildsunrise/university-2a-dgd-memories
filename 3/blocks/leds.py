# -*- coding: utf-8

ports = [
("comp[2..0]", "input", ur"Sortida per als indicadors de l'estat del joc"),
("LED_GREEN[7..0]", "output", ur"LEDs verds de la placa"),
]

unspecs = ur'''
La sortida no està definida si $comp$ no representa cap estat de joc conegut.
'''

simulation = ur'''
Comprovem que el patró de LEDs correspon amb l'entrada en tot moment.
'''
