# დაწერეთ პროგრამა, რომელიც დაბეჭდავს ორი მატრიცის ჯამს, ჯამი გამოითვლება შემდეგი წესით, 
# ერთი და იგივე ადგილზე მდგომი ელემენტები ემატება ერთმანეთს, მატრიცების განზომილებები უნდა იყოს ერთი და იგივე

# This program adds two matrix
matrix_a = [
    [7, 5, 3, 6],
    [2, 5, 6, 9],
    [6, 8, 9, 2]
]

matrix_b = [
    [2, 6, 4, 8],
    [8, 7, 5, 7],
    [3, 9, 1, 6]
]

matrix_sum = []

for i in range(len(matrix_a)):
    matrix_sum.append(list())
    for j in range(len(matrix_a[i])):
        matrix_sum[i].append(matrix_a[i][j] + matrix_b[i][j])
        
print(matrix_sum)