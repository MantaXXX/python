# Given three integers, in which two are equal to each other and the third one is different. Print the order number of this different one - 1, 2 or 3.

a = int(input())
b = int(input())
c = int(input())

if a != b and a != c:
  print(1)
elif b != a and b != c:
  print(2)
else:
  print(3)