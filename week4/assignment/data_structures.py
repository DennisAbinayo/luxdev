# DATA STRUCTURES

#Exercises
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

## print the third fruit (2nd index)
print(fruits[2])

## Dictionary

user = {
    "name": "Dennis",
    "age": 65
}

print(user["age"])


## Tuples

coord = (1, 2, 3)

coord[1] = 5 # TypeError because tuples are immutable


## List with duplicate values

duplicates = [1, 2, 2, 3, 4, 4, 4, 5]
print(duplicates)


## Sets

new_set = set(duplicates)
print(new_set)


### Challenge

user_inputs = []
for i in range(5):
    user_input = input(f'Enter input {i+1}: ')
    user_inputs.append(user_input)

set2 = set(user_inputs)
print(set2)