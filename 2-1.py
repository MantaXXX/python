# Given a two-digit integer, print its left digit (a tens digit) and then its right digit (a ones digit). Use the operator of integer division for obtaining the tens digit and the operator of taking remainder for obtaining the ones digit.

number = int(input())

firstDigit = number // 10
secondDigit = number % 10

print(firstDigit, secondDigit)

# 若已知輸入數字為兩位數可直接使用 a, b 接收兩數字(字串)
a, b = input()
print(a,b)