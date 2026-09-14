# Program to demonstrate List, Tuple and Dictionary

# List
my_list = [10, 20, 30, 40]
print("List:", my_list)

my_list.append(50)
print("List after append:", my_list)

my_list.remove(20)
print("List after remove:", my_list)


# Tuple
my_tuple = (10, 20, 30, 40)
print("\nTuple:", my_tuple)

my_tuple = my_tuple + (50,)
print("Tuple after adding:", my_tuple)

my_tuple = my_tuple[:1] + my_tuple[2:]
print("Tuple after removing:", my_tuple)


# Dictionary
my_dict = {"Name": "Sakshi", "Age": 20, "Course": "BTech"}
print("\nDictionary:", my_dict)

my_dict["College"] = "MIT-WPU"
print("Dictionary after adding:", my_dict)

del my_dict["Age"]
print("Dictionary after remove:", my_dict)
