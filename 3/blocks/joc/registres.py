# -*- coding: utf-8

ports = [
("eshft", "input", r"Habilitació d'emmagatzemament"),
("keycode[3..0]", "input", r"Xifra que s'està introduint (BCD)"),
("num[7..0]", "output", r"Nombre enmagatzemat (BCD, dos xifres)"),
("clk", "input", r"Rellotge, flanc de pujada"),
("nrst", "input", r"Reset asíncron, actiu baix"),
]

description = r'''
\emph{Shift register} per a dues xifres BCD.

Emmagatzema un nombre BCD de dues xifres, memoritzant les dues últimes
xifres carregades. Quan s'habilita la càrrega ($eshft = 1$), la xifra
BCD present a $keycode$ esdevé la xifra de menys pes del nombre
emmagatzemat; la xifra anterior esdevé la de més pes, i aquesta es descarta.
'''

unspecs = r'''
La sortida no pertanyirà al seu codi si es carrega una xifra no BCD.
'''

implementation = r'''
Dos biestables D amb habilitació de càrrega encadenats, de forma similar a un \emph{shift
register} però on les sortides es concatenen per formar la sortida $num$.
'''
