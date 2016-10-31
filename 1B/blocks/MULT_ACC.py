# -*- coding: utf-8

ports = [
("a[7..0]", "input", ur"Primer factor"),
("b", "input", ur"Segon factor"),
("z", "output", ur"Bit de sortida"),
("in[7..0]", "input", ur"Carry d'entrada"),
("out[7..0]", "output", ur"Carry de sortida"),
]

description = ur'''
Multiplicador $8 \times 1$ amb carry.

Multiplica els primer factor de 8~bits pel segon factor d'un bit, amb carry
d'entrada $in$ i retorna el bit resultant a la sortida $z$ i el carry de
sortida en $out$.

Nota: Aquest és un bloc auxiliar que s'encadena per a fer
multiplicadors $8 \times N$.
'''

implementation = ur'''
Al principi es multipliquen els dos factors amb un \textsf{MULT\_8x1}, i el
resultat es suma amb el carry d'entrada. Dels 9~bits de sortida de la suma (carry
inclós) el de menys pes es retorna a la sortida $z$ i els altres 8, al carry de
sortida.
'''
