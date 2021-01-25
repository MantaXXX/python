# Given a three-digit number. Find the sum of its digits.

number = int(input())
a = number // 100
b = (number - (a *100)) // 10
c = number % 10
total = a + b + c 

print(total)