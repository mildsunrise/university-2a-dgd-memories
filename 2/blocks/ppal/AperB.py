# -*- coding: utf-8

ports = [
("A[3..0]", "input", ur"Primer factor (BCD)"),
("B[3..0]", "input", ur"Segon factor (BCD)"),
("AxB[7..0]", "output", ur"Producte (BCD)"),
]

description = ur'''
Multiplicador BCD d'una xifra, amb resultat en dues xifres.

Retorna a la sortida $AxB$ el producte de $A$ amb $B$.
'''

unspecs = ur'''
La sortida no està definida si $A$ o $B$ no pertanyen al seu codi.
'''
