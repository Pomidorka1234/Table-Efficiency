import Definitions as DFN
import math

# Calculate most efficient cost combination from a table for a given maximum cost
def DualEfficiency(M, table = DFN.DualTable(), iteration = -1):
    print("The given table: " + "\n" + table.__str__())         # O(H)
    data0, data1, dataG = [], [], []
    tblHeight = table.label.height
    Vert0 = table.label.getVertex(-1, 0)                        # O(H)
    Vert1 = table.label.getVertex(-1, 1)                        # O(H)
    C = DFN.Matrix(table.label.height, 1, Vert0)                # O(H)
    P = DFN.Matrix(table.label.height, 1, Vert1)                # O(H)
    sumVert = table.label.sumVertex(-1, 0)                      # O(H)
    max = [M/Vert0[0], 0]
    for i in range(tblHeight):                                  # O(H)
        data0.append(math.floor(M/Vert0[i]))
        dataG.append(data0[i])
        data1.append(math.floor(M/sumVert))
        if i != 0:
            if M/Vert0[i] * table.label.matrix[i][1] >= max[0] * table.label.matrix[max[1]][1]:
                dataG[max[1]] = 0
                max = [M/Vert0[i], i]
            else:
                dataG[i] = 0

    G_max = table.Coef(data0)                                   # O(H)
    G_D = table.Coef(data1)                                     # O(H)

    G = table.Coef(dataG)                                       # O(H)

    #So far, O(10H) time complexity (O(H))

    #==============================================================================================================================================================================
    #Discrete method for finding most efficient coeficients
    if (True):
        DiscreteP = P.mult(G_D).matrix[0][0] + ((tblHeight - 1) * P.matrix[0][0]) / tblHeight
        G_D.matrix[max[1]][0] -= 2
        #while(iteration != 0):
            #for i in range(tblHeight):
                #if P.mult(G_D).matrix[0][0] >= DiscreteP and 
                
    #==============================================================================================================================================================================
    #The same method but without P deciding the coeficients
    if (False):
        print('')
    
    #==============================================================================================================================================================================
    print("The 𝛤 maximal coeficients and equal digit coeficients: " + "\n" + str(G_max) + "\n" + str(G_D) + "respectively.")
    print("The maximal profitable single coeficient: " + "\n" + str(G))
    print(C)

    #for i in range(iteration):
     #   while true:



# Calculate most efficient cost combination given a dependency table for a given maximum cost
def DependentDualEfficiency(M, table = DFN.DualTable(), dependent = DFN.DualTable(), iteration = -1):
    data0, data1 = [], []

DualEfficiency(20000, DFN.DualTable([200, 50, 300, 70, 600, 100, 2000, 500, 2500, 650, 4000, 900]))