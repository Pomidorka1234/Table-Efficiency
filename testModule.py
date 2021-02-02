import Definitions as DFN

tbl = DFN.BinaryTable([200, 50, 300, 70, 600, 100, 1000, 500, 2500, 650, 4000, 900])
vert = tbl.label.getVertex(-1, 1)
C = DFN.Matrix(len(vert), 1, tbl.label.getVertex(-1, 1))
g = tbl.Coef([2, 1, 5, 1, 1, 2])

print(g.mult(C))
