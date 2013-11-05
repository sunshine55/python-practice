matrix = dict()
# Establish a 2x2 matrix
matrix[(0,0)] = 0
matrix[(0,1)] = 1
matrix[(1,0)] = 2
matrix[(1,1)] = 3

for key,item in matrix.items():
    print key, item