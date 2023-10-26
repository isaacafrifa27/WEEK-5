# this is to ask you to input what number you will want to use to run the program
number = input("Enter a number: ")

# This asks the user input a number, which is a string, and it converts it to an integer to update the 'number' variable
number = int(number)

# this is to tell the program to print a certain message
print("The numbered entered was", number)

# this is telling the program to print a message if a condition is met or else it should print another message if the condition is not met
if (number % 2) == 0:
	print("That is an even number")
else:
	print("That is an odd number")

# This is to print the message below if the number input is divisible by 10
if (number % 10) == 0:
	print("The number is divisible by 10")


