import Definitions as DFN
import math

# Calculate most efficient cost combination from a table for a given maximum cost
def BinaryEfficiency(M, table = DFN.BinaryTable(), iteration = -1):
    print("The given table: " + "\n" + table.__str__())                      # O(H)
    tblHeight = table.label.height
    data0, data1, dataG = [], [], []
    C = DFN.Matrix(table.label.height, 1, table.label.getVertex(-1, 0))      # O(2H)
    P = DFN.Matrix(table.label.height, 1, table.label.getVertex(-1, 1))      # O(2H)
    sumVert = C.sumVertex(0, -1)                                             # O(H)
    max = [M/C.matrix[0][0], 0]
    for i in range(tblHeight):                                               # O(H)
        data0.append(math.floor(M/C.matrix[0][i]))
        dataG.append(data0[i])
        data1.append(math.floor(M/sumVert))
        if i != 0:
            if dataG[i] * P.matrix[0][i] > max[0] * P.matrix[0][max[1]]:
                dataG[max[1]] = 0
                max = [M/dataG[i], i]
            else:
                dataG[i] = 0

    Λ_max = table.Coef(data0)                                                # O(H)

    Λ_D = table.Coef(data1)                                                  # O(H)

    Λ = table.Coef(dataG)                                                    # O(H)

    #==============================================================================================================================================================================
    #Discrete method for finding most efficient coeficients
    if (True):
        DiscreteP = P.mult(Λ_D).matrix[0][0] + ((tblHeight - 1) * P.matrix[0][0]) / tblHeight
        Λ_D.matrix[max[1]][0] -= 2
        while(iteration != 0):
            for i in range(tblHeight):
                if P.mult(Λ_D).matrix[0][0] >= DiscreteP and C.mult(Λ_D).matrix[0][0] >= 0:
                    C += 1
            iteration -= 1
            
                
    #==============================================================================================================================================================================
    #The same method but without P deciding the coeficients
    if (False):
        print('')
    
    #==============================================================================================================================================================================
    #The upper vector & maximum coeficient method
    
    #==============================================================================================================================================================================
    print("The Λ maximal coeficients and equal digit coeficients: " + "\n" + str(Λ_max) + "\n" + str(Λ_D) + "respectively.")
    print("The maximal profitable single coeficient: " + "\n" + str(Λ))
    print(C)

    #for i in range(iteration):
     #   while true:



# Calculate most efficient cost combination given a dependency table for a given maximum cost
def DependentBinaryEfficiency(M, table = DFN.BinaryTable(), dependent = DFN.BinaryTable(), iteration = -1):
    data0, data1 = [], []

BinaryEfficiency(20000, DFN.BinaryTable([200, 50, 300, 70, 600, 100, 2000, 500, 2500, 650, 4000, 900]), 10)