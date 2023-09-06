# -*- coding: utf-8

top_level = True

ports = [
("OSC_50", "input", r"Rellotge a \SI{50}{\mega\hertz} intern"),
("KEY[0]", "input", r"Tecla~0 de la placa (actiu baix)"),
("COL[3..0]", "input", r"Pins de columna del teclat"),
("ROW[3..0]", "output", r"Pins de fila del teclat"),
("LED_GREEN[7..0]", "output", r"LEDs verds de la placa"),
("HEX7[6..0]", "output", r"Display set-segments~7"),
("HEX6[6..0]", "output", r"Display set-segments~6"),
("HEX5[6..0]", "output", r"Display set-segments~5"),
("HEX4[6..0]", "output", r"Display set-segments~4"),
("HEX3[6..0]", "output", r"Display set-segments~3"),
("HEX2[6..0]", "output", r"Display set-segments~2"),
("HEX1[6..0]", "output", r"Display set-segments~1"),
("HEX0[6..0]", "output", r"Display set-segments~0"),
]

description = r'''
Disseny a carregar a la placa FPGA.

Adapta el bloc principal, \textsf{joc}, al rellotge, reset, teclat, displays i LEDs
de la placa FPGA.
'''

implementation = r'''
En primer lloc, es fa servir \textsf{f\_div} per a obtenir un rellotge de més
baixa freqüència, que assignarem a $clk$ i es farà servir en la resta del disseny.
La tecla~0 de la placa es porta a $nrst$ i també es farà servir com a reset del disseny.

Llavors, es fa servir el bloc \textsf{keytest} per a escanejar el teclat i
s'obtenen els senyals $nkey$ i $keycode$.

Es porta tot al bloc \textsf{joc} que és on s'efectua tot el treball. Aquest bloc
exposa com a sortides l'estat actual del joc ($comp$), i el nombre a visualitzar
($num$).

Els LEDs estan controlats per una instància de \textsf{leds} on portem $comp$.
Els displays estan controlats per una instància de \textsf{hex\_disps} on portem les
dues xifres del resultat (entrades 7 i 6 respectivament). La resta d'entrades es
forcen a 1111 per a apagar els displays.
'''
