# Given a positive real number, print its first digit to the right of the decimal point.

number = float(input())
a = int(number * 10) 
b = a % 10

print(b)