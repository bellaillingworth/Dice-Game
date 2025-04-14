"""
This is a simulation dice game, two players start with a set amount of
money and take turns rolling a custom die. Rolls of 1–3 reduce a player's funds,
while rolls of 4–6 let them take money from their opponent.
The game continues until one player runs out of funds.

Group 15
Bella Illingworth, Drew Hansen, Nikko Higgins, Ryan DiGiallonardo
"""

import random

# take the inputs from the user
starting_player1 = float(input('Starting amount for Player 1: $'))
starting_player2 = float(input('Starting amount for Player 2: $'))
reps = int(input('Number of replications: '))

while reps < 1000 or reps > 10000:
    print("Make sure the number of replications is in between 1000 and 10000")
    reps = int(input('Number of replications: '))

while True:
    # Verify that the user input is correct and produce the dice probabilities
    prob = input("Dice probabilities: ")
    if prob.lower() == 'fair':
        dice_probabilities = [1/6] * 6
        break
    else:
        count = 0
        dice_probabilities = prob.split(',')
        for i in range(6): #checking the probabilities for uniform dice
            dice_probabilities[i] = float(dice_probabilities[i])
            count = count + dice_probabilities[i]
        if count != 1:
            print("Make sure dice probablities add up to one!")
            continue
        else:
            break

#variables for collectiong statistic     
dice = [1,2,3,4,5,6]
p1_avg_max = 0
p2_avg_max = 0
p1_avg_ending = 0
p2_avg_ending = 0
p1_wins = 0
p2_wins = 0

for i in range(reps):
    rounds_count = 0
    player1_earn = starting_player1
    player2_earn = starting_player2
    p1_max = starting_player1
    p2_max = starting_player2
    while player1_earn > 0 and player2_earn > 0:
        player1_diff = 0
    #player1 turn
        player1_roll = random.choices(dice, weights= dice_probabilities, k=1)
        player1_roll = player1_roll[0]    
        player1_diff = 0
    #player2 turn
        player2_roll = random.choices(dice, weights= dice_probabilities, k=1)
        player2_roll = player2_roll[0]    
        player2_diff = 0
        
    #if roll 1, 2 , or 3                    
        if player1_roll <= 3:
            player1_diff = -1 * player1_roll
        else:
            player1_diff = player1_roll
            
        if player2_roll <= 3:
            player2_diff = -1 * player2_roll
        else:
            player2_diff = player2_roll
                                
    #if roll 4, 5, or 6                            
        if player1_roll >= 4:
            player1_diff = min(player2_earn, player1_roll-3)
        if player2_roll >= 4:
            player2_diff = min(player1_earn, player2_roll-3)
            
    #calculating the amount of money each player earns each game     
        player1_earn = player1_earn + player1_diff
        player2_earn = player2_earn + player2_diff
    #finding the max amount for each game
        p1_max = max(p1_max, player1_earn)
        p2_max = max(p2_max, player2_earn)
        rounds_count += 1 #counting rounds for each game
        
   #collect the wins for each player
    if player1_earn > 0:
        p1_wins += 1
        
    if player2_earn > 0:
        p2_wins += 1
        
   #adding up the sum numbers for calculating the average
    p1_avg_max += p1_max
    p2_avg_max += p2_max
    p1_avg_ending += player1_earn
    p2_avg_ending += player2_earn
    
#final calculations          
average1 = p1_avg_ending/reps
average2 = p2_avg_ending/reps

p1_avg_max = p1_avg_max / reps
p2_avg_max = p2_avg_max / reps

p1_win_pct = p1_wins / reps
p2_win_pct = p2_wins / reps

avg_rounds = reps / rounds_count

#Display the results
print(f'Average ending amount for Player 1 : ${average1:.2f}')
print(f'Average ending amount for Player 2 : ${average2:.2f}')

print(f'Average highest amount that Player 1 achives: ${p1_avg_max:.2f}')
print(f'Average highest amount that Player 2 achives: ${p2_avg_max:.2f}')

print(f'Probability that Player 1 wins a game: {p1_win_pct * 100:.2f}%')
print(f'Probability that Player 2 wins a game: {p2_win_pct * 100:.2f}%')

print(f'Average nunber of rounds per game: {avg_rounds:.2f}')

        
