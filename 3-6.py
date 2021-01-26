# Given a three-digit integer X consisting of three different digits, print "YES" if its three digits are going in an ascending order from left to right and print "NO" otherwise.

x = int(input())
a = x // 100
b = x // 10 % 10
c = x % 10

if c > b > a:
  print('YES')
else:
  print('NO')
