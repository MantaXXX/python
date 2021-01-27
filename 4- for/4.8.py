# In mathematics, the factorial of an integer n, denoted by n! is the following product:
# n! = 1 × 2 × … × n

# For the given integer n calculate the value
# 1! + 2! + 3! + ... + n!

n = int(input())
sum = 0
for i in range(1, n+1):
  prod = 1
  for j in range (1, i+1):
    prod *= j

  sum += prod
print(sum)