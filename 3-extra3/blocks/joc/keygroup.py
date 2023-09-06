# -*- coding: utf-8

ports = [
("nkey", "input", r"Senyal que s'activa si s'ha premut una tecla (actiu baix)"),
("x[3..0]", "input", r"Índex de la tecla que s'ha premut"),
("bcd", "output", r"Senyal que s'activa si s'ha premut una xifra decimal"),
("ast", "output", r"Senyal que s'activa si s'ha premut la tecla asterisc"),
("coi", "output", r"Senyal que s'activa si s'ha premut la tecla coixinet"),
("let", "output", r"Senyal que s'activa si s'ha premut una lletra"),
]

description = r'''
Evalua la tecla premuda $x$, si n'hi ha, i activa una (o cap) de les sortides següents,
segons el tipus de tecla premuda:

\begin{itemize}
\item $bcd$ si és un dígit decimal. En aquest cas, $x$ és també
el valor d'aquest dígit en BCD.
\item $ast$ si és la tecla asterisc (\texttt{*}).
\item $coi$ si és la tecla coixinet (\texttt{\#}).
\item $let$ si és una lletra.
\end{itemize}
'''

implementation = r'''
Cada sortida estarà activa només si $nkey$ està actiu i $x$ és el valor adequat.
Per al cas de $bcd$ i $let$ no és un valor únic sino un rang, però es pot escriure de
forma compacta mitjançant una comparació.
'''

simulation = r'''
Ens fixem que detecti les lletres activant la nova sortida.
'''
