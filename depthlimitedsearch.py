# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:09:06 2023

@author: sriva
"""

def dls(graph, start, end, depth):
    stack = [[start, 0, -1]]
    path = [[start, 0, -1]]
    while len(stack)>0 and stack[-1][0]!=end:
        node = stack[-1]
        del stack[-1]
        if node[1]>=depth:
            continue
 
        for edge in graph:
            if edge[0]==node[0]:
                stack.append([edge[1], node[1]+1, node[0]])
                path.append([edge[1], node[1]+1, node[0]])
 
    if path[-1][0]==end:
        route = []
        route.append(path[-1][0])
        route.append(path[-1][2])
        del path[-1]
        path.reverse()
        for node in path:
            if node[0]==route[-1] and route[-1]!=-1:
                route.append(node[2])
        del route[-1]
        route.reverse()
        print(route)
        
graph = [[1, 2], [2, 4], [1, 4], [3, 4], [3, 5], [2, 6], [3, 6], [4, 5], [5, 6]]
start = 1
end = 6
depth = 3

dls(graph,start,end,depth)