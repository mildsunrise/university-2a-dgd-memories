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
Hem pres una forma poc usual de dissenyar aquest bloc: en comptes d'assignar
$comp$ de forma combinacional fora del \mintinline{vhdl}|process|, es fa dins
i només en certs casos (\emph{latch}). Hem vist que això simplifica molt el
codi i ens ha permés fer el disseny en només \textbf{2 estats} (repós, jugant)
en comptes de 5.

El diagrama de transició d'estats (només depen de les entrades $coi$, $neqx$; sortides $eshft$, $ecnt$) és el següent. Es tracta
d'una màquina de Mealy, però es representa la sortida dins de l'estat per simplicitat:

\begin{center} \begin{tikzpicture}[shorten >=1pt, node distance=2cm, >=stealth', auto]
  \node[state with output, initial above, initial text=reset] (st_idle) at (0,0) {idle \nodepart{lower} $0,1$};
  \node[state with output]          (st_playing) at (4,0) {playing \nodepart{lower} $bcd,0$};

  \path[->]
    (st_idle) edge [loop left, align=center] node {$0,-$} (st_idle)
    (st_idle) edge [bend left, align=center] node {$1,-$} (st_playing)
    
    (st_playing) edge [loop right, align=center] node {$0,0$} (st_playing)
    (st_playing) edge [bend left, align=center] node {$1,-$ \\ $-,1$} (st_idle)
  ;
\end{tikzpicture} \end{center}

Respecte a $comp$, se li assigna un valor només en els següents casos:

\begin{itemize}
\item En reset: \mintinline{vhdl}|"111"|
\item En estat \emph{idle}, $coi$ s'activa: \mintinline{vhdl}|"000"|
\item En estat \emph{playing}, $bcd$ s'activa: \mintinline{vhdl}|"000"|
\item En estat \emph{playing}, $ast$ s'activa: \mintinline{vhdl}|ngtx & neqx & nltx|
\item En estat \emph{playing}, $coi$ s'activa: \mintinline{vhdl}|"111"|
\end{itemize}
'''

simulation = ur'''
En aquesta simulació comprovem que les sortides es comporten correctament. Ens basem en una situació real que es donaria en el joc (p.e. no posariem les sortides $ngtx$, $netx$ o $nltx$ alhora).
'''
