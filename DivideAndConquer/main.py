num_array = list()
num = input("Enter how many elements you want:")
print ("Enter numbers in array: ")
for i in range(int(num)):
	n = input("num :")
	num_array.append(int(n))

var_length = len(num_array)

if var_length > 4:
	# string.split()
	print("Size is bigger than 4.\n")

elif var_length <= 4:
	# Do nothing.
	print("Size is less than 4.\n")
