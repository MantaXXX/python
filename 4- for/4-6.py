# In mathematics, the factorial of an integer n, denoted by n! is the following product:
# n! = 1 × 2 × … × n
# For the given integer n calculate the value n!. Don't use math module in this exercise.

sum = 1
for i in range(1, int(input())+1):
  sum *= i

print(sum)