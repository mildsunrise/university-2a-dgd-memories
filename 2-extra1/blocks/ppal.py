# -*- coding: utf-8

ports = [
("nkey", "input", ur"Senyal que s'activa si s'ha premut una tecla (actiu baix)"),
("keycode[3..0]", "input", ur"Índex de la tecla que s'ha premut"),
("show", "output", ur"Senyal que s'activa si s'ha de mostrar el resultat"),
("sigA", "output", ur"Signe del primer factor"),
("opA[3..0]", "output", ur"Mòdul del primer factor (BCD)"),
("sigB", "output", ur"Signe del segon factor"),
("opB[3..0]", "output", ur"Mòdul del segon factor (BCD)"),
("sigRes", "output", ur"Signe de la sortida pels displays"),
("res[7..0]", "output", ur"Mòdul de la sortida pels displays (BCD$^\dagger$)"),
("clk", "input", ur"Rellotge, flanc de pujada"),
("nrst", "input", ur"Reset asíncron, actiu baix"),
]

description = ur'''
Multiplicador BCD amb signe seqüencial.

El multiplicador té dos modes: en el d'introducció, es memoritzen els últims dos dígits
que l'usuari ha premut, i es permet canviar el signe de l'últim introduït prement \texttt{A};
en el de visualització, es mostra el producte d'aquests dos dígits a la sortida. Es pot passar
al mode d'introducció prement \texttt{*} i al mode de visualització prement \texttt{\#}.
'''

implementation = ur'''
En primer lloc, es fa servir \textsf{keygroup} per a detectar el tipus de tecla premuda,
i les sortides van a la màquina de control (\textsf{control}) d'on resulten els senyals
$show$, $intro$ i $negar$.

S'utilitza llavors una instància de \textsf{regs} per emmagatzemar el valor de $keycode$
als factors, així com el seu signe, governada per les sortides corresponents de la màquina
de control. Els dos factors (signe i mòdul per a cadascun) s'assignen a $sigA, opA$ i
$sigB, opB$ respectivament.

Els factors es retornen i també es porten a \textsf{AperB} per obtenir-ne el producte,
que es fa passar per \textsf{sel} just abans de retornar-lo a la sortida.
'''
