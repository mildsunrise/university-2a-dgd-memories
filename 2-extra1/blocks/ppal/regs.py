# -*- coding: utf-8

ports = [
("intro", "input", ur"Senyal que s'activa si s'ha d'emmagatzemar una xifra nova"),
("negar", "input", ur"Senyal que s'activa quan s'ha de negar el factor A"),
("keycode[3..0]", "input", ur"Xifra que s'està introduint (BCD)"),
("sigA", "output", ur"Primer signe desat"),
("opA[3..0]", "output", ur"Primera xifra desada (BCD)"),
("sigB", "output", ur"Segon signe desat"),
("opB[3..0]", "output", ur"Segona xifra desada (BCD)"),
("clk", "input", ur"Rellotge, flanc de pujada"),
("nrst", "input", ur"Reset asíncron, actiu baix"),
]

description = ur'''
Registres per als factors.

Emmagatzema les xifres premudes en dos registres per a $opA$ i $opB$.
També emmagatzema els dos signes per a cada factor, que es transfereixen en sèrie
igual que $opA$ i $opB$.

Inicialment ambdós son zero i positius; quan $intro$ és actiu, la xifra a l'entrada $keycode$
s'emmagatzema a $opA$ i el valor anterior de $opA$ s'emmagatzema a $opB$; $sigA$ s'emmagatzema
a $sigB$ i $sigA$ s'estableix a 0 (positiu).

Quan $negar$ és actiu, el signe de l'últim factor introduït (A) es nega.
'''

unspecs = ur'''
El comportament del bloc no està definit si $negar = intro = 1$.
'''

implementation = ur'''
Per als mòduls, dos biestables D amb habilitació de càrrega encadenats, de forma
similar a un \emph{shift register}. Les sortides dels biestables es retornen en
ordre a $opA$ i $opB$.

Per als signes, la disposició és molt similar (dos biestables D amb habilitació
de carrega encadenats) excepte que el primer biestable s'ha sustituit per un JK,
ja que el signe no prové de cap senyal sino que s'ha de generar. Si $negar$ està
actiu, es fa un \emph{toggle} activant $J$ i $K$. Si $intro$ està actiu, el nou
signe sempre és positiu (0) i per tant es força només $K$.
'''
