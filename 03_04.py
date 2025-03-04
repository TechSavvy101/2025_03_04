#question 1

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




#question 4

#question 5

#question 6 Tshiamo Mafojane

#question 7 Tshiamo Mafojane