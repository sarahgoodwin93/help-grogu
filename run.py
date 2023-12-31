# Imports
"""
Contains ASCII images used in the application - these were taken from
various websites, more information found in readme.
"""
import images


# Username
username = ""


# Game Intro Text
def intro_text():
    """
    Introduction to the game, allows users to input their name
    and explains the story and journey they are about to go on.
    Once the user has input their name correctly,
    the game will begin with the first challenge.
    If the user does not input their name with letters, the error
    message will show and they cannot continue until they do so.
    """
    print(
        "Welcome to the game that will take you " +
        "on an outer space adventure!"
        )
    print("Can you help Grogu find his way back to Din Djarin?")
    print(images.logo_img)
    print(images.welcome_message)
    print("What is your name?\n")
    while True:
        username = input("")
        if not username.isalpha():
            print(
                "Sorry, we don't know that language, please " +
                "use some letters we can understand"
            )
            continue
        else:
            print(f"Welcome {username}, let's begin!!")
            first_challenge()


# First Challenge Function
def first_challenge():
    """
    Outlines the first options of the game
    and allows the user to choose where the game will go.
    The while loops ensures the user only chooses a, b or c.
    2 options will end the game, the other continues onto the next challenge.
    """
    while True:
        user_choice = ""
        print("You discover that Mando might be on Moth Gideons light cruiser")
        print("But you need a ship to be able to catch up to him")
        print("Do you...")
        print(
            "A) Try to win a ship in a card game with sketchy " +
            "gamblers at the local drinking spot?"
            )
        print(
            "B) Try to sneak onboard a ship leaving " +
            "the shipyard as stowaways?"
            )
        print("C) Get Grogu to steal someone's keys using the force?")
        user_choice = str(input("What do you decide A, B or C? \n"))
        if user_choice == "A" or user_choice == "a":
            print("You lose the game and now owe all the gamblers a drink!")
            end_game()
            break
        elif user_choice == "B" or user_choice == "b":
            print("You get found and chucked off the ship!")
            end_game()
            break
        elif user_choice == "C" or user_choice == "c":
            print(
                "Grogu gets the keys and you find the ship, " +
                "time to get going!"
                )
            second_challenge()
            break
        else:
            print("You must choose A, B, or C")
            print("............TRY THAT AGAIN............")


# Second Challenge Function
def second_challenge():
    """
    Outline the second option of the game and
    allows the user to choose where the game will go.
    The while loops ensures the user only chooses a, b or c.
    2 options will end the game, the other continues onto the next challenge.
    """
    while True:
        user_choice = ""
        print(" ")
        print("You make it onto the ship")
        print("But the ship doesn't start")
        print("Do you...")
        print("A) Call the mechanic")
        print("B) Try to fix it yourselves")
        print("C) Head back into town to try to get a different ship")
        user_choice = str(input("What do you decide A, B or C? \n"))
        if user_choice == "A" or user_choice == "a":
            print(
                "Peli Motto answers your call! She tells " +
                "you how to fix the ship and off you go!"
                )
            third_challenge()
        elif user_choice == "B" or user_choice == "b":
            print(
                "Grogu drops the spanner down a shoot " +
                "and you can't fix the ship"
                )
            end_game()
        elif user_choice == "C" or user_choice == "c":
            print(
                "You head back to town and the gamblers " +
                "find you again and take Grogu for yet another drink!"
            )
            end_game()
        else:
            print("You must choose A, B or C")
            print("............TRY THAT AGAIN............")


# Third Challenge Function
def third_challenge():
    """
    Outline the third option of the game and
    allows the user to choose where the game will go.
    The while loops ensures the user only chooses a, b or c.
    2 options will end the game, the other continues onto the next challenge.
    """
    while True:
        user_choice = ""
        print(
            "Your ship just makes it to planet, " +
            "although it's still falling apart"
            )
        print(
            "You head into the local Salon to find " +
            "out some more information."
            )
        print(
            "Moth Giden troops have been spotted " +
            "on the other side of the planet!"
        )
        print("Do you...")
        print("A) Get a speedster to get there quick before they get away!")
        print("B) Get back on the ship and try to fly it across")
        print("C) Try to find out more info from the locals")
        user_choice = str(input("What do you decide A, B or C? \n"))
        if user_choice == "A" or user_choice == "a":
            print("You've made it, but they are no where to be seen!")
            fourth_challenge()
        elif user_choice == "B" or user_choice == "b":
            print(
                "AND CRASH. Sorry your ship is broken and it " +
                "will be a while before you can get it going again"
            )
            end_game()
        elif user_choice == "C" or user_choice == "c":
            print("Grogu has been distracted by a local's eggs...")
            print(images.grogu)
            end_game()
        else:
            print("You must choose A, B or C")
            print("............TRY THAT AGAIN............")


# Fourth Challenge Function
def fourth_challenge():
    """
    Outline the fourth option of the game and
    allows the user to choose where the game will go.
    The while loops ensures the user only chooses a, b or c.
    2 options will end the game, the other continues onto the next challenge.
    """
    while True:
        user_choice = ""
        print("You are looking everywhere for clues")
        print("And you find Mandos helmet!")
        print("Do you...")
        print("A) Use the force to try to locate him")
        print("B) Cry and go home")
        print("C) Go and get the Mandalorian covenant to try to help")
        user_choice = str(input("What do you decide A, B or C? \n"))
        if user_choice == "A" or user_choice == "a":
            print(
                "Grogu has found him! He is located " +
                "in a secret hideout a few clicks away!"
            )
            fifth_challenge()
        elif user_choice == "B" or user_choice == "b":
            print("You go home and Mando is lost forever")
            end_game()
        elif user_choice == "C" or user_choice == "c":
            print(
                "You get back to your ship to contact the " +
                "covenant, but who knows when they'll get here!"
                )
            end_game()
        else:
            print("You must choose A, B or C")
            print("............TRY THAT AGAIN............")


# Fifth Challenge Function
def fifth_challenge():
    """
    Outline the fifth option of the game and
    allows the user to choose where the game will go.
    The while loops ensures the user only chooses a, b or c.
    2 options will end the game, the other continues onto the next challenge.
    """
    while True:
        user_choice = ""
        print("You have used the force and found he is still on the planet")
        print("Taking your speedster to go to where they are hiding")
        print("Do you...")
        print("A) Break in and rescue him")
        print("B) Wait until he is transported out to attack their ships then")
        print("C) Wait for help")
        user_choice = str(input("What do you decide A, B or C? \n"))
        if user_choice == "A" or user_choice == "a":
            print(
                "You've got him!! Well done for rescuing Mando! " +
                "You can now go and enjoy more adventures together!"
                )
            win_game()
        elif user_choice == "B" or user_choice == "b":
            print(
                "You wait, and wait and they don't come back, you " +
                "decided to go get help and miss their ship departing..."
                )
            end_game()
        elif user_choice == "C" or user_choice == "c":
            print("Looks like no one is coming and Moth Giden got away!")
            end_game()
        else:
            print("You must choose A, B or C")
            print("............TRY THAT AGAIN............")


# End Game Function
def end_game():
    """
    Ends the game if the player loses and asks if the user wants to play again.
    If they choose yes the game will begin again with challenge 1.
    If they choose no the game will quit.
    The while loops ensures the user only chooses y or n.
    """
    while True:
        print("Do you want to play again? y/n \n")
        user_input = str(input("").lower())
        if user_input == "y" or user_input == "Y":
            print("............Welcome back, lets try again!!............")
            first_challenge()
        elif user_input == "n" or user_input == "N":
            print(
                "Thanks for helping Grogu try to get Mando back! " +
                "Better luck next time!"
                )
            quit()
        else:
            print("You must choose yes or no")
            print("............TRY THAT AGAIN............")
            end_game()


# Win Game Function
def win_game():
    """
    Message to be displayed if they win the game.
    It will ask if they want to choose again.
    If they choose yes the game will begin again with challenge 1.
    If they choose no the game will quit.
    The while loops ensures the user only chooses y or n.
    """
    while True:
        print("Do you want to play again? y/n \n")
        user_input = str(input("").lower())
        if user_input == "y" or user_input == "Y":
            print("............Welcome back, lets go!!............")
            first_challenge()
        elif user_input == "n" or user_input == "N":
            print("Thanks for helping Grogu rescue his best pal!!")
            quit()
        else:
            print("You must choose yes or no")
            print("............TRY THAT AGAIN............")
            win_game()


# Main Function
def main():
    """
    Main function to start the game at the intro text.
    """
    intro_text()


main()
