a = [2, 11, 7, 15]

for value in a:
    found = None
    for new_val in a:
        if (value + new_val) == 9:
            print(value, new_val)
            found = True
            break
    if found:
        break
