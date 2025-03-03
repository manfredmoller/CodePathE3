#Unit 1
# Session #1
# Problem Set #1

#Problem 1
print("Hello world!")
def hello_world():
     print("Hello world!")

# Problem 2
#def todays_mood():
 #       mood = "🥱"
  #      print("Today's mood: " + mood)

#todays_mood()

#Problem 3 The following function accepts one parameter menu. Copy this code to your Replit and add a function call so that "Lunch today is: 🍕" is printed to the console.
def print_menu(menu):
    print("Lunch today is: " + menu)

print_menu("🍜")

#Problem 4 Use the sum() function to calculate the sum of 13 and 27. Then, double the calculated sum and print the result to the console.
def sum(a, b):
    return a + b

sum(13, 27)
print(sum(13, 27) * 2)

#Problem 5 Write a function product() that returns the product of two integers, a and b.
def product(a, b):
    return a * b

product(22, 7)
print(product(22,7))

#Problem 6 Use condditional expression to compare values
#step1: 

#Write a function classify_age() that takes an integer age as a parameter and 
# returns "child" if 
# the age is less than 18, and returns "adult" otherwise.

def classify_age(age):
    return "child" if age < 18 else "adult"

print(classify_age(17))

#Problem 7  Write a function named what_time_is_it() 
# that takes an integer hour as a parameter.

def what_time_is_it(hour):
    if hour == 2:
        return "taco time 🌮"
        print()
    elif hour == 12:
        return "peanut butter jelly time"
    else:
        return "nap time 😪"
print(what_time_is_it(2))
print(what_time_is_it(12))
print(what_time_is_it(3))

#Problem 8 Write a function called blackjack() that takes an integer score as a parameter.
def blackjack(score):
    if score == 21:
        return "Blackjack!"
    elif score > 21:
        return "Bust!"
    elif score >= 17 and score < 21:
        return "Nice hand!"
    elif score < 17:
        return "Hit me!" 
print(blackjack(21))
print(blackjack(17))
print(blackjack(15))
print(blackjack(22))

#Problem 9 Write a function get_first() that takes in a list as a parameter and returns the first item in the list. 
# Return None if the list is empty.
def get_First(lst):
    if len(lst) == 0:
        return None
    else:
        return lst[0]
print(get_First([1, 2, 3]))
print(get_First([]))

#Problem 10
# Write a function get_last() that takes in a list as a parameter 
# and returns the last item in the list. 
# Return None if the list is empty.

def get_last(lst):
    if len(lst) == 0:
        return None
    else:
        return lst[-1]
print(get_last([1, 2, 3]))
print(get_last([0]))

#Problem 11
# Write a function counter() that uses the range 
# function to print numbers between 1 and a given stop value (inclusive).

def counter(stop):
    for i in range(1, stop + 1):
        print(i)
counter(4)

#Problem 12
#Write a function sum_ten() that returns 
# the sum of numbers from 1 to 10.

#UPI
#1.Initialize the accumulator variable
#2. iterate through the numbers from 1 to 10:
#3 Update the Accumulator Variable: In each iteration of the loop, 
# add the current number to the accumulator variable.
#4. Return the Result: After the loop has finished,
#  the accumulator variable will hold the 
# sum of all the numbers from 1 to 10. Return this value.


def sum_ten():
    total = 0
    for i in range(1, 11):
        total += i
    return total
    
print (sum_ten())

#Problem 13
#Write a function sum_positive_range() that returns the sum of 
# numbers from 1 to a given stop value (inclusive).

#UPI
#1. Initialize the accumulator variable
#Check if the stop value is less than 1
#2. Iterate through the numbers from 1 to stop:
#3. Update the Accumulator Variable: In each iteration of the loop,
#4. Return the Result: After the loop has finished,
# the accumulator variable will hold the sum of all the numbers from 1 to stop.


def sum_positive_range(stop):
      # Initialize the accumulator variable
  
    total = 0

    # Check if the stop value is less than 1
    if stop < 1:
        print ("Invalid input. Please enter a positive integer.")

   # Iterate through the numbers from 1 to stop (inclusive)
    for i in range(1, stop + 1):
        total += i

        # Return the result after the loop has finished
    return total

# Test cases to verify the function works as expected
print(sum_positive_range(5))
print(sum_positive_range(10))
print(sum_positive_range(-3))
print(sum_positive_range(0))

#Problem 14 Write a function sum_range() that returns the sum of numbers 
# from a given start value to a given stop value (inclusive).
def sum_range(start, stop):
    total = 0
    for i in range(start, stop + 1):
        total += i
    return total
print(sum_range(3, 9))

#Problem 15 Write a function print_negatives() that takes a list of integers lst and prints all negative numbers in the list.
#Initialize a flag to track if any negative numbers are found.
#Iterate through the list and print each negative number.
#After the loop, check the flag and print a message if no negative numbers were found.

def print_negatives(lst):
    found_negative = False # Initialize a flag to track if any negative numbers are found
    for num in lst:
        if num < 0:
            print(num)
            found_negative = True # Set the flag to True if a negative number is found
    if not found_negative: # After the loop, check the flag
            print("No negatives found")

print_negatives([1, -2, 3, -4, 5])
print_negatives([1, 2, 3, 4, 5])

#Unit1 
# Set Version 2
#Problem 1 Write a function greet_user() that takes in a string name as a parameter and prints "Hello <name>".
def greet_user(name):
    print("Hello " + name)
greet_user("Alice")

#Problem 2
# Write a function difference() that returns the difference 
# between two integers a and b (b should be subtracted from a).

def difference(a, b):
    return a - b
print(difference(10, 5))

#Problem 3 Given an integer list nums of length n, create a function concatenate_list() that creates and returns a list ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
#Specifically, ans is the concatenation of two nums lists.

def concatenate_list(nums):
    n = len(nums)
    ans = [0] * (2 * n)
    for i in range(n):
        ans[i] = nums[i]
        ans[i + n] = nums[i]
    return ans
print(concatenate_list([1, 2, 3, 4]))

#Problem 4
#Write a function sleep_assessment() that takes in an integer parameter hours indicating the number of hours the user slept.
#If hours is less than 8, print "Oof, go back to bed!".
#If hours is greater than or equal to 8 and less than or equal to 10, print "You got a good night's rest!".
#If hours is greater than 10, print "You're a sleep prodigy!".

def sleep_assessment(hours):
    if hours < 8:
        print("Oof, go back to bed!")
    elif hours >= 8 and hours <= 10:
        print("You got a good night's rest!")
    else:
        print("You're a sleep prodigy!")

sleep_assessment(7)
sleep_assessment(9)
sleep_assessment(11)

#Problem 5 Write a function calculate_tip() that takes in a float bill and a string service_quality as parameters.
#If service_quality is "poor", the function should return 10% of the bill value.
#If service_quality is "average", the function should return 15% of the bill value.
#If service_quality is "excellent", the function should return 20% of the bill value.
#If service_quality is any other value, the function should return None.

def calculate_tip(bill, service_quality):
    if service_quality == "poor":
        return bill * 0.10
    elif service_quality == "average":
        return bill * 0.15
    elif service_quality == "excellent":
        return bill * 0.20
    else:
        return None

tip1 = calculate_tip(44.53, "average")
print(tip1)
tip2 = calculate_tip(44.53, "poor")
print(tip2)
tip3 = calculate_tip(44.53, "excellent")
print(tip3)

#Problem 6: Rock, Paper, Scissors
#Write a function rock_paper_scissors() that determines the 
# winner of a game of Rock, Paper, Scissors. 
# The function accepts two strings as parameters: player1 and player2. 
# Each parameter can have a value of "rock", "paper", or "scissors".

#Print either "Player 1 wins!" or "Player 2 wins!" according to the following rules:
#Rock wins against scissors.
#Scissors wins against paper.
#Paper wins against rock.

#If both player1 and player2 have the same value, print "It's a tie!".

def rock_paper_scissors(player1, player2):
    if player1 == player2:
        print("It's a tie!")
    elif (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

rock_paper_scissors("rock", "rock")
rock_paper_scissors("scissors", "rock")
rock_paper_scissors("scissors", "paper")
rock_paper_scissors("rock", "paper")
rock_paper_scissors("paper", "rock")

#Problem 7: Unscramble and Divide
#Given the following lines of code, work with your group members to place the lines in order to write and call a function that divides each value in an input list by 2.

#a. result = []
#b. for number in lst:
#c. result.append(halved)
#d. halved = number/2
#e. halve_list([2,4,6,8])
#f. return result
#g. def halve_lst(lst):

def halve_list(lst):
    result = []
    for number in lst:
        halved = number / 2
        result.append(halved)
    return result
print(halve_list([2, 4, 6, 8]))

#problem 8: Write a function above_threshold() 
# that takes in a list of integers lst and an integer 
# threshold as parameters. The function iterates 
# through the original list and returns 
# a new list containing only numbers that are greater than threshold.

def above_threshold(lst, threshold):
    result = [] # Initialize an empty list to store numbers above the threshold
    for number in lst:  # Iterate through each number in the input list
        if number > threshold: # Check if the number is greater than the threshold
            result.append(number)   # If it is, add it to the result list
    return result # Return the new list containing numbers above the threshold
print(above_threshold([1, 2, 3, 4, 5], 3))

def above_threshold(lst, threshold):
    result = []
    for number in lst:
        if number > threshold:
            result.append(number)
    return result
print(above_threshold([1, 2, 3, 4, 5], 3))
print(above_threshold([10, 20, 30, 40], 25))

#Problem 9 Write a function countdown() that takes in two positive 
# integers m and n as parameters and prints numbers from m down to n.

def countdown(m, n):
    for i in range(m, n - 1, -1):
        print(i)
countdown (5, 1)

#Problem 10
#Write a function power() that takes in two integers base and exponent. 
# The function should return the value of the base number to the power of the exponent.

def power(base, exponent):
    result = 1  # Initialize result to 1
    for i in range(exponent):
        result *= base  # Multiply result by base in each iteration
    return result  # Return the final result

pow1 = power(2, 5)
print(pow1)
pow2 = power(3, 3)
print(pow2)

#Problem 11 
#Without using the built-in len() function, 
# write a function list_length() that takes 
# in a list lst as a parameter and returns the length of the list.

def list_length(lst):
    count = 0  # Initialize a counter variable
    for item in lst:  # Iterate through each item in the list
        count += 1  # Increment the counter for each item   
    return count  # Return the final count
print(list_length([1, 2, 3, 4, 5]))
print(list_length([]))

#Problem 12
#Write a function factorial() that takes in an integer n as a parameter 
# and returns its factorial. The factorial of a number is the product of 
# all positive integers less than or equal to that number. For example, the factorial of 5 
# (denoted as 5!) is 5! = 5 * 4 * 3 * 2 * 1 which equals 120.

def factorial(n):
    result = 1  # Initialize result to 1
    for i in range(1, n + 1):  # Iterate from 1 to n (inclusive)
        result *= i  # Multiply result by the current number
    return result  # Return the final result
print(factorial(3))

#Problem 13
#Write a function squares() that takes a list of integers
#nums as a parameter and returns a new list 
#containing the square of each number in the original list.

def squares(nums):
    result = []  # Initialize an empty list to store the squares
    for num in nums:  # Iterate through each number in the input list
        result.append(num ** 2)  # Calculate the square and add it to the result list
    return result  # Return the new list containing the squares
print(squares([1, 2, 3, 4, 5]))

#Problem 14
#Write a function multiply_list() that takes in a list of integers 
# lst and an integer multiplier as parameters. The function returns 
# a new list containing each value in lst multiplied by multiplier.

