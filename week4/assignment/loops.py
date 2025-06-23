# LOOPS

## Exercises

### one
for i in range(1, 11):
    print(i)

### two
user_input = input("Type some text (or 'stop' to quit): ")

while user_input != "stop":
    print(user_input)
    user_input = input("Type some text (or 'stop' to quit): ")
    

### three
for i in range(1, 21):
    if i % 2 == 0: # modulo operator to check divisibility bt 2
        print(i)

### four
# break - immediately exits the current loop entirely
# continue - skips the rest of the current lop iteration and proceeds to the next


## Challenge

# Guessing game
import random
actual_number = random.randint(1, 10)

guess = int(input('Enter a random number between 1 and 10: '))

while True:
    if guess > actual_number:
        print('Too high')
        guess = int(input('Try again: '))
    elif guess < actual_number:
        print('Too low')
        guess = int(input('Try again: '))
    else:
        print('Correct! You guessed the number.')
        break