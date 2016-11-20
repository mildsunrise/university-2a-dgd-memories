# -*- coding: utf-8

ports = [
("nkey", "input", ur"Senyal que s'activa si s'ha premut una tecla (actiu baix)"),
("keycode[3..0]", "input", ur"Índex de la tecla que s'ha premut"),
("show", "output", ur"Senyal que s'activa si s'ha de mostrar el resultat"),
("A[3..0]", "output", ur"Primer factor (BCD)"),
("B[3..0]", "output", ur"Segon factor (BCD)"),
("sel[7..0]", "output", ur"Sortida pels displays (BCD$^\dagger$)"),
("clk", "input", ur"Rellotge, flanc de pujada"),
("nrst", "input", ur"Reset asíncron, actiu baix"),
]

description = ur'''
Multiplicador BCD seqüencial.

El multiplicador té dos modes: en el d'introducció, es memoritzen els últims dos dígits
que l'usuari ha premut; en el de visualització, es mostra el producte d'aquests dos dígits a
la sortida. Es pot passar al mode d'introducció prement \texttt{*} i al mode de
visualització prement \texttt{\#}.
'''
