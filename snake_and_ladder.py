# snake and ladder application
import random       # to get random value random module is used

sOneHead = 2
sOneTail = 8

lOneStart = 10
lOneEnd = 20

pOneName = 'Max'
pOneInitialPosition = 0
pOneFinalPosition = 0

pTwoName = 'White'
pTwoInitialPosition = 0
pTwoFinalPosition = 0


while (pOneFinalPosition <= 100 or pTwoFinalPosition <= 100) :
    # player one rolls the dice 
    print('p 1 is playing')
    dice_value = random.choice([1,2,3,4,5,6])
    if pOneFinalPosition+dice_value <= 100 :
        pOneFinalPosition = pOneFinalPosition + dice_value
        print(pOneName + ' rolled a '+str(dice_value)+' and moved from '+str(pOneInitialPosition)+' to '+str(pOneFinalPosition))
        pOneInitialPosition = pOneFinalPosition
    if pOneFinalPosition == pOneInitialPosition == 100 :
        print('player 1 has wone the game')
        break 
    

    # player two rolls the dice
    print('p 2 is playing')
    dice_value = random.choice([1,2,3,4,5,6])
    if pTwoFinalPosition+dice_value <= 100 :
        pTwoFinalPosition = pTwoFinalPosition + dice_value
        print(pTwoName + ' rolled a '+str(dice_value)+' and moved from '+str(pTwoInitialPosition)+' to '+str(pTwoFinalPosition))
        pTwoInitialPosition = pTwoFinalPosition
    if pTwoFinalPosition == pTwoInitialPosition == 100 :
        print('player 2 has wone the game')
        break 

    
