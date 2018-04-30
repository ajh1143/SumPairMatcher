#Program that accepts a list of integers separated by spaces and a target integer.
#Prints out all of the pairs of numbers from the input list that sum to the target integer.
#Sorts lists so smaller values are shown first.

import sys
import itertools
import numpy as np
from operator import itemgetter

#accept integer list as line
line = sys.stdin.readline()
digits = line.strip().split(" ")
#Map digits to ints as list
castDigits = list(map(int, digits))
#accept target integer
target = sys.stdin.readline()
#Create list of all pairs of values using itertools combinations
combos = list(itertools.combinations(castDigits, 2))

#Create empty list for valid pairs
pairList = []
#Loop through each pair in combinations, create sum
for pair in combos:
    summed = pair[0] + pair[1]
    #check if sum matches target
    if summed == int(target):
        matchingPairs = pair[0], pair[1]
        #Check if matching pair is already in list
        if matchingPairs in pairList:
            pass
        else:
            pairList.append(matchingPairs)
    else:
        pass

#Create newList to generate ordered lists
newList = []
for each in pairList:
    if each [0] > each[1]:
        item = each[1], each[0]
        newList.append(item)
    else:
        item = each[0], each[1]
        newList.append(item)

#Sort the sorted list
sortedList = sorted(newList)
for each in sortedList:
    print(each[0], each[1])
