# Implement a group_by_owners function that Accepts a dictionary containing the file owner name for each file name.Returns a dictionary containing a list of file names for each owner name, in any order.

def fi(values):
    new_list = []
    a = values[0]
    if a[0] > a[1]:
        return "error"
    for i in values:
        if i[0] < a[1]:
            a[1] = i[1]
        else:
            if a not in new_list:
                new_list.append(a)
            if i not in new_list:
                new_list.append(i)
    if not new_list:
        new_list.append(a)
    return new_list
values = [[1, 3],[5,7],[9,10]]
print(fi(values))
