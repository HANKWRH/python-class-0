n, d = [int(x) for x in input().split()]
stuff = [int(x) for x in input().split()]
profit = []
thing_u_buy = stuff[0]
buy = False

for i in range(len(stuff)):
    if buy:
        if thing_u_buy - stuff[i] >= d:
            thing_u_buy = stuff[i]
            buy = False
    else:
        if thing_u_buy - stuff[i] >= d:
            profit.append(thing_u_buy - stuff[i])
            buy = True

print(sum(profit))