# -*- coding: utf-8

ports = [
("ecnt", "input", ur"Habilitació del compte"),
("numx[7..0]", "output", ur"Nombre de sortida (BCD, dos xifres)"),
("clk", "input", ur"Rellotge, flanc de pujada"),
("nrst", "input", ur"Reset asíncron, actiu baix"),
]

timings = [
  {
    "scale": 1.1,
    "slices": [ (0,9), (52,9) ],
  }
]
