# Importing the random library to generate random HP damage
import random
# Starting HP for the enemy
enemy_hp = 25
# Starting HP for the player
player_hp = 20
# Game Menu
print("\n( Game Start )")

print("\n1. Start Game \n2. Exit")
player_input = input ("> ")

if player_input == "2":
    print("Bye bye :)")

while True:

    print("\n1. Attack")
    print("2. Heal")
    print("3. Exit To Game Menu")
    player_choice = input ("> ")

    # Input
    if player_choice == "1":  

        # Player attack
        player_damage = random.randint(3, 7)
        enemy_hp -= player_damage
        print(f"\nYou hit Goblin for {player_damage} damage")
        print(f"Goblin HP: {enemy_hp}")

        # Check if the player's won
        if enemy_hp <= 0:
            print("\nYou've defeated Goblin!")
            break
    
        # Enemy attack
        enemy_damage = random.randint(3, 7)
        player_hp -= enemy_damage
        print(f"\nGoblin hits for {enemy_damage} damage")
        print(f"Player HP: {player_hp}")

    # Check if the Goblin's won
        if player_hp <= 0:
            print("\nGoblin Wins!")
            break

    elif player_choice == "2":
        pass

    elif player_choice == '3':
        pass

    # Anything other than '1' causes the player to lose
    else:
        print("\nYou've lost!")
        break



