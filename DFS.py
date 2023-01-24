# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 08:47:13 2023

@author: sriva
"""

from collections import defaultdict 


class Graph:
    
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        
    def addedge(self,u,v):
        self.graph[u].append(v)
        
    def DFSUtil(self,s,d,visited,path):
        
        visited[s]=True
        path.append(s)
        
        if s==d:
            print(path)
        else:
            for i in self.graph[s]:
                if visited[i]==False:
                    self.DFSUtil(i, d, visited, path)
        
        path.pop()
        visited[s]=False
        
    def DFS(self,s,d):
        
        visited = [False]*(self.V)
        path = []
        
        self.DFSUtil(s, d, visited, path)

g = Graph(4)
g.addedge(0, 1)
g.addedge(0, 2)
g.addedge(0, 3)
g.addedge(2, 0)
g.addedge(2, 1)
g.addedge(1, 3)
  
s = 2 ; d = 3
print ("Following are all different paths from % d to % d :" %(s, d))
g.DFS(s, d)        