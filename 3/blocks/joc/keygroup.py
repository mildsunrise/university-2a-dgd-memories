# -*- coding: utf-8

ports = [
("nkey", "input", ur"Senyal que s'activa si s'ha premut una tecla (actiu baix)"),
("x[3..0]", "input", ur"Índex de la tecla que s'ha premut"),
("bcd", "output", ur"Senyal que s'activa si s'ha premut una xifra decimal"),
("ast", "output", ur"Senyal que s'activa si s'ha premut la tecla asterisc"),
("coi", "output", ur"Senyal que s'activa si s'ha premut la tecla coixinet"),
]

description = ur'''
Evalua la tecla premuda $x$, si n'hi ha, i activa una (o cap) de les sortides següents,
segons el tipus de tecla premuda:

\begin{itemize}
\item $bcd$ si és un dígit decimal. En aquest cas, $x$ és també
el valor d'aquest dígit en BCD.
\item $ast$ si és la tecla asterisc (\texttt{*}).
\item $coi$ si és la tecla coixinet (\texttt{\#}).
\end{itemize}
'''

implementation = ur'''
Cada sortida estarà activa només si $nkey$ està actiu i $x$ és el valor adequat.
Per al cas de $bcd$ no és un valor únic sino un rang, però es pot escriure de
forma compacta mitjançant una comparació.
'''
