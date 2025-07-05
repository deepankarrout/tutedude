'''
Task 1: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly. 

'''
#Program

number = int(input('Enter a number: ')) #Take a input from user

if(number % 2 == 0): #Check number is divisible by 2 or not 
    print(number,'is an even number.') # If divisible then even
else:
    print(number,'is an odd number.') # Else odd
