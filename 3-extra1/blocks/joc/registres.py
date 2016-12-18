# -*- coding: utf-8

ports = [
("eshft", "input", ur"Habilitació d'emmagatzemament"),
("keycode[3..0]", "input", ur"Xifra que s'està introduint (BCD)"),
("num[7..0]", "output", ur"Nombre enmagatzemat (BCD, dos xifres)"),
("clk", "input", ur"Rellotge, flanc de pujada"),
("nrst", "input", ur"Reset asíncron, actiu baix"),
]

description = ur'''
\emph{Shift register} per a dues xifres BCD.

Emmagatzema un nombre BCD de dues xifres, memoritzant les dues últimes
xifres carregades. Quan s'habilita la càrrega ($eshft = 1$), la xifra
BCD present a $keycode$ esdevé la xifra de menys pes del nombre
emmagatzemat; la xifra anterior esdevé la de més pes, i aquesta es descarta.
'''

unspecs = ur'''
La sortida no pertanyirà al seu codi si es carrega una xifra no BCD.
'''

implementation = ur'''
Implementació senzilla, s'utilitzen dues senyals intermèdies $a$ i $b$
per desar les dues xifres. En el \mintinline{vhdl}|process| s'assignen condicionalment a $a$
i $keycode$ respectivament, i fora d'aquest es concatenen per formar la sortida.
'''

timings = []

notes = [ur''' 
La simulació d'aquest bloc no s'inclou ja que és idèntica a la anterior (llevat espuris,
el comportament no ha canviat).
''']

