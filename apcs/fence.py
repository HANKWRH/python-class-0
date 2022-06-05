_ = [int(x) for x in input()]
a = [int(x) for x in input().split()]
list_b = []
for i in range(len(a)):
    if a[i] == 0:
        if  i > 0 and i < (len(a)-1):
            list_b.append(min(a[i-1],a[i+1]))
        elif i == 0:
            list_b.append(a[i+1])
        else:
            list_b.append(a[i-1])

print(sum(list_b))