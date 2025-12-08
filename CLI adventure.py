def start_game():
    current_room = "hallway"
    inventory = []

    while True:
            if current_room == "hallway":
                print ("\nYou are in a dim hallway. There are doors on the left and right.")
                action = input("Where do you go (Left/Right/Quit):").strip().lower()
                if action == "left":
                    current_room = "supply"
                elif action == "right":
                    current_room = "pantry"
                elif action == "quit":
                    print("Thanks for playing!")
                    break
                else:
                    print("That's not a valid choice")
            elif current_room == "supply":
                print ("\nThe supply room is locked, but the door is slightly ajar.")
                action = input("Push door / Go back: ").strip().lower()
                if action == "push door":
                    print("You find a rusty key on the floor.")
                    if "key" not in inventory:
                        inventory.append("key")
                elif action == "go back":
                    current_room = "hallway"
                else:
                    print("Hmm, that doesn't work.")
            elif current_room == "pantry":
                print("\nYou enter a cold pantry. A locked fridge hums in the corner.")
                action = input("Open fridge / go back: ").strip().lower()
                if action == "open fridge":
                    if "key" in inventory:
                        print("You unlock the fridge and win the game. Victory is yours!")
                        break
                    else:
                        print("THe fridge won't budge. Looks locked.")
                elif action == "go back":
                    current_room = "hallway"
                else:
                    print("Not possible.")
start_game()