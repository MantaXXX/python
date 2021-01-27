# Given a string in which the letter h occurs at least twice. Remove from that string the first and the last occurrence of the letter h, as well as all the characters between them.

s = input()
# 找出第一位 h 索引值
a = s.find('h')
# 找出最後一位 h 索引值
b = s.rfind('h')

print(s[:a] + s[b+1:])