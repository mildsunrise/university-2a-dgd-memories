# -*- coding: utf-8

ports = [
("sigA", "input", ur"Signe del primer factor"),
("A[3..0]", "input", ur"Mòdul del primer factor (BCD)"),
("sigB", "input", ur"Signe del segon factor"),
("B[3..0]", "input", ur"Mòdul del segon factor (BCD)"),
("sigAmesB", "output", ur"Signe del producte"),
("AmesB[7..0]", "output", ur"Mòdul del producte (BCD)"),
]

description = ur'''
Sumador BCD d'una xifra amb signe, amb resultat en dues xifres.

Retorna a les sortides $sigAmesB$ i $AmesB$ el signe i mòdul de la suma de $sigA$, $A$ amb $sigB$, $B$.
'''

unspecs = ur'''
La sortida no està definida si $A$ o $B$ no pertanyen al seu codi.
'''

implementation = ur'''
Primer, s'expressa $A$ i $B$ en Ca2 de 5~bits, i es desen en senyals intermedis \mintinline{vhdl}|signed|.

Llavors, s'estenen els senyals intermedis a 8~bits, es sumen
i es passen a vector lògic per a obtenir el resultat de la suma en Ca2.

Finalment, s'utilitza \textsf{CA2\_BCD\_8B} per a extreure el mòdul del resultat en BCD de dues xifres,
i es retorna juntament amb el signe a les sortides corresponents.
'''
