print("Welcome to the Haunted House. To escape, you must find the hidden key!")
direction_choice = input("Which direction do you want to enter? Left press L or right press R: ")
if direction_choice == "L":
    print("You are haunted.")
else:
    door_way_want_enter = input("Which route do you want to enter? Basement press B or Attic press A: ")

    if door_way_want_enter == "B":
        print("You are haunted.")
    else:
        print("There is information for you: there are three doors. One leads to the kitchen, one to the bedroom, and one to the washroom. The key is in the kitchen.")
        door_you_want_to_open = input("Which door do you want to open? Door 1 press D1, door 2 press D2, or door 3 press D3: ")
        if door_you_want_to_open == "D1":
            print("Wrong door. You are haunted.")
        elif door_you_want_to_open == "D2":
            print("Wrong door. You are haunted.")
        else:
            print("You found the key. Go and open the door fast.")

print("Game over.")



