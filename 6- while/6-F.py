# Fibonacci numbers are the numbers in the integer sequence starting with 1, 1 where every number after the first two is the sum of the two preceding ones:

# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# Given a positive integer n, print the nth Fibonacci number.

n = int(input())
a = 1
b = 1
i = 3
while i <= n:
    a, b = b, a+b
    i += 1

print(b, end=' ')

# 另外寫法
prev, next = 1, 1
n = int(input())
for i in range(n - 2):
    prev, next = next, prev + next
print(next)
