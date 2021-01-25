# Given a three-digit number. Find the sum of its digits.

number = int(input())
a = number // 100
b = number // 10 % 10
c = number % 10
total = a + b + c 

print(total)