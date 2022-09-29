#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

import crayons
import requests

# Riddle API URL assigned to API variable
API = "https://riddles-api.vercel.app/random"


def showInstructions():
    """Show the game instructions when called"""
    # print a main menu and the commands, items and bonus
    print('''
    RPG Game
    ========
    Commands:
      go [direction: north, south, east or west]
      get [item]
    items:
      [key, potion, treasure, life, hammer]
    bonus:
      [riddles, teleport to frontdoor, monster]
    ''')

def showDescription():

    # print game description
    print(crayons.yellow('''
    =========
    Level 1: Find your way through this large hosuse by navigating through a series of rooms. Pick up choice items along the way until you get to dreamland.
    Level 2: Once in dreamland, grab the treasure and answer a dremaland  quiz to exit dreamland.
    Continue to navigate the migty house and find your way to the garden. in the garden, an important item is up for grabs.
    Level 3: Find your way to the front door. if you have three important items in yur possession, you stand a chance to win a grand prize by solving the dreamhosue riddle.
    =========
    '''))
    print(crayons.green('Hint! The key, potion and treasure are valuable'))
    print(crayons.red('Warning!!!!! Avoid the monster.'))


def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)

    a = rooms[currentRoom]
    print("You can go to any of the rooms listed below ")
    print(crayons.yellow(a.values()))

    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


    # an inventory, which is initially empty
inventory = []

    # A dictionary linking a room to other rooms
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
        'north': 'Master Bedroom'
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
        'south': 'Dining Room'

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
        'item': 'portalone',
        'home': 'Front Door'
    },

    'Hall Two': {
        'west': 'Stair Case'
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
        'south': 'Hall Two'
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
        'east': 'Temple'
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
        'item':'hammer'
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

decisionInitial = 1

   # breaking this while loop means the game is over
while (decisionInitial == 1):

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
            # check that they are allowed wherever they want to go
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


        if currentRoom == 'Dreamland':
            print(
                'You are trapped in dreamland. You have one chanve to wakeup or stay asleep forever.')
            print(f"{crayons.red('Danger!!! you have reached the forbidden room.')}")
            print(f"{crayons.yellow('Solve this riddle! to leave dreamland')}")

            resp = requests.get(f"{API}")
            print(resp.json().get("riddle"))
            riddle_answer = resp.json().get("answer")
            user_answer = input()

        # if user answer is not correct, user looses the game
            if (user_answer != riddle_answer):
                print(crayons.red("Stay asleep forever! "))
                break

        # if a player answers the riddle correctly , user gets teleported to front door
            else:
                print("Good Job! Proceed to the temple and grab the treasure")
                currentRoom = 'Temple'

        # Define how a player can win
        if currentRoom == 'Temple' and 'portalone' in inventory and 'key' in inventory and 'treasure' in inventory:

            print('You have found the treasure and escaped the house!!.....YOU WIN')
            break



