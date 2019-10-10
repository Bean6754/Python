num_array = list()
num = input("Enter how many elements you want:")
print ("Enter numbers in array: ")
for i in range(int(num)):
	n = input("num :")
	num_array.append(int(n))

var_length = len(num_array)

if var_length >= 2:
    # string.split()
    split_partA = num_array[:len(num_array)//2]
    split_partB = num_array[len(num_array)//2:]
    # print("Size is bigger than 4.\n")
    print(split_partA)
    print(split_partB)

elif var_length < 2:
	# Do nothing.
	print("Size is less than 2.\n")
	print("No need to divide.\n")
else:
    print("Error: An unknown error has occured.\n")
    exit()
