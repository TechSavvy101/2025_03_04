#1. Write a function to take user input and display it.
#Question: Write a Python function named get_and_display_input() that:
#question 1
def get_and_display_input(prompt):
    user_input = input(prompt)
    return user_input

user_name = get_and_display_input("Enter your name: ")
print(f"Hello, {user_name}")
#question 2 Kitso
def sum_two_numbers(a, b):
    return a + b

a = int(input("please enter your first value"))
b = int(input("please enter your second value"))
    
result = sum_two_numbers(a, b)
print(result)


#question 3 Kitso
def save_to_file():

    user_input = input("Please enter the text you want to save to the file: ")
    

    with open("user_input.txt", "w") as file:
        file.write(user_input)
    
    
    print("Your input has been saved to user_input.txt.")


save_to_file()

#4. Write a function to read a file and display its content.  [ THANDO GAMA ]

#Question: Write a function named read_from_file() that:
#Opens user_input.txt.
#Reads and displays the content.
#Handles errors if the file doesn’t exist.

def read_from_file():
    try:
        with open('user_input.txt', 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("The file 'user_input.txt' does not exist.")


#5. Write a function to append user input to an existing file. [ THANDO GAMA ]

#Question: Write a function named append_to_file() that:

#Takes a string input from the user.
#Appends it to user_input.txt without overwriting previous content.
#Displays a message confirming the update.

def append_to_file():
    user_input = input("Enter text to append: ")
    with open('user_input.txt', 'a') as file:
        file.write(user_input + '\n')
    print("The content has been successfully appended to 'user_input.txt'.")







#question 6 Tshiamo Mafojane


Square = lambda x: x ** 2
num = int(input("so like enter please enter the number to square please brother: "))
print("Square:", Square(num))

#question 7 Tshiamo Mafojane 
filter_even_numbers = lambda numbers: list(filter(lambda x: x % 2 != 0, numbers))
nums = list(map(int, input("buddy enter the numbers but use space inbetween then. MAKE SURE!!: ".split())))
print ("de Filtured odd numbers :) :", filter_even_numbers(nums))
