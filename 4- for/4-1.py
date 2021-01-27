# Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively.

a = int(input())
b = int(input())

print(*range(a, b+1))

# 另外寫法
for i in range(a, b+1):
  # end=' ' 把預設換行換成空格
  print(i, end=' ')