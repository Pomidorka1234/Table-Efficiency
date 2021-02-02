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

    def add(self, other):
        if (self.width == other.width and self.height == other.height):
            for i in range(self.height):
                for j in range(self.width):
                    self.matrix[i][j] += other.matrix[i][j]
    
    def mult(self, other):
        if (self.width == other.height):
            rawData = []
            for i in range(self.height * other.width):
                sum = 0
                for j in range(self.width):
                    sum += self.matrix[i - int(i/self.width)][j] * other.matrix[j][i - int(i/self.width)]
                rawData.append(sum)
            return Matrix(self.height, other.width, rawData)

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

    def sumVertex(self, row = -1, column = -1):
        sum = 0
        if row >= 0 and column == -1:
            for cell in self.matrix[row]:
                sum += cell
        if row == -1 and column >= 0:
            for i in range(self.height):
                sum += self.matrix[i][column]
        return sum

    def __str__(self):
        matrix = ''
        for i in range(self.height):
            for j in range(self.width):
                bracket = ''
                cell = self.matrix[i][j]
                if i == 0 and j == 0:
                    space = 0
                else:
                    space = len(str(cell - 1)) - 1
                    if len(str(cell - 1)) != len(str(cell)):
                        space += 1
                
                if i != 0 and (j == 0 or j == self.width - 1):
                    bracket = '∣  '
                if i == self.height - 1 and j == 0:
                    bracket = '⌊  '
                if i == 0 and j == 0:
                    bracket = '⌈  '
                    if self.height == 1:
                        bracket = '[  '
                matrix += bracket + str(self.matrix[i][j]) + "  " + " " * (len(str(self.matrix[self.height - 1][self.width - 1])) - 2 - space)

                bracket = ''

                if i != 0 and (j == 0 or j == self.width - 1):
                    bracket = '∣  '
                if i == self.height - 1 and j == self.width - 1:
                    bracket = '⌋'
                if i == 0 and j == self.width - 1:
                    bracket = '⌉'
                    if self.height == 1:
                        bracket = ']'
                
                matrix += bracket
            matrix += '\n'
        return matrix



class Table:
    def __init__(self, width ,rawData = ["x0", "y0"]):
        try:
            self.label = Matrix(width, int(len(rawData)/width), rawData)
        except:
            print("Please provide correct input")

    def __str__(self):
        table = ""
        for i in range(self.label.height):
            table += 'L' + str(i) + " | " + Matrix(self.label.width, 1, self.label.getVertex(i, -1)).__str__()
        return table
        

class BinaryTable(Table):

    def __init__(self, rawData = [0, 0]):
        super().__init__(2, rawData)


    def Coef(self, rawData):
        return Matrix(1, self.label.height, rawData)