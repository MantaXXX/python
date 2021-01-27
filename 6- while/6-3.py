# For a given integer X, find the greatest integer n where 2ⁿ is less than or equal to X. Print the exponent value and the result of the expression 2ⁿ.

x = int(input())
i = 1
while 2**i <= x:
  i += 1
print(i-1, 2 ** (i-1))