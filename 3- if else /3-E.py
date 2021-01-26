# Given two squares of a chessboard. If they are painted in the same color, print YES, otherwise print NO.
# The program receives four integers from 1 to 8, each specifying the column and row number, first two - for the first square, and then the last two - for the second square.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (x1+y1+x2+y2) % 2 == 0:
  print('YES')
else:
  print('NO')