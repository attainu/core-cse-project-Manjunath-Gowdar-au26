# snake and ladder application
import random 


message = """
    Welcome to Snake and Ladder Game.
    Developed by: Manjunath AG

    Snake and Ladder values:
    --> Enter 1 to select default values for snake and ladder.
    --> Enter 2 to give values manually.
    """
print(message)

# snake and ladder positions
# default values to snake 

# key is tail position of snake
# value is head position of snake
# Therefore value > key 
option=int(input())
if option == 1:
    snakes = {
        17:7,
        62:19,
        54:34,
        87:36,
        64:60,
        93:73,
        95:75,
        98:76
}

    # key is starting position of ladder
    # value is ending position of ladder
    # Therefore value > key 
    ladders = {
        1:38,
        4:14,
        9:31,
        21:42,
        28:84,
        51:67,
        72:91,
        80:99
    }
    player_one_name = 'Nithya'
    player_one_initial_position = 0
    player_one_final_position = 0

    player_two_name = 'Manjunath'
    player_two_initial_position = 0
    player_two_final_position = 0

# manual data entry for snakes
elif option == 2 :
    no_of_snakes = int(input('Enter total number of snakes in the game '))
    print('Head position of snake should be greater than Tail position of the snake')

    snakes = {}
    for i in range(no_of_snakes):
        key=int(input('Enter Head position of snake '+ str(i+1)+'\t'))
        value=int(input('Enter Tail position of snake '+ str(i+1)+'\t'))
        if value < key:
            snakes[key]=value
        else:
            print('Invalid input, Head position of snake should be greater than Tail position of the snake')
            break
    
    # manual data entry for ladder
    no_of_ladders = int(input('Enter total number of ladders in the game '))
    print('Starting position of the ladder should be lesser than the Ending position of the ladder')

    ladders = {}
    for i in range(no_of_ladders):
        key=int(input('Enter starting position of ladder '+ str(i+1)+'\t'))
        value=int(input('Enter ending position of ladder '+ str(i+1)+'\t'))
        if value > key:
            ladders[key]=value
        else:
            print('Invalid input, Ending position of ladder should be greater than Starting position of the ladder')
            break
    
    player_one_name = input('Enter player one name ')
    player_one_initial_position = 0
    player_one_final_position = 0

    player_two_name = input('Enter player two name ')
    player_two_initial_position = 0
    player_two_final_position = 0


while (player_one_final_position <= 100 or player_two_final_position <= 100) :
    # player one rolls the dice 
    print(player_one_name +' is playing')
    dice_value = random.choice([1,2,3,4,5,6])
    if player_one_final_position+dice_value <= 100 :
        player_one_final_position = player_one_final_position + dice_value
        print(player_one_name + ' rolled a '+str(dice_value)+' and moved from the position '+str(player_one_initial_position)+' to the position '+str(player_one_final_position))
        player_one_initial_position = player_one_final_position
    # if player_one_initial_position in snakes.keys
    if (player_one_final_position == player_one_initial_position == 100) :
        print(player_one_name+' has won the game')
        break 
    

    # player two rolls the dice
    print(player_two_name +' is playing')
    dice_value = random.choice([1,2,3,4,5,6])
    if player_two_final_position+dice_value <= 100 :
        player_two_final_position = player_two_final_position + dice_value
        print(player_two_name + ' rolled a '+str(dice_value)+' and moved from the position '+str(player_two_initial_position)+' to the position '+str(player_two_final_position))
        player_two_initial_position = player_two_final_position
    if (player_two_final_position == player_two_initial_position == 100) :
        print(player_two_name+' has won the game')
        break 

    
