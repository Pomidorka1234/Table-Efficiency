import TableClasses as TC
import math
import dataclasses as DC
from numpy import arange, sin
import numpy
from matplotlib import pyplot
class BinaryAlgorithms:
    def __init__(self, M: int, table: TC.BinaryTable):
        """
            O(n) Initialize variables for work with tables and efficiency algorithms
        """
        self.table = table
        self.M = M
        self.C = TC.Matrix(self.table.label.height, 1, self.table.label.getVertex(-1, 0))
        self.P = TC.Matrix(self.table.label.height, 1, self.table.label.getVertex(-1, 1))
        self.Csum = self.C.sumVertex(0, -1)
        self.Psum = self.P.sumVertex(0, -1)
        
        data0, data1, data2 = [], [], []
        maxM = [self.M / self.C.matrix[0][0], 0]
        for i in range(self.table.label.height):
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
        self.Λ_max = self.table.Coef(data0)
        self.Λ_D = self.table.Coef(data1)
        self.Λ = self.table.Coef(data2)

    def setTable(self, point: list) -> None:
        """[setter with dependencies: C,P,Csum,Psum]

        Args:
            point (int[2]): [the point to append]
        """
        self.table.label.matrix.append(point)
        self.C.matrix[0].append(point[0])
        self.P.matrix[0].append(point[1])
        self.C.width += 1
        self.P.width += 1
        self.Csum += point[0]
        self.Psum += point[1]


    def gradientVector(self, plot: bool) -> TC.BinaryTable:

        """[O(n * log(n)) Method to determine the highest gradient vector to determine the most efficient cost / profit value, estimated space short: (n * ⌊log(n) + 1⌋)]

        Args:
            plot (bool): [Whether to plot the graph or not]

        Returns:
            TC.BinaryTable: [Binary table consisting of a single variable representing the cost / profit values]
        """

        
        j, counter, limit = 0, 0, 0
        sus = []
        while counter != self.C.width :
            efV = [1, 0]
            for i in range(self.C.width):
                if j < self.C.width:
                    sus.append(True)
                j += 1
                if (sus[i] == False):
                    continue
                efCheck = [self.C.matrix[0][i], self.P.matrix[0][i]]

                if (efCheck[0] + limit > self.M):
                    sus[i] = False
                    counter += 1
                    continue
                if (efCheck[1] / efCheck[0] > efV[1] / efV[0]):
                    efV = [self.C.matrix[0][i], self.P.matrix[0][i]]
            limit = numpy.floor((self.M - limit) / efV[0]) * efV[0] + limit

        if (plot):
            x = arange(0, self.C.width + 1, 1)
            y = numpy.floor(numpy.log2(self.C.width) + 1) * self.C.width
            O = numpy.floor(numpy.log2(self.C.width)) * self.C.width

            pyplot.plot(x, (y / self.C.width) * x)
            pyplot.plot(x, (O / self.C.width) * x)

            pyplot.scatter(self.C.width, j)
            
            

    def exponentialIteration(self, iteration = -1) -> TC.BinaryTable:
        """[O(2^n) Method to determine the profitable cost / value relationship with each iteration through removal of coefficients to determine the most efficient cost / profit value]

        Args:
            iteration (int, optional): [The amount of iterations to perform the determination]. Defaults to -1, iterates until the maximal profit is reached.

        Returns:
            TC.BinaryTable: [Binary table consisting of a single variable representing the cost / profit values]
        """
        DiscreteP = self.P.mult(self.Λ).matrix[0][0] + ((self.table.label.height - 1) * self.P.matrix[0][0]) / self.table.label.height
        self.Λ_D.matrix[self.maxM[1]][0] -= 2
        while(iteration != 0):
            for i in range(self.table.label.height):
                if self.P.mult(self.Λ_D).matrix[0][0] >= DiscreteP and C.mult(self.Λ_D).matrix[0][0] >= 0:
                    C += 1
            iteration -= 1

    def maximalLambdaIteration(self) -> TC.BinaryTable:
        """[O(n^2) Method ]

        Returns:
            TC.BinaryTable: [description]
        """
        return 0

    

    def __str__(self) -> str:
        return "The given table: " + "\n" + self.table + "\n" + "The Λ maximal coeficients and equal digit coeficients: " + "\n" + self.Λ_max + "\n" + self.Λ_D + "respectively." + "\n" + "The maximal profitable single coeficient: " + "\n" + self.Λ


# Calculate most efficient cost combination from a table for a given maximum cost
def BinaryEfficiency(M, table = TC.BinaryTable(), iteration = -1):
    print("The given table: " + "\n" + table.__str__())                                # O(H)
    data0, data1, dataG = [], [], []
    C = TC.Matrix(table.label.height, 1, table.label.getVertex(-1, 0))      # O(2H)
    P = TC.Matrix(table.label.height, 1, table.label.getVertex(-1, 1))      # O(2H)
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
def DependentBinaryEfficiency(M, table = TC.BinaryTable(), dependent = TC.BinaryTable(), iteration = -1):
    data0, data1 = [], []

#BinaryEfficiency(20000, TC.BinaryTable([200, 50, 300, 70, 600, 100, 2000, 500, 2500, 650, 4000, 900]), 10)