# Given a string that may contain a letter p. Print the index of the second occurrence of p. If the letter p occurs only once, then print -1, and if the string does not contain the letter p, then print -2.

s = input()
a = s.find('p')
b = s.find('p', a+1)

if a == -1:
  print(-2)
else:
  print(b)