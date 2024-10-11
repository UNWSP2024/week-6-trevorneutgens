
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).
# The dice sum will be the output of this function.

import random
def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here
    roll_1 = random.randint(1,6)
    roll_2 = random.randint(1,6)
    # Sum 2 numbers
    roll_total = roll_1 + roll_2

    print(roll_total)
    # return sum to calling function
    return roll_total

#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
def main():
    total_rolls = 0
    number_of_rolls = 100

    # roll the dice 100 times and accumulate the total
    for number in range(number_of_rolls):
        total_rolls += randDice()

    # calculate the average
    average_roll = total_rolls / number_of_rolls
    # print the average rounded to 2 decimal places
    print(f"Average of {number_of_rolls} rolls: {average_roll:.2f}")

main()