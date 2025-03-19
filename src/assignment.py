"""
Template for student assignments.
Replace this with your actual assignment content.
"""
# Assignment: While Loops Practice
# Grade 10 Computer Science

# Task 1: Count by twos and print all even numbers from 2 to 50 (inclusive)
# Write your code for Task 1 below:
# TODO: Write a while loop that counts by 2s from 2 to 50 and prints each number
num = 0
while num < 51:
    print(str(num))
    num += 2
print("Task 1 complete!\n")

# Task 2: Print a 5x5 grid of # symbols using nested while loops
# Write your code for Task 2 below:
# TODO: Use nested while loops to print a 5x5 grid of # symbols
# Each row should have 5 # symbols
# There should be 5 rows in total
#remember to print without a new line use print("message", end="")
rep_noline = 0
rep_line = 0 
while rep_line != 5:
    rep_line += 1
    rep_noline = 0
    print("")
    while rep_noline != 5:
        print("#", end="")
        rep_noline += 1

