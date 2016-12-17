# -*- coding: utf-8

top_level = True

ports = [
("OSC_50", "input", ur"Rellotge a \SI{50}{\mega\hertz} intern"),
("KEY[0]", "input", ur"Tecla~0 de la placa (actiu baix)"),
("COL[3..0]", "input", ur"Pins de columna del teclat"),
("ROW[3..0]", "output", ur"Pins de fila del teclat"),
("LED_GREEN[7..0]", "output", ur"LEDs verds de la placa"),
("HEX7[6..0]", "output", ur"Display set-segments~7"),
("HEX6[6..0]", "output", ur"Display set-segments~6"),
("HEX5[6..0]", "output", ur"Display set-segments~5"),
("HEX4[6..0]", "output", ur"Display set-segments~4"),
("HEX3[6..0]", "output", ur"Display set-segments~3"),
("HEX2[6..0]", "output", ur"Display set-segments~2"),
("HEX1[6..0]", "output", ur"Display set-segments~1"),
("HEX0[6..0]", "output", ur"Display set-segments~0"),
# TODO: verify
]

description = ur'''
Disseny a carregar a la placa FPGA.

% TODO
'''

implementation = ur'''
% TODO

En primer lloc, es fa servir \textsf{f\_div} per a obtenir un rellotge de més
baixa freqüència, que assignarem a $clk$ i es farà servir en la resta del disseny.
La tecla~0 de la placa es porta a $nrst$ i també es farà servir com a reset del disseny.

Llavors, es fa servir el bloc \textsf{keytest} per a escanejar el teclat i
s'obtenen els senyals $nkey$ i $keycode$. 

Es porta tot al bloc \textsf{ppal} que és on s'efectua tot el treball. Aquest bloc
exposa com a sortides el mode actual en que es troba ($show$), els factors ($opA$ i $opB$)
i el resultat $res$.

Els LEDs estan controlats per una instància de \textsf{leds} on portem $show$.
Els displays estan controlats per una instància de \textsf{hex\_disps} on portem els factors
(entrades 6 i 4 respectivament) i el resultat (entrades 1, 0). La resta d'entrades es
forcen a 1111 per a apagar els displays.
'''
