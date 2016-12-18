# -*- coding: utf-8

ports = [
("numx[7..0]", "input", ur"Primer nombre (BCD, dos xifres)"),
("num[7..0]", "input", ur"Segon nombre (BCD, dos xifres)"),
("ngtx", "output", ur"Indica que $num$ és major que $numx$ (actiu baix)"),
("neqx", "output", ur"Indica que $num$ és igual que $numx$ (actiu baix)"),
("nltx", "output", ur"Indica que $num$ és menor que $numx$ (actiu baix)"),
]

unspecs = ur'''
La sortida no està definida si alguna de les dues entrades no pertany al seu codi.
'''

simulation = ur'''
Aquesta simulació pot resultar liosa en el sentit que hem de tenir clar l'ordre de comparació. Per exemple, nosaltres hem interpretat el significat de $ngtx$ com «$num$ greater than $numx$» a l'hora de fer el codi del comparador (una interpretació semblant amb $neqx$ i $nltx$). Tenint compte això hem de verificar que el bloc funciona adequadament.
'''
