import sys
import itertools


class SumPairMatcher(object):
"""
#Program that accepts a list of integers separated by spaces and a target integer.
#Prints out all of the pairs of numbers from the input list that sum to the target integer.
#Sorts lists so smaller values are shown first.
""" 
    
    def getLine(self):
        # accept integer list as line
        line = sys.stdin.readline()
        digits = line.strip().split(" ")
        return digits

    def mapper(self, rawInput):
        # Map digits to ints as list
        castDigits = list(map(int, rawInput))
        return castDigits

    def getTarget(self):
        # accept target integer
        target = sys.stdin.readline()
        return target

    def combinator(self, mappedDigits):
        # Create list of all pairs of values using itertools combinations
        combos = list(itertools.combinations(mappedDigits, 2))
        return combos

    def createPairList(self, combinatorResults, targetSum):
        # Create empty list for valid pairs
        pairList = []
        # Loop through each pair in combinations, create sum
        for pair in combinatorResults:
            summed = pair[0] + pair[1]
            # check if sum matches target
            if summed == int(targetSum):
                matchingPairs = pair[0], pair[1]
                # Check if matching pair is already in list
                if matchingPairs in pairList:
                    pass
                else:
                    pairList.append(matchingPairs)
            else:
                pass
        return pairList

    def orderPairs(self, pairResults):
        # Create newList to generate ordered lists
        newList = []
        for each in pairResults:
            if each[0] > each[1]:
                item = each[1], each[0]
                newList.append(item)
            else:
                item = each[0], each[1]
                newList.append(item)
        return newList

    def finalSort(self, unsortedList):
        # Sort the sorted list
        sortedList = sorted(unsortedList)
        for each in sortedList:
            print(each[0], each[1])
        return None

if __name__ == "__main__":
    a = SumPairMatcher()
    inputLine = a.getLine()
    mappedDigits = a.mapper(inputLine)
    target = a.getTarget()
    combos = a.combinator(mappedDigits)
    unorderedPairs = a.createPairList(combos, target)
    orderedPairs = a.orderPairs(unorderedPairs)
    a.finalSort(orderedPairs)
