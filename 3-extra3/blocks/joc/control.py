# -*- coding: utf-8

ports = [
("bcd", "input", r"Senyal que s'activa si s'ha premut una xifra decimal"),
("ast", "input", r"Senyal que s'activa si s'ha premut la tecla asterisc"),
("coi", "input", r"Senyal que s'activa si s'ha premut la tecla coixinet"),
("let", "input", r"Senyal que s'activa si s'ha premut una lletra"),
("ngtx", "input", r"Indica que el nombre introduït és major que la solució"),
("neqx", "input", r"Indica que el nombre introduït coincideix amb la solució"),
("nltx", "input", r"Indica que el nombre introduït és menor que la solució"),
("show", "output", r"Indica que s'ha de visualitzar la solució, no el nombre introduït"),
("eshft", "output", r"Senyal que s'activa quan s'ha d'enregistrar la xifra premuda"),
("ecnt", "output", r"Senyal que d'habilitació del comptador"),
("comp[2..0]", "output", r"Sortida per als indicadors de l'estat del joc"),
("clk", "input", r"Rellotge, flanc de pujada"),
("nrst", "input", r"Reset asíncron, actiu baix"),
]

description = r'''
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

Per a la funcionalitat de trampa, la sortida $show$ indica quan s'ha de visualitzar
la solució en comptes del nombre introduït per l'usuari.
'''

unspecs = r'''
El comportament del bloc no està definit si més d'una de les entrades $bcd, ast, coi, let$ està activa a la vegada.
El comportament del bloc no està definit si cap de les entrades $ngtx, neqx, nltx$ està activa, o més d'una ho està.
'''

implementation = r'''
Gràcies al \emph{latch} només cal un tercer estat, que anomenarem \emph{cheating},
per a implementar la trampa. S'afegeix una sortida $show$ que s'activarà només
en aquest estat, indicant a la resta del disseny que s'ha de visualitzar la solució
en comptes del nombre introduït.

El diagrama de transició d'estats (només depen de les entrades $coi$, $let$, $neqx$; sortides $show$, $eshft$, $ecnt$) és el següent. Es tracta
d'una màquina de Mealy, però es representa la sortida dins de l'estat per simplicitat:

\begin{center} \begin{tikzpicture}[shorten >=1pt, node distance=2cm, >=stealth', auto]
  \node[state with output, initial above, initial text=reset] (st_idle) at (0,0) {idle \nodepart{lower} $0,0,1$};
  \node[state with output]          (st_playing) at (5,0) {playing \nodepart{lower} $0,bcd,0$};
  \node[state with output]          (st_cheating) at (5,-5) {cheating \nodepart{lower} $1,0,0$};

  \path[->]
    (st_idle) edge [loop left, align=center] node {$0,-,-$} (st_idle)
    (st_idle) edge [bend left, align=center] node {$1,-,-$} (st_playing)

    (st_playing) edge [loop right, align=center] node {$0,0,0$} (st_playing)
    (st_playing) edge [bend left, align=center] node {$1,-,-$ \\ $-,-,1$} (st_idle)
    (st_playing) edge [bend left, align=center] node {$-,1,-$} (st_cheating)

    (st_cheating) edge [loop right, align=center] node {$0,0,-$} (st_cheating)
    (st_cheating) edge [bend left, align=center] node {$-,1,-$} (st_playing)

    (st_cheating) edge [bend left, align=center] node {$1,-,-$} (st_idle)
  ;
\end{tikzpicture} \end{center}

Respecte a $comp$, se li assigna un valor només en els següents casos:

\begin{itemize}
\item En reset: \mintinline{vhdl}|"111"|
\item En estat \emph{idle}, $coi$ s'activa: \mintinline{vhdl}|"000"|
\item En estat \emph{playing}, $bcd$ o $let$ s'activa: \mintinline{vhdl}|"000"|
\item En estat \emph{playing}, $ast$ s'activa: \mintinline{vhdl}|ngtx & neqx & nltx|
\item En estat \emph{playing} o \emph{cheating}, $coi$ s'activa: \mintinline{vhdl}|"111"|
\end{itemize}
'''

simulation = r'''
Introduïm comandes que simulen una partida real del joc. En aquest cas ens centrem en que el funcionament de la trampa sigui el correcte.
'''
