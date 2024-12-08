a = [[1, 2], [3, 4]]
b = [[2, 0], [1, 2]]
result = [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
print('Resultant Matrix:', result)