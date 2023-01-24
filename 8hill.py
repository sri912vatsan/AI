# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 12:28:08 2023

@author: sriva
"""

def displaced_tiles(state):
    heuristic = 0
 
    for i in range(len(state)):
        if state[i] != i:
            heuristic += 1
 
    return heuristic
 
def manhattan_distance(state):
    heuristic = 0
    k = 0
 
    for i in range(3):
        for j in range(3):
            heuristic += abs(i - (state[k] / 3)) + abs(j - (state[k] % 3))
            k += 1
 
    return heuristic
 
def getNextState(state):
    nextStates = []
    pos0 = state.index(0)
 
    for i in adjacency[pos0]:
        nextState = [x for x in state]
        temp = nextState[i]
        nextState[i] = 0
        nextState[pos0] = temp
        nextStates.append(nextState)
 
    return nextStates
 
def listEqual(l1, l2):
    if len(l1) != len(l2):
        return False
 
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
 
    return True
 
def hill_climb(start, end, sortFun):
    queue = [start]
    visited = []
 
    while len(queue) > 0:
        queue = sorted(queue, key = sortFun)
        # Displaced Tiles - 1122
        # Manhattan Distance - 2611
 
        # print("Queue:", queue)
        # print("Visited Nodes:", visited)
        # print()
 
        n = queue[0]
        del queue[0]
 
        if listEqual(n, end):
            print("End State:", n)
            print("Number of states visited:", len(visited))
            return True
 
        nextStates = getNextState(n)
        for state in nextStates:
            # if state not in visited and sortFun(state) < sortFun(n):
            if state not in visited:
                queue.append(state)
        visited.append(n)
 
    return False
 
start = [7, 2, 4, 5, 0, 6, 8, 3, 1]
# start = [1, 4, 2, 3, 0, 5, 6, 7, 8]
# start = [1, 0, 2, 3, 4, 5, 6, 7, 8]
# start = [0, 1, 2, 3, 4, 5, 6, 7, 8]
end = [0, 1, 2, 3, 4, 5, 6, 7, 8]
 
adjacency = {
             0: [1, 3], 
             1: [0, 2, 4], 
             2: [1, 5], 
             3: [0, 4, 6], 
             4: [1, 3, 5, 7], 
             5: [2, 4, 6], 
             6: [5, 7], 
             7: [4, 6, 8], 
             8: [5, 7]
            }
 
print("Manhattan Distance:")
if hill_climb(start, end, manhattan_distance):
    print("Solution found!\n\n")
else:
    print("No Solution!\n\n")
 
print("Displaced Tiles:")
if hill_climb(start, end, displaced_tiles):
    print("Solution found!")
else:
    print("No Solution!")
 
 
#9) Missionaries and Cannibal
from copy import copy, deepcopy
 
def leftBankCount(state):
    return state[0][0] + state[0][1]
 
def isSafe(state):
    if (state[0][1] > 0 and state[0][0] > state[0][1]) or (state[1][1] > 0 and state[1][0] > state[1][1]):
        return False
    else:
        return True
 
def getNextState(state):
    nextStates = []
 
    if state[2] == 0:
        temp = deepcopy(state)
        if temp[0][0] >= 2:
            temp[0][0] -= 2 
            temp[1][0] += 2
            if isSafe(temp):
                temp[2] = 1
                nextStates.append(temp)
        temp = deepcopy(state)
        if temp[0][1] >= 2:
            temp[0][1] -= 2
            temp[1][1] += 2
            if isSafe(temp):
                temp[2] = 1
                nextStates.append(temp)
        temp = deepcopy(state)
        if temp[0][0] >= 1 and temp[0][1] >= 1:
            temp[0][0] -= 1
            temp[0][1] -= 1
            temp[1][0] += 1
            temp[1][1] += 1
            if isSafe(temp):
                temp[2] = 1
                nextStates.append(temp)
        temp = deepcopy(state)
        if temp[0][0] >= 1:
            temp[0][0] -= 1
            temp[1][0] += 1
            if isSafe(temp):
                temp[2] = 1
                nextStates.append(temp)
        temp = deepcopy(state)
        if temp[0][1] >= 1:
            temp[0][1] -= 1
            temp[1][1] += 1
            if isSafe(temp):
                temp[2] = 1
                nextStates.append(temp)
    else:
        temp = deepcopy(state)
        if temp[1][0] >= 2:
            temp[1][0] -= 2 
            temp[0][0] += 2
            if isSafe(temp):
                temp[2] = 0
                nextStates.append(temp)
        temp = deepcopy(state)
        if temp[1][1] >= 2:
            temp[1][1] -= 2
            temp[0][1] += 2
            if isSafe(temp):
                temp[2] = 0
                nextStates.append(temp)
        temp = deepcopy(state)
        if temp[1][0] >= 1 and temp[1][1] >= 1:
            temp[1][0] -= 1
            temp[1][1] -= 1
            temp[0][0] += 1
            temp[0][1] += 1
            if isSafe(temp):
                temp[2] = 0
                nextStates.append(temp)
        temp = deepcopy(state)
        if temp[1][0] >= 1:
            temp[1][0] -= 1
            temp[0][0] += 1
            if isSafe(temp):
                temp[2] = 0
                nextStates.append(temp)
        temp = deepcopy(state)
        if temp[1][1] >= 1:
            temp[1][1] -= 1
            temp[0][1] += 1
            if isSafe(temp):
                temp[2] = 0
                nextStates.append(temp)
 
    # print("Next States:", nextStates)
    return nextStates
 
def listEqual(l1, l2):
    if l1[0][0] == l2[0][0] and l1[0][1] == l2[0][1] and l1[1][0] == l2[1][0] and l1[1][1] == l2[1][1] and l1[2] == l2[2]:
        return True
    else:
        return False
 
def hill_climb(start, end):
    queue = [start]
    visited = []
 
    while len(queue) > 0:
        queue = sorted(queue, key = leftBankCount)
 
        print("Queue:", queue)
        # print("Visited Nodes:", visited)
        # print()
 
        n = queue[0]
        del queue[0]
 
        if listEqual(n, end):
            print("End State:", n)
            print("Number of states visited:", len(visited))
            return True
 
        nextStates = getNextState(n)
        for state in nextStates:
            # if state not in visited and sortFun(state) < sortFun(n):
            if state not in visited:
                queue.append(state)
        visited.append(n)
 
    return False
 
start = [[3, 3], [0, 0], 0]
# start = [[2, 0], [1, 3], 1]
end = [[0, 0], [3, 3], 1]
 
if hill_climb(start, end):
    print("Solution found!\n\n")
else:
    print("No Solution!\n\n")