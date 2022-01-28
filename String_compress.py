def compress(string):
    res = ""
    count = 1
    iteration_value = 0
    for i in range(len(string)-1):
        iteration_value += 1
        if(string[i] == string[i+1]):
            count+=1
            if iteration_value == len(string)-1:
                res = res + f"{count}{string[i]}"
        else:
            res = res + f"{count}{string[i]}"
            count = 1
            if iteration_value == len(string)-1:
                res = res + f"{count}{string[i+1]}"
    return res
    
input_val = "accsdfffddff"

print(compress(input_val))

output_val = "1a2c1s1d3f2d2f"
