# The Birthday Paradox, also called the Birthday Problem, is the surprisingly high probability that two people will have the same birthday even in a small group of people. In a group of 70 people, there’s a 99.9 percent chance of two people having a matching birthday. But even in a group as small as 23 people, there’s a 50 percent chance of a matching birthday. This program performs several probability experiments to determine the percentages for groups of different sizes. We call these types of experiments, in which we conduct multiple random trials to understand the likely outcomes, Monte Carlo experiments.

import random
import datetime as dt
import time

def atleast_one_matching_birthday(birthday):
    if(len(birthday) == len(set(birthday))):
        return False
    return True

def generate_random_date():
    start_date = dt.date(2000,1,1)
    random_number = random.randint(0, 365)
    random_date = start_date + dt.timedelta(days=random_number)
    return random_date

def generate_birthdays(num):
    birthdays = []
    for i in range(num):
        birthdays.append(generate_random_date())
    return birthdays
    

def main():
    print("This Birthday Paradox problems tell how many people can share the same birthday with what probability.")
    num_of_birthday = int(input("How many no. of birthday to generate?\n>>> "))

    count = 0
    print("Starting Simulation...\n\n")
    for _ in range(100_000):
        # Generate num_of_birthdayy
        birthdays = generate_birthdays(num_of_birthday)
        
        # If atleast one matched birthday found
        if atleast_one_matching_birthday(birthdays):
            count += 1
    
    print("Simulation Ends.")
    prob = (count/100_000) * 100
    print(f"In this experiment, in the group of {num_of_birthday} people, we found {count} groups where they had atleast one matching birthdate\nThe probability of {num_of_birthday} people having the same birthday is {prob}%.\n")
    print(f"There is about a {prob}% chance that at least two people in a group of {num_of_birthday} share the same birthday.")
    
if __name__ == "__main__":
    main()