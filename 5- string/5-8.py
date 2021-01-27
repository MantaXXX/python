# Given a string in which the letter h occurs at least twice, reverse the sequence of characters enclosed between the first and last occurrences of it.

s = input()
# 找出第一位 h 索引值
a = s.find('h')
# 找出最後一位 h 索引值
b = s.rfind('h')
# 中間反轉
c = s[b:a:-1]

print(s[:a] + c + s[b:])