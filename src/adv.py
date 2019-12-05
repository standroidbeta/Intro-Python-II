from src.room import Room
from src.player import Player
import sys

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Being lost for days in a hostile jungle trying to find two of the most 
valued and long-lost weapons has finally paid off!. 
                                
                           The Sword of Infinite Power
                                        and
                            The Shield of All Strength
                    
It is your mission to find these two relics for both the value that
they both and for your own protection.. 

The only exit is to the south.""",
                     ['The Sword of Infinite Power', 'The Shield of All Strength']),

}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

p_name = input('Please state your name.:''\n')

# Create an instance by using the player's inserted name
# and set the starting room to outside.

p = Player(p_name, room['outside'])

# Write a loop that:
#


# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#

def start_game():
    print('|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|\n')
    # * Prints the current room name
    print(f"Greetings {p_name}!\nThe room that you are in is:", p.current_room.name, '\n')
    print('|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|\n')
    # * Prints the current description (the textwrap module might be useful here).
    print('Available Directions:', p.current_room.description, '\n')
    print('|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|\n')
    # If the user enters "q", quit the game.
    print("Press 'q' anytime to quit the game. Otherwise have fun playing!\n")
    print('|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|\n')


start_game()


def play_game():
    while True:
        player_dir = input(f"{p_name}, where would you like to go? (Please press n, s, e or w):\n").lower()

        print('|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|')

        if player_dir == "n":
            # Check to see if n (North) exists. (How to check the existence of a direction?)
            if p.current_room.n_to is not None and p.items == []:
                p.current_room = p.current_room.n_to
                print("You are now in the:", p.current_room.name)
                print("Directions:", p.current_room.description)
            else:
                print("That's an invalid move. Please try again.")

        elif player_dir == "e":
            if p.current_room.e_to is not None and p.items == []:
                p.current_room = p.current_room.e_to
                print("You are now in the:", p.current_room.name)
                print("Directions:", p.current_room.description)
            else:
                print("That's an invalid move. Please try again.")

        elif player_dir == "s":
            if p.current_room.s_to is not None and p.items == []:
                p.current_room = p.current_room.s_to
                print("You are now in the:", p.current_room.name)
                print("Directions:", p.current_room.description)
            else:
                print("That's an invalid move. Please try again.")

        elif player_dir == "w":
            if p.current_room.w_to is not None and p.items == []:
                p.current_room = p.current_room.w_to
                print("You are now in the:", p.current_room.name)
                print("Directions:", p.current_room.description)
            else:
                print("That's an invalid move. Please try again.")

        elif player_dir == 'q':
            print("Thank you for playing!")
            sys.exit()


play_game()
