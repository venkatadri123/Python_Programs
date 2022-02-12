weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']

new = {}

for val in weekdays:
    if val in new:
        new[val] = new[val]+1
    else:
        new[val] = 1
d = [[i,new[i]] for i in new]
print(d)
# out = [[‘wed’, 1], [‘sun’, 2], [‘thu’, 1], [‘tue’, 1], [‘mon’, 3], [‘fri’, 1]]
