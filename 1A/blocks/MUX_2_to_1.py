# -*- coding: utf-8

ports = [
("a", "input", ur"Entrada 1"),
("b", "input", ur"Entrada 0"),
("sel", "input", ur"Bit de selecció"),
("z", "output", ur"Sortida"),
]

description = ur'''
Multiplexor de 2 entrades.

Estableix la sortida $z$ a l'entrada $b$ si $sel = 0$,
o a l'entrada $a$ si $sel = 1$.
'''

implementation = ur'''
Implementació feta a partir de la simplificació mínima a 2 nivells en SdP,
que correspon a l'expressió algebraica:

\begin{equation*}
  z = a \cdot sel + b \cdot \overline{sel}
\end{equation*}
'''
