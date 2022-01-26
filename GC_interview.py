#  input = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}

# Implement a group_by_owners function that:

# Accepts a dictionary containing the file owner name for each file name.Returns a dictionary containing a list of file names for each owner name, in any order.

def finding_owner_name(input_obj):
    output = {}
    for i in input_obj:
        if input_obj[i] in output:
            output.get(input_obj[i]).append(i)
        else:
            output[input_obj[i]] = [i]
    return output
    

data = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
print(finding_owner_name(data))
# output= {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.
