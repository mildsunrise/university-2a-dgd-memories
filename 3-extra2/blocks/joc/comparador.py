# -*- coding: utf-8

ports = [
("numx[11..0]", "input", ur"Primer nombre (BCD, tres xifres)"),
("num[11..0]", "input", ur"Segon nombre (BCD, tres xifres)"),
("ngtx", "output", ur"Indica que $num$ és major que $numx$"),
("neqx", "output", ur"Indica que $num$ és igual que $numx$"),
("nltx", "output", ur"Indica que $num$ és menor que $numx$"),
]

unspecs = ur'''
La sortida no està definida si alguna de les dues entrades no pertany al seu codi.
'''

description = ur'''
Comparador BCD de tres xifres.

Compara el valor en BCD de les dues entrades i activa la sortida corresponent:
%
\begin{align*}
  ngtx &= \begin{cases}
    1 & \text{si $num > numx$} \\
    0 & \text{altrament}
  \end{cases} \\
  neqx &= \begin{cases}
    1 & \text{si $num = numx$} \\
    0 & \text{altrament}
  \end{cases} \\
  nltx &= \begin{cases}
    1 & \text{si $num < numx$} \\
    0 & \text{altrament}
  \end{cases}
\end{align*}
'''

implementation = ur'''
Es fan servir tres instàncies del bloc \textsf{comparador\_single} encadenades,
comparant cadascuna de les tres xifres de $num$ i $numx$ (el bloc és un comparador binari
genèric, per tant serveix per a BCD d'una xifra).
'''

# TODO: simulation
