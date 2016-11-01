# -*- coding: utf-8

ports = [
(u"a[2..0]", "input", "Entrada a descodificar (binari natural)"),
(u"z[7..0]", "output", "Sortides del codi"),
]

description = ur'''
Descodificador en binari natural de 3~bits.

Activa la sortida $a$-èsima i retorna 0 a totes les altres.
'''

implementation = ur'''
Implementació feta en VHDL expandint l'expressió algebraica següent per
a tots els valors possibles de $i$:

\begin{equation*}
  z_i = \begin{cases}
    1 & \quad \text{si $a = i$} \\
    0 & \quad \text{altrament}
  \end{cases}
\end{equation*}
'''

simulation = ur'''
Per a comprovar que el descodificador funciona adequadament, un cop feta la simulació hem de comprovar que la posició del $1$ coincideixi amb el valor de $a$ (la ordenació escollida per a la posició del bit és $7..0$).
'''
