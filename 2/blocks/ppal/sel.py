# -*- coding: utf-8

ports = [
("res[7..0]", "input", ur"Resultat actual (BCD)"),
("show", "input", ur"Senyal que s'activa si s'ha de mostrar el resultat"),
("sel[7..0]", "output", ur"Sortida pels displays (BCD$^\dagger$)"),
]

description = ur'''
Controla la sortida del bloc multiplicador, que posteriorment serà convertida a set-segments
i es mostrarà als displays del resultat.

Si $show$ és actiu, la sortida $sel$ és directament l'entrada $res$. En cas contrari,
la sortida són xifres BCD invàlides per tal d'apagar els displays que mostren
el resultat.
'''

notes = [ur'''
El funcionament d'aquest bloc es basa en que els conversors a set-segments
apaguen els displays per a una xifra BCD invàlida. Això és el cas per a
\textsf{BCD7seg}.
''']
