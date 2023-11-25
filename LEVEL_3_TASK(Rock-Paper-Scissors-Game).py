#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random

choices = ["rock", "paper", "scissors"]

user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
computer_choice = random.choice(choices)

print("Computer's choice:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")

