import random


# returns n (rows) x m (cols) matrix with random values ranging from a to b
def init_random_matrix(n, m, a=0, b=0):
    M = []
    for y in range(n):
        M.append([random.randint(a, b) for _ in range(m)])
    return M

# print matrix format
def print_matrix(M):
    for y in range(len(M)):
        for x in range(len(M[y])):
            print("{0:>8}".format(str(M[y][x])),end="")
        print()

# multiply two matrices 
def matrix_multiplication(M1, M2):
    if not len(M1[0]) == len(M2):       # Spaltenzahl von M1 muss gleich Zeilenzahl von M2 sein!
        if len(M1) == len(M2[0]):
            return matrix_multiplication(M2, M1)
        else:
            print("Error - Multiplication is not possible with given dimensions")
            return

    n = len(M1)
    m = len(M1[0])
    d = len(M2[0])
    M_mul = init_random_matrix(n, d)
    for N in range(n):
        for D in range(d):
            for M in range(m):
                M_mul[N][D] += M1[N][M] * M2[M][D]

    return M_mul




# 4x3 matrix; Werte von 1 bis 9
# 4 zeilen und 3 spalten
# M = init_random_matrix(4,3,1,9)
# print("Zeilen = ", len(M))              # = n
# print("Spalten = ", len(M[0]))          # = m
# print_matrix(M)
#  M1 *  M2 = Mneu
# 3x2 * 2x4 = 3x4
# nxm * mxd = nxd


# drive code
M1 = init_random_matrix(3,2,-99,99)
M2 = init_random_matrix(2,4,-99,99)
M_neu = matrix_multiplication(M1, M2)

print("M1")
print_matrix(M1)
print("\nM2")
print_matrix(M2)
print("\nM1 * M2")
print_matrix(M_neu)