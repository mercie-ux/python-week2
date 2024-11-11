#Tasks:
#Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
#empty list to store user input
integers = []
# Get the number of integers the user wants to add
count= int(input("How many numbers would you like to be added to the list?"))
# Loop to get each integer input from the user
for i in range(count):
    num =  int(input(f"Enter number {i + 1}: "))
    integers.append(num)
#the sum of all numbers in the list
total_sum = sum(integers)
# output of the list and sum
print("\nYour list of numbers:", integers);
print("The sum of all numbers in the list is:", total_sum);


#Create a tuple containing the names of five of your favorite books. 
favourite_books = ("pyschology of Money", "Rich Dad Poor Dad", "Emotional intelligence", "Master you emotions", "Atomic habits")
# Then, use a for loop to print each book name on a separate line.
for books in favourite_books:
    print(books);

#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. 
# an empty dictionary that stores a person's info
person_info = {}
# Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
# Collect information from the user and store it in the dictionary
person_info['name'] = input("Enter your name: ")
person_info['age'] = input("How old are you? ")
person_info['favourite_color'] = input("What's your favourite color? ")

#output of the dictonary
print("\nHere is the information you provided about you: ", person_info);

#Write a program that accepts user input to create two sets of integers. Then, 
# create a new set that contains only the elements that are common to both sets.

def create_set(set_number):
    user_input = input(f"Enter integers for Set {set_number}, separated by spaces: ")
    return set(map(int, user_input.spilt()))

# create two sets
set1 = create_set(1)
set2 = create_set(2)

# the intersection of the two sets
common_elements = set1.intersection(set2)

# output of the common set
print("\nThe common elements in both set are:" , common_elements);

#Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.
# define list of words
list_of_words = ["Kenya", "Uganda", "Tanzania", "Rwanda", "Egypt", "Nigeria"]
# list comprehension to create a new list that contains only the words that have an odd number of characters.
odd_length_words = [word for word in list_of_words if len(word) % 2 != 0]
# output
print("Words with an odd number of characters:", odd_length_words);
