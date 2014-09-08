# Matt Ersted and Saikrishna Arcot
# Least Squares using Python
# Initializing matrices A and b for line
matrix_a = [[0.0, 1.0], [1.0, 1.0], [2.0, 1.0], [3.0, 1.0], [4.0, 1.0]]
matrix_b = [1.5, 2.5, 3.5, 5.0, 7.5]
matrix_at = []
# Transposing A
for x in range(len(matrix_a[0])):
    tempList = []
    for i in range(len(matrix_a)):
        value = matrix_a[i][x]
        tempList.append(value)
    matrix_at.append(tempList)
# Multiplying At by A to get AtA
matrix_ata = []
for x in range(2):
    sum1 = 0
    sum2 = 0
    m = 0
    for i in range(5):
        value1 = matrix_at[x][i] * matrix_a[i][m]
        value2 = matrix_at[x][i] * matrix_a[i][m + 1]
        sum1 += value1
        sum2 += value2
    matrix_ata.append([sum1, sum2])
# Multiplying At by b to get Atb
matrix_atb = []
for x in range(2):
    sum3 = 0
    for i in range(5):
        value = matrix_at[x][i] * matrix_b[i]
        sum3 += value
    matrix_atb.append(sum3)
# Augment matrices A and b for row reduction
temp_matrix_ata = matrix_ata
temp_matrix_ata[0].append(matrix_atb[0])
temp_matrix_ata[1].append(matrix_atb[1])
matrix = [temp_matrix_ata[0], temp_matrix_ata[1]]
# Gaussian Elimination for row echelon form
z = 1
i = 0
mult = matrix[z][i] / matrix[i][i]
for k in range(3):
    matrix[z][k] = matrix[z][k] - mult * matrix[i][k]
# Gaussian Elimination for row reduced echelon form
mult = matrix[i][z] / matrix[z][z]
for k in range(3):
    matrix[i][k] = matrix[i][k] - mult * matrix[z][k]
x = len(matrix[0]) - 1
# Dividing row 1 by m11
for d in range(2):
    matrix[d][x] = matrix[d][x] / matrix[d][d]
    matrix[d][d] = matrix[d][d] / matrix[d][d]
a = matrix[0][2]
b = matrix[1][2]
print("The line of best fit is y = {0:.2f}x + {1:.2f}".format(a, b))
#---------------------------------------------------------------------
# Initializing matrices A and b for parabola
matrix_a = [[0.0, 0.0, 1.0], [1.0, 1.0, 1.0], [4.0, 2.0, 1.0], 
                [9.0, 3.0, 1.0], [16.0, 4.0, 1.0]]
matrix_b = [1.5, 2.5, 3.5, 5.0, 7.5]
matrix_at = []
# Transposing A
for x in range(len(matrix_a[0])):
    tempList = []
    for i in range(len(matrix_a)):
        value = matrix_a[i][x]
        tempList.append(value)
    matrix_at.append(tempList)
# Multiplying At by A to get AtA
matrix_ata = []
for x in range(3):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    m = 0
    for i in range(5):
        value1 = matrix_at[x][i] * matrix_a[i][m]
        value2 = matrix_at[x][i] * matrix_a[i][m + 1]
        value3 = matrix_at[x][i] * matrix_a[i][m + 2]
        sum1 += value1
        sum2 += value2
        sum3 += value3
    matrix_ata.append([sum1, sum2, sum3])
# Multiplying At by b to get Atb
matrix_atb = []
for x in range(3):
    sum3 = 0
    for i in range(5):
        value = matrix_at[x][i] * matrix_b[i]
        sum3 += value
    matrix_atb.append(sum3)
# Augment matrices A and b for row reduction
temp_matrix_ata = matrix_ata
for e in range(3):
    temp_matrix_ata[e].append(matrix_atb[e])
matrix = [temp_matrix_ata[0], temp_matrix_ata[1], temp_matrix_ata[2]]
# Gaussian elimination for row echelon form
for i in range(2):
    for z in range(i + 1, 3):
        #calculates multiple from ratio of entries in row
        mult = matrix[z][i] / matrix[i][i]
        for k in range(4):
            matrix[z][k] = matrix[z][k] - mult * matrix[i][k]
# Gaussian elimination for row reduced echelon form
for n in range(2):
    mult = matrix[n][2] / matrix[2][2]
    for k in range(4):
        matrix[n][k] = matrix[n][k] - mult * matrix[2][k]
mult = matrix[0][1] / matrix[1][1]
for k in range(4):
    matrix[0][k] = matrix[0][k] - mult * matrix[1][k]
# Dividing each row by its respective pivot value
for z in range(3):
    matrix[z][3] = matrix[z][3] / matrix[z][z]
    matrix[z][z] = matrix[z][z] / matrix[z][z]
a = matrix[0][3]
b = matrix[1][3]
z = matrix[2][3]
print("The parabola of best fit is y = {0:.2f}x^2 + {1:.2f}x + {2:.2f}".format(a, b, z))