# -*- coding: utf-8

ports = [
("nkey", "input", r"Senyal que s'activa si s'ha premut una tecla (actiu baix)"),
("keycode[3..0]", "input", r"Índex de la tecla que s'ha premut"),
("comp[2..0]", "output", r"Sortida per als indicadors de l'estat del joc"),
("num[7..0]", "output", r"Sortida pels displays (BCD)"),
("clk", "input", r"Rellotge, flanc de pujada"),
("nrst", "input", r"Reset asíncron, actiu baix"),
]

description = r'''
Implementa la funcionalitat del joc.

Inicialment, el joc es troba en estat de repós. Quan l'usuari prem \texttt{\#},
el joc genera internament un nombre (suposadament aleatori) i comença la partida.
L'usuari prem els dígits per a introduir un nombre als visualitzadors. Quan es prem \texttt{*},
el joc compara el nombre introduït amb la solució, i mostra el resultat de la comparació
a l'usuari. Si el nombre introduït coincidia amb la solució, la partida es finalitza
i es torna a l'estat de repós.
'''

implementation = r'''
En primer lloc, els senyals d'entrada es porten a una instància de \textsf{keygroup}
per a classificar el tipus de tecla premuda, si n'hi ha. Aquesta informació es porta
a una instància de \textsf{control}.

S'instància també \textsf{registres} per emmagatzemar el nombre introduït; l'entrada
és $keycode$ i l'habilitació de càrrega arriba des de \textsf{control}.

Per altra banda, s'instància també un bloc \textsf{comptador}, que es farà servir per
generar la solució, on l'habilitació de compte arriba també de \textsf{control}.

Els dos nombres BCD de sortida de \textsf{registres} i \textsf{comptador} es porten
a una instància de \textsf{comparador} per a comparar-los. Els resultats de la comparació
es porten de tornada a la instància de \textsf{control}.

Finalment, s'exporten les sortides $num$ (de \textsf{registres}) i $comp$ (de \textsf{control}).
'''

simulation = r'''
Per a fer la simulació, hem escollit valors de $keycode$ verosímils respecte a l'us real del bloc. Aprofitem que coneixem que la resposta és 01 (ja que el comptador que genera $numx$ funciona d'acord amb el clock, i només hem deixar passar-ne un abans de començar la partida) per a comprovar que una vegada encertat el resultat, el teclat es bloqueja. També comprovem que els dígits introduïts es posicionen correctament (de dreta a esquerra) i que s'il·luminen els LEDs corresponents. Mostrem la sortida $num$ en hexadecimal per comoditat.
'''
