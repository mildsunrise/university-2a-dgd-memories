# -*- coding: utf-8

ports = [
("sigA", "input", ur"Signe del primer factor"),
("A[3..0]", "input", ur"Mòdul del primer factor (BCD)"),
("sigB", "input", ur"Signe del segon factor"),
("B[3..0]", "input", ur"Mòdul del segon factor (BCD)"),
("sigAxB", "output", ur"Signe del producte"),
("AxB[7..0]", "output", ur"Mòdul del producte (BCD)"),
]

description = ur'''
Multiplicador BCD d'una xifra amb signe, amb resultat en dues xifres.

Retorna a la sortides $sigAxB$ i $AxB$ el signe i mòdul del producte de $sigA$, $A$ amb $sigB$, $B$.
'''

unspecs = ur'''
La sortida no està definida si $A$ o $B$ no pertanyen al seu codi.
'''

implementation = ur'''
Es fa servir \textsf{MULT\_8x8} per a dur a terme la multiplicació del mòdul
(els factors son també binari natural), i el resultat es converteix
de binari natural a BCD de dues xifres mitjançant \textsf{CA2\_BCD\_8B},
abans de ser retornat a $AxB$.

Per a calcular el signe del producte es fa servir una \textsf{XOR} entre els
dos signes d'entrada.
'''
