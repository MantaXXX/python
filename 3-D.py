# Given a square of a chessboard. If it's a black square, print YES, otherwise print NO.
#The program receives two integers from 1 to 8 specifying the column and row number of the square.

x = int(input())
y = int(input())

if (x+y) % 2 == 0:
  print('YES')
else:
  print('NO')