
import snake_and_ladder

# function start will create instance of the call game and call's the method.
def start():
    # creating instance of the class Game from the module snake_and_ladder
    game_one = snake_and_ladder.Game()

    # running the game 
    input('Hit enter to start the game')
    game_one.play()

# calling the function start 
start()