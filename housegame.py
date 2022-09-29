#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

import crayons

import requests

#Riddle API URL assigned to API variable
API = "https://riddles-api.vercel.app/random"


def showInstructions():
    """Show the game instructions when called"""
    # print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction: north, south, east or west]
      get [item]
    ''')


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
        'east' : 'Utility Room',
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

    'Master Bedroon': {
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
        'north' : 'Garage2',
        'west': 'Secret Passage'
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
        'east' : 'Forbidden'
    }




}

# start the player in the Hall
currentRoom = 'Hall'
# Call this function to display instructions to player
showInstructions()

# breaking this while loop means the game is over
while True:

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

        # Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

	# Player must answer a riddle to get out of this room and teleport to Front Door

    if currentRoom == 'Forbidden':
        print('Danger!!! you have reached the forbidden room. Answer this riddle! to save your life')
        print(f"{crayons.red('Danger!!! you have reached the forbidden room.')}")
        print (f"{crayons.yellow('Answer this riddle! to save your life')}")

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

    if currentRoom == 'Patio' and 'portalone' in inventory and 'potion' in inventory:

        print('You have ten seconds to get an from the kitchen.............. ')

    
        print('You escaped the house with the ultra rare key and magic potion.............. YOU WIN!')
        break
