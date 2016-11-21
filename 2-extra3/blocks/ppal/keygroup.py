# -*- coding: utf-8

ports = [
("nkey", "input", ur"Senyal que s'activa si s'ha premut una tecla (actiu baix)"),
("x[3..0]", "input", ur"Índex de la tecla que s'ha premut"),
("bcd", "output", ur"Senyal que s'activa si s'ha premut una xifra decimal"),
("ast", "output", ur"Senyal que s'activa si s'ha premut una tecla de sel·lecció d'operació"),
("coi", "output", ur"Senyal que s'activa si s'ha premut la tecla coixinet"),
("coi", "output", ur"Senyal que s'activa si s'ha premut la tecla A"),
("selop[1..0]", "output", ur"Índex d'operació que s'ha premut"),
]

description = ur'''
Evalua la tecla premuda $x$, si n'hi ha, i activa una (o cap) de les sortides següents,
segons el tipus de tecla premuda:

\begin{itemize}
\item $bcd$ si és un dígit decimal. En aquest cas, $x$ és també
el valor d'aquest dígit en BCD.
\item $ast$ si és una tecla de sel·lecció d'operació (\texttt{*}, \texttt{B}, \texttt{C}, \texttt{D}).
\item $coi$ si és la tecla coixinet (\texttt{\#}).
\item $neg$ si és la tecla \texttt{A}.
\end{itemize}

Addicionalment, si $ast = 1$, la sortida $selop$ conté l'índex d'operació a realitzar (veure Especificació).
'''

implementation = ur'''
Cada sortida estarà activa només si $nkey$ està actiu i $x$ és el valor adequat.
Per al cas de $bcd$ no és un valor únic sino un rang, però es pot escriure de
forma compacta mitjançant una comparació. Per a $ast$ i $keycode$ es segueix un
raonament similar.
'''
