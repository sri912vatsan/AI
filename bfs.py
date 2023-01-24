# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:08:20 2023

@author: sriva
"""

graph = [[1, 2], [2, 4], [1, 4], [3, 4], [3, 5], [2, 6], [3, 6], [4, 5], [5, 6]]
start = 1
end = 6
queue = []
queue.append([start])
 
while(len(queue)>0):
    path = queue.pop(0)
    node = path[-1]
 
    if node==end:
        print(path)
        break
 
    for edge in graph:
        if edge[0]==node:
            new_path = list(path)
            new_path.append(edge[1])
            queue.append(new_path)