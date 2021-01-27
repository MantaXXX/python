# Given a sequence of non-negative integers, where each number is written in a separate line. Determine the length of the sequence. The sequence ends with 0. Print the length of the sequence (not counting the 0). The numbers following the number 0 should be omitted.

a = int(input())
i = 0
while a != 0:
  i += 1
  a = int(input())
print(i)