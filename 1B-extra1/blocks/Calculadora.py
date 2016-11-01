# -*- coding: utf8

ports = [
(u"A[3..0]", "input", u"Primera entrada (Ca2)"),
(u"B[3..0]", "input", u"Segona entrada (Ca2)"),
(u"selop[1..0]", "input", u"Operació a efectuar"),
(u"Z[7..0]", "output", u"Valor de sortida (Ca2)"),
(u"r", "output", u"Bit d'alarma"),
]

description = ur'''
Calculadora seleccionable.

Efectua el càlcul corresponent segons el valor de $selop$:

\begin{equation*}
  Z = \begin{cases}
    A \times B & \quad \text{si $selop = 00$} \\
    A \times A & \quad \text{si $selop = 01$} \\
    B \times B & \quad \text{si $selop = 10$} \\
    2^A \times 2^B & \quad \text{si $selop = 11$}
  \end{cases}
\end{equation*}

El bit d'alarma estarà activat a menys que $Z$ pugui representar exactament el
resultat matemàtic i sigui representable en dos xifres decimals.
'''

implementation = ur'''
Per una banda calculem $A+B$ mitjançant el bloc \textsf{SUM\_4B}. Llavors agafem
els tres bits de menys pes i els fem passar pel bloc \textsf{DEC\_3B}. La sortida
equival a $2^{A+B}$ i el desem en la senyal intermèdia $P$.

També comprovem si la suma anterior està dins de rang segons el procediment habitual
(que els sumands tinguin signe diferent, o bé que el seu signe coincideixi amb la
sortida) i ho desem al senyal booleà $s\_in\_range$.

Llavors, la sortida $Z$ serà $A \times B$, $A \times A$, $B \times B$ o $P$, segons
el valor corresponent de $selop$. El bit d'alarma $r$ s'activarà només si $selop =
11$ i la suma està fora de rang o fora de l'interval $\left[0, 6\right]$.
'''

simulation = ur'''
Hem dividit el temps en quatre grans sectors, un per a cada valor de $selop$.
Un cop simulat, comprovem que per als tres primers $r$ està sempre baix, i que el
resultat és sempre el correcte. Per a l'últim sector ($selop = 11$) comprovem que
$selop$ només està desactivat quan la sortida està en rang.
'''
