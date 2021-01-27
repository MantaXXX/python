# For a given integer N, print all the squares of positive integers where the square is less than or equal to N, in ascending order.

n = int(input())
i = 1
while i**2 <= n:
  print(i**2, end=' ')
  i += 1