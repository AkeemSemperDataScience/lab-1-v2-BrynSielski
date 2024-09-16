def lab1Question1(input_gb):
    # Convert the input of a number of gigabytes to the number of bytes
    num_bytes = None
    # Do the work here
    # The solution to this goes here (and in all of them below...)
    # Set the variable num_bytes to the answer and return it
    # Bytes > Kilobytes > Megabytes > Gigabytes
    num_bytes = input_gb * 1024 * 1024 * 1024
    return num_bytes


def lab1Question2(name):
    # Take an input of a name, return True if there is an odd number of characters in the name, False otherwise
    # Return None if the input is not a string
    is_odd = None

    if len(name) % 2 == 0: #there is an even number of characters
        is_odd = False
    else:
        is_odd = True
    # is odd = true, is even = false
    # if input is not a string, return "none"

    return is_odd


def lab1Question3(input_string, input_number):
    # Take in two inputs - a string and a number
    # Return the character of the string in the index given by number.  If this index does not exist, then return -1.
    character_at = -1
    # need to take input_number's number and subtract 1 for correct spot since count starts at 0
    character_at =  input_string[input_number - 1]
    # take that number and take input string's character are corrosponding place

    return character_at


def lab1Question4(file_name):
    # Take an input of a file name.
    # Read that file and return a list of all numbers in that file
    #list_of_nums = [type(int), type(float)] #need to figure out how to read the file, extract numbers
    # open file using "open" command
    # define 'list_of_nums' as string from opened file
    # extract floats and integers from 'a'
    a = open(file_name)
    #print(list_of_nums.read())
    a.read()
    list_of_nums = map(#floats and integers of 'a'
    #print(a)

    #list_of_nums = file_name

    return list_of_nums


def lab1Question5(list_numbers):
    # Take an input of a list of numbers
    # Return the mode from that list. 
    mode_of_list = None

    # find the mode of the original list of numbers (most common number)
    # define mode_of_list to be the outcome of the count
    mode_of_list = max(list_numbers, key=list_numbers.count)

    return mode_of_list


def lab1Question6(quarters, dimes, nickels, pennies):
    # Take in 4 inputs - the number of quarters, dimes, nickels, and pennies in a handful
    # Return the total amount in dollars
    # For example, if the handful contains 4 quarters, 3 dimes, 2 nickels, and 1 penny, the function should return 1.41.
    total = None

    total = ((quarters * .25) + (dimes * .1) + (nickels * .05) + (pennies * .01))

    return total

## Example of calling a function to test these... 
# Question 1 Check:
in_gb = 10
expected_bytes = 10*1024*1024*1024
calculated_bytes = lab1Question1(in_gb)

print("Input gigabytes: ", in_gb)
print("Expected bytes: ", expected_bytes)
print("Calculated bytes: ", calculated_bytes)
if expected_bytes == calculated_bytes:
    print("Test passed")
else:
    print("Test failed")

# You can make similar tests to check if things work for you. 
# This is kind of annoying, I am aware, but it is a really important skill in programming. 
# Determining how to check if your code works, and define specific tests for what "working" means is 
# something that allows you to tackele any larger problem - you can break it into smaller bits, attack one bit at a time,
# check to ensure you've done it correctly, and then move on to the next bit.

#question 2 check
name = "Bryn"
print("there is an odd amount of characters in", name, "-", lab1Question2(name))

#question 3 check
input_string = "Hello!"
input_number = 2
print("the", input_number, "stndrdth letter of", input_string, "is", lab1Question3(input_string, input_number))

#question 4 check
file_name = "Numbers.txt"
print(lab1Question4(file_name))

#question 5 check
list_numbers = ["15", "17", "17", "14", "15", "16", "17"]
print(lab1Question5(list_numbers))

#question 6 check
quarters = 4
dimes = 3
nickels = 2
pennies = 1
print("Your total is...", lab1Question6(quarters, dimes, nickels, pennies), "!")
print("# of quarters:", quarters,"=", (quarters*.25))
print("# of dimes:", dimes,"=", (dimes*.1))
print("# of nickels:", nickels, "=", (nickels*.05))
print("# of pennies:", pennies,"=", (pennies*.01)) 
