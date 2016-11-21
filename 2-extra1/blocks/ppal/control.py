# -*- coding: utf-8

ports = [
("bcd", "input", ur"Senyal que s'activa si s'ha premut una xifra decimal"),
("ast", "input", ur"Senyal que s'activa si s'ha premut la tecla asterisc"),
("coi", "input", ur"Senyal que s'activa si s'ha premut la tecla coixinet"),
("neg", "input", ur"Senyal que s'activa si s'ha premut la tecla \texttt{A}"),
("intro", "output", ur"Senyal que s'activa si s'ha d'emmagatzemar una xifra nova"),
("negar", "input", ur"Senyal que s'activa quan s'ha de negar el factor A"),
("show", "output", ur"Senyal que s'activa si s'ha de mostrar el resultat"),
("clk", "input", ur"Rellotge, flanc de pujada"),
("nrst", "input", ur"Reset asíncron, actiu baix"),
]

description = ur'''
Bloc de control d'estat per al multiplicador.

El senyal $show$ indica si el multiplicador està en mode visualització o introducció,
i el senyal $intro$ s'activa quan el multiplicador està en mode introducció i l'usuari
prem una xifra decimal. El senyal $negar$ s'activa quan el multiplicador està en mode
introducció i l'usuari prem la tecla \texttt{A}.
'''

unspecs = ur'''
El comportament del bloc no està definit si més d'una entrada està activa a la vegada.
'''

implementation = ur'''
Es tracta d'una màquina de Mealy amb diagrama d'estats (per simplicitat, es
representarà la sortida dins els nodes d'estat):

\begin{center} \begin{tikzpicture}[shorten >=1pt, node distance=2cm, >=stealth', auto]
  \node[state with output, initial above, initial text=reset] (st_show) at (0,0) {show \nodepart{lower} $0,0,1$};
  \node[state with output]          (st_intro) at (4,0) {intro \nodepart{lower} $bcd,neg,0$};

  \path[->]
    (st_show) edge [loop left] node {$-,0,-,-$} (st_show)
    (st_show) edge [bend left] node {$-,1,-,-$} (st_intro)
    
    (st_intro) edge [loop right] node {$-,-,0,-$} (st_intro)
    (st_intro) edge [bend left] node {$-,-,1,-$} (st_show)
  ;
\end{tikzpicture} \end{center}

Quan arriba el flanc de rellotge, es força l'estat \mintinline{vhdl}|st_show| si $ast$ és
actiu, o l'estat \mintinline{vhdl}|st_intro| si $coi$ és actiu.

La sortida $show$ indica l'estat actual de la màquina. La sortida $intro$ és activa
només quan $bcd$ és activa i ens trobem en l'estat \mintinline{vhdl}|st_intro|, i la
sortida $negar$ és activa només quan $neg$ és activa i ens trobem en l'estat \mintinline{vhdl}|st_intro|.
'''
