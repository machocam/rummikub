#------------------------------------
#Author : Rodrigo Camacho 
#Twitter: @mixcocam  -> contact me there if you have something to say

#DESCRIPTION:
##This program minimizes (using heuristics) the number of points that a given player is left with at the end of a game of rummikub. It, in turn, helps the player to win the game. Since there is no "emotional" content to this game, this program could essentially play instead of the human.

#------------------------------------

#Every chip on the either the board, or the table is going to be an entery in an array within an array that will contain them all.
#The wild cards are going to be given a number = 0. An exception of this case is going to have to be made in all logic.

from operator import itemgetter
import random

chips = [
    [3, "blue"],
    [4, "blue"],
    [5, "blue"],
    [6, "blue"],
    [3, "red"],
    [3, "black"]
        ]


def check_series(chips, start):
    #-------Variables
    total_results = []
    sub_results = []
    mycards = sorted(chips, key = itemgetter(0))
    #-------Variables
    for item0 in mycards[start:]:
        sub_results.append(item0)
        for item1 in mycards[start + 1:]:
            #----Here code is included to use jockers. 
            if (item1[0] == sub_results[-1][0] + 1 or item1[0] == 20) and (item0[1] == item1[1] or item1[1] == "jocker"):
                sub_results.append(item1)
        if len(sub_results) >= 3:
            for item in sub_results:
                mycards.remove(item)
            total_results.append(sub_results)
            sub_results = []
        else: 
            sub_results = []     
    return total_results, mycards

def check_groups(chips):
    #-------Variables
    total_results = []
    sub_results = []
    mycards = sorted(chips, key = itemgetter(0))
    #-------Variables
    for item0 in mycards:
        sub_results.append(item0)
        for item1 in mycards:
            #----Here code is included to use jockers. 
            if (item1[0] == sub_results[-1][0] or item1[0] == 20) and (item0[1] != item1[1] or item1[1] == "jocker"):
                sub_results.append(item1)
        if len(sub_results) >= 3:
            for item in sub_results: 
                mycards.remove(item)
            total_results.append(sub_results)
            sub_results = []
        else: 
            sub_results = []
    return total_results, mycards

def check_one_group(mycards, start):
    #-------Variables
    total_results = []
    #-------Variables
    total_results.append(mycards[start])
    for item in mycards: 
        if (item[0] == total_results[-1][0] or item[0] == 20) and (item[1] != total_results[-1][1] or item[1] == "jocker"):
            total_results.append(item)
    if len(total_results) >= 3:
        return total_results
    else: 
        return False 
      
def check_one_series(mycards, start):
    #-------Variables
    total_results = []
    #-------Variables
    total_results.append(mycards[start])
    for item in mycards: 
        if (item[0] == total_results[-1][0] + 1 or item[0] == 20) and (item[1] == total_results[-1][1] or item[1] == "jocker"):
            total_results.append(item)
    if len(total_results) >= 3:
        return total_results
    else: 
        return False    

def random_trials (trials):
    #-------Variables
    all_results = []
    mycards = chips
    temp_cards = mycards
    results = []
    points = 0
    #-------Variables
    for num1 in range(trials):
        for num2 in range(trials):
            out_put = check_one_group(temp_cards, random.randint(0,len(temp_cards)-1))
            if out_put:
                results.append(out_put)
                for item in out_put:
                    try: 
                        temp_cards.remove(item)
                    except: 
                        pass
            out_put = check_one_series(temp_cards, random.randint(0,len(temp_cards)-1))
            if out_put: 
                results.append(out_put)
                for item in out_put: 
                    try:
                        temp_cards.remove(item)
                    except: 
                        pass
        for item in temp_cards:
            points += item[0]
        results.append(points)
        points = 0
        if results not in all_results:
            all_results.append(results)
            results = []
            temp_cards = mycards
	return all_results[-1][-1], chips
    
def lets_play(chips):
	all_strats = []
	for num in range(len(chips)):
		chips_left = chips
		out_tup = ()
		strat = []
		points = 0
		if check_series(chips, num)[0]:
			strat.append(check_series(chips, num)[0])
			chips_left = check_series(chips, num)[1]
		if check_groups(chips_left)[0]: 
			strat.append(check_groups(chips_left)[0])
			chips_left = check_groups(chips_left)[1]
		for item in chips_left:
			points += item[0]
		out_tup = (strat, points)
		all_strats.append(out_tup)


	return sorted(all_strats, key = itemgetter(1))

print lets_play(chips)[0]

