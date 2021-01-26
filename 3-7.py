# Let's call an integer a palindrome if it remains the same after reading its digits from right to left. Given a four-digit integer, print "YES" if it's a palindrome and print "NO" otherwise.

a,b,c,d = int(input())

if a == d and b == c:
  print('YES')
else:
  print('NO')