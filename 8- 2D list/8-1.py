# Given two integers - the number of rows m and columns n of m×n 2d list - and subsequent m rows of n integers, followed by one integer c. Multiply every element by c and print the result.

# 讀資料
row, col = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(row)]
mul = int(input())

for i in range(row):
    for j in range(col):
        a[i][j] *= mul

for row in a:
    print(*a)
