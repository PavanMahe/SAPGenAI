#List creation with fruits
fruits = ['apple', 'banana', 'cherry', 'date']
#list with number of fruits
num_fruits = [5, 10, 15, 20]
# I want to print first and last fruit of the list
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
#add item to the list
fruits.append('elderberry') 
#add item at middle of the list
fruits.insert(2, 'blueberry')
print("Fruits after additions:", fruits)
#extract the sublist from index 1 to 3
sublist = fruits[1:4]
print("Sublist of fruits from index 1 to 3:", sublist)  
#remove an item from the list
fruits.remove('banana')
print("Fruits after removal of banana:", fruits)
#sort the list alphabetically
fruits.sort()
print("Sorted fruits:", fruits)
#reverse the list
fruits.reverse()
print("Reversed fruits:", fruits)
#remove and return the last item
last_fruit = fruits.pop()   
print("Popped fruit:", last_fruit)
print("Fruits after popping last item:", fruits)
#list membership test
if 'cherry' in fruits:
    print("Cherry is in the fruit list.")
#List conatenation fruits and num_fruits    
combined = fruits + [str(num) for num in num_fruits]
print("Combined list of fruits and number of fruits:", combined)

#list comprehesion number squares
squares = [x**2 for x in num_fruits]

print("Squares of number of fruits:", squares)
# Difference between lists and sets in Python
# Lists are ordered and allow duplicate elements
example_list = [1, 2, 2, 3, 4]
print("Example list (ordered, allows duplicates):", example_list)

# Sets are unordered and do not allow duplicate elements
example_set = {1, 2, 2, 3, 4}
print("Example set (unordered, no duplicates):", example_set)