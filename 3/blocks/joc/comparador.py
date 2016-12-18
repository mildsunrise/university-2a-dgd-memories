# -*- coding: utf-8

ports = [
("numx[7..0]", "input", ur"Primer nombre (BCD, dos xifres)"),
("num[7..0]", "input", ur"Segon nombre (BCD, dos xifres)"),
("ngtx", "output", ur"Indica que $num$ és major que $numx$"),
("neqx", "output", ur"Indica que $num$ és igual que $numx$"),
("nltx", "output", ur"Indica que $num$ és menor que $numx$"),
]

unspecs = ur'''
La sortida no està definida si alguna de les dues entrades no pertany al seu codi.
'''

description = ur'''
Comparador BCD de dues xifres.

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
Es fa servir el paquet \mintinline{vhdl}|std_logic_unsigned| i es duen a terme comparacions
entre les xifres individuals d'ambdos termes, que s'assignen a les senyals
intermèdies $a_1, a_0$ i $b_1, b_0$ respectivament.
'''

simulation = ur'''
Aquesta simulació pot resultar liosa en el sentit que hem de tenir clar l'ordre de comparació. Per exemple, nosaltres hem interpretat el significat de $ngtx$ com «$num$ greater than $numx$» a l'hora de fer el codi del comparador (una interpretació semblant amb $neqx$ i $nltx$). Tenint compte això hem de verificar que el bloc funciona adequadament.
'''
