Name = input("What's Your Name: ")
print("Hey," + Name + " Welcome to my game." )

should_we_play = input("Do you want to play? ").lower()

if should_we_play == "yes" or should_we_play == "y":
    print("We are gonna play")
    direction = input("Do you want to go left or right (left/right) ").lower()

    if direction=="left" or direction == "l":
        print("You went left and fell of a cliff. Game over..!! Try again")
    elif direction=="right" or direction == "r":
        choice = input("Now you see a bridge. Do you want to swim or cross it? (swim/cross) ").lower()
        if choice=="swim" or choice=="s":
            print("You got eaten by an alligator. You die. Game over..!!")
        elif choice=="cross" or choice=="c":
            print("Hurray..!!! You found the Gold and Won..!!!")
        else:
            print("Sorry, Not a valid reply. You die..!")
    else:
        print("Sorry, Not a valid reply. You die..!")    

else:
    print("We are not gonna play...")