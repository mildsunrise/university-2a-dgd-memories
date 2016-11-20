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

implementation = ur'''
Es fa servir \textsf{MULT\_8x8} per a dur a terme la multiplicació
(els factors son també binari natural), i el resultat es converteix
de binari natural a BCD de dues xifres mitjançant \textsf{CA2\_BCD\_8B},
abans de ser retornat a $AxB$.
'''
