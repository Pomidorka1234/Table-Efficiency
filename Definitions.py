class Matrix:
    def __init__(self, width, height, rawData):
        self.width = width
        self.height = height
        self.raw = rawData
        self.matrix = []
        for i in range(self.height):
            self.matrix.append([])
            for j in range(self.width):
                self.matrix[i].append(self.raw[j + i * self.width])
    
    #def mult(self, matrix):
        #if (self.width == matrix.height):
        #    return Matrix(self.height, matrix.width, )

    def getVertex(self, row = -1, column = -1):
        Pos = []
        if column != -1:
            for i in range(self.height):
                Pos.append(self.matrix[i][column])
            

        if row != -1:
            if Pos == []:
                Pos = self.matrix[row]
            else:
                Pos = Pos[row]
        return Pos



    def __str__(self):
        matrix = ''
        for i in range(self.height):
            for j in range(self.width):
                cell = self.matrix[i][j]
                if i == 0 and j == 0:
                    space = 0
                else:
                    space = len(str(cell - 1)) - 1
                    if len(str(cell - 1)) != len(str(cell)):
                        space += 1
                matrix += str(self.matrix[i][j]) + "  " + " " * (len(str(self.matrix[self.height - 1][self.width - 1])) - 1 - space)
            matrix += '\n'
        return matrix



class Table:
    def __init__(self, width ,rawData = ["x0", "x1"]):
        #try:
            self.label = Matrix(width, int(len(rawData)/width), rawData)
        #except:
        #    print("Please provide correct input")
    
    def sumVertex(self, vertex = ['column', 0]):
        sum = 0
        for i in self.label.getVertex(vertex[0] == vertex[1]):
            sum += i
        return sum

    def __str__(self):
        table = ""
        for i in range(self.label.height):
            table += 'L' + str(i) + " | " + Matrix(self.label.width, 1, self.label.getVertex(i, -1)).__str__()
        return table
        

class BinaryTable(Table):

    def __init__(self, rawData = [0, 0]):
        super().__init__(2, rawData)


    def Gamma(self, rawData):
        return Matrix(1, self.label.height, rawData)