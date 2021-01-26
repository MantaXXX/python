# Given a two-digit integer, swap its digits and print the result.

number = int(input())

firstDigit = number // 10
secondDigit = number % 10

print(secondDigit, firstDigit)


# 另外寫法，將輸入文字視為字串
a, b = input()
print(b+a)