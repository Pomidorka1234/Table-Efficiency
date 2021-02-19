import TableClasses as TC
#import localib as lb
import math
#import dataclasses as DC
from numpy import arange
import numpy
from matplotlib import pyplot

class BinaryAlgorithms:
    def __init__(self, M: int, table: TC.BinaryTable) -> None:
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
        self.Λ_max = TC.Matrix(1, self.C.width, data0)
        self.Λ = TC.Matrix(1, self.C.width, data1)
        self.Λ_D = TC.Matrix(1, self.C.width, data2)

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


    def gradientVector(self, plot: bool) -> TC.Matrix:

        """[O(n * log(n)) Method to determine the highest gradient vector to determine the most efficient cost / profit value, estimated space short: (n * ⌊log(n) + 1⌋)]

        Args:
            plot (bool): [Whether to plot the graph or not]

        Returns:
            TC.BinaryTable: [Binary table consisting of a single variable representing the cost / profit values]
        """

        Λ = TC.Matrix(0, 0, 0)
        Λ.height = self.C.width
        Λ.width = 1
        j, counter, limit = 0, 0, 0
        sus = []
        while counter != self.C.width:
            efV = [self.C.matrix[0][0], self.P.matrix[0][0], 0]
            for i in range(self.C.width):
                if j < self.C.width:
                    sus.append(True)
                    Λ.matrix.append([0])
                j += 1
                if (sus[i] == False):
                    continue

                efCheck = [self.C.matrix[0][i], self.P.matrix[0][i]]

                if (efCheck[0] + limit > self.M):
                    sus[i] = False
                    counter += 1
                    continue
                if (efCheck[1] / efCheck[0] > efV[1] / efV[0]):
                    efV = [self.C.matrix[0][i], self.P.matrix[0][i], i]
            
            Λ.matrix[efV[2]][0] += int(numpy.floor((self.M - limit) / efV[0]))

            limit = efV[0] * numpy.floor((self.M - limit) / efV[0]) + limit

        if (plot):
            x = arange(0, self.C.width + 1, 1)
            y = numpy.floor(numpy.log2(self.C.width) + 1) * self.C.width
            O = numpy.floor(numpy.log2(self.C.width)) * self.C.width

            pyplot.plot(x, (y / self.C.width) * x, (O / self.C.width) * x)

            pyplot.scatter(self.C.width, j, 5, 5)

        return Λ
            
            

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
        return "The given table: " + "\n" + self.table.__str__() + "\n" + "The Λ maximal coeficients and equal digit coeficients: " + "\n" + self.Λ_max.__str__() + "\n" + self.Λ_D.__str__() + "respectively." + "\n" + "The maximal profitable single coeficient: " + "\n" + self.Λ.__str__()

class BinaryDependencyAlgorithms:
    def __init__(self, M: int, table: TC.BinaryTable, penalty: list) -> None:
        self.M = M
        self.penalty = penalty
        self.table = table
        self.remainder = self.table.tableGtransform(self.penalty[0], self.penalty[1])
        self.remainder2 = 0

        self.C = TC.Matrix(self.table.label.height, 1, self.table.label.getVertex(-1, 0))
        self.P = TC.Matrix(self.table.label.height, 1, self.table.label.getVertex(-1, 1))
        self.Csum = self.C.sumVertex(0, -1)
        self.Psum = self.P.sumVertex(0, -1)

    def gradientVector(self):
        Λ = TC.Matrix(0, 0, 0)
        Λ.height = self.C.width
        Λ.width = 1
        j, counter, limit = 0, 0, 0
        sus = []

        while counter != self.C.width:
            efV = [self.C.matrix[0][0], self.P.matrix[0][0], 0]
            for i in range(self.C.width):
                if j < self.C.width:
                    sus.append(True)
                    Λ.matrix.append([0])
                j += 1
                if (sus[i] == False):
                    continue

                efCheck = [self.C.matrix[0][i], self.P.matrix[0][i]]

                if (efCheck[0] + limit > self.M):
                    sus[i] = False
                    counter += 1
                    continue
                if (efCheck[1] / efCheck[0] > efV[1] / efV[0]):
                    efV = [self.C.matrix[0][i], self.P.matrix[0][i], i]

            remainder2 = 0
            Λ.matrix[efV[2]][0] += int(numpy.floor((self.M - limit) / (efV[0] + (self.penalty[1] * self.remainder[efV[2]]) / self.penalty[0]) - remainder2))

            limit = efV[0] * numpy.floor((self.M - limit) / efV[0]) + limit

"""class NarySimiliarAlgorithms:
    def __init__(self, M: int, table: TC.Table, treeRelationship: lb.NaryTree) -> None:

        self.table = table
        self.tree = treeRelationship
        self.M = M
        self.C = TC.Matrix(self.table.label.height, 1, self.table.label.getVertex(-1, 0))
        self.P = TC.Matrix(self.table.label.height, 1, self.table.label.getVertex(-1, 1))
        self.Csum = self.C.sumVertex(0, -1)
        self.Psum = self.P.sumVertex(0, -1)

    def convertToBinary(self) -> BinaryAlgorithms:
        while(self.tree.)


class NarySimiliarDependencyAlgorithms:
    def __init__(self, M: int, table: TC.Table, penalty: list, treeRelationship: lb.NaryTree) -> None:

        self.table = table
        self.M = M
        self.C = TC.Matrix(self.table.label.height, 1, self.table.label.getVertex(-1, 0))
        self.P = TC.Matrix(self.table.label.height, 1, self.table.label.getVertex(-1, 1))
        self.Csum = self.C.sumVertex(0, -1)
        self.Psum = self.P.sumVertex(0, -1)
"""

class NaryAlgorithms:
    def __init__(self, M: int, table: TC.Table) -> None:

        self.table = table
        self.M = M
        self.C = TC.Matrix(self.table.label.height, 1, self.table.label.getVertex(-1, 0))
        self.P = TC.Matrix(self.table.label.height, 1, self.table.label.getVertex(-1, 1))
        self.Csum = self.C.sumVertex(0, -1)
        self.Psum = self.P.sumVertex(0, -1)

class NaryDependencyAlgorithms:
    def __init__(self, M: int, table: TC.Table, penalty: list) -> None:

        self.table = table
        self.M = M
        self.C = TC.Matrix(self.table.label.height, 1, self.table.label.getVertex(-1, 0))
        self.P = TC.Matrix(self.table.label.height, 1, self.table.label.getVertex(-1, 1))
        self.Csum = self.C.sumVertex(0, -1)
        self.Psum = self.P.sumVertex(0, -1)