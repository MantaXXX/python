# Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the sum of the sequence.

a = int(input())
i = 0
sum = 0
while a != 0:
  i += 1
  sum += a
  a = int(input())
print(sum)