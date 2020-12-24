import Definitions as DFN
import math

def BinaryEfficiency(table, M):
    data0, data1 = [], []
    for i in range(table.label["cost"].raw):
        data0[i] = math.floor(M / table.label["cost"].raw[i])
        data1[i] = math.floor(M / table.sum())
    𝛤_max = table.Gamma(data0)
    𝛤_D = table.Gamma(data1)

    E = table.label["cost"].mult(𝛤_max)
    ᴇ = table.label["profit"].mult(𝛤_max) 
