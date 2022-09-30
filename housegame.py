#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

import crayons
import requests
from time import sleep

# Riddle API URL assigned to API variable
API = "https://riddles-api.vercel.app/random"


def showInstructions():
    """Show the game instructions when called"""
    # print a main menu and the commands, items and bonus
    print('''
    Magic House Navigator
    ========
    Commands:
      go [direction: (north, south, east or west)]
      get [item]
    items:
      [key, potion, treasure, portaone, magic ring]
    bonus and evil:
      [riddles, teleport with (home), monster]
    ''')


def showDescription():
    """Show how to play the game when called"""

    # print a description of how to play and win the game
    print(crayons.yellow('''
    ===================================================
    Aim: Win the game and earn a trip to Magic Land
    Level 1: Find your way through this large hosuse by navigating through a series of rooms. Pick up choice items along the way until you get to dreamland.
    Level 2: Once in dreamland,  answer a dremaland  quiz to exit dreamland and teleport to the temple.
    Level 3: Continue to navigate the migty house and find your way to the garden. in the garden, an important item is up for grabs.
    Level 3: Find your way to the forbidden room through the secret passage. An important item awaits,if you can solve the riddle. 
    level 4: Go to the patio, with the right items, you Win! and earn a Navigator Badge.
    ===================================================
    '''))
    print(crayons.green('Hint! The key, magic ring, portalone, and treasure are valuable'))
    print(crayons.green(
        'Hint! Sometimes, It is okay to not know the answer'))
    print(crayons.green(
        'Hint! go ghostmode to leave temple'))
    print(crayons.red('Warning!!!!! Avoid the monster.'))


def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('-------------------------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)

    a = rooms[currentRoom]
    print("You can go to any of these rooms or grab a item if available")
    print("-------------------------------------------")
    print(crayons.red(a.values()))
    print("-------------------------------------------")

    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


    # an inventory, which is initially empty
inventory = []

# A dictionary of rooms linkng rooms to each other
rooms = {

    'Front Door': {
        'east': 'Hall',
        'home': 'Patio'
    },

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'west': 'Front Door',
        'item': 'key'
    },

    'Hall Two': {
        'west': 'Stair Case',
        'north': 'Dream Land'
    },


    'Hall Three': {
        'north': 'Kitchen',
        'south': 'Garage1',
        'east': 'Utility Room',
        'west': 'Laundary'
    },

    'Kitchen': {
        'north': 'Hall',
        'south': 'Hall Three',
        'item': 'monster',
    },
    'Dining Room': {
        'west': 'Hall',
        'north': 'Garden',
        'east': 'Living Room',
        'item': 'potion'
    },
    'Garden': {
        'south': 'Dining Room',
        'item': 'magic ring'

    },

    'Living Room': {
        'west': 'Dining Room',
        'south': 'Rest Room1',
        'north': 'Stair Case',
        'east': 'Game Room'
    },

    'Game Room': {
        'west': 'Living Room',
        'south': 'Theatre',
        'north': 'Rest Room2'
    },

    'Theatre': {
        'north': 'Game Room',
        'south': 'Secret Passage'
    },


    'Stair Case': {
        'west': 'Patio',
        'south': 'Living Room',
        'east': 'Hall Two',
    },

    'Patio': {
        'east': 'Stair Case',
        'home': 'Front Door'
    },

    'Rest Room1': {
        'north': 'Living Room'
    },

    'Rest Room2': {
        'south': 'Game Room'
    },

    'Forbidden': {
        'north': 'Garage2'
    },

    'Dream Land': {
        'south': 'Hall Two',
        
    },

    'Garage1': {
        'south': 'Hall Three',
        'east': 'Garage2'
    },


    'Garage2': {
        'west': 'Garage1',
        'south': 'Forbidden',
        'north': 'Utility Room',
        'east': 'Abyss'
    },


    'Forbidden': {
        'north': 'Garage2',
        'west': 'Secret Passage',
        'east': 'Temple',
        'item':'portalone'
    },

    'Abyss': {
        'west': 'Garage2'
    },

    'Utility Room': {
        'west': 'Hall Three',
        'south': 'Garage2',
    },

    'Laundary': {
        'east': 'Hall Three'
    },

    'Secret Passage': {
        'north': 'Theatre',
        'east': 'Forbidden',
        'item': 'hammer'
    },

    'Temple': {
        'ghostmode': 'Laundary',
        'west': 'Forbidden',
        'item': 'treasure'
    }

}

# start the player in the Hall
currentRoom = 'Hall'

# Calling this function to describe gameplay to user
showDescription()
# Call this function to display instructions to player
showInstructions()



# this while loop ensures tha the game keeps running until a conditin is met
# breaking this while loop means the game is over
while True:

    # Calling this funtion to displayplayer status
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they a player is allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print(crayons.red('You can\'t go that way!'))

    # if they type 'get' first
    if move[0] == 'get':
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory.append(move[1])
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

        # If a player enters a room with a monster

    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break

    # If player is in the forbidden room
    # Player must answer a riddle to get out of this room and teleport to Front Door

    if currentRoom == 'Forbidden':
        print(f"{crayons.red('Danger!!! you have reached the forbidden room.')}")
        print(f"{crayons.yellow('Answer this riddle! to save your life')}")

        resp = requests.get(f"{API}")
        print(resp.json().get("riddle"))
        riddle_answer = resp.json().get("answer")
        user_answer = input()

    # if user answer is not correct, user looses the game
        if (user_answer != riddle_answer):
            print(crayons.red("You have met your end! "))
            break

    # if a player answers the riddle correctly , user gets teleported to front door
        else:
            print("You are safe! Proceed to front door")
            currentRoom = 'Front Door'

    # If player is in Dream Land room
    # Player can fail a riddle to get out of this room and teleport to Temple
    if currentRoom == 'Dream Land':
        print(f"{crayons.red('You are trapped in dreamland. You have one chance to wakeup or stay asleep forever.')}")
        print(f"{crayons.yellow('Solve this riddle! to leave dreamland')}")

        resp = requests.get(f"{API}")
        print(resp.json().get("riddle"))
        riddle_answer = resp.json().get("answer")
        user_answer = input()

    # If user answer is not correct, player spends some time sleeping!!!
    # Player gets to chooose the sleep duration 
        if (user_answer != riddle_answer):
            print(crayons.red("Wrong answer!! Now you will fall asleep. "))

            #p Pompt plyer to choose a numner nad store that value as a string in "num" variable
            num =input(crayons.red("Before falling asleep, pick a number from (10-60): "))

            # Convert the variable to an integer
            number =int(num)
            # Create a range of numbers with the variable and loop through it.
            for i in range(number):
                # Use sleep function to set time that user sleeps (0.5  x  g)s
                sleep(1)
                print('Sleep in peace!!!! for: ',number,'s')
            # Teleport player to 'Rest Room" agfter waking up from sleep
            currentRoom = 'Rest Room2'
            
    # If a player answers the riddle correctly , player gets teleported to front door
        else:
            print("Good Job! Proceed to the temple and grab the treasure")
            currentRoom = 'Temple'

    # Define how a player can win
    if currentRoom == 'Patio' and 'portalone' in inventory and 'key' in inventory and 'treasure' in inventory and 'magic ring' in inventory:

        print('Congatulations YOU WIN!!! You have earned the Navigtor Badge!! You have earned a trip to Magic Land!!')
        break
