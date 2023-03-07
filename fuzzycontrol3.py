# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 08:26:53 2023

@author: sriva
"""

import numpy as np
import matplotlib.pyplot as plt 

def triangular(a,b,c):
    x = 0
    x = np.maximum(0,np.minimum((c-x)/(c-b), (x-a)/(b-a)))
    return x

def trapezoidal(a,b,c,d):
    x = 0
    if a==b:
        x = np.maximum(0, np.minimum(1, (d-x)/(d-c)))
        return x
    if c==d:
        x = np.maximum(0,np.minimum(1, (x-a)/(b-a)))
        return x
    return np.maximum(0,np.minimum(np.minimum(1, (x-a)/(b-a)),(d-x)/(d-c)))

def gaussian(a,b,c):
    x = 0
    x = 1/(1+(((x-c)/a)**(2*b)))
    return x

class Variable:
    def __init__(self,name):
        self.name = name 
        self.sets = []
        self.functions = {}
        
    def add_triangular(self,set_name,a,b,c):
        self.sets.append(set_name)
        self.functions[set_name] = triangular(a, b, c)
        
    def add_trapezoidal(self,set_name,a,b,c,d):
        self.sets.append(set_name)
        self.functions[set_name] = trapezoidal(a, b, c, d)
        
    def add_gaussian(self,set_name,a,b,c):
        self.sets.append(set_name)
        self.functions[set_name] = gaussian(a,b,c)
        
    def plot(self,xmin,xmax):
        x = np.arange(xmin,xmax,0.1)
        plt.figure()
        ax = plt.add_subplot(1,1,1)
        ax.set_title(self.name)
        for _set in self.sets:
            y = self(_set,x)
            ax.plot(x,y)
        plt.show()
        
    def __call__(self,fuzzyset,crispval):
        return self.functions[fuzzyset](crispval)
    
class Controller:
    def __init__(self,name,inputs,output):
        self.name = name
        
        self.inputs = { x.name:x for x in inputs}
        self.input_names = [x for x in inputs]
        
        self.output = output 
        self.output_name = output.name 
        
        self.rules = []
        
    def add_rule(self,rule):
        self.rules.append(rule)
        
    def fuzzify(self,values):
        result = {}
        for rule in self.rules:
            key = rule["out"][self.output_name]
            if key in result.keys():
                result[key]=max(result[key],self.compute(rule,values))
            else:
                result[key] = self.compute(rule,values)
        return result 
                
    def defuzzifyFunction(self,x,fuzzyvalues):
        values = np.zeros(x.shape)
        for _set in self.output.sets:
            if _set in fuzzyvalues.keys():
                values = np.maximum(values,np.minimum(fuzzyvalues[_set],self.output(_set,x)))
        return values 
    
    def defuzzify(self,xmin,xmax,fuzzyvalues,w=0.01):
        x = np.arange(xmin,xmax,0.1)
        y = self.defuzzifyFunction(x, fuzzyvalues)
        
        centroid = 0
        areas = 0
        
        for _x,_y in zip(x,y):
            area = w*_y
            centroid += ((_x+(w/2))*area)
            areas += area 
            
        return centroid/area 
    
    def calculate(self,rule,outkey,val):
        fuzzyvalues = []
        for key in rule.keys():
            if key in ["or","and"]:
                fuzzyvalues.append(self.compute(rule[key],key,val))
            else:
                crispval = val[key]
                fuzzyset = rule[key]
                fuzzyvalues.append(self.inputs[key](fuzzyset,crispval))
                
        if outkey=="or":
            return max(fuzzyvalues)
        else:
            return min(fuzzyvalues)
        
    def compute(self,rule,values):
        keys = list(rule["in"].keys())
        if len(keys)==1:
            if keys[0]=="or":
                self.calculate(rule["in"]["or"],"or",values)
            else:
                self.calculate(rule["in"]["and"],"and",values)
                

if __name__ == "main":
    
    acceleration = Variable("acceleration")
    acceleration.
        
    
    
            
                
                
        
    
