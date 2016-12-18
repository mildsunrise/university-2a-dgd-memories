# -*- coding: utf-8

ports = [
("eshft", "input", ur"Habilitació d'emmagatzemament"),
("keycode[3..0]", "input", ur"Xifra que s'està introduint (BCD)"),
("num[11..0]", "output", ur"Nombre enmagatzemat (BCD, tres xifres)"),
("clk", "input", ur"Rellotge, flanc de pujada"),
("nrst", "input", ur"Reset asíncron, actiu baix"),
]

description = ur'''
\emph{Shift register} per a tres xifres BCD.

Emmagatzema un nombre BCD de tres xifres, memoritzant les tres últimes
xifres carregades. Quan s'habilita la càrrega ($eshft = 1$), la xifra
BCD present a $keycode$ esdevé la xifra de menys pes del nombre
emmagatzemat; les xifres existents es mouen cap a l'esquerra, descartant
la de més pes.
'''

unspecs = ur'''
La sortida no pertanyirà al seu codi si es carrega una xifra no BCD.
'''

implementation = ur'''
Implementació senzilla, s'utilitzen tres senyals intermèdies $c$, $b$ i $a$,
per desar cada xifra. En el \mintinline{vhdl}|process| s'assignen condicionalment a $b$, $a$
i $keycode$ respectivament, i fora d'aquest es concatenen per formar la sortida.
'''

simulation = ur'''
Comprovem que els registres emmagatzemen les xifres en l'ordre correcte.
'''
