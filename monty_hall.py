import random

switch_wins = 0
stay_wins = 0

for i in range(10000):
    doors = [1,2,3]

    #player picks a door at random
    picked_door = random.choice(doors)
    #prize door is selected at random 
    prize_door = random.choice(doors)

    #goat doors are set from the remaining doors
    goat_doors = [d for d in doors if d is not prize_door]


    for door in goat_doors:
        if door is not picked_door:
            #remove one of the goat doors (if the chosen door is a goat door, it removes the other one)
            doors.remove(door)
            break

    #makes a second pick between a goat door and the prize door also at random
    second_pick = random.choice(doors)

    #second pick different from picked door meaning switch
    if second_pick != picked_door:
        if second_pick == prize_door:
            switch_wins += 1
            continue
        stay_wins += 1
        continue
    if second_pick == prize_door:
        stay_wins += 1
        continue
    switch_wins += 1
    continue


print("stay: {}\nswitch: {}".format(stay_wins,switch_wins))


