# *args and **kwargs


integer_array = [2, 8, 4, 7, 9, 5, 1]
target = 10


for i, item inenumerate(numbers):
    for j in range(i+1, len(numbers)):
    	total_of_two_items = numbers[i] + numbers[j]
    	if(total_of_two_items == total_number):
        	print'{first_item} {second_item}'.format(first_item=i+1, second_item=j+1)
        	print'\n'


'''
SELECT DeptName, MAX(Salary) 
FROM Employee e RIGHT JOIN Department d 
ON e.DeptId = d.DeptID 
GROUP BY DeptName;
'''
