# Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the average of the sequence.

a = int(input())
i = 0
sum = 0
average = 0
while a != 0:
  sum += a
  i += 1
  average = sum / i
  a = int(input())

print(average)
