import BasicConcepts as BC

class Matrix:
    """Matrix that is of a list * list type"""

    def __init__(self, width: int, height: int, rawData: list) -> None:
        """O(n*m) Initializes the matrix type

        Args:
            width (int): [the width of the matrix]
            height (int): [the height of the matrix]
            rawData (list): [raw list to distribute in the matrix]
        """
        self.width = width
        self.height = height
        self.matrix = []
        for i in range(self.height):
            self.matrix.append([])
            for j in range(self.width):
                self.matrix[i].append(rawData[j + i * self.width])

    def add(self, other):
        """[O(n^2) Add two matrices]

        Args:
            other (Matrix): [The second matrix to append]

        Returns:
            Matrix: [Added matrix]
        """
        if (self.width == other.width and self.height == other.height):
            newMatrix = []
            for i in range(self.height):
                newMatrix.append([])
                for j in range(self.width):
                    newMatrix[i].append(self.matrix[i][j] + other.matrix[i][j])
            return newMatrix
        else:
            return 'Unaddable matrices'

    def mult(self, other):
        """[O(n^2) Multiply two matrices]

        Args:
            other (Matrix): [The second multipliable]

        Returns:
            [Matrix]: [Multiplied matrix]
        """
        if (self.width == other.height):
            rawData = []
            for i in range(self.height * other.width):
                sumCross = 0
                for j in range(self.width):
                    sumCross += self.matrix[i - int(i/self.width)][j] * other.matrix[j][i - int(i/self.width)]
                rawData.append(sumCross)
            return Matrix(self.height, other.width, rawData)
        else:
            return "immultiplicable matrices"

    def getVertex(self, row = -1, column = -1):
        """[O(n) Get a vertex or a value inside the matrix]

        Args:
            row (int, optional): [The row vertex]. Defaults to -1.
            column (int, optional): [The column vertex]. Defaults to -1.

        Returns:
            [Matrix]: [The chosen vertex, or a value or none in default]
        """
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

    def sumVertex(self, row = -1, column = -1) -> int:
        """[O(n) Get the sum of value in a vertex]

        Args:
            row (int, optional): [The row vertex]. Defaults to -1.
            column (int, optional): [The column vertex]. Defaults to -1.

        Returns:
            [int]: [The chosen vertex to sum up]
        """
        sum = 0
        if row >= 0 and column == -1:
            for cell in self.matrix[row]:
                sum += cell
        if row == -1 and column >= 0:
            for i in range(self.height):
                sum += self.matrix[i][column]
        return sum

    def nullify(self, row = -1, column = -1) -> None:
        """[O(n) Nullify a vertex or a value inside a matrix]

        Args:
            row (int, optional): [description]. Defaults to -1.
            column (int, optional): [description]. Defaults to -1.
        """
        
        if column != -1 and row != -1:
            self.matrix[row][column] = None

        if column != -1 and row == -1:
            for i in range(self.height):
                self.matrix[i][column] = None
            
        if column == -1 and row != -1:
            self.matrix[row] = None

    def __str__(self) -> str:
        """[O(n*m) Format a string of n by m matrix]

        Returns:
            [str]: [Represent the matrix in the mathematical matrix format]
        """
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
                
                if i != 0 and (j == 0):
                    bracket = '∣  '
                if i == self.height - 1 and j == 0:
                    bracket = '⌊  '
                if i == 0 and j == 0:
                    bracket = '⌈  '
                    if self.height == 1:
                        bracket = '[  '
                matrix += bracket + str(self.matrix[i][j]) + "  " + " " * (len(str(self.matrix[self.height - 1][self.width - 1])) - 2 - space)

                bracket = ''

                if i != 0 and (j == self.width - 1):
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
    """
        Table that is of a list * matrix type
    """
    def __init__(self, width: int ,rawData: list) -> None:
        """[O(n) Initialize table's matrix]

        Args:
            width (int): [the width of table's matrix]
            rawData (list): [raw list to distribute in the table's matrix by list's size per width]. Defaults to ["x0", "y0"].
        """
        
        self.label = Matrix(width, int(len(rawData)/width), rawData)

        
    def tableGtransform(self, x: int, n: int) -> list:
        remainder = []
        for i in range(self.label.height):
            gmod = BC.G(self.label.matrix[i][1], x, n)
            self.label.matrix[i][0] += gmod
            remainder.append(self.label.matrix[i][1] - gmod)
        return remainder
            

    def __str__(self) -> str:
        """[O(n*m) Format a string of n by m matrix]

        Returns:
            [str]: [Represent the table in the tabled matrix format]
        """
        
        table = ""
        for i in range(self.label.height):
            table += 'L' + str(i) + " |  "
            for j in range(self.label.width):
                space = " " * (len(str(self.label.matrix[self.label.height - 1][j])) - len(str(self.label.matrix[i][j])))
                table += space + str(self.label.matrix[i][j]) + "  "
            table += '\n'
        return table
        

class BinaryTable(Table):
    """[Binary table that is of a Table type]

    Args:
        Table (Table): [Table super type]
    """
    def __init__(self, rawData: list) -> None:
        """[O(n) Initialize table's matrix]

        Args:
            rawData (list, optional): [raw list to distribute in the table's matrix by half of a list's size]. Defaults to [0, 0].
        """
        super().__init__(2, rawData)


    def Coef(self, rawData: list) -> Matrix:
        """[Make a Matrix of table's height]

        Args:
            rawData (list): [raw list to distribute in the table's matrix by list's size]

        Returns:
            [Matrix]: [Heighted matrix]
        """
        return Matrix(1, self.label.height, rawData)