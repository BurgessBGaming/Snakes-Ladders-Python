import random
import time
dice_roll = 0
dice = ''
player1pos = 0
player2pos = 0
player3pos = 0
player4pos = 0
savep1pos = 0
savep2pos = 0
savep3pos = 0
savep4pos = 0
players = 0
computers = 0
double_meter1 = 0
double_meter2 = 0
double_meter3 = 0
double_meter4 = 0
double_meter_cap = 100
goal = 100
turns = []
p1_items = ['Back', '', '', '']
p2_items = ['Back', '', '', '']
p3_items = ['Back', '', '', '']
p4_items = ['Back', '', '', '']
p1_status = ''
p2_status = ''
p3_status = ''
p4_status = ''
item_chance = 20
item_roll = 0
item_get = ''
item_replace = 0
item_fix = 0
item_use = 0
pear_effect = 0
signal = 0
game = 0

def titleScreen():
    print(' ------------------------------------------')
    print('|     /---/      S N A K E S       ____    |')
    print('|    /---/                        / . .\   |')
    print('|   /---/             &           \  ---<  |')
    print('|  /---/                           \  /    |')
    print('| /---/         L A D D E R S      / /     |')
    print(' ------------------------------------------')
    print('                 Ver. 1.1.0               ')
    time.sleep(2)
    print('')
    input('            Press Enter to Begin          ')
    print('')

def playerCount():
    global players
    print('How Many Players?')
    time.sleep(2)
    players = int(input('1, 2, 3, 4: '))
    if players > 4 or players < 1:
        print('Nope! Pick again!')
        playerCount()
        time.sleep(2)
        print('')
    else:
        computers = 4 - players
        if players == 1:
            print('You will play a game with', players, 'human and', computers, 'computers!')
        elif computers == 1:
            print('You will play a game with', players, 'humans and', computers, 'computer!')
        else:
            print('You will play a game with', players, 'humans and', computers, 'computers!')
        time.sleep(2)
        print('')
    
def turnOrder():
    global players
    global p1turnroll
    global p2turnroll
    global p3turnroll
    global p4turnroll
    print('Who goes first?')
    time.sleep(2)
    print('Player 1! GO!')
    time.sleep(1)
    dice = input('Roll! (Press Enter to Roll)')
    dice_roll = random.choice(range(1, 7))
    print('The die rolled', dice_roll)
    time.sleep(2)
    p1turnroll = dice_roll
    print('')
    
    if players >= 2:
        print('Player 2! GO!')
        time.sleep(1)
        dice = input('Roll! (Press Enter to Roll)')
        dice_roll = random.choice(range(1, 7))
        print('The die rolled', dice_roll)
        time.sleep(2)
        p2turnroll = dice_roll 
        print('')
    else:
        print('Player 2! GO!')
        time.sleep(1)
        dice_roll = random.choice(range(1, 7))
        print('The die rolled', dice_roll)
        time.sleep(2)
        p2turnroll = dice_roll
        print('')
        
    if players >= 3:
        print('Player 3! GO!')
        time.sleep(1)
        dice = input('Roll! (Press Enter to Roll)')
        dice_roll = random.choice(range(1, 7))
        print('The die rolled', dice_roll)
        time.sleep(2)
        p3turnroll = dice_roll 
        print('')
    else:
        print('Player 3! GO!')
        time.sleep(1)
        dice_roll = random.choice(range(1, 7))
        print('The die rolled', dice_roll)
        time.sleep(2)
        p3turnroll = dice_roll
        print('')
        
    if players >= 4:
        print('Player 4! GO!')
        time.sleep(1)
        dice = input('Roll! (Press Enter to Roll)')
        dice_roll = random.choice(range(1, 7))
        print('The die rolled', dice_roll)
        time.sleep(2)
        p4turnroll = dice_roll 
        print('')
    else:
        print('Player 4! GO!')
        time.sleep(1)
        dice_roll = random.choice(range(1, 7))
        print('The die rolled', dice_roll)
        time.sleep(2)
        p4turnroll = dice_roll
        print('')
    
def turnRollAgain():
    #Roll again
    global p1turnroll
    global p2turnroll
    global p3turnroll
    global p4turnroll
    global players
    global turns
    if p1turnroll == p2turnroll and p1turnroll != p3turnroll and p1turnroll != p4turnroll:
        print('Players 1 & 2, roll again!')
        time.sleep(2)
        print('')
        print('Player 1! GO!')
        time.sleep(1)
        dice = input('Roll! (Press Enter to Roll)')
        dice_roll = random.choice(range(1, 7))
        print('The die rolled', dice_roll)
        p1turnroll = dice_roll
        time.sleep(2)
        print('')
        
        if players >= 2:
            print('Player 2! GO!')
            time.sleep(1)
            dice = input('Roll! (Press Enter to Roll)')
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p2turnroll = dice_roll 
            time.sleep(2)
            print('')
        else:
            print('Player 2! GO!')
            time.sleep(1)
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p2turnroll = dice_roll
            time.sleep(2)
            print('')
            
    elif p1turnroll == p3turnroll and p1turnroll != p2turnroll and p1turnroll != p4turnroll:
        print('Players 1 & 3, roll again!')
        time.sleep(2)
        print('')
        print('Player 1! GO!')
        time.sleep(1)
        dice = input('Roll! (Press Enter to Roll)')
        dice_roll = random.choice(range(1, 7))
        print('The die rolled', dice_roll)
        p1turnroll = dice_roll
        time.sleep(2)
        print('')
        
        if players >= 3:
            print('Player 3! GO!')
            time.sleep(1)
            dice = input('Roll! (Press Enter to Roll)')
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p3turnroll = dice_roll
            time.sleep(2)
            print('')
        else:
            print('Player 3! GO!')
            time.sleep(1)
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p3turnroll = dice_roll
            time.sleep(2)
            print('')
            
    elif p1turnroll == p4turnroll and p1turnroll != p2turnroll and p1turnroll != p3turnroll:
        print('Players 1 & 4, roll again!')
        time.sleep(2)
        print('')
        print('Player 1! GO!')
        time.sleep(1)
        dice = input('Roll! (Press Enter to Roll)')
        dice_roll = random.choice(range(1, 7))
        print('The die rolled', dice_roll)
        p1turnroll = dice_roll
        time.sleep(2)
        print('')
        
        if players >= 4:
            print('Player 4! GO!')
            time.sleep(1)
            dice = input('Roll! (Press Enter to Roll)')
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p4turnroll = dice_roll 
            time.sleep(2)
            print('')
        else:
            print('Player 4! GO!')
            time.sleep(1)
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p4turnroll = dice_roll
            time.sleep(2)
            print('')
            
    elif p2turnroll == p3turnroll and p2turnroll != p1turnroll and p2turnroll != p4turnroll:
        print('Players 2 & 3, roll again!')
        time.sleep(2)
        print('')
        if players >= 2:
            print('Player 2! GO!')
            time.sleep(1)
            dice = input('Roll! (Press Enter to Roll)')
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p2turnroll = dice_roll
            time.sleep(2)
            print('')
        else:
            print('Player 2! GO!')
            time.sleep(1)
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p2turnroll = dice_roll
            time.sleep(2)
            print('')
        
        if players >= 3:
            print('Player 3! GO!')
            time.sleep(1)
            dice = input('Roll! (Press Enter to Roll)')
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p3turnroll = dice_roll 
            time.sleep(2)
            print('')
        else:
            print('Player 3! GO!')
            time.sleep(1)
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p3turnroll = dice_roll
            time.sleep(2)
            print('')
            
    elif p2turnroll == p4turnroll and p2turnroll != p1turnroll and p2turnroll != p3turnroll:
        print('Players 2 & 4, roll again!')
        time.sleep(2)
        print('')
        if players >= 2:
            print('Player 2! GO!')
            time.sleep(1)
            dice = input('Roll! (Press Enter to Roll)')
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p2turnroll = dice_roll
            time.sleep(2)
            print('')
        else:
            print('Player 2! GO!')
            time.sleep(1)
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p2turnroll = dice_roll
            time.sleep(2)
            print('')
        
        if players >= 4:
            print('Player 4! GO!')
            time.sleep(1)
            dice = input('Roll! (Press Enter to Roll)')
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p4turnroll = dice_roll 
            time.sleep(2)
            print('')
        else:
            print('Player 4! GO!')
            time.sleep(1)
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p4turnroll = dice_roll
            time.sleep(2)
            print('')
            
    elif p3turnroll == p4turnroll and p3turnroll != p1turnroll and p3turnroll != p2turnroll:
        print('Players 3 & 4, roll again!')
        time.sleep(2)
        print('')
        if players >= 3:
            print('Player 3! GO!')
            time.sleep(1)
            dice = input('Roll! (Press Enter to Roll)')
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p3turnroll = dice_roll 
            time.sleep(2)
            print('')
        else:
            print('Player 3! GO!')
            time.sleep(1)
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p3turnroll = dice_roll
            time.sleep(2)
            print('')
        
        if players >= 4:
            print('Player 4! GO!')
            time.sleep(1)
            dice = input('Roll! (Press Enter to Roll)')
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p4turnroll = dice_roll 
            time.sleep(2)
            print('')
        else:
            print('Player 4! GO!')
            time.sleep(1)
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p4turnroll = dice_roll
            time.sleep(2)
            print('')
            
    elif p1turnroll == p2turnroll and p1turnroll == p3turnroll and p1turnroll != p4turnroll:
        print('Players 1, 2 & 3, roll again!')
        time.sleep(2)
        print('')
        print('Player 1! GO!')
        time.sleep(1)
        dice = input('Roll! (Press Enter to Roll)')
        dice_roll = random.choice(range(1, 7))
        print('The die rolled', dice_roll)
        p1turnroll = dice_roll
        time.sleep(2)
        print('')
        
        if players >= 2:
            print('Player 2! GO!')
            time.sleep(1)
            dice = input('Roll! (Press Enter to Roll)')
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p2turnroll = dice_roll 
            time.sleep(2)
            print('')
        else:
            print('Player 2! GO!')
            time.sleep(1)
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p2turnroll = dice_roll
            time.sleep(2)
            print('')

        if players >= 3:
            print('Player 3! GO!')
            time.sleep(1)
            dice = input('Roll! (Press Enter to Roll)')
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p3turnroll = dice_roll 
            time.sleep(2)
            print('')
        else:
            print('Player 3! GO!')
            time.sleep(1)
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p3turnroll = dice_roll
            time.sleep(2)
            print('')

    elif p1turnroll == p2turnroll and p1turnroll == p4turnroll and p1turnroll != p3turnroll:
        print('Players 1, 2 & 4, roll again!')
        time.sleep(2)
        print('')
        print('Player 1! GO!')
        time.sleep(1)
        dice = input('Roll! (Press Enter to Roll)')
        dice_roll = random.choice(range(1, 7))
        print('The die rolled', dice_roll)
        p1turnroll = dice_roll
        time.sleep(2)
        print('')

        if players >= 2:
            print('Player 2! GO!')
            time.sleep(1)
            dice = input('Roll! (Press Enter to Roll)')
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p2turnroll = dice_roll 
            time.sleep(2)
            print('')
        else:
            print('Player 2! GO!')
            time.sleep(1)
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p2turnroll = dice_roll
            time.sleep(2)
            print('')

        if players >= 4:
            print('Player 4! GO!')
            time.sleep(1)
            dice = input('Roll! (Press Enter to Roll)')
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p4turnroll = dice_roll 
            time.sleep(2)
            print('')
        else:
            print('Player 4! GO!')
            time.sleep(1)
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p4turnroll = dice_roll
            time.sleep(2)
            print('')
            
    elif p2turnroll == p3turnroll and p2turnroll == p4turnroll and p2turnroll != p1turnroll:
        print('Players 2, 3 & 4, roll again!')
        time.sleep(2)
        print('')
        if players >= 2:
            print('Player 2! GO!')
            time.sleep(1)
            dice = input('Roll! (Press Enter to Roll)')
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p2turnroll = dice_roll 
            time.sleep(2)
            print('')
        else:
            print('Player 2! GO!')
            time.sleep(1)
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p2turnroll = dice_roll
            time.sleep(2)
            print('')

        if players >= 3:
            print('Player 3! GO!')
            time.sleep(1)
            dice = input('Roll! (Press Enter to Roll)')
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p3turnroll = dice_roll 
            time.sleep(2)
            print('')
        else:
            print('Player 3! GO!')
            time.sleep(1)
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p3turnroll = dice_roll
            time.sleep(2)
            print('')

        if players >= 4:
            print('Player 4! GO!')
            time.sleep(1)
            dice = input('Roll! (Press Enter to Roll)')
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p4turnroll = dice_roll 
            time.sleep(2)
            print('')
        else:
            print('Player 4! GO!')
            time.sleep(1)
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p4turnroll = dice_roll
            time.sleep(2)
            print('')

    elif p1turnroll == p2turnroll and p1turnroll == p3turnroll and p1turnroll == p4turnroll:
        print('Everyone, roll again!')
        time.sleep(2)
        print('')
        print('Player 1! GO!')
        time.sleep(1)
        dice = input('Roll! (Press Enter to Roll)')
        dice_roll = random.choice(range(1, 7))
        print('The die rolled', dice_roll)
        p1turnroll = dice_roll
        time.sleep(2)
        print('')

        if players >= 2:
            print('Player 2! GO!')
            time.sleep(1)
            dice = input('Roll! (Press Enter to Roll)')
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p2turnroll = dice_roll 
            time.sleep(2)
            print('')
        else:
            print('Player 2! GO!')
            time.sleep(1)
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p2turnroll = dice_roll
            time.sleep(2)
            print('')

        if players >= 3:
            print('Player 3! GO!')
            time.sleep(1)
            dice = input('Roll! (Press Enter to Roll)')
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p3turnroll = dice_roll 
            time.sleep(2)
            print('')
        else:
            print('Player 3! GO!')
            time.sleep(1)
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p3turnroll = dice_roll
            time.sleep(2)
            print('')

        if players >= 4:
            print('Player 4! GO!')
            time.sleep(1)
            dice = input('Roll! (Press Enter to Roll)')
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p4turnroll = dice_roll 
            time.sleep(2)
            print('')
        else:
            print('Player 4! GO!')
            time.sleep(1)
            dice_roll = random.choice(range(1, 7))
            print('The die rolled', dice_roll)
            p4turnroll = dice_roll
            time.sleep(2)
            print('')

def finalOrder():
    global p1turnroll
    global p2turnroll
    global p3turnroll
    global p4turnroll
    global turns
    global game
    turns = [p1turnroll, p2turnroll, p3turnroll, p4turnroll]
    turns.sort()
    turns.reverse()
    
    if max(turns) == p1turnroll:
        print('Player 1 goes first!')
        time.sleep(2)
        #Second
        if turns[1] == p2turnroll:
            print('Followed by Player 2!')
        elif turns[1] == p3turnroll:
            print('Followed by Player 3!')
        elif turns[1] == p4turnroll:
            print('Followed by Player 4!')
        time.sleep(2)
        #Third
        if turns[2] == p2turnroll:
            print('Next is Player 2!')
        elif turns[2] == p3turnroll:
            print('Next is Player 3!')
        elif turns[2] == p4turnroll:
            print('Next is Player 4!')
        time.sleep(2)
        #Fourth
        if turns[3] == p2turnroll:
            print('And last, Player 2!')
        elif turns[3] == p3turnroll:
            print('And last, Player 3!')
        elif turns[3] == p4turnroll:
            print('And last, Player 4!')
        time.sleep(2)
    elif max(turns) == p2turnroll:
        print('Player 2 goes first!')
        time.sleep(2)
        #Second
        if turns[1] == p1turnroll:
            print('Followed by Player 1!')
        elif turns[1] == p3turnroll:
            print('Followed by Player 3!')
        elif turns[1] == p4turnroll:
            print('Followed by Player 4!')
        time.sleep(2)
        #Third
        if turns[2] == p1turnroll:
            print('Next is Player 1!')
        elif turns[2] == p3turnroll:
            print('Next is Player 3!')
        elif turns[2] == p4turnroll:
            print('Next is Player 4!')
        time.sleep(2)
        #Fourth
        if turns[3] == p1turnroll:
            print('And last, Player 1!')
        elif turns[3] == p3turnroll:
            print('And last, Player 3!')
        elif turns[3] == p4turnroll:
            print('And last, Player 4!')
        time.sleep(2)
    elif max(turns) == p3turnroll:
        print('Player 3 goes first!')
        time.sleep(2)
        #Second
        if turns[1] == p1turnroll:
            print('Followed by Player 1!')
        elif turns[1] == p2turnroll:
            print('Followed by Player 2!')
        elif turns[1] == p4turnroll:
            print('Followed by Player 4!')
        time.sleep(2)
        #Third
        if turns[2] == p1turnroll:
            print('Next is Player 1!')
        elif turns[2] == p2turnroll:
            print('Next is Player 2!')
        elif turns[2] == p4turnroll:
            print('Next is Player 4!')
        time.sleep(2)
        #Fourth
        if turns[3] == p1turnroll:
            print('And last, Player 1!')
        elif turns[3] == p2turnroll:
            print('And last, Player 2!')
        elif turns[3] == p4turnroll:
            print('And last, Player 4!')
        time.sleep(2)
    elif max(turns) == p4turnroll:
        print('Player 4 goes first!')
        time.sleep(2)
        #Second
        if turns[1] == p1turnroll:
            print('Followed by Player 1!')
        elif turns[1] == p2turnroll:
            print('Followed by Player 2!')
        elif turns[1] == p3turnroll:
            print('Followed by Player 3!')
        time.sleep(2)
        #Third
        if turns[2] == p1turnroll:
            print('Next is Player 1!')
        elif turns[2] == p2turnroll:
            print('Next is Player 2!')
        elif turns[2] == p3turnroll:
            print('Next is Player 3!')
        time.sleep(2)
        #Fourth
        if turns[3] == p1turnroll:
            print('And last, Player 1!')
        elif turns[3] == p2turnroll:
            print('And last, Player 2!')
        elif turns[3] == p3turnroll:
            print('And last, Player 3!')
        time.sleep(2)
    game = 1
    print('')

def P1DiceRoll():
    global double_meter1
    global player1pos
    global player2pos
    global player3pos
    global player4pos
    global double_meter_cap
    global dice
    global item_chance
    global item_roll
    global p1_items
    global p1_status
    global p2_status
    global p3_status
    global p4_status
    global item_get
    global item_fix
    global item_use
    global savep1pos
    global savep2pos
    global savep3pos
    global savep4pos
    global signal
    item_fix = 1
    print('Player 1! GO!')
    time.sleep(1)
    print('Double Meter:', double_meter1)
    print('Current position:', player1pos)
    print('Status Effect:', p1_status)
    if double_meter1 == double_meter_cap:
            print('Double Roll Ready!')
    if dice != 'Single' or dice != 'Double' or dice != 'Item':
        dice = input('Single/Double/Item: ')
    if dice.lower() == 'single':
        dice_roll = random.choice(range(1, 7))
        print('The die rolled', dice_roll)
        time.sleep(1)
        if p1_status == 'Apple':
            dice_roll += 3
            p1_status = ''
        elif p1_status == 'G-Apple':
            dice_roll += 6
            p1_status = ''
        elif p1_status == 'Pear':
            dice_roll -= 3
            p1_status = ''
        elif p1_status == 'G-Pear':
            dice_roll -= 6
            p1_status = ''
        elif p1_status == 'EX':
            ex_dice_roll = random.choice(range(1, 7))
            print('Extra die rolls', ex_dice_roll)
            dice_roll += ex_dice_roll
            p1_status = ''
            time.sleep(1)
        elif p1_status == 'Double':
            dice_roll *= 2
            p1_status = ''
        elif p1_status == 'Half':
            dice_roll //= 2
            p1_status = ''
        print('Player 1 moves', dice_roll, 'spaces!')
        player1pos += dice_roll
        time.sleep(1)
        print('Player 1 is now at space #',player1pos)
        time.sleep(2)
        for i in range(dice_roll):
            double_meter1 += 5
        if double_meter1 > double_meter_cap:
            while double_meter1 != double_meter_cap:
                double_meter1 -= 1
    elif dice.lower() == 'double':
        if double_meter1 == 100:    
            print('DOUBLE ROLL!')
            time.sleep(1)
            dice_roll = random.choice(range(2, 13))
            print('The dice rolled', dice_roll)
            time.sleep(1)
            if p1_status == 'Apple':
                dice_roll += 3
                p1_status = ''
            elif p1_status == 'G-Apple':
                dice_roll += 6
                p1_status = ''
            elif p1_status == 'Pear':
                dice_roll -= 3
                p1_status = ''
            elif p1_status == 'G-Pear':
                dice_roll -= 6
                p1_status = ''
            elif p1_status == 'EX':
                ex_dice_roll = random.choice(range(1, 7))
                print('Extra die rolls', ex_dice_roll)
                dice_roll += ex_dice_roll
                p1_status = ''
                time.sleep(1)
            elif p1_status == 'Double':
                dice_roll *= 2
                p1_status = ''
            elif p1_status == 'Half':
                dice_roll //= 2
                p1_status = ''
            print('Player 1 moves', dice_roll, 'spaces!')
            player1pos += dice_roll
            time.sleep(1)
            print('Player 1 is now at space #',player1pos)
            time.sleep(2)
            double_meter1 = 0
        else:
            print("Can't use double roll.")
            time.sleep(2)
            P1DiceRoll()
    elif dice.lower() == 'item':
        if item_use == 1:
            print('Select your item:', p1_items)
            item_select = input()
            if item_select.lower() == 'back':
                P1DiceRoll()
            elif item_select.lower() == 'plus apple':
                if p1_items[1] == 'Plus Apple' or p1_items[2] == 'Plus Apple' or p1_items[3] == 'Plus Apple':
                    print('Player 1 used the Plus Apple!')
                    time.sleep(2)
                    if p1_status == 'Pear':
                        print('The pear effect has been cancelled. They will roll normally.')
                        p1_status = ''
                    elif p1_status == 'G-Pear':
                        print('The Golden Pear effect has been halved. They will now go -3.')
                        p1_status = 'Pear'
                    else:
                        print("They'll move 3 extra spaces with this next roll!")
                        p1_status = 'Apple'
                    time.sleep(2)
                    if p1_items.index('Plus Apple') == 1:
                        p1_items[1] = ''
                    elif p1_items.index('Plus Apple') == 2:
                        p1_items[2] = ''
                    elif p1_items.index('Plus Apple') == 3:
                        p1_items[3] = ''
                    item_use = 0
                    P1DiceRoll()
                else:
                    print("You don't have a Plus Apple!")
                    time.sleep(2)
                    P1DiceRoll()
            elif item_select.lower() == 'golden plus apple':
                if p1_items[1] == 'Golden Plus Apple' or p1_items[2] == 'Golden Plus Apple' or p1_items[3] == 'Golden Plus Apple':
                    print('Player 1 used the Golden Plus Apple!')
                    time.sleep(2)
                    if p1_status == 'Pear':
                        print('The pear effect has been overridden. They will now move +3.')
                        p1_status = 'Apple'
                    elif p1_status == 'G-Pear':
                        print('The Golden Pear cancelled. They will roll normally.')
                        p1_status = ''
                    else:
                        print("They'll move 6 extra spaces with this next roll!")
                        p1_status = 'G-Apple'
                    time.sleep(2)
                    if p1_items.index('Golden Plus Apple') == 1:
                        p1_items[1] = ''
                    elif p1_items.index('Golden Plus Apple') == 2:
                        p1_items[2] = ''
                    elif p1_items.index('Golden Plus Apple') == 3:
                        p1_items[3] = ''
                    item_use = 0
                    P1DiceRoll()
                else:
                    print("You don't have a Golden Plus Apple!")
                    time.sleep(2)
                    P1DiceRoll()
            elif item_select.lower() == 'minus pear':
                if p1_items[1] == 'Minus Pear' or p1_items[2] == 'Minus Pear' or p1_items[3] == 'Minus Pear':
                    print('Player 1 used the Minus Pear!')
                    time.sleep(2)
                    print('Who would you like to use it on?')
                    print('1 / 2 / 3 / 4')
                    pear_effect = int(input())
                    if pear_effect == 1:
                        print('Player 1 used the Minus Pear on themselves!')
                        if p1_status == 'Apple':
                            print('The apple effect has been cancelled. They will roll normally.')
                            p1_status = ''
                        elif p1_status == 'G-Apple':
                            print('The Golden Apple effect has been halved. They will now go +3.')
                            p1_status = 'Apple'
                        else:
                            print("They'll move 3 less spaces with this next roll!")
                            p1_status = 'Pear'
                    elif pear_effect == 2:
                        print('Player 1 used the Minus Pear on Player 2!')
                        if p2_status == 'Apple':
                            print('The apple effect has been cancelled. They will roll normally.')
                            p2_status = ''
                        elif p2_status == 'G-Apple':
                            print('The Golden Apple effect has been halved. They will now go +3.')
                            p2_status = 'Apple'
                        else:
                            print("They'll move 3 less spaces with this next roll!")
                            p2_status = 'Pear'
                    elif pear_effect == 3:
                        print('Player 1 used the Minus Pear on Player 3!')
                        if p3_status == 'Apple':
                            print('The apple effect has been cancelled. They will roll normally.')
                            p3_status = ''
                        elif p3_status == 'G-Apple':
                            print('The Golden Apple effect has been halved. They will now go +3.')
                            p3_status = 'Apple'
                        else:
                            print("They'll move 3 less spaces with this next roll!")
                            p3_status = 'Pear'
                    elif pear_effect == 4:
                        print('Player 1 used the Minus Pear on Player 4!')
                        if p4_status == 'Apple':
                            print('The apple effect has been cancelled. They will roll normally.')
                            p4_status = ''
                        elif p4_status == 'G-Apple':
                            print('The Golden Apple effect has been halved. They will now go +3.')
                            p4_status = 'Apple'
                        else:
                            print("They'll move 3 less spaces with this next roll!")
                            p4_status = 'Pear'
                    else:
                        print('You ended up tossing the pear...')
                    time.sleep(2)
                    if p1_items.index('Minus Pear') == 1:
                        p1_items[1] = ''
                    elif p1_items.index('Minus Pear') == 2:
                        p1_items[2] = ''
                    elif p1_items.index('Minus Pear') == 3:
                        p1_items[3] = ''
                    item_use = 0
                    P1DiceRoll()
                else:
                    print("You don't have a Minus Pear!")
                    time.sleep(2)
                    P1DiceRoll()
            elif item_select.lower() == 'golden minus pear':
                if p1_items[1] == 'Golden Minus Pear' or p1_items[2] == 'Golden Minus Pear' or p1_items[3] == 'Golden Minus Pear':
                    print('Player 1 used the Golden Minus Pear!')
                    time.sleep(2)
                    print('Who would you like to use it on?')
                    print('1 / 2 / 3 / 4')
                    pear_effect = int(input())
                    if pear_effect == 1:
                        print('Player 1 used the Golden Minus Pear on themselves!')
                        if p1_status == 'Apple':
                            print('The apple effect has been overridden. They now go -3.')
                            p1_status = 'Pear'
                        elif p1_status == 'G-Apple':
                            print('The Golden Apple effect has been cancelled. They will roll normally.')
                            p1_status = ''
                        else:
                            print("They'll move 6 less spaces with this next roll!")
                            p1_status = 'G-Pear'
                    elif pear_effect == 2:
                        print('Player 1 used the Golden Minus Pear on Player 2!')
                        if p2_status == 'Apple':
                            print('The apple effect has been overridden. They now go -3.')
                            p2_status = 'Pear'
                        elif p2_status == 'G-Apple':
                            print('The Golden Apple effect has been cancelled. They will roll normally.')
                            p2_status = ''
                        else:
                            print("They'll move 6 less spaces with this next roll!")
                            p2_status = 'G-Pear'
                    elif pear_effect == 3:
                        print('Player 1 used the Minus Pear on Player 3!')
                        if p3_status == 'Apple':
                            print('The apple effect has been overridden. They now go -3.')
                            p3_status = 'Pear'
                        elif p3_status == 'G-Apple':
                            print('The Golden Apple effect has been cancelled. They will roll normally.')
                            p3_status = ''
                        else:
                            print("They'll move 6 less spaces with this next roll!")
                            p3_status = 'G-Pear'
                    elif pear_effect == 4:
                        print('Player 1 used the Minus Pear on Player 4!')
                        if p4_status == 'Apple':
                            print('The apple effect has been overridden. They now go -3.')
                            p4_status = 'Pear'
                        elif p4_status == 'G-Apple':
                            print('The Golden Apple effect has been cancelled. They will roll normally.')
                            p4_status = ''
                        else:
                            print("They'll move 6 less spaces with this next roll!")
                            p4_status = 'G-Pear'
                    else:
                        print('You ended up tossing the pear...')
                    time.sleep(2)
                    if p1_items.index('Golden Minus Pear') == 1:
                        p1_items[1] = ''
                    elif p1_items.index('Golden Minus Pear') == 2:
                        p1_items[2] = ''
                    elif p1_items.index('Golden Minus Pear') == 3:
                        p1_items[3] = ''
                    item_use = 0
                    P1DiceRoll()
                else:
                    print("You don't have a Golden Minus Pear!")
                    time.sleep(2)
                    P1DiceRoll()
            elif item_select.lower() == 'extra die':
                if p1_items[1] == 'Extra Die' or p1_items[2] == 'Extra Die' or p1_items[3] == 'Extra Die':
                    print('Player 1 used the Extra Die!')
                    time.sleep(2)
                    print("They'll gain an extra roll on this next turn!")
                    time.sleep(2)
                    p1_status = 'EX'
                    if p1_items.index('Extra Die') == 1:
                        p1_items[1] = ''
                    elif p1_items.index('Extra Die') == 2:
                        p1_items[2] = ''
                    elif p1_items.index('Extra Die') == 3:
                        p1_items[3] = ''
                    item_use = 0
                    P1DiceRoll()
                else:
                    print("You don't have an Extra Die!")
                    time.sleep(2)
                    P1DiceRoll()
            elif item_select.lower() == 'selection die':
                if p1_items[1] == 'Selection Die' or p1_items[2] == 'Selection Die' or p1_items[3] == 'Selection Die':
                    print('Player 1 used the Selection Die!')
                    time.sleep(2)
                    print("How many spaces do you want to move? (1-6)")
                    dice_roll = int(input())
                    print('The die rolled', dice_roll)
                    time.sleep(1)
                    if p1_status == 'Apple':
                        dice_roll += 3
                    elif p1_status == 'G-Apple':
                        dice_roll += 6
                    elif p1_status == 'Pear':
                        dice_roll -= 3
                    elif p1_status == 'G-Pear':
                        dice_roll -= 6
                    elif p1_status == 'EX':
                        ex_dice_roll = random.choice(range(1, 7))
                        print('Extra die rolls', ex_dice_roll)
                        dice_roll += ex_dice_roll
                        time.sleep(1)
                    elif p1_status == 'Double':
                        dice_roll *= 2
                    elif p1_status == 'Half':
                        dice_roll //= 2
                        p1_status = ''
                    print('Player 1 moves', dice_roll, 'spaces!')
                    player1pos += dice_roll
                    time.sleep(1)
                    print('Player 1 is now at space #',player1pos)
                    time.sleep(2)
                    if p1_items.index('Selection Die') == 1:
                        p1_items[1] = ''
                    elif p1_items.index('Selection Die') == 2:
                        p1_items[2] = ''
                    elif p1_items.index('Selection Die') == 3:
                        p1_items[3] = ''
                else:
                    print("You don't have a Selection Die!")
                    time.sleep(2)
                    item_use = 0
                    P1DiceRoll()
            elif item_select.lower() == 'swap box':
                if p1_items[1] == 'Swap Box' or p1_items[2] == 'Swap Box' or p1_items[3] == 'Swap Box':
                    print('Player 1 used the Swap Box!')
                    time.sleep(2)
                    swap = random.choice([2, 3, 4])
                    if swap == 2:
                        player1pos = player2pos
                        player2pos = savep1pos
                        print('Players 1 and 2 swapped places!')
                        time.sleep(1)
                        print('Player 1 is now at space #',player1pos)
                        time.sleep(1.5)
                        print('Player 2 is now at space #',player2pos)
                    if swap == 3:
                        player1pos = player3pos
                        player3pos = savep1pos
                        print('Players 1 and 3 swapped places!')
                        time.sleep(1)
                        print('Player 1 is now at space #',player1pos)
                        time.sleep(1.5)
                        print('Player 3 is now at space #',player3pos)
                    if swap == 4:
                        player1pos = player4pos
                        player4pos = savep1pos
                        print('Players 1 and 4 swapped places!')
                        time.sleep(1)
                        print('Player 1 is now at space #',player1pos)
                        time.sleep(1.5)
                        print('Player 4 is now at space #',player4pos)
                    if p1_items.index('Swap Box') == 1:
                        p1_items[1] = ''
                    elif p1_items.index('Swap Box') == 2:
                        p1_items[2] = ''
                    elif p1_items.index('Swap Box') == 3:
                        p1_items[3] = ''
                    item_use = 0
                    P1DiceRoll()
                else:
                    print("You don't have a Swap Box!")
                    time.sleep(2)
                    P1DiceRoll()
            elif item_select.lower() == 'great snake':
                if p1_items[1] == 'Great Snake' or p1_items[2] == 'Great Snake' or p1_items[3] == 'Great Snake':
                    print('Player 1 used the Great Snake!')
                    time.sleep(2)
                    g_snake = random.choice([1, 2, 3, 4])
                    if g_snake == 1:
                        print('Snake backfired!')
                        time.sleep(2)
                        print('Player 1 goes down 20 spaces!')
                        player1pos -= 20
                        if player1pos < 0:
                            while player1pos != 0:
                                player1pos += 1
                    if g_snake == 2:
                        print('Player 2 goes down 20 spaces!')
                        player2pos -= 20
                        if player2pos < 0:
                            while player2pos != 0:
                                player2pos += 1
                    if g_snake == 3:
                        print('Player 3 goes down 20 spaces!')
                        player3pos -= 20
                        if player3pos < 0:
                            while player3pos != 0:
                                player3pos += 1
                    if g_snake == 4:
                        print('Player 4 goes down 20 spaces!')
                        player4pos -= 20
                        if player4pos < 0:
                            while player4pos != 0:
                                player4pos += 1
                    if p1_items.index('Great Snake') == 1:
                        p1_items[1] = ''
                    elif p1_items.index('Great Snake') == 2:
                        p1_items[2] = ''
                    elif p1_items.index('Great Snake') == 3:
                        p1_items[3] = ''
                    item_use = 0
                    P1DiceRoll()
                else:
                    print("You don't have a Great Snake!")
                    time.sleep(2)
                    P1DiceRoll()
            elif item_select.lower() == 'god snake':
                if p1_items[1] == 'God Snake' or p1_items[2] == 'God Snake' or p1_items[3] == 'God Snake':
                    print('Player 1 used the God Snake!')
                    time.sleep(2)
                    g_snake = random.choice([1, 2, 3, 4])
                    if g_snake == 1:
                        print('Snake backfired!')
                        time.sleep(2)
                        print('Player 1 goes down to the beginning!')
                        player1pos = 0
                    if g_snake == 2:
                        print('Player 2 goes down to the beginning!')
                        player2pos = 0
                    if g_snake == 3:
                        print('Player 3 goes down to the beginning!')
                        player3pos = 0
                    if g_snake == 4:
                        print('Player 4 goes down to the beginning!')
                        player4pos = 0
                    if p1_items.index('God Snake') == 1:
                        p1_items[1] = ''
                    elif p1_items.index('God Snake') == 2:
                        p1_items[2] = ''
                    elif p1_items.index('God Snake') == 3:
                        p1_items[3] = ''
                    item_use = 0
                    P1DiceRoll()
                else:
                    print("You don't have a God Snake!")
                    time.sleep(2)
                    P1DiceRoll()
            elif item_select.lower() == 'double-or-nothing die':
                if p1_items[1] == 'Double-or-Nothing Die' or p1_items[2] == 'Double-or-Nothing Die' or p1_items[3] == 'Double-or-Nothing Die':
                    print('Player 1 used the Double-or-Nothing Die!')
                    time.sleep(2)
                    print("Take your chance! It's Double or Nothing!")
                    input('(Press Enter)')
                    dice_roll = random.choice(range(1, 7))
                    myst_die = random.choice(range(1, 7))
                    print('You rolled:', dice_roll)
                    time.sleep(1)
                    print('The die rolled:', myst_die)
                    time.sleep(2)
                    if dice_roll > myst_die:
                        print('Congratulations! Your next roll will be doubled!')
                        p1_status = 'Double'
                    else:
                        print('Oh... it all fell to nothing. Your next roll will be halved.')
                        p1_status = 'Half'
                    time.sleep(2)
                    if p1_items.index('Double-or-Nothing Die') == 1:
                        p1_items[1] = ''
                    elif p1_items.index('Double-or-Nothing Die') == 2:
                        p1_items[2] = ''
                    elif p1_items.index('Double-or-Nothing Die') == 3:
                        p1_items[3] = ''
                    item_use = 0
                    P1DiceRoll()
                else:
                    print("You don't have a Double-or-Nothing Die!")
                    time.sleep(2)
                    P1DiceRoll()
            elif item_select.lower() == 'magic ladder':
                if p1_items[1] == 'Magic Ladder' or p1_items[2] == 'Magic Ladder' or p1_items[3] == 'Magic Ladder':
                    print('Player 1 used the Magic Ladder!')
                    time.sleep(2)
                    mag_ladder = random.choice(range(5, 16))
                    print('The ladder took Player 1 up', mag_ladder, 'spaces!')
                    player1pos += mag_ladder
                    time.sleep(2)
                    if p1_items.index('Magic Ladder') == 1:
                        p1_items[1] = ''
                    elif p1_items.index('Magic Ladder') == 2:
                        p1_items[2] = ''
                    elif p1_items.index('Magic Ladder') == 3:
                        p1_items[3] = ''
                    item_use = 0
                    if player1pos in snakes:
                        print('Uh-oh! You landed on a snake!')
                        time.sleep(2)
                        signal = 1
                        snake()
                    elif player1pos in ladders:
                        print('Woo-hoo! You landed on a ladder!')
                        time.sleep(2)
                        signal = 1
                        ladder()
                    elif player1pos > goal:
                        print('Ooh... you overshot that one!')
                        player1pos -= dice_roll
                        time.sleep(2)
                    else:
                        P1DiceRoll()
                else:
                    print("You don't have a Magic Ladder!")
                    time.sleep(2)
                    P1DiceRoll()
            elif item_select.lower() == 'ultimate fate':
                if p1_items[1] == 'Ultimate Fate' or p1_items[2] == 'Ultimate Fate' or p1_items[3] == 'Ultimate Fate':
                    print('Player 1 used the Ultimate Fate!')
                    time.sleep(2)
                    print("One dice roll decides everyone's fate!")
                    input('(Press enter to decide fate)')
                    dice_roll = random.choice(range(1, 7))
                    print('The dice rolls', dice_roll, end = '')
                    print(". Your fate reads...")
                    time.sleep(2)
                    if dice_roll == 1:
                        print('Everyone must return to the beginning!')
                        time.sleep(2)
                        player1pos = 0
                        player2pos = 0
                        player3pos = 0
                        player4pos = 0
                    elif dice_roll == 2:
                        print('Everyone gets the effects of the Golden Minus Pear!')
                        time.sleep(2)
                        p1_status = 'G-Pear'
                        p2_status = 'G-Pear'
                        p3_status = 'G-Pear'
                        p4_status = 'G-Pear'
                    elif dice_roll == 3:
                        print('Everyone gets infected with the Plus Apple!')
                        time.sleep(2)
                        p1_status = 'Apple'
                        p2_status = 'Apple'
                        p3_status = 'Apple'
                        p4_status = 'Apple'
                    elif dice_roll == 4:
                        print('Everyone gets their locations rearranged!')
                        time.sleep(2)
                        player1pos = random.choice([savep2pos, savep3pos, savep4pos])
                        player2pos = random.choice([savep1pos, savep3pos, savep4pos])
                        player3pos = random.choice([savep2pos, savep1pos, savep4pos])
                        player4pos = random.choice([savep2pos, savep3pos, savep1pos])
                        print('Player 1 is now at space #',player1pos)
                        time.sleep(1)
                        print('Player 2 is now at space #',player2pos)
                        time.sleep(1)
                        print('Player 3 is now at space #',player3pos)
                        time.sleep(1)
                        print('Player 4 is now at space #',player4pos)
                        time.sleep(2)
                    elif dice_roll == 5:
                        print('Everyone gets the effects of the Minus Pear!')
                        time.sleep(2)
                        p1_status = 'Pear'
                        p2_status = 'Pear'
                        p3_status = 'Pear'
                        p4_status = 'Pear'
                    elif dice_roll == 6:
                        print('Everyone gets the effects of the Golden Plus Apple!')
                        time.sleep(2)
                        p1_status = 'G-Apple'
                        p2_status = 'G-Apple'
                        p3_status = 'G-Apple'
                        p4_status = 'G-Apple'
                    time.sleep(2)
                    if p1_items.index('Ultimate Fate') == 1:
                        p1_items[1] = ''
                    elif p1_items.index('Ultimate Fate') == 2:
                        p1_items[2] = ''
                    elif p1_items.index('Ultimate Fate') == 3:
                        p1_items[3] = ''
                    item_use = 0
                    P1DiceRoll()
                else:
                    print("You don't have an Ultimate Fate!")
                    time.sleep(2)
                    P1DiceRoll()
            else:
                P1DiceRoll()
    else:
        print("We didn't get that... Try Again!")
        time.sleep(2)
        P1DiceRoll()
    if player1pos in snakes:
        print('Uh-oh! You landed on a snake!')
        time.sleep(2)
        signal = 1
        snake()
    elif player1pos in ladders:
        print('Woo-hoo! You landed on a ladder!')
        time.sleep(2)
        signal = 1
        ladder()
    if player1pos > goal:
        print('Ooh... you overshot that one!')
        player1pos -= dice_roll
        time.sleep(2)
    savep1pos = player1pos
    endCheck()
    item_use = 1
    if item_fix == 1:
        item_roll = random.choice(range(1, 101))
        if item_roll <= item_chance:
            print('Whoa! You get to play an item game!')
            time.sleep(2)
            left_or_right = input('Left or Right?: ')
            if left_or_right.lower() == 'left':
                item_get = random.choice(['Plus Apple', 'Minus Pear', 'Golden Plus Apple', 'Golden Minus Pear', 'Selection Die', 'Extra Die'])
                print('You recieved:', item_get)
                if p1_items[1] == '':
                    p1_items[1] = item_get
                elif p1_items[2] == '':
                    p1_items[2] = item_get
                elif p1_items[3] == '':
                    p1_items[3] = item_get
                else:
                    print('Uh oh! No more room!')
                    time.sleep(1)
                    print('Which item slot do you want to replace?')
                    print(p1_items)
                    print('1, 2, or 3 (input anything else to toss item)')
                    item_replace = int(input())
                    if item_replace == 1:
                        print('Goodbye,', p1_items[1])
                        time.sleep(1)
                        p1_items[1] = item_get
                        print('Hello,', p1_items[1])
                    elif item_replace == 2:
                        print('Goodbye,', p1_items[2])
                        time.sleep(1)
                        p1_items[2] = item_get
                        print('Hello,', p1_items[2])
                    elif item_replace == 3:
                        print('Goodbye,', p1_items[3])
                        time.sleep(1)
                        p1_items[3] = item_get
                        print('Hello,', p1_items[3])
                    else:
                        print('You threw the', item_get, 'away!')
            elif left_or_right.lower() == 'right':
                item_get = random.choice(['Swap Box', 'Great Snake', 'God Snake', 'Double-or-Nothing Die', 'Magic Ladder', 'Ultimate Fate'])
                print('You recieved:', item_get)
                if p1_items[1] == '':
                    p1_items[1] = item_get
                elif p1_items[2] == '':
                    p1_items[2] = item_get
                elif p1_items[3] == '':
                    p1_items[3] = item_get
                else:
                    print('Uh oh! No more room!')
                    time.sleep(1)
                    print('Which item slot do you want to replace?')
                    print(p1_items) 
                    print('1, 2, or 3 (input anything else to toss item)')
                    item_replace = int(input())
                    if item_replace == 1:
                        print('Goodbye,', p1_items[1])
                        time.sleep(1)
                        p1_items[1] = item_get
                        print('Hello,', p1_items[1])
                    elif item_replace == 2:
                        print('Goodbye,', p1_items[2])
                        time.sleep(1)
                        p1_items[2] = item_get
                        print('Hello,', p1_items[2])
                    elif item_replace == 3:
                        print('Goodbye,', p1_items[3])
                        time.sleep(1)
                        p1_items[3] = item_get
                        print('Hello,', p1_items[3])
                    else:
                        print('You threw the', item_get, 'away!')
            else:
                item_get = random.choice(['Plus Apple', 'Minus Pear', 'Golden Plus Apple', 'Golden Minus Pear', 'Selection Die', 'Extra Die', 'Swap Box', 'Great Snake', 'God Snake', 'Double-or-Nothing Die', 'Magic Ladder', 'Ultimate Fate'])
                print('You recieved:', item_get)
                if p1_items[1] == '':
                    p1_items[1] = item_get
                elif p1_items[2] == '':
                    p1_items[2] = item_get
                elif p1_items[3] == '':
                    p1_items[3] = item_get
                else:
                    print('Uh oh! No more room!')
                    time.sleep(1)
                    print('Which item slot do you want to replace?')
                    print(p1_items) 
                    print('1, 2, or 3 (input anything else to toss item)')
                    item_replace = int(input())
                    if item_replace == 1:
                        print('Goodbye,', p1_items[1])
                        time.sleep(1)
                        p1_items[1] = item_get
                        print('Hello,', p1_items[1])
                    elif item_replace == 2:
                        print('Goodbye,', p1_items[2])
                        time.sleep(1)
                        p1_items[2] = item_get
                        print('Hello,', p1_items[2])
                    elif item_replace == 3:
                        print('Goodbye,', p1_items[3])
                        time.sleep(1)
                        p1_items[3] = item_get
                        print('Hello,', p1_items[3])
                    else:
                        print('You threw the', item_get, 'away!')
            item_fix = 0
            if player1pos < 0:
                while player1pos != 0:
                    player1pos += 1
            time.sleep(2)
    print('')

def P2DiceRoll():
    global double_meter2
    global players
    global player1pos
    global player2pos
    global player3pos
    global player4pos
    global double_meter_cap
    global dice
    global item_chance
    global item_roll
    global p2_items
    global p1_status
    global p2_status
    global p3_status
    global p4_status
    global item_get
    global item_fix
    global item_use
    global savep1pos
    global savep2pos
    global savep3pos
    global savep4pos
    global signal
    item_fix = 1
    print('Player 2! GO!')
    time.sleep(1)
    print('Double Meter:', double_meter2)
    print('Current position:', player2pos)
    print('Status Effect:', p2_status)
    if double_meter2 == double_meter_cap:
        print('Double Roll Ready!')
    if dice != 'Single' or dice != 'Double' or dice != 'Item':
        if players >= 2:
            dice = input('Single/Double/Item: ')
        else:
            if double_meter2 == double_meter_cap:
                if p2_items[1] != '' or p2_items[2] != '' or p2_items[3] != '':
                    if item_use == 1:
                        dice = random.choice(['Single', 'Double', 'Item'])
                    else:
                        dice = random.choice(['Single', 'Double'])
                else:
                    dice = random.choice(['Single', 'Double'])
            elif p2_items[1] != '' or p2_items[2] != '' or p2_items[3] != '':
                if item_use == 1:
                    dice = random.choice(['Single', 'Item'])
                else:
                    dice = 'Single'
            else:
                dice = 'Single'
    if dice.lower() == 'single':
        dice_roll = random.choice(range(1, 7))
        print('The die rolled', dice_roll)
        time.sleep(1)
        if p2_status == 'Apple':
            dice_roll += 3
            p2_status = ''
        elif p2_status == 'G-Apple':
            dice_roll += 6
            p2_status = ''
        elif p2_status == 'Pear':
            dice_roll -= 3
            p2_status = ''
        elif p2_status == 'G-Pear':
            dice_roll -= 6
            p2_status = ''
        elif p2_status == 'EX':
            ex_dice_roll = random.choice(range(1, 7))
            print('Extra die rolls', ex_dice_roll)
            dice_roll += ex_dice_roll
            p2_status = ''
            time.sleep(1)
        elif p2_status == 'Double':
            dice_roll *= 2
            p2_status = ''
        elif p2_status == 'Half':
            dice_roll //= 2
            p2_status = ''
        print('Player 2 moves', dice_roll, 'spaces!')
        player2pos += dice_roll
        time.sleep(1)
        print('Player 2 is now at space #',player2pos)
        time.sleep(2)
        for i in range(dice_roll):
            double_meter2 += 5
        if double_meter2 > double_meter_cap:
            while double_meter2 != double_meter_cap:
                double_meter2 -= 1
    elif dice.lower() == 'double':
        if double_meter2 == 100:    
            print('DOUBLE ROLL!')
            time.sleep(1)
            dice_roll = random.choice(range(2, 13))
            print('The dice rolled', dice_roll)
            time.sleep(1)
            if p2_status == 'Apple':
                dice_roll += 3
                p2_status = ''
            elif p2_status == 'G-Apple':
                dice_roll += 6
                p2_status = ''
            elif p2_status == 'Pear':
                dice_roll -= 3
                p2_status = ''
            elif p2_status == 'G-Pear':
                dice_roll -= 6
                p2_status = ''
            elif p2_status == 'EX':
                ex_dice_roll = random.choice(range(1, 7))
                print('Extra die rolls', ex_dice_roll)
                dice_roll += ex_dice_roll
                p2_status = ''
                time.sleep(1)
            elif p2_status == 'Double':
                dice_roll *= 2
                p2_status = ''
            elif p1_status == 'Half':
                dice_roll //= 2
                p1_status = ''
            print('Player 2 moves', dice_roll, 'spaces!')
            player2pos += dice_roll
            time.sleep(1)
            print('Player 2 is now at space #',player2pos)
            time.sleep(2)
            double_meter2 = 0
        else:
            print("Can't use double roll.")
            time.sleep(2)
            P2DiceRoll()
    elif dice.lower() == 'item':
        if item_use == 1:
            print('Select your item:', p2_items)
            if players >= 2:
                item_select = input()
            else:
                item_select = random.choice(p2_items)
            if item_select.lower() == 'back':
                P2DiceRoll()
            elif item_select.lower() == 'plus apple':
                if p2_items[1] == 'Plus Apple' or p2_items[2] == 'Plus Apple' or p2_items[3] == 'Plus Apple':
                    print('Player 2 used the Plus Apple!')
                    time.sleep(2)
                    if p2_status == 'Pear':
                        print('The pear effect has been cancelled. They will roll normally.')
                        p2_status = ''
                    elif p2_status == 'G-Pear':
                        print('The Golden Pear effect has been halved. They will now go -3.')
                        p2_status = 'Pear'
                    else:
                        print("They'll move 3 extra spaces with this next roll!")
                        p2_status = 'Apple'
                    time.sleep(2)
                    if p2_items.index('Plus Apple') == 1:
                        p2_items[1] = ''
                    elif p2_items.index('Plus Apple') == 2:
                        p2_items[2] = ''
                    elif p2_items.index('Plus Apple') == 3:
                        p2_items[3] = ''
                    item_use = 0
                    P2DiceRoll()
                else:
                    print("You don't have a Plus Apple!")
                    time.sleep(2)
                    P2DiceRoll()
            elif item_select.lower() == 'golden plus apple':
                if p2_items[1] == 'Golden Plus Apple' or p2_items[2] == 'Golden Plus Apple' or p2_items[3] == 'Golden Plus Apple':
                    print('Player 2 used the Golden Plus Apple!')
                    time.sleep(2)
                    if p2_status == 'Pear':
                        print('The pear effect has been overridden. They will now move +3.')
                        p2_status = 'Apple'
                    elif p2_status == 'G-Pear':
                        print('The Golden Pear cancelled. They will roll normally.')
                        p2_status = ''
                    else:
                        print("They'll move 6 extra spaces with this next roll!")
                        p2_status = 'G-Apple'
                    time.sleep(2)
                    if p2_items.index('Golden Plus Apple') == 1:
                        p2_items[1] = ''
                    elif p2_items.index('Golden Plus Apple') == 2:
                        p2_items[2] = ''
                    elif p2_items.index('Golden Plus Apple') == 3:
                        p2_items[3] = ''
                    item_use = 0
                    P2DiceRoll()
                else:
                    print("You don't have a Golden Plus Apple!")
                    time.sleep(2)
                    P2DiceRoll()
            elif item_select.lower() == 'minus pear':
                if p2_items[1] == 'Minus Pear' or p2_items[2] == 'Minus Pear' or p2_items[3] == 'Minus Pear':
                    print('Player 2 used the Minus Pear!')
                    time.sleep(2)
                    if players >= 2:
                        print('Who would you like to use it on?')
                        print('1 / 2 / 3 / 4')
                        pear_effect = int(input())
                    else:
                        pear_effect = random.choice(range(1, 5))
                    if pear_effect == 1:
                        print('Player 2 used the Minus Pear on Player 1!')
                        if p1_status == 'Apple':
                            print('The apple effect has been cancelled. They will roll normally.')
                            p1_status = ''
                        elif p1_status == 'G-Apple':
                            print('The Golden Apple effect has been halved. They will now go +3.')
                            p1_status = 'Apple'
                        else:
                            print("They'll move 3 less spaces with this next roll!")
                            p1_status = 'Pear'
                    elif pear_effect == 2:
                        print('Player 2 used the Minus Pear on themselves!')
                        if p2_status == 'Apple':
                            print('The apple effect has been cancelled. They will roll normally.')
                            p2_status = ''
                        elif p2_status == 'G-Apple':
                            print('The Golden Apple effect has been halved. They will now go +3.')
                            p2_status = 'Apple'
                        else:
                            print("They'll move 3 less spaces with this next roll!")
                            p2_status = 'Pear'
                    elif pear_effect == 3:
                        print('Player 2 used the Minus Pear on Player 3!')
                        if p3_status == 'Apple':
                            print('The apple effect has been cancelled. They will roll normally.')
                            p3_status = ''
                        elif p3_status == 'G-Apple':
                            print('The Golden Apple effect has been halved. They will now go +3.')
                            p3_status = 'Apple'
                        else:
                            print("They'll move 3 less spaces with this next roll!")
                            p3_status = 'Pear'
                    elif pear_effect == 4:
                        print('Player 2 used the Minus Pear on Player 4!')
                        if p4_status == 'Apple':
                            print('The apple effect has been cancelled. They will roll normally.')
                            p4_status = ''
                        elif p4_status == 'G-Apple':
                            print('The Golden Apple effect has been halved. They will now go +3.')
                            p4_status = 'Apple'
                        else:
                            print("They'll move 3 less spaces with this next roll!")
                            p4_status = 'Pear'
                    else:
                        print('You ended up tossing the pear...')
                    time.sleep(2)
                    if p2_items.index('Minus Pear') == 1:
                        p2_items[1] = ''
                    elif p2_items.index('Minus Pear') == 2:
                        p2_items[2] = ''
                    elif p2_items.index('Minus Pear') == 3:
                        p2_items[3] = ''
                    item_use = 0
                    P2DiceRoll()
                else:
                    print("You don't have a Minus Pear!")
                    time.sleep(2)
                    P2DiceRoll()
            elif item_select.lower() == 'golden minus pear':
                if p2_items[1] == 'Golden Minus Pear' or p2_items[2] == 'Golden Minus Pear' or p2_items[3] == 'Golden Minus Pear':
                    print('Player 2 used the Golden Minus Pear!')
                    time.sleep(2)
                    if players >= 2:
                        print('Who would you like to use it on?')
                        print('1 / 2 / 3 / 4')
                        pear_effect = int(input())
                    else:
                        pear_effect = random.choice(range(1, 5))
                    if pear_effect == 1:
                        print('Player 2 used the Golden Minus Pear on Player 1!')
                        if p1_status == 'Apple':
                            print('The apple effect has been overridden. They now go -3.')
                            p1_status = 'Pear'
                        elif p1_status == 'G-Apple':
                            print('The Golden Apple effect has been cancelled. They will roll normally.')
                            p1_status = ''
                        else:
                            print("They'll move 6 less spaces with this next roll!")
                            p1_status = 'G-Pear'
                    elif pear_effect == 2:
                        print('Player 2 used the Golden Minus Pear on themselves!')
                        if p2_status == 'Apple':
                            print('The apple effect has been overridden. They now go -3.')
                            p2_status = 'Pear'
                        elif p2_status == 'G-Apple':
                            print('The Golden Apple effect has been cancelled. They will roll normally.')
                            p2_status = ''
                        else:
                            print("They'll move 6 less spaces with this next roll!")
                            p2_status = 'G-Pear'
                    elif pear_effect == 3:
                        print('Player 2 used the Minus Pear on Player 3!')
                        if p3_status == 'Apple':
                            print('The apple effect has been overridden. They now go -3.')
                            p3_status = 'Pear'
                        elif p3_status == 'G-Apple':
                            print('The Golden Apple effect has been cancelled. They will roll normally.')
                            p3_status = ''
                        else:
                            print("They'll move 6 less spaces with this next roll!")
                            p3_status = 'G-Pear'
                    elif pear_effect == 4:
                        print('Player 2 used the Minus Pear on Player 4!')
                        if p4_status == 'Apple':
                            print('The apple effect has been overridden. They now go -3.')
                            p4_status = 'Pear'
                        elif p4_status == 'G-Apple':
                            print('The Golden Apple effect has been cancelled. They will roll normally.')
                            p4_status = ''
                        else:
                            print("They'll move 6 less spaces with this next roll!")
                            p4_status = 'G-Pear'
                    else:
                        print('You ended up tossing the pear...')
                    time.sleep(2)
                    if p2_items.index('Golden Minus Pear') == 1:
                        p2_items[1] = ''
                    elif p2_items.index('Golden Minus Pear') == 2:
                        p2_items[2] = ''
                    elif p2_items.index('Golden Minus Pear') == 3:
                        p2_items[3] = ''
                    item_use = 0
                    P2DiceRoll()
                else:
                    print("You don't have a Golden Minus Pear!")
                    time.sleep(2)
                    P2DiceRoll()
            elif item_select.lower() == 'extra die':
                if p2_items[1] == 'Extra Die' or p2_items[2] == 'Extra Die' or p2_items[3] == 'Extra Die':
                    print('Player 2 used the Extra Die!')
                    time.sleep(2)
                    print("They'll gain an extra roll on this next turn!")
                    time.sleep(2)
                    p2_status = 'EX'
                    if p2_items.index('Extra Die') == 1:
                        p2_items[1] = ''
                    elif p2_items.index('Extra Die') == 2:
                        p2_items[2] = ''
                    elif p2_items.index('Extra Die') == 3:
                        p2_items[3] = ''
                    item_use = 0
                    P2DiceRoll()
                else:
                    print("You don't have an Extra Die!")
                    time.sleep(2)
                    P2DiceRoll()
            elif item_select.lower() == 'selection die':
                if p2_items[1] == 'Selection Die' or p2_items[2] == 'Selection Die' or p2_items[3] == 'Selection Die':
                    print('Player 2 used the Selection Die!')
                    time.sleep(2)
                    if players >= 2:
                        print("How many spaces do you want to move? (1-6)")
                        dice_roll = int(input())
                    else:
                        dice_roll = random.choice(range(1, 7))
                    print('The die rolled', dice_roll)
                    time.sleep(1)
                    if p2_status == 'Apple':
                        dice_roll += 3
                    elif p2_status == 'G-Apple':
                        dice_roll += 6
                    elif p2_status == 'Pear':
                        dice_roll -= 3
                    elif p2_status == 'G-Pear':
                        dice_roll -= 6
                    elif p2_status == 'EX':
                        ex_dice_roll = random.choice(range(1, 7))
                        print('Extra die rolls', ex_dice_roll)
                        dice_roll += ex_dice_roll
                        time.sleep(1)
                    elif p2_status == 'Double':
                        dice_roll *= 2
                    elif p2_status == 'Half':
                        dice_roll //= 2
                        p2_status = ''
                    print('Player 2 moves', dice_roll, 'spaces!')
                    player2pos += dice_roll
                    time.sleep(1)
                    print('Player 2 is now at space #',player2pos)
                    time.sleep(2)
                    if p2_items.index('Selection Die') == 1:
                        p2_items[1] = ''
                    elif p2_items.index('Selection Die') == 2:
                        p2_items[2] = ''
                    elif p2_items.index('Selection Die') == 3:
                        p2_items[3] = ''
                else:
                    print("You don't have a Selection Die!")
                    time.sleep(2)
                    item_use = 0
                    P2DiceRoll()
            elif item_select.lower() == 'swap box':
                if p2_items[1] == 'Swap Box' or p2_items[2] == 'Swap Box' or p2_items[3] == 'Swap Box':
                    print('Player 2 used the Swap Box!')
                    time.sleep(2)
                    swap = random.choice([1, 3, 4])
                    if swap == 1:
                        player1pos = player2pos
                        player2pos = savep1pos
                        print('Players 1 and 2 swapped places!')
                        time.sleep(1)
                        print('Player 1 is now at space #',player1pos)
                        time.sleep(1.5)
                        print('Player 2 is now at space #',player2pos)
                    if swap == 3:
                        player2pos = player3pos
                        player3pos = savep2pos
                        print('Players 2 and 3 swapped places!')
                        time.sleep(1)
                        print('Player 2 is now at space #',player2pos)
                        time.sleep(1.5)
                        print('Player 3 is now at space #',player3pos)
                    if swap == 4:
                        player2pos = player4pos
                        player4pos = savep2pos
                        print('Players 2 and 4 swapped places!')
                        time.sleep(1)
                        print('Player 2 is now at space #',player2pos)
                        time.sleep(1.5)
                        print('Player 4 is now at space #',player4pos)
                    if p2_items.index('Swap Box') == 1:
                        p2_items[1] = ''
                    elif p2_items.index('Swap Box') == 2:
                        p2_items[2] = ''
                    elif p2_items.index('Swap Box') == 3:
                        p2_items[3] = ''
                    item_use = 0
                    P2DiceRoll()
                else:
                    print("You don't have a Swap Box!")
                    time.sleep(2)
                    P2DiceRoll()
            elif item_select.lower() == 'great snake':
                if p2_items[1] == 'Great Snake' or p2_items[2] == 'Great Snake' or p2_items[3] == 'Great Snake':
                    print('Player 2 used the Great Snake!')
                    time.sleep(2)
                    g_snake = random.choice([1, 2, 3, 4])
                    if g_snake == 1:
                        print('Player 1 goes down 20 spaces!')
                        player1pos -= 20
                        if player1pos < 0:
                            while player1pos != 0:
                                player1pos += 1
                    if g_snake == 2:
                        print('Snake backfired!')
                        time.sleep(2)
                        print('Player 2 goes down 20 spaces!')
                        player2pos -= 20
                        if player2pos < 0:
                            while player2pos != 0:
                                player2pos += 1
                    if g_snake == 3:
                        print('Player 3 goes down 20 spaces!')
                        player3pos -= 20
                        if player3pos < 0:
                            while player3pos != 0:
                                player3pos += 1
                    if g_snake == 4:
                        print('Player 4 goes down 20 spaces!')
                        player4pos -= 20
                        if player4pos < 0:
                            while player4pos != 0:
                                player4pos += 1
                    if p2_items.index('Great Snake') == 1:
                        p2_items[1] = ''
                    elif p2_items.index('Great Snake') == 2:
                        p2_items[2] = ''
                    elif p2_items.index('Great Snake') == 3:
                        p2_items[3] = ''
                    item_use = 0
                    P2DiceRoll()
                else:
                    print("You don't have a Great Snake!")
                    time.sleep(2)
                    P2DiceRoll()
            elif item_select.lower() == 'god snake':
                if p2_items[1] == 'God Snake' or p2_items[2] == 'God Snake' or p2_items[3] == 'God Snake':
                    print('Player 2 used the God Snake!')
                    time.sleep(2)
                    g_snake = random.choice([1, 2, 3, 4])
                    if g_snake == 1:
                        print('Player 1 goes down to the beginning!')
                        player1pos = 0
                    if g_snake == 2:
                        print('Snake backfired!')
                        time.sleep(2)
                        print('Player 2 goes down to the beginning!')
                        player2pos = 0
                    if g_snake == 3:
                        print('Player 3 goes down to the beginning!')
                        player3pos = 0
                    if g_snake == 4:
                        print('Player 4 goes down to the beginning!')
                        player4pos = 0
                    if p2_items.index('God Snake') == 1:
                        p2_items[1] = ''
                    elif p2_items.index('God Snake') == 2:
                        p2_items[2] = ''
                    elif p2_items.index('God Snake') == 3:
                        p2_items[3] = ''
                    item_use = 0
                    P2DiceRoll()
                else:
                    print("You don't have a God Snake!")
                    time.sleep(2)
                    P2DiceRoll()
            elif item_select.lower() == 'double-or-nothing die':
                if p2_items[1] == 'Double-or-Nothing Die' or p2_items[2] == 'Double-or-Nothing Die' or p2_items[3] == 'Double-or-Nothing Die':
                    print('Player 1 used the Double-or-Nothing Die!')
                    time.sleep(2)
                    print("Take your chance! It's Double or Nothing!")
                    if players >= 2:
                        input('(Press Enter)')
                    dice_roll = random.choice(range(1, 7))
                    myst_die = random.choice(range(1, 7))
                    print('You rolled:', dice_roll)
                    time.sleep(1)
                    print('The die rolled:', myst_die)
                    time.sleep(2)
                    if dice_roll > myst_die:
                        print('Congratulations! Your next roll will be doubled!')
                        p2_status = 'Double'
                    else:
                        print('Oh... it all fell to nothing. Your next roll will be halved.')
                        p2_status = 'Half'
                    time.sleep(2)
                    if p2_items.index('Double-or-Nothing Die') == 1:
                        p2_items[1] = ''
                    elif p2_items.index('Double-or-Nothing Die') == 2:
                        p2_items[2] = ''
                    elif p2_items.index('Double-or-Nothing Die') == 3:
                        p2_items[3] = ''
                    item_use = 0
                    P2DiceRoll()
                else:
                    print("You don't have a Double-or-Nothing Die!")
                    time.sleep(2)
                    P2DiceRoll()
            elif item_select.lower() == 'magic ladder':
                if p2_items[1] == 'Magic Ladder' or p2_items[2] == 'Magic Ladder' or p2_items[3] == 'Magic Ladder':
                    print('Player 2 used the Magic Ladder!')
                    time.sleep(2)
                    mag_ladder = random.choice(range(5, 16))
                    print('The ladder took Player 2 up', mag_ladder, 'spaces!')
                    player2pos += mag_ladder
                    time.sleep(2)
                    if p2_items.index('Magic Ladder') == 1:
                        p2_items[1] = ''
                    elif p2_items.index('Magic Ladder') == 2:
                        p2_items[2] = ''
                    elif p2_items.index('Magic Ladder') == 3:
                        p2_items[3] = ''
                    item_use = 0
                    if player2pos in snakes:
                        print('Uh-oh! You landed on a snake!')
                        time.sleep(2)
                        signal = 2
                        snake()
                    elif player2pos in ladders:
                        print('Woo-hoo! You landed on a ladder!')
                        time.sleep(2)
                        signal = 2
                        ladder()
                    elif player2pos > goal:
                        print('Ooh... you overshot that one!')
                        player2pos -= dice_roll
                        time.sleep(2)
                    else:
                        P2DiceRoll()
                else:
                    print("You don't have a Magic Ladder!")
                    time.sleep(2)
                    P2DiceRoll()
            elif item_select.lower() == 'ultimate fate':
                if p2_items[1] == 'Ultimate Fate' or p2_items[2] == 'Ultimate Fate' or p2_items[3] == 'Ultimate Fate':
                    print('Player 2 used the Ultimate Fate!')
                    time.sleep(2)
                    print("One dice roll decides everyone's fate!")
                    if players >= 2:
                        input('(Press enter to decide fate)')
                    dice_roll = random.choice(range(1, 7))
                    print('The dice rolls', dice_roll, end = '')
                    print(". Your fate reads...")
                    time.sleep(2)
                    if dice_roll == 1:
                        print('Everyone must return to the beginning!')
                        time.sleep(2)
                        player1pos = 0
                        player2pos = 0
                        player3pos = 0
                        player4pos = 0
                    elif dice_roll == 2:
                        print('Everyone gets the effects of the Golden Minus Pear!')
                        time.sleep(2)
                        p1_status = 'G-Pear'
                        p2_status = 'G-Pear'
                        p3_status = 'G-Pear'
                        p4_status = 'G-Pear'
                    elif dice_roll == 3:
                        print('Everyone gets infected with the Plus Apple!')
                        time.sleep(2)
                        p1_status = 'Apple'
                        p2_status = 'Apple'
                        p3_status = 'Apple'
                        p4_status = 'Apple'
                    elif dice_roll == 4:
                        print('Everyone gets their locations rearranged!')
                        time.sleep(2)
                        player1pos = random.choice([savep2pos, savep3pos, savep4pos])
                        player2pos = random.choice([savep1pos, savep3pos, savep4pos])
                        player3pos = random.choice([savep2pos, savep1pos, savep4pos])
                        player4pos = random.choice([savep2pos, savep3pos, savep1pos])
                        print('Player 1 is now at space #',player1pos)
                        time.sleep(1)
                        print('Player 2 is now at space #',player2pos)
                        time.sleep(1)
                        print('Player 3 is now at space #',player3pos)
                        time.sleep(1)
                        print('Player 4 is now at space #',player4pos)
                        time.sleep(2)
                    elif dice_roll == 5:
                        print('Everyone gets the effects of the Minus Pear!')
                        time.sleep(2)
                        p1_status = 'Pear'
                        p2_status = 'Pear'
                        p3_status = 'Pear'
                        p4_status = 'Pear'
                    elif dice_roll == 6:
                        print('Everyone gets the effects of the Golden Plus Apple!')
                        time.sleep(2)
                        p1_status = 'G-Apple'
                        p2_status = 'G-Apple'
                        p3_status = 'G-Apple'
                        p4_status = 'G-Apple'
                    time.sleep(2)
                    if p2_items.index('Ultimate Fate') == 1:
                        p2_items[1] = ''
                    elif p2_items.index('Ultimate Fate') == 2:
                        p2_items[2] = ''
                    elif p2_items.index('Ultimate Fate') == 3:
                        p2_items[3] = ''
                    item_use = 0
                    P2DiceRoll()
                else:
                    print("You don't have an Ultimate Fate!")
                    time.sleep(2)
                    P2DiceRoll()
            else:
                P2DiceRoll()
    else:
        print("We didn't get that... Try Again!")
        time.sleep(2)
        P2DiceRoll()
    if player2pos in snakes:
        print('Uh-oh! You landed on a snake!')
        time.sleep(2)
        signal = 2
        snake()
    elif player2pos in ladders:
        print('Woo-hoo! You landed on a ladder!')
        time.sleep(2)
        signal = 2
        ladder()
    if player2pos > goal:
        print('Ooh... you overshot that one!')
        player2pos -= dice_roll
        time.sleep(2)
    savep2pos = player2pos
    endCheck()
    item_use = 1
    if item_fix == 1:
        item_roll = random.choice(range(1, 101))
        if item_roll <= item_chance:
            print('Whoa! You get to play an item game!')
            time.sleep(2)
            if players >= 2:
                left_or_right = input('Left or Right?: ')
            else:
                left_or_right = random.choice(['Left', 'Right'])
            if left_or_right.lower() == 'left':
                item_get = random.choice(['Plus Apple', 'Minus Pear', 'Golden Plus Apple', 'Golden Minus Pear', 'Selection Die', 'Extra Die'])
                print('You recieved:', item_get)
                if p2_items[1] == '':
                    p2_items[1] = item_get
                elif p2_items[2] == '':
                    p2_items[2] = item_get
                elif p2_items[3] == '':
                    p2_items[3] = item_get
                else:
                    print('Uh oh! No more room!')
                    time.sleep(1)
                    if players >= 2:
                        print('Which item slot do you want to replace?')
                        print(p2_items)
                        print('1, 2, or 3 (input anything else to toss item)')
                        item_replace = int(input())
                    else:
                        item_replace = random.choice(range(1, 4))
                    if item_replace == 1:
                        print('Goodbye,', p2_items[1])
                        time.sleep(1)
                        p2_items[1] = item_get
                        print('Hello,', p2_items[1])
                    elif item_replace == 2:
                        print('Goodbye,', p2_items[2])
                        time.sleep(1)
                        p2_items[2] = item_get
                        print('Hello,', p2_items[2])
                    elif item_replace == 3:
                        print('Goodbye,', p2_items[3])
                        time.sleep(1)
                        p2_items[3] = item_get
                        print('Hello,', p2_items[3])
                    else:
                        print('You threw the', item_get, 'away!')
            elif left_or_right.lower() == 'right':
                item_get = random.choice(['Plus Apple', 'Minus Pear', 'Golden Plus Apple', 'Golden Minus Pear', 'Selection Die', 'Extra Die', 'Swap Box', 'Great Snake', 'God Snake', 'Double-or-Nothing Die', 'Magic Ladder', 'Ultimate Fate'])
                print('You recieved:', item_get)
                if p2_items[1] == '':
                    p2_items[1] = item_get
                elif p2_items[2] == '':
                    p2_items[2] = item_get
                elif p2_items[3] == '':
                    p2_items[3] = item_get
                else:
                    print('Uh oh! No more room!')
                    time.sleep(1)
                    if players >= 2:
                        print('Which item slot do you want to replace?')
                        print(p2_items)
                        print('1, 2, or 3 (input anything else to toss item)')
                        item_replace = int(input())
                    else:
                        item_replace = random.choice(range(1, 4))
                    if item_replace == 1:
                        print('Goodbye,', p2_items[1])
                        time.sleep(1)
                        p2_items[1] = item_get
                        print('Hello,', p2_items[1])
                    elif item_replace == 2:
                        print('Goodbye,', p2_items[2])
                        time.sleep(1)
                        p2_items[2] = item_get
                        print('Hello,', p2_items[2])
                    elif item_replace == 3:
                        print('Goodbye,', p2_items[3])
                        time.sleep(1)
                        p2_items[3] = item_get
                        print('Hello,', p2_items[3])
                    else:
                        print('You threw the', item_get, 'away!')
            else:
                item_get = random.choice(['Swap Box', 'Great Snake', 'God Snake', 'Double-or-Nothing Die', 'Magic Ladder', 'Ultimate Fate'])
                print('You recieved:', item_get)
                if p2_items[1] == '':
                    p2_items[1] = item_get
                elif p2_items[2] == '':
                    p2_items[2] = item_get
                elif p2_items[3] == '':
                    p2_items[3] = item_get
                else:
                    print('Uh oh! No more room!')
                    time.sleep(1)
                    if players >= 2:
                        print('Which item slot do you want to replace?')
                        print(p2_items)
                        print('1, 2, or 3 (input anything else to toss item)')
                        item_replace = int(input())
                    else:
                        item_replace = random.choice(range(1, 4))
                    if item_replace == 1:
                        print('Goodbye,', p2_items[1])
                        time.sleep(1)
                        p2_items[1] = item_get
                        print('Hello,', p2_items[1])
                    elif item_replace == 2:
                        print('Goodbye,', p2_items[2])
                        time.sleep(1)
                        p2_items[2] = item_get
                        print('Hello,', p2_items[2])
                    elif item_replace == 3:
                        print('Goodbye,', p2_items[3])
                        time.sleep(1)
                        p2_items[3] = item_get
                        print('Hello,', p2_items[3])
                    else:
                        print('You threw the', item_get, 'away!')
            item_fix = 0
            if player2pos < 0:
                while player2pos != 0:
                    player2pos += 1
            time.sleep(2)
    print('')
 
def P3DiceRoll():
    global double_meter3
    global players
    global player1pos
    global player2pos
    global player3pos
    global player4pos
    global double_meter_cap
    global dice
    global item_chance
    global item_roll
    global p3_items
    global p1_status
    global p2_status
    global p3_status
    global p4_status
    global item_get
    global item_fix
    global item_use
    global savep1pos
    global savep2pos
    global savep3pos
    global savep4pos
    global signal
    item_fix = 1
    print('Player 3! GO!')
    time.sleep(1)
    print('Double Meter:', double_meter3)
    print('Current position:', player3pos)
    print('Status Effect:', p3_status)
    if double_meter3 == double_meter_cap:
        print('Double Roll Ready!')
    if dice != 'Single' or dice != 'Double' or dice != 'Item':
        if players >= 3:
            dice = input('Single/Double/Item: ')
        else:
            if double_meter3 == double_meter_cap:
                if p3_items[1] != '' or p3_items[2] != '' or p3_items[3] != '':
                    if item_use == 1:
                        dice = random.choice(['Single', 'Double', 'Item'])
                    else:
                        dice = random.choice(['Single', 'Double'])
                else:
                    dice = random.choice(['Single', 'Double'])
            elif p3_items[1] != '' or p3_items[2] != '' or p3_items[3] != '':
                if item_use == 1:
                    dice = random.choice(['Single', 'Item'])
                else:
                    dice = 'Single'
            else:
                dice = 'Single'
    if dice.lower() == 'single':
        dice_roll = random.choice(range(1, 7))
        print('The die rolled', dice_roll)
        time.sleep(1)
        if p3_status == 'Apple':
            dice_roll += 3
            p3_status = ''
        elif p3_status == 'G-Apple':
            dice_roll += 6
            p3_status = ''
        elif p3_status == 'Pear':
            dice_roll -= 3
            p3_status = ''
        elif p3_status == 'G-Pear':
            dice_roll -= 6
            p3_status = ''
        elif p3_status == 'EX':
            ex_dice_roll = random.choice(range(1, 7))
            print('Extra die rolls', ex_dice_roll)
            dice_roll += ex_dice_roll
            p3_status = ''
            time.sleep(1)
        elif p3_status == 'Double':
            dice_roll *= 2
            p3_status = ''
        print('Player 3 moves', dice_roll, 'spaces!')
        player3pos += dice_roll
        time.sleep(1)
        print('Player 3 is now at space #',player3pos)
        time.sleep(2)
        for i in range(dice_roll):
            double_meter3 += 5
        if double_meter3 > double_meter_cap:
            while double_meter3 != double_meter_cap:
                double_meter3 -= 1
    elif dice.lower() == 'double':
        if double_meter3 == 100:    
            print('DOUBLE ROLL!')
            time.sleep(1)
            dice_roll = random.choice(range(2, 13))
            print('The dice rolled', dice_roll)
            time.sleep(1)
            if p3_status == 'Apple':
                dice_roll += 3
                p3_status = ''
            elif p3_status == 'G-Apple':
                dice_roll += 6
                p3_status = ''
            elif p3_status == 'Pear':
                dice_roll -= 3
                p3_status = ''
            elif p3_status == 'G-Pear':
                dice_roll -= 6
                p3_status = ''
            elif p3_status == 'EX':
                ex_dice_roll = random.choice(range(1, 7))
                print('Extra die rolls', ex_dice_roll)
                dice_roll += ex_dice_roll
                p3_status = ''
                time.sleep(1)
            elif p3_status == 'Double':
                dice_roll *= 2
                p3_status = ''
            print('Player 3 moves', dice_roll, 'spaces!')
            player3pos += dice_roll
            time.sleep(1)
            print('Player 3 is now at space #',player3pos)
            time.sleep(2)
            double_meter3 = 0
        else:
            print("Can't use double roll.")
            time.sleep(2)
            P3DiceRoll()
    elif dice.lower() == 'item':
        if item_use == 1:
            print('Select your item:', p3_items)
            if players >= 3:
                item_select = input()
            else:
                item_select = random.choice(p3_items)
            if item_select.lower() == 'back':
                P3DiceRoll()
            elif item_select.lower() == 'plus apple':
                if p3_items[1] == 'Plus Apple' or p3_items[2] == 'Plus Apple' or p3_items[3] == 'Plus Apple':
                    print('Player 3 used the Plus Apple!')
                    time.sleep(2)
                    if p3_status == 'Pear':
                        print('The pear effect has been cancelled. They will roll normally.')
                        p3_status = ''
                    elif p3_status == 'G-Pear':
                        print('The Golden Pear effect has been halved. They will now go -3.')
                        p3_status = 'Pear'
                    else:
                        print("They'll move 3 extra spaces with this next roll!")
                        p3_status = 'Apple'
                    time.sleep(2)
                    if p3_items.index('Plus Apple') == 1:
                        p3_items[1] = ''
                    elif p3_items.index('Plus Apple') == 2:
                        p3_items[2] = ''
                    elif p3_items.index('Plus Apple') == 3:
                        p3_items[3] = ''
                    item_use = 0
                    P3DiceRoll()
                else:
                    print("You don't have a Plus Apple!")
                    time.sleep(2)
                    P3DiceRoll()
            elif item_select.lower() == 'golden plus apple':
                if p3_items[1] == 'Golden Plus Apple' or p3_items[2] == 'Golden Plus Apple' or p3_items[3] == 'Golden Plus Apple':
                    print('Player 3 used the Golden Plus Apple!')
                    time.sleep(2)
                    if p3_status == 'Pear':
                        print('The pear effect has been overridden. They will now move +3.')
                        p3_status = 'Apple'
                    elif p3_status == 'G-Pear':
                        print('The Golden Pear cancelled. They will roll normally.')
                        p3_status = ''
                    else:
                        print("They'll move 6 extra spaces with this next roll!")
                        p3_status = 'G-Apple'
                    time.sleep(2)
                    if p3_items.index('Golden Plus Apple') == 1:
                        p3_items[1] = ''
                    elif p3_items.index('Golden Plus Apple') == 2:
                        p3_items[2] = ''
                    elif p3_items.index('Golden Plus Apple') == 3:
                        p3_items[3] = ''
                    item_use = 0
                    P3DiceRoll()
                else:
                    print("You don't have a Golden Plus Apple!")
                    time.sleep(2)
                    P3DiceRoll()
            elif item_select.lower() == 'minus pear':
                if p3_items[1] == 'Minus Pear' or p3_items[2] == 'Minus Pear' or p3_items[3] == 'Minus Pear':
                    print('Player 3 used the Minus Pear!')
                    time.sleep(2)
                    if players >= 3:
                        print('Who would you like to use it on?')
                        print('1 / 2 / 3 / 4')
                        pear_effect = int(input())
                    else:
                        pear_effect = random.choice(range(1, 5))
                    if pear_effect == 1:
                        print('Player 3 used the Minus Pear on Player 1!')
                        if p1_status == 'Apple':
                            print('The apple effect has been cancelled. They will roll normally.')
                            p1_status = ''
                        elif p1_status == 'G-Apple':
                            print('The Golden Apple effect has been halved. They will now go +3.')
                            p1_status = 'Apple'
                        else:
                            print("They'll move 3 less spaces with this next roll!")
                            p1_status = 'Pear'
                    elif pear_effect == 2:
                        print('Player 3 used the Minus Pear on Player 2!')
                        if p2_status == 'Apple':
                            print('The apple effect has been cancelled. They will roll normally.')
                            p2_status = ''
                        elif p2_status == 'G-Apple':
                            print('The Golden Apple effect has been halved. They will now go +3.')
                            p2_status = 'Apple'
                        else:
                            print("They'll move 3 less spaces with this next roll!")
                            p2_status = 'Pear'
                    elif pear_effect == 3:
                        print('Player 3 used the Minus Pear on themselves!')
                        if p3_status == 'Apple':
                            print('The apple effect has been cancelled. They will roll normally.')
                            p3_status = ''
                        elif p3_status == 'G-Apple':
                            print('The Golden Apple effect has been halved. They will now go +3.')
                            p3_status = 'Apple'
                        else:
                            print("They'll move 3 less spaces with this next roll!")
                            p3_status = 'Pear'
                    elif pear_effect == 4:
                        print('Player 3 used the Minus Pear on Player 4!')
                        if p4_status == 'Apple':
                            print('The apple effect has been cancelled. They will roll normally.')
                            p4_status = ''
                        elif p4_status == 'G-Apple':
                            print('The Golden Apple effect has been halved. They will now go +3.')
                            p4_status = 'Apple'
                        else:
                            print("They'll move 3 less spaces with this next roll!")
                            p4_status = 'Pear'
                    else:
                        print('You ended up tossing the pear...')
                    time.sleep(2)
                    if p3_items.index('Minus Pear') == 1:
                        p3_items[1] = ''
                    elif p3_items.index('Minus Pear') == 2:
                        p3_items[2] = ''
                    elif p3_items.index('Minus Pear') == 3:
                        p3_items[3] = ''
                    item_use = 0
                    P3DiceRoll()
                else:
                    print("You don't have a Minus Pear!")
                    time.sleep(2)
                    P3DiceRoll()
            elif item_select.lower() == 'golden minus pear':
                if p3_items[1] == 'Golden Minus Pear' or p3_items[2] == 'Golden Minus Pear' or p3_items[3] == 'Golden Minus Pear':
                    print('Player 3 used the Golden Minus Pear!')
                    time.sleep(2)
                    if players >= 3:
                        print('Who would you like to use it on?')
                        print('1 / 2 / 3 / 4')
                        pear_effect = int(input())
                    else:
                        pear_effect = random.choice(range(1, 5))
                    if pear_effect == 1:
                        print('Player 3 used the Golden Minus Pear on Player 1!')
                        if p1_status == 'Apple':
                            print('The apple effect has been overridden. They now go -3.')
                            p1_status = 'Pear'
                        elif p1_status == 'G-Apple':
                            print('The Golden Apple effect has been cancelled. They will roll normally.')
                            p1_status = ''
                        else:
                            print("They'll move 6 less spaces with this next roll!")
                            p1_status = 'G-Pear'
                    elif pear_effect == 2:
                        print('Player 3 used the Golden Minus Pear on Player 2!')
                        if p2_status == 'Apple':
                            print('The apple effect has been overridden. They now go -3.')
                            p2_status = 'Pear'
                        elif p2_status == 'G-Apple':
                            print('The Golden Apple effect has been cancelled. They will roll normally.')
                            p2_status = ''
                        else:
                            print("They'll move 6 less spaces with this next roll!")
                            p2_status = 'G-Pear'
                    elif pear_effect == 3:
                        print('Player 3 used the Minus Pear on themselves!')
                        if p3_status == 'Apple':
                            print('The apple effect has been overridden. They now go -3.')
                            p3_status = 'Pear'
                        elif p3_status == 'G-Apple':
                            print('The Golden Apple effect has been cancelled. They will roll normally.')
                            p3_status = ''
                        else:
                            print("They'll move 6 less spaces with this next roll!")
                            p3_status = 'G-Pear'
                    elif pear_effect == 4:
                        print('Player 3 used the Minus Pear on Player 4!')
                        if p4_status == 'Apple':
                            print('The apple effect has been overridden. They now go -3.')
                            p4_status = 'Pear'
                        elif p4_status == 'G-Apple':
                            print('The Golden Apple effect has been cancelled. They will roll normally.')
                            p4_status = ''
                        else:
                            print("They'll move 6 less spaces with this next roll!")
                            p4_status = 'G-Pear'
                    else:
                        print('You ended up tossing the pear...')
                    time.sleep(2)
                    if p3_items.index('Golden Minus Pear') == 1:
                        p3_items[1] = ''
                    elif p3_items.index('Golden Minus Pear') == 2:
                        p3_items[2] = ''
                    elif p3_items.index('Golden Minus Pear') == 3:
                        p3_items[3] = ''
                    item_use = 0
                    P3DiceRoll()
                else:
                    print("You don't have a Golden Minus Pear!")
                    time.sleep(2)
                    P3DiceRoll()
            elif item_select.lower() == 'extra die':
                if p3_items[1] == 'Extra Die' or p3_items[2] == 'Extra Die' or p3_items[3] == 'Extra Die':
                    print('Player 3 used the Extra Die!')
                    time.sleep(2)
                    print("They'll gain an extra roll on this next turn!")
                    time.sleep(2)
                    p3_status = 'EX'
                    if p3_items.index('Extra Die') == 1:
                        p3_items[1] = ''
                    elif p3_items.index('Extra Die') == 2:
                        p3_items[2] = ''
                    elif p3_items.index('Extra Die') == 3:
                        p3_items[3] = ''
                    item_use = 0
                    P3DiceRoll()
                else:
                    print("You don't have an Extra Die!")
                    time.sleep(2)
                    P3DiceRoll()
            elif item_select.lower() == 'selection die':
                if p3_items[1] == 'Selection Die' or p3_items[2] == 'Selection Die' or p3_items[3] == 'Selection Die':
                    print('Player 3 used the Selection Die!')
                    time.sleep(2)
                    if players >= 3:
                        print("How many spaces do you want to move? (1-6)")
                        dice_roll = int(input())
                    else:
                        dice_roll = random.choice(range(1, 7))
                    print('The die rolled', dice_roll)
                    time.sleep(1)
                    if p3_status == 'Apple':
                        dice_roll += 3
                    elif p3_status == 'G-Apple':
                        dice_roll += 6
                    elif p3_status == 'Pear':
                        dice_roll -= 3
                    elif p3_status == 'G-Pear':
                        dice_roll -= 6
                    elif p3_status == 'EX':
                        ex_dice_roll = random.choice(range(1, 7))
                        print('Extra die rolls', ex_dice_roll)
                        dice_roll += ex_dice_roll
                        time.sleep(1)
                    elif p3_status == 'Double':
                        dice_roll *= 2
                    elif p3_status == 'Half':
                        dice_roll //= 2
                        p3_status = ''
                    print('Player 3 moves', dice_roll, 'spaces!')
                    player3pos += dice_roll
                    time.sleep(1)
                    print('Player 3 is now at space #',player3pos)
                    time.sleep(2)
                    if p3_items.index('Selection Die') == 1:
                        p3_items[1] = ''
                    elif p3_items.index('Selection Die') == 2:
                        p3_items[2] = ''
                    elif p3_items.index('Selection Die') == 3:
                        p3_items[3] = ''
                else:
                    print("You don't have a Selection Die!")
                    time.sleep(2)
                    item_use = 0
                    P3DiceRoll()
            elif item_select.lower() == 'swap box':
                if p3_items[1] == 'Swap Box' or p3_items[2] == 'Swap Box' or p3_items[3] == 'Swap Box':
                    print('Player 3 used the Swap Box!')
                    time.sleep(2)
                    swap = random.choice([1, 2, 4])
                    if swap == 1:
                        player1pos = player3pos
                        player3pos = savep1pos
                        print('Players 1 and 3 swapped places!')
                        time.sleep(1)
                        print('Player 1 is now at space #',player1pos)
                        time.sleep(1.5)
                        print('Player 3 is now at space #',player3pos)
                    if swap == 2:
                        player2pos = player3pos
                        player3pos = savep2pos
                        print('Players 2 and 3 swapped places!')
                        time.sleep(1)
                        print('Player 2 is now at space #',player2pos)
                        time.sleep(1.5)
                        print('Player 3 is now at space #',player3pos)
                    if swap == 4:
                        player3pos = player4pos
                        player4pos = savep3pos
                        print('Players 3 and 4 swapped places!')
                        time.sleep(1)
                        print('Player 3 is now at space #',player3pos)
                        time.sleep(1.5)
                        print('Player 4 is now at space #',player4pos)
                    if p3_items.index('Swap Box') == 1:
                        p3_items[1] = ''
                    elif p3_items.index('Swap Box') == 2:
                        p3_items[2] = ''
                    elif p3_items.index('Swap Box') == 3:
                        p3_items[3] = ''
                    item_use = 0
                    P3DiceRoll()
                else:
                    print("You don't have a Swap Box!")
                    time.sleep(2)
                    P3DiceRoll()
            elif item_select.lower() == 'great snake':
                if p3_items[1] == 'Great Snake' or p3_items[2] == 'Great Snake' or p3_items[3] == 'Great Snake':
                    print('Player 3 used the Great Snake!')
                    time.sleep(2)
                    g_snake = random.choice([1, 2, 3, 4])
                    if g_snake == 1:
                        print('Player 1 goes down 20 spaces!')
                        player1pos -= 20
                        if player1pos < 0:
                            while player1pos != 0:
                                player1pos += 1
                    if g_snake == 2:
                        print('Player 2 goes down 20 spaces!')
                        player2pos -= 20
                        if player2pos < 0:
                            while player2pos != 0:
                                player2pos += 1
                    if g_snake == 3:
                        print('Snake backfired!')
                        time.sleep(2)
                        print('Player 3 goes down 20 spaces!')
                        player3pos -= 20
                        if player3pos < 0:
                            while player3pos != 0:
                                player3pos += 1
                    if g_snake == 4:
                        print('Player 4 goes down 20 spaces!')
                        player4pos -= 20
                        if player4pos < 0:
                            while player4pos != 0:
                                player4pos += 1
                    if p3_items.index('Great Snake') == 1:
                        p3_items[1] = ''
                    elif p3_items.index('Great Snake') == 2:
                        p3_items[2] = ''
                    elif p3_items.index('Great Snake') == 3:
                        p3_items[3] = ''
                    item_use = 0
                    P3DiceRoll()
                else:
                    print("You don't have a Great Snake!")
                    time.sleep(2)
                    P3DiceRoll()
            elif item_select.lower() == 'god snake':
                if p3_items[1] == 'God Snake' or p3_items[2] == 'God Snake' or p3_items[3] == 'God Snake':
                    print('Player 3 used the God Snake!')
                    time.sleep(2)
                    g_snake = random.choice([1, 2, 3, 4])
                    if g_snake == 1:
                        print('Player 1 goes down to the beginning!')
                        player1pos = 0
                    if g_snake == 2:
                        print('Player 2 goes down to the beginning!')
                        player2pos = 0
                    if g_snake == 3:
                        print('Snake backfired!')
                        time.sleep(2)
                        print('Player 3 goes down to the beginning!')
                        player3pos = 0
                    if g_snake == 4:
                        print('Player 4 goes down to the beginning!')
                        player4pos = 0
                    if p3_items.index('God Snake') == 1:
                        p3_items[1] = ''
                    elif p3_items.index('God Snake') == 2:
                        p3_items[2] = ''
                    elif p3_items.index('God Snake') == 3:
                        p3_items[3] = ''
                    item_use = 0
                    P3DiceRoll()
                else:
                    print("You don't have a God Snake!")
                    time.sleep(2)
                    P3DiceRoll()
            elif item_select.lower() == 'double-or-nothing die':
                if p3_items[1] == 'Double-or-Nothing Die' or p3_items[2] == 'Double-or-Nothing Die' or p3_items[3] == 'Double-or-Nothing Die':
                    print('Player 3 used the Double-or-Nothing Die!')
                    time.sleep(2)
                    print("Take your chance! It's Double or Nothing!")
                    if players >= 3:
                        input('(Press Enter)')
                    dice_roll = random.choice(range(1, 7))
                    myst_die = random.choice(range(1, 7))
                    print('You rolled:', dice_roll)
                    time.sleep(1)
                    print('The die rolled:', myst_die)
                    time.sleep(2)
                    if dice_roll > myst_die:
                        print('Congratulations! Your next roll will be doubled!')
                        p3_status = 'Double'
                    else:
                        print('Oh... it all fell to nothing. Your next roll will be halved.')
                        p3_status = 'Half'
                    time.sleep(2)
                    if p3_items.index('Double-or-Nothing Die') == 1:
                        p3_items[1] = ''
                    elif p3_items.index('Double-or-Nothing Die') == 2:
                        p3_items[2] = ''
                    elif p3_items.index('Double-or-Nothing Die') == 3:
                        p3_items[3] = ''
                    item_use = 0
                    P3DiceRoll()
                else:
                    print("You don't have a Double-or-Nothing Die!")
                    time.sleep(2)
                    P3DiceRoll()
            elif item_select.lower() == 'magic ladder':
                if p3_items[1] == 'Magic Ladder' or p3_items[2] == 'Magic Ladder' or p3_items[3] == 'Magic Ladder':
                    print('Player 3 used the Magic Ladder!')
                    time.sleep(2)
                    mag_ladder = random.choice(range(5, 16))
                    print('The ladder took Player 3 up', mag_ladder, 'spaces!')
                    player3pos += mag_ladder
                    time.sleep(2)
                    if p3_items.index('Magic Ladder') == 1:
                        p3_items[1] = ''
                    elif p3_items.index('Magic Ladder') == 2:
                        p3_items[2] = ''
                    elif p3_items.index('Magic Ladder') == 3:
                        p3_items[3] = ''
                    item_use = 0
                    if player3pos in snakes:
                        print('Uh-oh! You landed on a snake!')
                        time.sleep(2)
                        signal = 3
                        snake()
                    elif player3pos in ladders:
                        print('Woo-hoo! You landed on a ladder!')
                        time.sleep(2)
                        signal = 3
                        ladder()
                    elif player3pos > goal:
                        print('Ooh... you overshot that one!')
                        player3pos -= dice_roll
                        time.sleep(2)
                    else:
                        P3DiceRoll()
                else:
                    print("You don't have a Magic Ladder!")
                    time.sleep(2)
                    P3DiceRoll()
            elif item_select.lower() == 'ultimate fate':
                if p3_items[1] == 'Ultimate Fate' or p3_items[2] == 'Ultimate Fate' or p3_items[3] == 'Ultimate Fate':
                    print('Player 3 used the Ultimate Fate!')
                    time.sleep(2)
                    print("One dice roll decides everyone's fate!")
                    if players >= 3:
                        input('(Press enter to decide fate)')
                    dice_roll = random.choice(range(1, 7))
                    print('The dice rolls', dice_roll, end = '')
                    print(". Your fate reads...")
                    time.sleep(2)
                    if dice_roll == 1:
                        print('Everyone must return to the beginning!')
                        time.sleep(2)
                        player1pos = 0
                        player2pos = 0
                        player3pos = 0
                        player4pos = 0
                    elif dice_roll == 2:
                        print('Everyone gets the effects of the Golden Minus Pear!')
                        time.sleep(2)
                        p1_status = 'G-Pear'
                        p2_status = 'G-Pear'
                        p3_status = 'G-Pear'
                        p4_status = 'G-Pear'
                    elif dice_roll == 3:
                        print('Everyone gets infected with the Plus Apple!')
                        time.sleep(2)
                        p1_status = 'Apple'
                        p2_status = 'Apple'
                        p3_status = 'Apple'
                        p4_status = 'Apple'
                    elif dice_roll == 4:
                        print('Everyone gets their locations rearranged!')
                        time.sleep(2)
                        player1pos = random.choice([savep2pos, savep3pos, savep4pos])
                        player2pos = random.choice([savep1pos, savep3pos, savep4pos])
                        player3pos = random.choice([savep2pos, savep1pos, savep4pos])
                        player4pos = random.choice([savep2pos, savep3pos, savep1pos])
                        print('Player 1 is now at space #',player1pos)
                        time.sleep(1)
                        print('Player 2 is now at space #',player2pos)
                        time.sleep(1)
                        print('Player 3 is now at space #',player3pos)
                        time.sleep(1)
                        print('Player 4 is now at space #',player4pos)
                        time.sleep(2)
                    elif dice_roll == 5:
                        print('Everyone gets the effects of the Minus Pear!')
                        time.sleep(2)
                        p1_status = 'Pear'
                        p2_status = 'Pear'
                        p3_status = 'Pear'
                        p4_status = 'Pear'
                    elif dice_roll == 6:
                        print('Everyone gets the effects of the Golden Plus Apple!')
                        time.sleep(2)
                        p1_status = 'G-Apple'
                        p2_status = 'G-Apple'
                        p3_status = 'G-Apple'
                        p4_status = 'G-Apple'
                    time.sleep(2)
                    if p3_items.index('Ultimate Fate') == 1:
                        p3_items[1] = ''
                    elif p3_items.index('Ultimate Fate') == 2:
                        p3_items[2] = ''
                    elif p3_items.index('Ultimate Fate') == 3:
                        p3_items[3] = ''
                    item_use = 0
                    P3DiceRoll()
                else:
                    print("You don't have an Ultimate Fate!")
                    time.sleep(2)
                    P3DiceRoll()
            else:
                P3DiceRoll()
    else:
        print("We didn't get that... Try Again!")
        time.sleep(2)
        P3DiceRoll()
    if player3pos in snakes:
        print('Uh-oh! You landed on a snake!')
        time.sleep(2)
        signal = 3
        snake()
    elif player3pos in ladders:
        print('Woo-hoo! You landed on a ladder!')
        time.sleep(2)
        signal = 3
        ladder()
    if player3pos > goal:
        print('Ooh... you overshot that one!')
        player3pos -= dice_roll
        time.sleep(2)
    savep3pos = player3pos
    endCheck()
    item_use = 1
    if item_fix == 1:
        item_roll = random.choice(range(1, 101))
        if item_roll <= item_chance:
            print('Whoa! You get to play an item game!')
            time.sleep(2)
            if players >= 3:
                left_or_right = input('Left or Right?: ')
            else:
                left_or_right = random.choice(['Left', 'Right'])
            if left_or_right.lower() == 'left':
                item_get = random.choice(['Plus Apple', 'Minus Pear', 'Golden Plus Apple', 'Golden Minus Pear', 'Selection Die', 'Extra Die'])
                print('You recieved:', item_get)
                if p3_items[1] == '':
                    p3_items[1] = item_get
                elif p3_items[2] == '':
                    p3_items[2] = item_get
                elif p3_items[3] == '':
                    p3_items[3] = item_get
                else:
                    print('Uh oh! No more room!')
                    time.sleep(1)
                    if players >= 3:
                        print('Which item slot do you want to replace?')
                        print(p3_items)
                        print('1, 2, or 3 (input anything else to toss item)')
                        item_replace = int(input())
                    else:
                        item_replace = random.choice(range(1, 4))
                    if item_replace == 1:
                        print('Goodbye,', p3_items[1])
                        time.sleep(1)
                        p3_items[1] = item_get
                        print('Hello,', p3_items[1])
                    elif item_replace == 2:
                        print('Goodbye,', p3_items[2])
                        time.sleep(1)
                        p3_items[2] = item_get
                        print('Hello,', p3_items[2])
                    elif item_replace == 3:
                        print('Goodbye,', p3_items[3])
                        time.sleep(1)
                        p3_items[3] = item_get
                        print('Hello,', p3_items[3])
                    else:
                        print('You threw the', item_get, 'away!')
            elif left_or_right.lower() == 'right':
                item_get = random.choice(['Swap Box', 'Great Snake', 'God Snake', 'Double-or-Nothing Die', 'Magic Ladder', 'Ultimate Fate'])
                print('You recieved:', item_get)
                if p3_items[1] == '':
                    p3_items[1] = item_get
                elif p3_items[2] == '':
                    p3_items[2] = item_get
                elif p3_items[3] == '':
                    p3_items[3] = item_get
                else:
                    print('Uh oh! No more room!')
                    time.sleep(1)
                    if players >= 3:
                        print('Which item slot do you want to replace?')
                        print(p3_items)
                        print('1, 2, or 3 (input anything else to toss item)')
                        item_replace = int(input())
                    else:
                        item_replace = random.choice(range(1, 4))
                    if item_replace == 1:
                        print('Goodbye,', p3_items[1])
                        time.sleep(1)
                        p3_items[1] = item_get
                        print('Hello,', p3_items[1])
                    elif item_replace == 2:
                        print('Goodbye,', p3_items[2])
                        time.sleep(1)
                        p3_items[2] = item_get
                        print('Hello,', p3_items[2])
                    elif item_replace == 3:
                        print('Goodbye,', p3_items[3])
                        time.sleep(1)
                        p3_items[3] = item_get
                        print('Hello,', p3_items[3])
                    else:
                        print('You threw the', item_get, 'away!')
            else:
                item_get = random.choice(['Plus Apple', 'Minus Pear', 'Golden Plus Apple', 'Golden Minus Pear', 'Selection Die', 'Extra Die', 'Swap Box', 'Great Snake', 'God Snake', 'Double-or-Nothing Die', 'Magic Ladder', 'Ultimate Fate'])
                print('You recieved:', item_get)
                if p3_items[1] == '':
                    p3_items[1] = item_get
                elif p3_items[2] == '':
                    p3_items[2] = item_get
                elif p3_items[3] == '':
                    p3_items[3] = item_get
                else:
                    print('Uh oh! No more room!')
                    time.sleep(1)
                    if players >= 3:
                        print('Which item slot do you want to replace?')
                        print(p3_items)
                        print('1, 2, or 3 (input anything else to toss item)')
                        item_replace = int(input())
                    else:
                        item_replace = random.choice(range(1, 4))
                    if item_replace == 1:
                        print('Goodbye,', p3_items[1])
                        time.sleep(1)
                        p3_items[1] = item_get
                        print('Hello,', p3_items[1])
                    elif item_replace == 2:
                        print('Goodbye,', p3_items[2])
                        time.sleep(1)
                        p3_items[2] = item_get
                        print('Hello,', p3_items[2])
                    elif item_replace == 3:
                        print('Goodbye,', p3_items[3])
                        time.sleep(1)
                        p3_items[3] = item_get
                        print('Hello,', p3_items[3])
                    else:
                        print('You threw the', item_get, 'away!')
            item_fix = 0
            if player3pos < 0:
                while player3pos != 0:
                    player3pos += 1
            time.sleep(2)
    print('')
    
def P4DiceRoll():
    global double_meter4
    global players
    global player1pos
    global player2pos
    global player3pos
    global player4pos
    global double_meter_cap
    global dice
    global item_chance
    global item_roll
    global p4_items
    global p1_status
    global p2_status
    global p3_status
    global p4_status
    global item_get
    global item_fix
    global item_use
    global savep1pos
    global savep2pos
    global savep3pos
    global savep4pos
    global signal
    item_fix = 1
    print('Player 4! GO!')
    time.sleep(1)
    print('Double Meter:', double_meter4)
    print('Current position:', player4pos)
    print('Status Effect:', p4_status)
    if double_meter4 == double_meter_cap:
        print('Double Roll Ready!')
    if dice != 'Single' or dice != 'Double' or dice != 'Item':
        if players >= 4:
            dice = input('Single/Double/Item: ')
        else:
            if double_meter4 == double_meter_cap:
                if p4_items[1] != '' or p4_items[2] != '' or p4_items[3] != '':
                    if item_use == 1:
                        dice = random.choice(['Single', 'Double', 'Item'])
                    else:
                        dice = random.choice(['Single', 'Double'])
                else:
                    dice = random.choice(['Single', 'Double'])
            elif p4_items[1] != '' or p4_items[2] != '' or p4_items[3] != '':
                if item_use == 1:
                    dice = random.choice(['Single', 'Item'])
                else:
                    dice = 'Single'
            else:
                dice = 'Single'
    if dice.lower() == 'single':
        dice_roll = random.choice(range(1, 7))
        print('The die rolled', dice_roll)
        time.sleep(1)
        if p4_status == 'Apple':
            dice_roll += 3
            p4_status = ''
        elif p4_status == 'G-Apple':
            dice_roll += 6
            p4_status = ''
        elif p4_status == 'Pear':
            dice_roll -= 3
            p4_status = ''
        elif p4_status == 'G-Pear':
            dice_roll -= 6
            p4_status = ''
        elif p4_status == 'EX':
            ex_dice_roll = random.choice(range(1, 7))
            print('Extra die rolls', ex_dice_roll)
            dice_roll += ex_dice_roll
            p4_status = ''
            time.sleep(1)
        elif p4_status == 'Double':
            dice_roll *= 2
            p4_status = ''
        print('Player 4 moves', dice_roll, 'spaces!')
        player4pos += dice_roll
        time.sleep(1)
        print('Player 4 is now at space #',player4pos)
        time.sleep(2)
        for i in range(dice_roll):
            double_meter4 += 5
        if double_meter4 > double_meter_cap:
            while double_meter4 != double_meter_cap:
                double_meter4 -= 1
    elif dice.lower() == 'double':
        if double_meter4 == 100:    
            print('DOUBLE ROLL!')
            time.sleep(1)
            dice_roll = random.choice(range(2, 13))
            print('The dice rolled', dice_roll)
            time.sleep(1)
            if p4_status == 'Apple':
                dice_roll += 3
                p4_status = ''
            elif p4_status == 'G-Apple':
                dice_roll += 6
                p4_status = ''
            elif p4_status == 'Pear':
                dice_roll -= 3
                p4_status = ''
            elif p4_status == 'G-Pear':
                dice_roll -= 6
                p4_status = ''
            elif p4_status == 'EX':
                ex_dice_roll = random.choice(range(1, 7))
                print('Extra die rolls', ex_dice_roll)
                dice_roll += ex_dice_roll
                p4_status = ''
                time.sleep(1)
            elif p4_status == 'Double':
                dice_roll *= 2
                p4_status = ''
            print('Player 4 moves', dice_roll, 'spaces!')
            player4pos += dice_roll
            time.sleep(1)
            print('Player 4 is now at space #',player4pos)
            time.sleep(2)
            double_meter4 = 0
        else:
            print("Can't use double roll.")
            time.sleep(2)
            P4DiceRoll()
    elif dice.lower() == 'item':
        if item_use == 1:
            print('Select your item:', p4_items)
            if players >= 4:
                item_select = input()
            else:
                item_select = random.choice(p4_items)
            if item_select.lower() == 'back':
                P4DiceRoll()
            elif item_select.lower() == 'plus apple':
                if p4_items[1] == 'Plus Apple' or p4_items[2] == 'Plus Apple' or p4_items[3] == 'Plus Apple':
                    print('Player 4 used the Plus Apple!')
                    time.sleep(2)
                    if p4_status == 'Pear':
                        print('The pear effect has been cancelled. They will roll normally.')
                        p4_status = ''
                    elif p4_status == 'G-Pear':
                        print('The Golden Pear effect has been halved. They will now go -3.')
                        p4_status = 'Pear'
                    else:
                        print("They'll move 3 extra spaces with this next roll!")
                        p4_status = 'Apple'
                    time.sleep(2)
                    if p4_items.index('Plus Apple') == 1:
                        p4_items[1] = ''
                    elif p4_items.index('Plus Apple') == 2:
                        p4_items[2] = ''
                    elif p4_items.index('Plus Apple') == 3:
                        p4_items[3] = ''
                    item_use = 0
                    P4DiceRoll()
                else:
                    print("You don't have a Plus Apple!")
                    time.sleep(2)
                    P4DiceRoll()
            elif item_select.lower() == 'golden plus apple':
                if p4_items[1] == 'Golden Plus Apple' or p4_items[2] == 'Golden Plus Apple' or p4_items[3] == 'Golden Plus Apple':
                    print('Player 4 used the Golden Plus Apple!')
                    time.sleep(2)
                    if p4_status == 'Pear':
                        print('The pear effect has been overridden. They will now move +3.')
                        p4_status = 'Apple'
                    elif p4_status == 'G-Pear':
                        print('The Golden Pear cancelled. They will roll normally.')
                        p4_status = ''
                    else:
                        print("They'll move 6 extra spaces with this next roll!")
                        p4_status = 'G-Apple'
                    time.sleep(2)
                    if p4_items.index('Golden Plus Apple') == 1:
                        p4_items[1] = ''
                    elif p4_items.index('Golden Plus Apple') == 2:
                        p4_items[2] = ''
                    elif p4_items.index('Golden Plus Apple') == 3:
                        p4_items[3] = ''
                    item_use = 0
                    P4DiceRoll()
                else:
                    print("You don't have a Golden Plus Apple!")
                    time.sleep(2)
                    P4DiceRoll()
            elif item_select.lower() == 'minus pear':
                if p4_items[1] == 'Minus Pear' or p4_items[2] == 'Minus Pear' or p4_items[3] == 'Minus Pear':
                    print('Player 4 used the Minus Pear!')
                    time.sleep(2)
                    if players >= 4:
                        print('Who would you like to use it on?')
                        print('1 / 2 / 3 / 4')
                        pear_effect = int(input())
                    else:
                        pear_effect = random.choice(range(1, 5))
                    if pear_effect == 1:
                        print('Player 4 used the Minus Pear on Player 1!')
                        if p1_status == 'Apple':
                            print('The apple effect has been cancelled. They will roll normally.')
                            p1_status = ''
                        elif p1_status == 'G-Apple':
                            print('The Golden Apple effect has been halved. They will now go +3.')
                            p1_status = 'Apple'
                        else:
                            print("They'll move 3 less spaces with this next roll!")
                            p1_status = 'Pear'
                    elif pear_effect == 2:
                        print('Player 4 used the Minus Pear on Player 2!')
                        if p2_status == 'Apple':
                            print('The apple effect has been cancelled. They will roll normally.')
                            p2_status = ''
                        elif p2_status == 'G-Apple':
                            print('The Golden Apple effect has been halved. They will now go +3.')
                            p2_status = 'Apple'
                        else:
                            print("They'll move 3 less spaces with this next roll!")
                            p2_status = 'Pear'
                    elif pear_effect == 3:
                        print('Player 4 used the Minus Pear on Player 3!')
                        if p3_status == 'Apple':
                            print('The apple effect has been cancelled. They will roll normally.')
                            p3_status = ''
                        elif p3_status == 'G-Apple':
                            print('The Golden Apple effect has been halved. They will now go +3.')
                            p3_status = 'Apple'
                        else:
                            print("They'll move 3 less spaces with this next roll!")
                            p3_status = 'Pear'
                    elif pear_effect == 4:
                        print('Player 4 used the Minus Pear on themselves!')
                        if p4_status == 'Apple':
                            print('The apple effect has been cancelled. They will roll normally.')
                            p4_status = ''
                        elif p4_status == 'G-Apple':
                            print('The Golden Apple effect has been halved. They will now go +3.')
                            p4_status = 'Apple'
                        else:
                            print("They'll move 3 less spaces with this next roll!")
                            p4_status = 'Pear'
                    else:
                        print('You ended up tossing the pear...')
                    time.sleep(2)
                    if p4_items.index('Minus Pear') == 1:
                        p4_items[1] = ''
                    elif p4_items.index('Minus Pear') == 2:
                        p4_items[2] = ''
                    elif p4_items.index('Minus Pear') == 3:
                        p4_items[3] = ''
                    item_use = 0
                    P4DiceRoll()
                else:
                    print("You don't have a Minus Pear!")
                    time.sleep(2)
                    P4DiceRoll()
            elif item_select.lower() == 'golden minus pear':
                if p4_items[1] == 'Golden Minus Pear' or p4_items[2] == 'Golden Minus Pear' or p4_items[3] == 'Golden Minus Pear':
                    print('Player 4 used the Golden Minus Pear!')
                    time.sleep(2)
                    if players >= 4:
                        print('Who would you like to use it on?')
                        print('1 / 2 / 3 / 4')
                        pear_effect = int(input())
                    else:
                        pear_effect = random.choice(range(1, 5))
                    if pear_effect == 1:
                        print('Player 4 used the Golden Minus Pear on Player 1!')
                        if p1_status == 'Apple':
                            print('The apple effect has been overridden. They now go -3.')
                            p1_status = 'Pear'
                        elif p1_status == 'G-Apple':
                            print('The Golden Apple effect has been cancelled. They will roll normally.')
                            p1_status = ''
                        else:
                            print("They'll move 6 less spaces with this next roll!")
                            p1_status = 'G-Pear'
                    elif pear_effect == 2:
                        print('Player 4 used the Golden Minus Pear on Player 2!')
                        if p2_status == 'Apple':
                            print('The apple effect has been overridden. They now go -3.')
                            p2_status = 'Pear'
                        elif p2_status == 'G-Apple':
                            print('The Golden Apple effect has been cancelled. They will roll normally.')
                            p2_status = ''
                        else:
                            print("They'll move 6 less spaces with this next roll!")
                            p2_status = 'G-Pear'
                    elif pear_effect == 3:
                        print('Player 4 used the Minus Pear on Player 3!')
                        if p3_status == 'Apple':
                            print('The apple effect has been overridden. They now go -3.')
                            p3_status = 'Pear'
                        elif p3_status == 'G-Apple':
                            print('The Golden Apple effect has been cancelled. They will roll normally.')
                            p3_status = ''
                        else:
                            print("They'll move 6 less spaces with this next roll!")
                            p3_status = 'G-Pear'
                    elif pear_effect == 4:
                        print('Player 4 used the Minus Pear on themselves!')
                        if p4_status == 'Apple':
                            print('The apple effect has been overridden. They now go -3.')
                            p4_status = 'Pear'
                        elif p4_status == 'G-Apple':
                            print('The Golden Apple effect has been cancelled. They will roll normally.')
                            p4_status = ''
                        else:
                            print("They'll move 6 less spaces with this next roll!")
                            p4_status = 'G-Pear'
                    else:
                        print('You ended up tossing the pear...')
                    time.sleep(2)
                    if p4_items.index('Golden Minus Pear') == 1:
                        p4_items[1] = ''
                    elif p4_items.index('Golden Minus Pear') == 2:
                        p4_items[2] = ''
                    elif p4_items.index('Golden Minus Pear') == 3:
                        p4_items[3] = ''
                    item_use = 0
                    P4DiceRoll()
                else:
                    print("You don't have a Golden Minus Pear!")
                    time.sleep(2)
                    P4DiceRoll()
            elif item_select.lower() == 'extra die':
                if p4_items[1] == 'Extra Die' or p4_items[2] == 'Extra Die' or p4_items[3] == 'Extra Die':
                    print('Player 4 used the Extra Die!')
                    time.sleep(2)
                    print("They'll gain an extra roll on this next turn!")
                    time.sleep(2)
                    p4_status = 'EX'
                    if p4_items.index('Extra Die') == 1:
                        p4_items[1] = ''
                    elif p4_items.index('Extra Die') == 2:
                        p4_items[2] = ''
                    elif p4_items.index('Extra Die') == 3:
                        p4_items[3] = ''
                    item_use = 0
                    P4DiceRoll()
                else:
                    print("You don't have an Extra Die!")
                    time.sleep(2)
                    P4DiceRoll()
            elif item_select.lower() == 'selection die':
                if p4_items[1] == 'Selection Die' or p4_items[2] == 'Selection Die' or p4_items[3] == 'Selection Die':
                    print('Player 4 used the Selection Die!')
                    time.sleep(2)
                    if players >= 4:
                        print("How many spaces do you want to move? (1-6)")
                        dice_roll = int(input())
                    else:
                        dice_roll = random.choice(range(1, 7))
                    print('The die rolled', dice_roll)
                    time.sleep(1)
                    if p4_status == 'Apple':
                        dice_roll += 3
                    elif p4_status == 'G-Apple':
                        dice_roll += 6
                    elif p4_status == 'Pear':
                        dice_roll -= 3
                    elif p4_status == 'G-Pear':
                        dice_roll -= 6
                    elif p4_status == 'EX':
                        ex_dice_roll = random.choice(range(1, 7))
                        print('Extra die rolls', ex_dice_roll)
                        dice_roll += ex_dice_roll
                        time.sleep(1)
                    elif p4_status == 'Double':
                        dice_roll *= 2
                    elif p4_status == 'Half':
                        dice_roll //= 2
                        p4_status = ''
                    print('Player 4 moves', dice_roll, 'spaces!')
                    player4pos += dice_roll
                    time.sleep(1)
                    print('Player 4 is now at space #',player4pos)
                    time.sleep(2)
                    if p4_items.index('Selection Die') == 1:
                        p4_items[1] = ''
                    elif p4_items.index('Selection Die') == 2:
                        p4_items[2] = ''
                    elif p4_items.index('Selection Die') == 3:
                        p4_items[3] = ''
                else:
                    print("You don't have a Selection Die!")
                    time.sleep(2)
                    item_use = 0
                    P4DiceRoll()
            elif item_select.lower() == 'swap box':
                if p4_items[1] == 'Swap Box' or p4_items[2] == 'Swap Box' or p4_items[3] == 'Swap Box':
                    print('Player 4 used the Swap Box!')
                    time.sleep(2)
                    swap = random.choice([1, 2, 3])
                    if swap == 1:
                        player1pos = player4pos
                        player4pos = savep1pos
                        print('Players 1 and 4 swapped places!')
                        time.sleep(1)
                        print('Player 1 is now at space #',player1pos)
                        time.sleep(1.5)
                        print('Player 4 is now at space #',player4pos)
                    if swap == 2:
                        player2pos = player4pos
                        player4pos = savep2pos
                        print('Players 2 and 4 swapped places!')
                        time.sleep(1)
                        print('Player 2 is now at space #',player2pos)
                        time.sleep(1.5)
                        print('Player 4 is now at space #',player4pos)
                    if swap == 3:
                        player3pos = player4pos
                        player4pos = savep3pos
                        print('Players 3 and 4 swapped places!')
                        time.sleep(1)
                        print('Player 3 is now at space #',player3pos)
                        time.sleep(1.5)
                        print('Player 4 is now at space #',player4pos)
                    if p4_items.index('Swap Box') == 1:
                        p4_items[1] = ''
                    elif p4_items.index('Swap Box') == 2:
                        p4_items[2] = ''
                    elif p4_items.index('Swap Box') == 3:
                        p4_items[3] = ''
                    item_use = 0
                    P4DiceRoll()
                else:
                    print("You don't have a Swap Box!")
                    time.sleep(2)
                    P4DiceRoll()
            elif item_select.lower() == 'great snake':
                if p4_items[1] == 'Great Snake' or p4_items[2] == 'Great Snake' or p4_items[3] == 'Great Snake':
                    print('Player 4 used the Great Snake!')
                    time.sleep(2)
                    g_snake = random.choice([1, 2, 3, 4])
                    if g_snake == 1:
                        print('Player 1 goes down 20 spaces!')
                        player1pos -= 20
                        if player1pos < 0:
                            while player1pos != 0:
                                player1pos += 1
                    if g_snake == 2:
                        print('Player 2 goes down 20 spaces!')
                        player2pos -= 20
                        if player2pos < 0:
                            while player2pos != 0:
                                player2pos += 1
                    if g_snake == 3:
                        print('Player 3 goes down 20 spaces!')
                        player3pos -= 20
                        if player3pos < 0:
                            while player3pos != 0:
                                player3pos += 1
                    if g_snake == 4:
                        print('Snake backfired!')
                        time.sleep(2)
                        print('Player 4 goes down 20 spaces!')
                        player4pos -= 20
                        if player4pos < 0:
                            while player4pos != 0:
                                player4pos += 1
                    if p4_items.index('Great Snake') == 1:
                        p4_items[1] = ''
                    elif p4_items.index('Great Snake') == 2:
                        p4_items[2] = ''
                    elif p4_items.index('Great Snake') == 3:
                        p4_items[3] = ''
                    item_use = 0
                    P4DiceRoll()
                else:
                    print("You don't have a Great Snake!")
                    time.sleep(2)
                    P4DiceRoll()
            elif item_select.lower() == 'god snake':
                if p4_items[1] == 'God Snake' or p4_items[2] == 'God Snake' or p4_items[3] == 'God Snake':
                    print('Player 4 used the God Snake!')
                    time.sleep(2)
                    g_snake = random.choice([1, 2, 3, 4])
                    if g_snake == 1:
                        print('Player 1 goes down to the beginning!')
                        player1pos = 0
                    if g_snake == 2:
                        print('Player 2 goes down to the beginning!')
                        player2pos = 0
                    if g_snake == 3:
                        print('Player 3 goes down to the beginning!')
                        player3pos = 0
                    if g_snake == 4:
                        print('Snake backfired!')
                        time.sleep(2)
                        print('Player 4 goes down to the beginning!')
                        player4pos = 0
                    if p4_items.index('God Snake') == 1:
                        p4_items[1] = ''
                    elif p4_items.index('God Snake') == 2:
                        p4_items[2] = ''
                    elif p4_items.index('God Snake') == 3:
                        p4_items[3] = ''
                    item_use = 0
                    P4DiceRoll()
                else:
                    print("You don't have a God Snake!")
                    time.sleep(2)
                    P4DiceRoll()
            elif item_select.lower() == 'double-or-nothing die':
                if p4_items[1] == 'Double-or-Nothing Die' or p4_items[2] == 'Double-or-Nothing Die' or p4_items[3] == 'Double-or-Nothing Die':
                    print('Player 4 used the Double-or-Nothing Die!')
                    time.sleep(2)
                    print("Take your chance! It's Double or Nothing!")
                    if players >= 4:
                        input('(Press Enter)')
                    dice_roll = random.choice(range(1, 7))
                    myst_die = random.choice(range(1, 7))
                    print('You rolled:', dice_roll)
                    time.sleep(1)
                    print('The die rolled:', myst_die)
                    time.sleep(2)
                    if dice_roll > myst_die:
                        print('Congratulations! Your next roll will be doubled!')
                        p4_status = 'Double'
                    else:
                        print('Oh... it all fell to nothing. Your next roll will be halved.')
                        p4_status = 'Half'
                    time.sleep(2)
                    if p4_items.index('Double-or-Nothing Die') == 1:
                        p4_items[1] = ''
                    elif p4_items.index('Double-or-Nothing Die') == 2:
                        p4_items[2] = ''
                    elif p4_items.index('Double-or-Nothing Die') == 3:
                        p4_items[3] = ''
                    item_use = 0
                    P4DiceRoll()
                else:
                    print("You don't have a Double-or-Nothing Die!")
                    time.sleep(2)
                    P4DiceRoll()
            elif item_select.lower() == 'magic ladder':
                if p4_items[1] == 'Magic Ladder' or p4_items[2] == 'Magic Ladder' or p4_items[3] == 'Magic Ladder':
                    print('Player 4 used the Magic Ladder!')
                    time.sleep(2)
                    mag_ladder = random.choice(range(5, 16))
                    print('The ladder took Player 4 up', mag_ladder, 'spaces!')
                    player4pos += mag_ladder
                    time.sleep(2)
                    if p4_items.index('Magic Ladder') == 1:
                        p4_items[1] = ''
                    elif p4_items.index('Magic Ladder') == 2:
                        p4_items[2] = ''
                    elif p4_items.index('Magic Ladder') == 3:
                        p4_items[3] = ''
                    item_use = 0
                    if player4pos in snakes:
                        print('Uh-oh! You landed on a snake!')
                        time.sleep(2)
                        signal = 4
                        snake()
                    elif player4pos in ladders:
                        print('Woo-hoo! You landed on a ladder!')
                        time.sleep(2)
                        signal = 4
                        ladder()
                    if player4pos > goal:
                        print('Ooh... you overshot that one!')
                        player4pos -= dice_roll
                        time.sleep(2)
                    else:
                        P4DiceRoll()
                else:
                    print("You don't have a Magic Ladder!")
                    time.sleep(2)
                    P4DiceRoll()
            elif item_select.lower() == 'ultimate fate':
                if p4_items[1] == 'Ultimate Fate' or p4_items[2] == 'Ultimate Fate' or p4_items[3] == 'Ultimate Fate':
                    print('Player 4 used the Ultimate Fate!')
                    time.sleep(2)
                    print("One dice roll decides everyone's fate!")
                    if players >= 4:
                        input('(Press enter to decide fate)')
                    dice_roll = random.choice(range(1, 7))
                    print('The dice rolls', dice_roll, end = '')
                    print(". Your fate reads...")
                    time.sleep(2)
                    if dice_roll == 1:
                        print('Everyone must return to the beginning!')
                        time.sleep(2)
                        player1pos = 0
                        player2pos = 0
                        player3pos = 0
                        player4pos = 0
                    elif dice_roll == 2:
                        print('Everyone gets the effects of the Golden Minus Pear!')
                        time.sleep(2)
                        p1_status = 'G-Pear'
                        p2_status = 'G-Pear'
                        p3_status = 'G-Pear'
                        p4_status = 'G-Pear'
                    elif dice_roll == 3:
                        print('Everyone gets infected with the Plus Apple!')
                        time.sleep(2)
                        p1_status = 'Apple'
                        p2_status = 'Apple'
                        p3_status = 'Apple'
                        p4_status = 'Apple'
                    elif dice_roll == 4:
                        print('Everyone gets their locations rearranged!')
                        time.sleep(2)
                        player1pos = random.choice([savep2pos, savep3pos, savep4pos])
                        player2pos = random.choice([savep1pos, savep3pos, savep4pos])
                        player3pos = random.choice([savep2pos, savep1pos, savep4pos])
                        player4pos = random.choice([savep2pos, savep3pos, savep1pos])
                        print('Player 1 is now at space #',player1pos)
                        time.sleep(1)
                        print('Player 2 is now at space #',player2pos)
                        time.sleep(1)
                        print('Player 3 is now at space #',player3pos)
                        time.sleep(1)
                        print('Player 4 is now at space #',player4pos)
                        time.sleep(2)
                    elif dice_roll == 5:
                        print('Everyone gets the effects of the Minus Pear!')
                        time.sleep(2)
                        p1_status = 'Pear'
                        p2_status = 'Pear'
                        p3_status = 'Pear'
                        p4_status = 'Pear'
                    elif dice_roll == 6:
                        print('Everyone gets the effects of the Golden Plus Apple!')
                        time.sleep(2)
                        p1_status = 'G-Apple'
                        p2_status = 'G-Apple'
                        p3_status = 'G-Apple'
                        p4_status = 'G-Apple'
                    time.sleep(2)
                    if p4_items.index('Ultimate Fate') == 1:
                        p4_items[1] = ''
                    elif p4_items.index('Ultimate Fate') == 2:
                        p4_items[2] = ''
                    elif p4_items.index('Ultimate Fate') == 3:
                        p4_items[3] = ''
                    item_use = 0
                    P4DiceRoll()
                else:
                    print("You don't have an Ultimate Fate!")
                    time.sleep(2)
                    P4DiceRoll()
            else:
                P4DiceRoll()
    else:
        print("We didn't get that... Try Again!")
        time.sleep(2)
        P4DiceRoll()
    if player4pos in snakes:
        print('Uh-oh! You landed on a snake!')
        time.sleep(2)
        signal = 4
        snake()
    elif player4pos in ladders:
        print('Woo-hoo! You landed on a ladder!')
        time.sleep(2)
        signal = 4
        ladder()
    if player4pos > goal:
        print('Ooh... you overshot that one!')
        player4pos -= dice_roll
        time.sleep(2)
    savep4pos = player4pos
    endCheck()
    item_use = 1
    if item_fix == 1:
        item_roll = random.choice(range(1, 101))
        if item_roll <= item_chance:
            print('Whoa! You get to play an item game!')
            time.sleep(2)
            if players >= 4:
                left_or_right = input('Left or Right?: ')
            else:
                left_or_right = random.choice(['Left', 'Right'])
            if left_or_right.lower() == 'left':
                item_get = random.choice(['Plus Apple', 'Minus Pear', 'Golden Plus Apple', 'Golden Minus Pear', 'Selection Die', 'Extra Die'])
                print('You recieved:', item_get)
                if p4_items[1] == '':
                    p4_items[1] = item_get
                elif p4_items[2] == '':
                    p4_items[2] = item_get
                elif p4_items[3] == '':
                    p4_items[3] = item_get
                else:
                    print('Uh oh! No more room!')
                    time.sleep(1)
                    if players >= 4:
                        print('Which item slot do you want to replace?')
                        print(p4_items)
                        print('1, 2, or 3 (input anything else to toss item)')
                        item_replace = int(input())
                    else:
                        item_replace = random.choice(range(1, 4))
                    if item_replace == 1:
                        print('Goodbye,', p4_items[1])
                        time.sleep(1)
                        p4_items[1] = item_get
                        print('Hello,', p4_items[1])
                    elif item_replace == 2:
                        print('Goodbye,', p4_items[2])
                        time.sleep(1)
                        p4_items[2] = item_get
                        print('Hello,', p4_items[2])
                    elif item_replace == 3:
                        print('Goodbye,', p4_items[3])
                        time.sleep(1)
                        p4_items[3] = item_get
                        print('Hello,', p4_items[3])
                    else:
                        print('You threw the', item_get, 'away!')
            elif left_or_right.lower() == 'right':
                item_get = random.choice(['Swap Box', 'Great Snake', 'God Snake', 'Double-or-Nothing Die', 'Magic Ladder', 'Ultimate Fate'])
                print('You recieved:', item_get)
                if p4_items[1] == '':
                    p4_items[1] = item_get
                elif p4_items[2] == '':
                    p4_items[2] = item_get
                elif p4_items[3] == '':
                    p4_items[3] = item_get
                else:
                    print('Uh oh! No more room!')
                    time.sleep(1)
                    if players >= 4:
                        print('Which item slot do you want to replace?')
                        print(p4_items)
                        print('1, 2, or 3 (input anything else to toss item)')
                        item_replace = int(input())
                    else:
                        item_replace = random.choice(range(1, 4))
                    if item_replace == 1:
                        print('Goodbye,', p4_items[1])
                        time.sleep(1)
                        p4_items[1] = item_get
                        print('Hello,', p4_items[1])
                    elif item_replace == 2:
                        print('Goodbye,', p4_items[2])
                        time.sleep(1)
                        p4_items[2] = item_get
                        print('Hello,', p4_items[2])
                    elif item_replace == 3:
                        print('Goodbye,', p4_items[3])
                        time.sleep(1)
                        p4_items[3] = item_get
                        print('Hello,', p4_items[3])
                    else:
                        print('You threw the', item_get, 'away!')
            else:
                item_get = random.choice(['Plus Apple', 'Minus Pear', 'Golden Plus Apple', 'Golden Minus Pear', 'Selection Die', 'Extra Die', 'Swap Box', 'Great Snake', 'God Snake', 'Double-or-Nothing Die', 'Magic Ladder', 'Ultimate Fate'])
                print('You recieved:', item_get)
                if p4_items[1] == '':
                    p4_items[1] = item_get
                elif p4_items[2] == '':
                    p4_items[2] = item_get
                elif p4_items[3] == '':
                    p4_items[3] = item_get
                else:
                    print('Uh oh! No more room!')
                    time.sleep(1)
                    if players >= 4:
                        print('Which item slot do you want to replace?')
                        print(p4_items)
                        print('1, 2, or 3 (input anything else to toss item)')
                        item_replace = int(input())
                    else:
                        item_replace = random.choice(range(1, 4))
                    if item_replace == 1:
                        print('Goodbye,', p4_items[1])
                        time.sleep(1)
                        p4_items[1] = item_get
                        print('Hello,', p4_items[1])
                    elif item_replace == 2:
                        print('Goodbye,', p4_items[2])
                        time.sleep(1)
                        p4_items[2] = item_get
                        print('Hello,', p4_items[2])
                    elif item_replace == 3:
                        print('Goodbye,', p4_items[3])
                        time.sleep(1)
                        p4_items[3] = item_get
                        print('Hello,', p4_items[3])
                    else:
                        print('You threw the', item_get, 'away!')
            item_fix = 0
            if player4pos < 0:
                while player4pos != 0:
                    player4pos += 1
            time.sleep(2)
    print('')

def preGame():
    playerCount()
    turnOrder()
    for i in range(100):    
        turnRollAgain()
    finalOrder()
    boardSelect()

def boardSelect():
    global board
    global snakes
    global ladders
    board = random.choice(range(1, 4))
    if board == 1:
        snakes = [17, 54, 62, 64, 87, 93, 94, 98]
        ladders = [1, 4, 9, 21, 28, 51, 72, 80]
    elif board == 2:
        snakes = [27, 40, 43, 54, 66, 76, 89, 99]
        ladders = [4, 13, 33, 42, 50, 62, 74]
    elif board == 3:
        snakes = [33, 41, 49, 56, 62, 87, 93, 95, 98]
        ladders = [2, 10, 27, 51, 61, 65, 71, 81]
    print('Board Selected: Board', board)
    time.sleep(1)
    print('')
    
def moveTurns():
    global p1turnroll
    global p2turnroll
    global p3turnroll
    global p4turnroll
    global turns
    global game
    
    if max(turns) == p1turnroll:
        if game == 1:
            P1DiceRoll()
        time.sleep(2)
        #Second
        if turns[1] == p2turnroll:
            if game == 1:
                P2DiceRoll()
        elif turns[1] == p3turnroll:
            if game == 1:
                P3DiceRoll()
        elif turns[1] == p4turnroll:
            if game == 1:
                P4DiceRoll()
        time.sleep(2)
        #Third
        if turns[2] == p2turnroll:
            if game == 1:
                P2DiceRoll()
        elif turns[2] == p3turnroll:
            if game == 1:
                P3DiceRoll()
        elif turns[2] == p4turnroll:
            if game == 1:
                P4DiceRoll()
        time.sleep(2)
        #Fourth
        if turns[3] == p2turnroll:
            if game == 1:
                P2DiceRoll()
        elif turns[3] == p3turnroll:
            if game == 1:
                P3DiceRoll()
        elif turns[3] == p4turnroll:
            if game == 1:
                P4DiceRoll()
        time.sleep(2)
    elif max(turns) == p2turnroll:
        if game == 1:
            P2DiceRoll()
        #Second
        if turns[1] == p1turnroll:
            if game == 1:
                P1DiceRoll()
        elif turns[1] == p3turnroll:
            if game == 1:
                P3DiceRoll()
        elif turns[1] == p4turnroll:
            if game == 1:
                P4DiceRoll()
        time.sleep(2)
        #Third
        if turns[2] == p1turnroll:
            if game == 1:
                P1DiceRoll()
        elif turns[2] == p3turnroll:
            if game == 1:
                P3DiceRoll()
        elif turns[2] == p4turnroll:
            if game == 1:
                P4DiceRoll()
        time.sleep(2)
        #Fourth
        if turns[3] == p1turnroll:
            if game == 1:
                P1DiceRoll()
        elif turns[3] == p3turnroll:
            if game == 1:
                P3DiceRoll()
        elif turns[3] == p4turnroll:
            if game == 1:
                P4DiceRoll()
        time.sleep(2)
    elif max(turns) == p3turnroll:
        if game == 1:
            P3DiceRoll()
        time.sleep(2)
        #Second
        if turns[1] == p1turnroll:
            if game == 1:
                P1DiceRoll()
        elif turns[1] == p2turnroll:
            if game == 1:
                P2DiceRoll()
        elif turns[1] == p4turnroll:
            if game == 1:
                P4DiceRoll()
        time.sleep(2)
        #Third
        if turns[2] == p1turnroll:
            if game == 1:
                P1DiceRoll()
        elif turns[2] == p2turnroll:
            if game == 1:
                P2DiceRoll()
        elif turns[2] == p4turnroll:
            if game == 1:
                P4DiceRoll()
        time.sleep(2)
        #Fourth
        if turns[3] == p1turnroll:
            if game == 1:
                P1DiceRoll()
        elif turns[3] == p2turnroll:
            if game == 1:
                P2DiceRoll()
        elif turns[3] == p4turnroll:
            if game == 1:
                P4DiceRoll()
        time.sleep(2)
    elif max(turns) == p4turnroll:
        if game == 1:    
            P4DiceRoll()
        time.sleep(2)
        #Second
        if turns[1] == p1turnroll:
            if game == 1:
                P1DiceRoll()
        elif turns[1] == p2turnroll:
            if game == 1:
                P2DiceRoll()
        elif turns[1] == p3turnroll:
            if game == 1:
                P3DiceRoll()
        time.sleep(2)
        #Third
        if turns[2] == p1turnroll:
            if game == 1:
                P1DiceRoll()
        elif turns[2] == p2turnroll:
            if game == 1:
                P2DiceRoll()
        elif turns[2] == p3turnroll:
            if game == 1:
                P3DiceRoll()
        time.sleep(2)
        #Fourth
        if turns[3] == p1turnroll:
            if game == 1:
                P1DiceRoll()
        elif turns[3] == p2turnroll:
            if game == 1:
                P2DiceRoll()
        elif turns[3] == p3turnroll:
            if game == 1:
                P3DiceRoll()
        time.sleep(2)

def snake():
    global board
    if board == 1:
        board1snake()
    elif board == 2:
        board2snake()
    elif board == 3:
        board3snake()

def ladder():
    global board
    if board == 1:
        board1ladder()
    elif board == 2:
        board2ladder()
    elif board == 3:
        board3ladder()
        
def board1snake():
    global signal
    global player1pos
    global player2pos
    global player3pos
    global player4pos
    if signal == 1:
        if player1pos == 17:
            player1pos = 7
        elif player1pos == 54:
            player1pos = 34
        elif player1pos == 62:
            player1pos = 19
        elif player1pos == 64:
            player1pos = 60
        elif player1pos == 87:
            player1pos = 36
        elif player1pos == 93:
            player1pos = 73
        elif player1pos == 94:
            player1pos = 75
        elif player1pos == 98:
            player1pos = 79
        print('You are now at space #', player1pos)
    elif signal == 2:
        if player2pos == 17:
            player2pos = 7
        elif player2pos == 54:
            player2pos = 34
        elif player2pos == 62:
            player2pos = 19
        elif player2pos == 64:
            player2pos = 60
        elif player2pos == 87:
            player2pos = 36
        elif player2pos == 93:
            player2pos = 73
        elif player2pos == 94:
            player2pos = 75
        elif player2pos == 98:
            player2pos = 79
        print('You are now at space #', player2pos)
    elif signal == 3:
        if player3pos == 17:
            player3pos = 7
        elif player3pos == 54:
            player3pos = 34
        elif player3pos == 62:
            player3pos = 19
        elif player3pos == 64:
            player3pos = 60
        elif player3pos == 87:
            player3pos = 36
        elif player3pos == 93:
            player3pos = 73
        elif player3pos == 94:
            player3pos = 75
        elif player3pos == 98:
            player3pos = 79
        print('You are now at space #', player3pos)
    elif signal == 4:
        if player4pos == 17:
            player4pos = 7
        elif player4pos == 54:
            player4pos = 34
        elif player4pos == 62:
            player4pos = 19
        elif player4pos == 64:
            player4pos = 60
        elif player4pos == 87:
            player4pos = 36
        elif player4pos == 93:
            player4pos = 73
        elif player4pos == 94:
            player4pos = 75
        elif player4pos == 98:
            player4pos = 79
        print('You are now at space #', player4pos)
    time.sleep(2)
            
def board1ladder():
    global signal
    global player1pos
    global player2pos
    global player3pos
    global player4pos
    if signal == 1:
        if player1pos == 1:
            player1pos = 38
        elif player1pos == 4:
            player1pos = 14
        elif player1pos == 9:
            player1pos = 31
        elif player1pos == 21:
            player1pos = 42
        elif player1pos == 28:
            player1pos = 84
        elif player1pos == 51:
            player1pos = 67
        elif player1pos == 72:
            player1pos = 91
        elif player1pos == 80:
            player1pos = 99
        print('You are now at space #', player1pos)
    elif signal == 2:
        if player2pos == 1:
            player2pos = 38
        elif player2pos == 4:
            player2pos = 14
        elif player2pos == 9:
            player2pos = 31
        elif player2pos == 21:
            player2pos = 42
        elif player2pos == 28:
            player2pos = 84
        elif player2pos == 51:
            player2pos = 67
        elif player2pos == 72:
            player2pos = 91
        elif player2pos == 80:
            player2pos = 99
        print('You are now at space #', player2pos)
    elif signal == 3:
        if player3pos == 1:
            player3pos = 38
        elif player3pos == 4:
            player3pos = 14
        elif player3pos == 9:
            player3pos = 31
        elif player3pos == 21:
            player3pos = 42
        elif player3pos == 28:
            player3pos = 84
        elif player3pos == 51:
            player3pos = 67
        elif player3pos == 72:
            player3pos = 91
        elif player3pos == 80:
            player3pos = 99
        print('You are now at space #', player3pos)
    elif signal == 4:
        if player4pos == 1:
            player4pos = 38
        elif player4pos == 4:
            player4pos = 14
        elif player4pos == 9:
            player4pos = 31
        elif player4pos == 21:
            player4pos = 42
        elif player4pos == 28:
            player4pos = 84
        elif player4pos == 51:
            player4pos = 67
        elif player4pos == 72:
            player4pos = 91
        elif player4pos == 80:
            player4pos = 99
        print('You are now at space #', player4pos)
    time.sleep(2)
    
def board2snake():
    global signal
    global player1pos
    global player2pos
    global player3pos
    global player4pos
    if signal == 1:
        if player1pos == 27:
            player1pos = 5
        elif player1pos == 40:
            player1pos = 3
        elif player1pos == 43:
            player1pos = 18
        elif player1pos == 54:
            player1pos = 31
        elif player1pos == 66:
            player1pos = 45
        elif player1pos == 76:
            player1pos = 58
        elif player1pos == 89:
            player1pos = 53
        elif player1pos == 99:
            player1pos = 41
        print('You are now at space #', player1pos)
    elif signal == 2:
        if player2pos == 27:
            player2pos = 5
        elif player2pos == 40:
            player2pos = 3
        elif player2pos == 43:
            player2pos = 18
        elif player2pos == 54:
            player2pos = 31
        elif player2pos == 66:
            player2pos = 45
        elif player2pos == 76:
            player2pos = 58
        elif player2pos == 89:
            player2pos = 53
        elif player2pos == 99:
            player2pos = 41
        print('You are now at space #', player2pos)
    elif signal == 3:
        if player3pos == 27:
            player3pos = 5
        elif player3pos == 40:
            player3pos = 3
        elif player3pos == 43:
            player3pos = 18
        elif player3pos == 54:
            player3pos = 31
        elif player3pos == 66:
            player3pos = 45
        elif player3pos == 76:
            player3pos = 58
        elif player3pos == 89:
            player3pos = 53
        elif player3pos == 99:
            player3pos = 41
        print('You are now at space #', player3pos)
    elif signal == 4:
        if player4pos == 27:
            player4pos = 5
        elif player4pos == 40:
            player4pos = 3
        elif player4pos == 43:
            player4pos = 18
        elif player4pos == 54:
            player4pos = 31
        elif player4pos == 66:
            player4pos = 45
        elif player4pos == 76:
            player4pos = 58
        elif player4pos == 89:
            player4pos = 53
        elif player4pos == 99:
            player4pos = 41
        print('You are now at space #', player4pos)
    time.sleep(2)
            
def board2ladder():
    global signal
    global player1pos
    global player2pos
    global player3pos
    global player4pos
    if signal == 1:
        if player1pos == 4:
            player1pos = 25
        elif player1pos == 13:
            player1pos = 46
        elif player1pos == 33:
            player1pos = 49
        elif player1pos == 42:
            player1pos = 63
        elif player1pos == 50:
            player1pos = 69
        elif player1pos == 62:
            player1pos = 81
        elif player1pos == 74:
            player1pos = 92
        print('You are now at space #', player1pos)
    elif signal == 2:
        if player2pos == 4:
            player2pos = 25
        elif player2pos == 13:
            player2pos = 46
        elif player2pos == 33:
            player2pos = 49
        elif player2pos == 42:
            player2pos = 63
        elif player2pos == 50:
            player2pos = 69
        elif player2pos == 62:
            player2pos = 81
        elif player2pos == 74:
            player2pos = 92
        print('You are now at space #', player2pos)
    elif signal == 3:
        if player3pos == 4:
            player3pos = 25
        elif player3pos == 13:
            player3pos = 46
        elif player3pos == 33:
            player3pos = 49
        elif player3pos == 42:
            player3pos = 63
        elif player3pos == 50:
            player3pos = 69
        elif player3pos == 62:
            player3pos = 81
        elif player3pos == 74:
            player3pos = 92
        print('You are now at space #', player3pos)
    elif signal == 4:
        if player4pos == 4:
            player4pos = 25
        elif player4pos == 13:
            player4pos = 46
        elif player4pos == 33:
            player4pos = 49
        elif player4pos == 42:
            player4pos = 63
        elif player4pos == 50:
            player4pos = 69
        elif player4pos == 62:
            player4pos = 81
        elif player4pos == 74:
            player4pos = 92
        print('You are now at space #', player4pos)
    time.sleep(2)
    
def board3snake():
    global signal
    global player1pos
    global player2pos
    global player3pos
    global player4pos
    if signal == 1:
        if player1pos == 33:
            player1pos = 6
        elif player1pos == 41:
            player1pos = 20
        elif player1pos == 49:
            player1pos = 9
        elif player1pos == 56:
            player1pos = 53
        elif player1pos == 62:
            player1pos = 5
        elif player1pos == 87:
            player1pos = 16
        elif player1pos == 93:
            player1pos = 73
        elif player1pos == 95:
            player1pos = 75
        elif player1pos == 98:
            player1pos = 64
        print('You are now at space #', player1pos)
    elif signal == 2:
        if player2pos == 33:
            player2pos = 6
        elif player2pos == 41:
            player2pos = 20
        elif player2pos == 49:
            player2pos = 9
        elif player1pos == 56:
            player2pos = 53
        elif player2pos == 62:
            player2pos = 5
        elif player2pos == 87:
            player2pos = 16
        elif player2pos == 93:
            player2pos = 73
        elif player2pos == 95:
            player2pos = 75
        elif player2pos == 98:
            player2pos = 64
        print('You are now at space #', player2pos)
    elif signal == 3:
        if player3pos == 33:
            player3pos = 6
        elif player3pos == 41:
            player3pos = 20
        elif player3pos == 49:
            player3pos = 9
        elif player1pos == 56:
            player3pos = 53
        elif player3pos == 62:
            player3pos = 5
        elif player3pos == 87:
            player3pos = 16
        elif player3pos == 93:
            player3pos = 73
        elif player3pos == 95:
            player3pos = 75
        elif player3pos == 98:
            player3pos = 64
        print('You are now at space #', player3pos)
    elif signal == 4:
        if player4pos == 33:
            player4pos = 6
        elif player4pos == 41:
            player4pos = 20
        elif player4pos == 49:
            player4pos = 9
        elif player1pos == 56:
            player4pos = 53
        elif player4pos == 62:
            player4pos = 5
        elif player4pos == 87:
            player4pos = 16
        elif player4pos == 93:
            player4pos = 73
        elif player4pos == 95:
            player4pos = 75
        elif player4pos == 98:
            player4pos = 64
        print('You are now at space #', player4pos)
    time.sleep(2)
            
def board3ladder():
    global signal
    global player1pos
    global player2pos
    global player3pos
    global player4pos
    if signal == 1:
        if player1pos == 2:
            player1pos = 37
        elif player1pos == 10:
            player1pos = 32
        elif player1pos == 27:
            player1pos = 46
        elif player1pos == 51:
            player1pos = 68
        elif player1pos == 61:
            player1pos = 79
        elif player1pos == 65:
            player1pos = 84
        elif player1pos == 71:
            player1pos = 91
        elif player1pos == 81:
            player1pos = 100
        print('You are now at space #', player1pos)
    elif signal == 2:
        if player2pos == 2:
            player2pos = 37
        elif player2pos == 10:
            player2pos = 32
        elif player2pos == 27:
            player2pos = 46
        elif player2pos == 51:
            player2pos = 68
        elif player2pos == 61:
            player2pos = 79
        elif player2pos == 65:
            player2pos = 84
        elif player2pos == 71:
            player2pos = 91
        elif player2pos == 81:
            player2pos = 100
        print('You are now at space #', player2pos)
    elif signal == 3:
        if player3pos == 2:
            player3pos = 37
        elif player3pos == 10:
            player3pos = 32
        elif player3pos == 27:
            player3pos = 46
        elif player3pos == 51:
            player3pos = 68
        elif player3pos == 61:
            player3pos = 79
        elif player3pos == 65:
            player3pos = 84
        elif player3pos == 71:
            player3pos = 91
        elif player3pos == 81:
            player3pos = 100
        print('You are now at space #', player3pos)
    elif signal == 4:
        if player4pos == 2:
            player4pos = 37
        elif player4pos == 10:
            player4pos = 32
        elif player4pos == 27:
            player4pos = 46
        elif player4pos == 51:
            player4pos = 68
        elif player4pos == 61:
            player4pos = 79
        elif player4pos == 65:
            player4pos = 84
        elif player4pos == 71:
            player4pos = 91
        elif player4pos == 81:
            player4pos = 100
        print('You are now at space #', player4pos)
    time.sleep(2)
    
def mainGame():
    global player1pos
    global player2pos
    global player3pos
    global player4pos
    global players
    global game
    while game == 1:
        moveTurns()
    
def endCheck():	
    global game
    global player1pos
    global player2pos
    global player3pos
    global player4pos
    if player1pos == 100:
        print('Congratulations Player 1! You Win!')
        time.sleep(5)
        game = 0
    elif player2pos == 100:
        print('Congratulations Player 2! You Win!')
        time.sleep(5)
        game = 0
    elif player3pos == 100:
        print('Congratulations Player 3! You Win!')
        time.sleep(5)
        game = 0
    elif player4pos == 100:
        print('Congratulations Player 4! You Win!')
        time.sleep(5)
        game = 0

def postGame():
    print('')
    print('Subscribe to Burgess Be Gaming for more Python games!')
    print('This game took me weeks to develop, and I plan to release updates as time goes on!')
    print('Hope you enjoyed the game! Open the file to play again!')
    time.sleep(3)
    input('                 Press Enter to Exit Game               ')

def main():
    titleScreen()
    preGame()
    mainGame()
    postGame()
    
if __name__ == "__main__":
    main()