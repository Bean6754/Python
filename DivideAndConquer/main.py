# Get user input for size of array then array values.
num_array = list()
num = input("Enter how many elements you want:")
print ("Enter numbers in array: ")
for i in range(int(num)):
	n = input("num :")
	num_array.append(int(n))

# Get array length (useful for if statement later).
var_length = len(num_array)

# Divide array by 2 if array size is greater than or equal to 2.
if var_length >= 2:
    split_partA = num_array[:len(num_array)//2]
    split_partB = num_array[len(num_array)//2:]
    # print("Size is bigger than 4.\n")
    print(split_partA)
    print(split_partB)

# Do nothing if array size is less than 2.
elif var_length < 2:
	print("Size is less than 2.\n")
	print("No need to divide.\n")

# If if statement fails for unknown reason. Exit the program.
else:
    print("Error: An unknown error has occured.\n")
    exit()
