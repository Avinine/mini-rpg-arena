# Importing the random library to generate random HP damage
import random

# Game Menu
print("\n( Game Start )")
print("1. Fight \n2. Exit")
# Getting user's input to use in condition
user_input = input ("> ")
# Starting HP for the enemy
enemy_hp = 25
# Starting HP for the player
player_hp = 20

# Keep the game running until the player exits
while True:
    if user_input == "1":
        attack_choice = input("Attack the Goblin \n send '1'  ")
        if attack_choice == "1":
            enemy_hp -= 5
            print(f"Goblin HP: {enemy_hp}")
            print("Goblin attacks back!")
            player_hp -= 5
            print(f"Your HP: {player_hp}")

        else:
            print("You've lost!")
            break

        if player_hp <= 0:
            print("Goblin Wins!")
            break

        if enemy_hp <= 0:
            print("You've defeated Goblin!")
            break
    
    elif user_input == "2":
        print("Bye bye :)")
        break

