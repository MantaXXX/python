# Given an integer not less than 2. Print its smallest integer divisor greater than 1.

a = int(input())
i = 1
while i <= a:
  if a % i == 0 and i > 1:
    print(i)
    break
  i += 1


# 另外寫法
a = int(input())
i = 2
while a % i != 0:
  i += 1
print(i)