# Given a string, delete all its characters whose indices are divisible by 3.

s = input()
# 建立空字串
answer = ''
for i in range(len(s)):
  if i % 3 != 0:
    answer += s[i]

print(answer)