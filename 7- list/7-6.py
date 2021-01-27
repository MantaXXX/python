# Given a list of numbers with all elements sorted in ascending order, determine and print the number of distinct elements in it.

# set 為集合，為不重複內容
a = [int(s) for s in input().split()]
# 先轉為 set 集合，再計算長度
print(len(set(a)))


# 另外寫法
b = []
count = 0
for i in a:
    if i not in b:
        b.append(i)
        count += 1

print(count)
