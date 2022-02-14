#when you can't decide roll a dice 

import random

def make_choice(choices):
    choices_list = choices.split(",")
    print(random.choice(choices_list))


def main():
    print("***Please separate each of your choices by a comma***")
    choices = input("Enter your choices: ")
    make_choice(choices)

if __name__ == "__main__": main()
    
