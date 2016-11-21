# -*- coding: utf-8

ports = [
("sigA", "input", ur"Signe del primer factor"),
("A[3..0]", "input", ur"Mòdul del primer factor (BCD)"),
("sigB", "input", ur"Signe del segon factor"),
("B[3..0]", "input", ur"Mòdul del segon factor (BCD)"),
("selop[1..0]", "input", ur"Índex d'operació a realitzar"),
("sigRes", "output", ur"Signe del producte"),
("res[7..0]", "output", ur"Mòdul del producte (BCD)"),
]

description = ur'''
Calculadora BCD d'una xifra amb signe, amb resultat en dues xifres.

Retorna a les sortides $sigRes$ i $res$ el signe i mòdul de la operació corresponent,
segons el valor de $selop$:

\begin{description}
\item[00] Producte de $A$ per $B$
\item[01] Quadrat de $A$
\item[10] Quadrat de $B$
\item[11] Suma de $A$ amb $B$
\end{description}
'''

unspecs = ur'''
La sortida no està definida si $A$ o $B$ no pertanyen al seu codi.
'''

implementation = ur'''
Per a les primeres tres operacions ($selop \neq 11$), el resultat s'agafa d'un
bloc \textsf{AperB} amb les dues entrades com sigui oportú. Per a l'última operació,
la sortida prové d'un bloc \textsf{AmesB}.
'''
