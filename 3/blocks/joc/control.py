# -*- coding: utf-8

ports = [
("bcd", "input", ur"Senyal que s'activa si s'ha premut una xifra decimal"),
("ast", "input", ur"Senyal que s'activa si s'ha premut la tecla asterisc"),
("coi", "input", ur"Senyal que s'activa si s'ha premut la tecla coixinet"),
("ngtx", "input", ur"Indica que el nombre introduït és major que la solució (actiu baix)"),
("neqx", "input", ur"Indica que el nombre introduït coincideix amb la solució (actiu baix)"),
("nltx", "input", ur"Indica que el nombre introduït és menor que la solució (actiu baix)"),
("eshft", "output", ur"Senyal que s'activa quan s'ha d'enregistrar la xifra premuda"),
("ecnt", "output", ur"Senyal que d'habilitació del comptador"),
("comp[2..0]", "output", ur"Sortida per als indicadors de l'estat del joc"),
("clk", "input", ur"Rellotge, flanc de pujada"),
("nrst", "input", ur"Reset asíncron, actiu baix"),
]

description = ur'''
Màquina de control del joc.

Emmagatzema i actualitza l'estat del joc, habilitant el comptador o el registre segons convingui.
La sortida $comp$ son tres bits (aproximadament, «major» / «igual» / «menor») que tenen
combinacions amb diversos significats i que controlen els LEDs de la placa:

\begin{description}
\item[111] El joc s'acaba d'inicialitzar i es troba en espera (no s'ha jugat cap partida).
\item[000] S'ha començat una nova partida, s'està esperant que es comprovi un nombre.
\item[100] L'usuari ha comprovat un nombre que ha resultat ser major que la solució.
\item[001] L'usuari ha comprovat un nombre que ha resultat ser menor que la solució.
\item[010] L'usuari ha comprovat un nombre que ha resultat ser igual a la solució;
s'ha acabat la partida i el joc es troba en espera.
\end{description}
'''

unspecs = ur'''
El comportament del bloc no està definit si més d'una de les entrades $bcd, ast, coi$ està activa a la vegada.
El comportament del bloc no està definit si cap de les entrades $ngtx, neqx, nltx$ està activa, o més d'una ho està.
'''

implementation = ur'''
% TODO
'''

simulation = ur'''
En aquesta simulació comprovem que les sortides es comporten correctament. Ens basem en una situació real que es donaria en el joc (p.e. no posariem les sortides $ngtx$, $netx$ o $nltx$ alhora).
'''
