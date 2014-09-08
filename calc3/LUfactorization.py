# Matthew Ersted
# LU Factorization
# 2/20/14

# Asks the user for size of matrix
input_n = input("Enter size of nxn matrix:")
n = int(input_n)

#hold matrix data in a list titled matrix
matrix = []
#each row to be held in aList
aList = []

#gather the matrix entries from the user
for x in range(1, n + 1): #row x
    for y in range(1, n + 1): #column y
        #convert integers to string to be printed out
        stringx = str(x)
        stringy = str(y)
        i = input("Enter entry for column " + stringy + " and row " + stringx + ":")
        m = int(i)
        aList.append(m)
    #appends row to entire matrix
    matrix.append(aList)
    #resets aList to empty list
    aList = []
    
#saves original matrix to print out later
printout = matrix

#initializes lower and upper triangular matrix lists
l = []
u = []

#each row of identity matrix to be held in listlist
#to be appended to lower matrix list
listlist = []

#initializes lower triangular matrix as the identity matrix
for x in range(n):
    for y in range(n):
        #puts 1's on the main diagonal
        if x == y:
            num = 1
        #puts 0's everywhere else
        else: 
            num = 0
        listlist.append(num)
    #appends row to matrix
    l.append(listlist)
    listlist = []

#gaussian elimination
for i in range(n):
    for z in range(i + 1, n):
        #calculates multiple from ratio of entries in row
        mult = matrix[z][i] / matrix[i][i]
        l[z][i] = mult #changes 0 in lower triangular matrix to the multiple
        #applies the row elimination to original matrix to find upper
        for k in range(n):
            matrix[z][k] = matrix[z][k] - mult * matrix[i][k]

#sets upper triangular matrix to altered original matrix
u = matrix

#prints out original matrix, with its lower and upper triangular
#matrices as its factorization
print("original matrix:")
print(printout)
print("lower triangular:")
print(l)
print("upper triangular:")
print(u)
