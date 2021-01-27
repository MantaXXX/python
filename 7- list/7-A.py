# Given a list of numbers, count a number of pairs of equal elements. Any two elements that are equal to each other should be counted exactly once.

a = [int(s) for s in input().split()]
count = 0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            count += -1

print(count)
