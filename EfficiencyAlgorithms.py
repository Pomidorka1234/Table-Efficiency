import TableTypes as TT
import math
import dataclasses as DC
import jupyter as JP

class BinaryAlogrithms:
    def __init__(self, M: int, table: TT.BinaryTable):
        """
            O(n) Initialize variables for work with tables and efficiency algorithms
        """
        self.table = table
        self.M = M
        self.C = TT.Matrix(table.label.height, 1, table.label.getVertex(-1, 0))
        self.P = TT.Matrix(table.label.height, 1, table.label.getVertex(-1, 1))
        self.Csum = self.C.sumVertex(0, -1)
        self.Psum = self.P.sumVertex(0, -1)
        
        data0, data1, data2 = [], [], []
        maxM = [self.M / self.C.matrix[0][0], 0]
        for i in range(self.table.height):
            data0.append(math.floor(self.M / self.C.matrix[0][i]))
            data1.append(data0[i])
            data2.append(math.floor(self.M / self.Csum))

            if i != 0:
                if data1[i] * self.P.matrix[0][i] > maxM[0] * self.P.matrix[0][maxM[1]]:
                    data1[maxM[1]] = 0
                    maxM = [self.M / data1[i], i]
                else:
                    data1[i] = 0
        
        self.maxM = maxM
        self.Λ_max = table.Coef(data0)
        self.Λ_D = table.Coef(data1)
        self.Λ = table.Coef(data2)


    def gradientVector(self) -> TT.BinaryTable:
        """[O(n) Method to determine the highest gradient vector to determine the most efficient cost / profit value]

        Returns:
            TT.BinaryTable: [Binary table consisting of a single variable representing the cost / profit values]
        """
        efV = [0, 1]
    
        for i in range(self.C.width):
            efCheck = [self.P.matrix[0][i], self.C.matrix[0][i]]
            if (self.C.matrix[0][i] > self.M):
                self.P.nullify(i)
                self.C.nullify(i)
                continue
            if (efCheck[0] / efCheck[1] > efV[0] / efV[1]):
                efV = [self.P.matrix[0][i], self.C.matrix[0][i]]

    def exponentialIteration(self, iteration = -1) -> TT.BinaryTable:
        """[O(2^n) Method to determine the profitable cost / value relationship with each iteration through removal of coefficients to determine the most efficient cost / profit value]

        Args:
            iteration (int, optional): [The amount of iterations to perform the determination]. Defaults to -1, iterates until the maximal profit is reached.

        Returns:
            TT.BinaryTable: [Binary table consisting of a single variable representing the cost / profit values]
        """
        DiscreteP = self.P.mult(self.Λ).matrix[0][0] + ((self.table.label.height - 1) * self.P.matrix[0][0]) / self.table.label.height
        self.Λ_D.matrix[self.maxM[1]][0] -= 2
        while(iteration != 0):
            for i in range(self.table.label.height):
                if self.P.mult(self.Λ_D).matrix[0][0] >= DiscreteP and C.mult(self.Λ_D).matrix[0][0] >= 0:
                    C += 1
            iteration -= 1

    def maximalLambdaIteration(self) -> TT.BinaryTable:
        """[O(n^2) Method ]

        Returns:
            TT.BinaryTable: [description]
        """
        return 0

    

    def __str__(self) -> str:
        return "The given table: " + "\n" + self.table + "\n" + "The Λ maximal coeficients and equal digit coeficients: " + "\n" + self.Λ_max + "\n" + self.Λ_D + "respectively." + "\n" + "The maximal profitable single coeficient: " + "\n" + self.Λ


# Calculate most efficient cost combination from a table for a given maximum cost
def BinaryEfficiency(M, table = TT.BinaryTable(), iteration = -1):
    print("The given table: " + "\n" + table.__str__())                                # O(H)
    data0, data1, dataG = [], [], []
    C = TT.Matrix(table.label.height, 1, table.label.getVertex(-1, 0))      # O(2H)
    P = TT.Matrix(table.label.height, 1, table.label.getVertex(-1, 1))      # O(2H)
    sumVert = C.sumVertex(0, -1)                                             # O(H)
    max = [M/C.matrix[0][0], 0]
    for i in range(table.label.height):                                               # O(H)
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
    #The upper vector & maximum coeficient method

    efV = [0, 1]
    

    for i in range(C.width):
        efCheck = [P.matrix[0][i], C.matrix[0][i]]
        if (C.matrix[0][i] > M):
            P.nullify(i)
            C.nullify(i)
            continue
        if (efCheck[0] / efCheck[1] > efV[0] / efV[1]):
            efV = [P.matrix[0][i], C.matrix[0][i]]
        
    
    #==============================================================================================================================================================================

    #==============================================================================================================================================================================
    #Discrete method for finding most efficient coeficients
    if (False):
        DiscreteP = P.mult(Λ).matrix[0][0] + ((table.label.height - 1) * P.matrix[0][0]) / table.label.height
        Λ_D.matrix[max[1]][0] -= 2
        while(iteration != 0):
            for i in range(table.label.height):
                if P.mult(Λ_D).matrix[0][0] >= DiscreteP and C.mult(Λ_D).matrix[0][0] >= 0:
                    C += 1
            iteration -= 1
            
                
    #==============================================================================================================================================================================
    #The same method but without P deciding the coeficients
    if (False):
        print('')
    print("The Λ maximal coeficients and equal digit coeficients: " + "\n" + str(Λ_max) + "\n" + str(Λ_D) + "respectively.")
    print("The maximal profitable single coeficient: " + "\n" + str(Λ))
    print(C)

    #for i in range(iteration):
     #   while true:



# Calculate most efficient cost combination given a dependency table for a given maximum cost
def DependentBinaryEfficiency(M, table = TT.BinaryTable(), dependent = TT.BinaryTable(), iteration = -1):
    data0, data1 = [], []

BinaryEfficiency(20000, TT.BinaryTable([200, 50, 300, 70, 600, 100, 2000, 500, 2500, 650, 4000, 900]), 10)