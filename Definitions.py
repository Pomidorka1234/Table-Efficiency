class Matrix:
    def __init__(self, height, width, data):
        self.height = height
        self.width = width
        self.matrix = []
        for i in range(self.height):
            self.matrix.append([])
            for j in range(self.width):
                self.matrix[i].append(data[j + i * self.width])
        self.raw = data
    
    #def mult(self, matrix):
        #if (self.width == matrix.height):
        #    return Matrix(self.height, matrix.width, )



class Table:
    def __init__(self, props):
        self.label = { }
        for i in range(len(props)):
            self.label.update(props[i])
    
    def sum(self, data = []):
        if len(data) == 0:
            data = self.label["cost"]
        sum = 0
        for i in range(data.height * data.width):
            sum += data.raw[i]
        return sum

class BinaryTable(Table):
    def __init__(self, cost, profit):
        self.label = {
            "cost": Matrix(len(cost), 1, cost),
            "profit": Matrix(len(profit), 1, profit)
        }
        super().__init__([cost, profit])

    def Gamma(self, data):
        return Matrix(self.sum(self.label["cost"]), 1, data)