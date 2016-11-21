# -*- coding: utf-8

ports = [
("sigRes", "input", ur"Signe del resultat actual"),
("res[7..0]", "input", ur"Mòdul del resultat actual (BCD)"),
("show", "input", ur"Senyal que s'activa si s'ha de mostrar el resultat"),
("sigSel", "output", ur"Signe a visualitzar als displays del resultat"),
("sel[7..0]", "output", ur"Mòdul a visualitzar als displays del resultat (BCD$^\dagger$)"),
]

description = ur'''
Controla la sortida del bloc multiplicador, que posteriorment serà convertida a set-segments
i es mostrarà als displays del resultat.

Si $show$ és actiu, la sortida $sel$ és directament l'entrada $res$, i el mateix amb $sigSel$ i $sigRes$.
En cas contrari, la sortida són xifres BCD invàlides per tal d'apagar els displays que mostren el resultat,
i signe positiu per al mateix propòsit.
'''

notes = [ur'''
El funcionament d'aquest bloc es basa en que els conversors a set-segments
apaguen els displays per a una xifra BCD invàlida, i per a signe positiu.
Això és el cas per a \textsf{BCD7seg} i \textsf{CA2\_SIG\_SS}.
''']
