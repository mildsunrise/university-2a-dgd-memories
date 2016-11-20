# -*- coding: utf-8

ports = [
("intro", "input", ur"Senyal que s'activa si s'ha d'emmagatzemar una xifra nova"),
("keycode[3..0]", "input", ur"Xifra que s'està introduint (BCD)"),
("opA[3..0]", "output", ur"Primera xifra desada (BCD)"),
("opB[3..0]", "output", ur"Segona xifra desada (BCD)"),
("clk", "input", ur"Rellotge, flanc de pujada"),
("nrst", "input", ur"Reset asíncron, actiu baix"),
]

description = ur'''
Registres per als factors.

Emmagatzema les xifres premudes en dos registres per a $opA$ i $opB$.
Inicialment ambdós son zero; quan $intro$ és actiu, la xifra a l'entrada $keycode$
s'emmagatzema a $opA$ i el valor anterior de $opA$ s'emmagatzema a $opB$.
'''

implementation = ur'''
Dos biestables D amb habilitació de càrrega encadenats, de forma similar a un \emph{shift
register}. Les sortides dels biestables es retornen en ordre a $opA$ i $opB$.
'''
