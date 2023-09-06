# -*- coding: utf-8

ports = [
("numx[3..0]", "input", r"Primer nombre"),
("num[3..0]", "input", r"Segon nombre"),
("ngtxi", "input", r"Entrada «major que» encadenada"),
("neqxi", "input", r"Entrada «igual que» encadenada"),
("nltxi", "input", r"Entrada «menor que» encadenada"),
("ngtx", "output", r"Indica que $num$ és major que $numx$"),
("neqx", "output", r"Indica que $num$ és igual que $numx$"),
("nltx", "output", r"Indica que $num$ és menor que $numx$"),
]

description = r'''
Comparador de busos de 4~bits encadenable.

Si $neqxi = 1$, compara el valor en binari natural de les dues entrades i activa la sortida corresponent:
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

En cas contrari, les entrades es porten directament a les sortides:
%
\begin{align*}
  ngtx &= ngtxi \\
  neqx &= neqxi \\
  nltx &= nltxi
\end{align*}
'''

implementation = r'''
Es fa servir el paquet \mintinline{vhdl}|std_logic_unsigned| i s'assigna cada sortida a la comparació que toca.

Però en cas que $neqxi$ no estigui activat, les sortides reben el valor directament de les entrades, i no de les comparacions.
'''

timings = [
  {
    "scale": 6,
    "slices": [(9.7,1.7), (14.4,1.7)],
  }
]

simulation = r'''
En aquest cas hem fet la simulació de totes les comparacions possibles, en funció de les entrades $ngtxi$, $neqxi$ i $nltxi$. Hem centrat la simulació en una de les parts clau del comparador, quan $neqxi = 1$. Hem de tenir en compte com interpretar la sortida. En el nostre cas comparem $num$ respecte a $numx$.
'''
