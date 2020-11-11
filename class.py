import random


class Matrix:
    def __init__(self, n, m, a, b):             # n*m matrix (rows*cols) 
        self.M = []
        for y in range(n):
            self.M.append([random.randint(a, b) for _ in range(m)])


    def __str__(self):
        s = ""
        for y in range(len(self.M)):
            for x in range(len(self.M[y])):
                s += ("{0:>5}".format(str(self.M[y][x]))) + " "
            s += "\n"
        return s

    # multiply two matrices 
    def __mul__(self, other):
        pass



# 4x3 matrix; Werte von 1 bis 9
M = Matrix(4,3,1,9)
print(M)
print(M.M)