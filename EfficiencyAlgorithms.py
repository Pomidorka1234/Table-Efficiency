import Definitions as DFN
import math

# Calculate most efficient cost combination from a table for a given maximum cost
def BinaryEfficiency(M, table = DFN.BinaryTable(), iteration = -1):
    print("The given table: " + "\n" + table)
    data0, data1 = [], []
    for cost in table.label.getVertex(-1, 0):
        data0.append(math.floor(M/cost))
        data1.append(math.floor(M/table.sumVertex()))

    𝛤_max = table.Coef(data0)
    𝛤_D = table.Coef(data1)
    E = DFN.Matrix(len(table.label.getVertex(-1, 0)), 1, table.label.getVertex(-1, 0)).mult(𝛤_max)
    ᴇ = table.label["profit"].mult(𝛤_max)

    print("The 𝛤 maximal coeficients and equal digit coeficients: " + 𝛤_max + "   " + 𝛤_D)

# Calculate most efficient cost combination given a dependency table for a given maximum cost
def DependentBinaryEfficiency(M, table = DFN.BinaryTable(), dependent = DFN.BinaryTable(), iteration = -1):
    data0, data1 = [], []