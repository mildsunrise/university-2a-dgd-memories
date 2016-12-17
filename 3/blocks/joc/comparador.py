# -*- coding: utf-8

ports = [
("numx[7..0]", "input", ur"Primer nombre (BCD, dos xifres)"),
("num[7..0]", "input", ur"Segon nombre (BCD, dos xifres)"),
("ngtx", "output", ur"Indica que el primer nombre és major que el segon (actiu baix)"),
("neqx", "output", ur"Indica que el primer nombre és igual que el segon (actiu baix)"),
("nltx", "output", ur"Indica que el primer nombre és menor que el segon (actiu baix)"),
]

unspecs = ur'''
La sortida no està definida si alguna de les dues entrades no pertany al seu codi.
'''
