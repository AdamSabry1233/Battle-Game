while True:
    wizard = 'Wizard'
    elf = 'Elf'
    human = 'Human'
    orc = 'Orc'

    orc_hp = 130
    wizard_hp = 70
    elf_hp = 100
    human_hp = 150

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    orc_damage = 120

    dragon_hp = 300
    dragon_damage = 50

    while True:
        print('0) Exit')
        print('1)', wizard)
        print('2)', elf)
        print('3)', human)
        print('4)', orc)

        decision = input("Choose your character (or enter '0' to exit): ")

        if decision == '0':
            print("Exiting the game. Goodbye!")
            exit()  # This will terminate the program
        if decision == '1' or decision.lower() == 'wizard':
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        if decision == '2' or decision.lower() == 'elf':
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        if decision == '3' or decision.lower() == 'human':
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        if decision == '4' or decision.lower() == 'orc':
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break
        else: 
            print("Unknown Character")

    print(f"You have chosen the character {character}.")
    print(f"Health: {my_hp}")
    print(f"Damage: {my_damage}")

    print()

    while True:
        dragon_hp -= my_damage  # Update dragon's hitpoints
        print("The", character, "damaged the Dragon!")
        print("The Dragon's hitpoints are now: ",dragon_hp)
        print()
        if dragon_hp <= 0:
            print("The Dragon has lost the battle!")
            break

        my_hp -= dragon_damage  # Update character's hitpoints
        print("The Dragon strikes back at the",character)
        print("The", character +"'s", "hitpoints are now:",my_hp)
        print()
        if my_hp <= 0:
            print("The", character, "has lost the battle!")
            break
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thank you for playing. Goodbye!")
            exit()
