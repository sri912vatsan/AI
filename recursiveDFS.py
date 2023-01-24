# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:07:08 2023

@author: sriva
"""

graph = [[1, 2], [2, 4], [1, 4], [3, 4], [3, 5], [2, 6], [3, 6], [4, 5], [5, 6]]
start = 1
end = 6
path = [start]
 
while start!=end:
    for edge in graph:
        if edge[0]==start:
            start = edge[1]
            break
    path.append(start)
 
print(path)