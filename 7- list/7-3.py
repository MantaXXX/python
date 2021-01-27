# Given a list of numbers, find and print all its elements that are greater than their left neighbor.

a = [int(s) for s in input().split()]
for i in range(1, len(a)):
    if a[i-1] < a[i]:
        print(a[i], end=' ')
