# Chess bishop moves diagonally in any number of squares. Given two different squares of the chessboard, determine whether a bishop can go from the first square to the second one in a single move.

# The program receives four numbers from 1 to 8 each specifying the column and the row number, first two - for the first square, and the last two - for the second square. The program should output YES if a bishop can go from the first square to the second one in a single move or NO otherwise.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if abs(x1-x2) == abs(y1-y2):
  print('YES')
else:
  print('NO')