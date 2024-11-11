# empty list called my_list
my_list = []
# adding items to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# output of the items added to my_list
print(my_list);

# Insert the value 15 at the second position in the list.
my_list = [10, 20, 30, 40]
my_list.insert(1, 15)
print(my_list);

#Extend my_list with another list: [50, 60, 70].
my_list = [10, 20, 30, 40]
my_list.extend([50, 60, 70])
print(my_list);

#Remove the last element from my_list.
my_list = [10, 20, 30, 40, 50, 60, 70]
my_list.remove(70)
print(my_list);

# Sort my_list in ascending order.
my_list = [10, 20, 30, 40, 50, 60, 70]
my_list.sort()
print(my_list);

# Find and print the index of the value 30 in my_list.
my_list = [10, 20, 30, 40, 50, 60, 70]
print(my_list.index(30));