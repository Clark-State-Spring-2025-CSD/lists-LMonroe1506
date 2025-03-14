#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = [5,7,2,9,1,1,3,8,6,9]
#Player Two = [3,8,5,5,8,1,4,7,4,7]
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

import random

player_one = [random.randint(1,50) for i in range(10)]
player_two = [random.randint(1,50) for i in range(10)]

player_one_wins = 0
player_two_wins = 0

for p1, p2 in zip(player_one, player_two):
    if p1 > p2:
        player_one_wins += 1
    elif p2 > p1:
        player_two_wins += 1

player_one_highest = max(player_one)
player_one_highest_index = player_one.index(player_one_highest)
player_one_lowest = min(player_one)
player_one_lowest_index = player_one.index(player_one_lowest)

player_two_highest = max(player_two)
player_two_highest_index = player_two.index(player_two_highest)
player_two_lowest = min(player_two)
player_two_lowest_index = player_two.index(player_two_lowest)

print(f"Player One = {player_one}")
print(f"Player Two = {player_two}")

print(f"Player one won {player_one_wins} times")
print(f"Player two won {player_two_wins} times")
print(f"Player one's highest number is {player_one_highest} at index {player_one_highest_index}")
print(f"Player two's highest number is {player_two_highest} at index {player_two_highest_index}")
print(f"Player one's lowest number is {player_one_lowest} at index {player_one_lowest_index}")
print(f"Player two's lowest number is {player_two_lowest} at index {player_two_lowest_index}")