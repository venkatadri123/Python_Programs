d = [1, 1, 2, 2, 4, 4, 5, 5, 5, 7, 7, 8, 9]

new = {}
n = "1"
for val in range(len(d)):
    if val < len(d)-1:
        # if d[val] == d[val+1] or (d[val] + 1) == d[val+1]:
        if d[val+1] - d[val] < 2:
            if n in new:
                new[n].append(d[val])
            else:
                new[n] = [d[val]]
        else:
            new[n].append(d[val])
            n = str(val)
    else:
        if d[val] == d[val-1] or d[val-1]+1 == d[val]:
            new[n].append(d[val])
        else:
            new[str(val)] = d[val]
        
print(new)
