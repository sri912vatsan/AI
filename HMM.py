# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 22:10:26 2023

@author: sriva
"""

#HMM
# Forward Algorithm

H = {'A': 0.2, 'C': 0.3, 'G': 0.3, 'T': 0.2}
L = {'A': 0.3, 'C': 0.2, 'G': 0.2, 'T': 0.3}
transitionP = {('S', 'H'): 0.5, ('S', 'L'): 0.5, ('H', 'H'): 0.5, ('L', 'L'): 0.6, ('L', 'H'): 0.4, ('H', 'L'): 0.5}
seq = 'GGCA'
P = []

for i in seq:
    if len(P) == 0:
        p = [transitionP[('S', 'H')] * H[i], transitionP[('S', 'L')] * L[i]]
    else:
        p = []
        # H
        # (H -> H) + (L -> H)
        p.append(P[-1][0] * transitionP[('H', 'H')] * H[i] + P[-1][1] * transitionP[('L', 'H')] * H[i])
        # L
        # (L -> L) + (H -> L)
        p.append(P[-1][1] * transitionP[('L', 'L')] * L[i] + P[-1][0] * transitionP[('H', 'L')] * L[i])
    P.append(p)

print(P)
print()
print(P[-1][0] + P[-1][1])


# Viterbi Algorithm

H = {'A': -2.322, 'C': -1.737, 'G': -1.737, 'T': -2.322}
L = {'A': -1.737, 'C': -2.322, 'G': -2.322, 'T': -1.737}
transitionP = {('S', 'H'): -1, ('S', 'L'): -1, ('H', 'H'): -1, ('L', 'L'): -0.737, ('L', 'H'): -1.322, ('H', 'L'): -1}
seq = 'GGCACTGAA'
P = []
parent = []

for i in seq:
    if len(P) == 0:
        p = [transitionP[('S', 'H')] + H[i], transitionP[('S', 'L')] + L[i]]
    else:
        p = []
        par = []
        # H
        p.append(H[i] + max(P[-1][0] + transitionP[('H', 'H')], P[-1][1] + transitionP[('L', 'H')]))
        if P[-1][0] + transitionP[('H', 'H')] > P[-1][1] + transitionP[('L', 'H')]:
            par.append('H')
        else:
            par.append('L')
        # L
        p.append(L[i] + max(P[-1][0] + transitionP[('H', 'L')], P[-1][1] + transitionP[('L', 'L')]))
        if P[-1][0] + transitionP[('H', 'L')] > P[-1][1] + transitionP[('L', 'L')]:
            par.append('H')
        else:
            par.append('L')

        parent.append(par)
        
    P.append(p)

# Backtracking
path = []
if P[-1][0] > P[-1][1]:
    path.extend([par[0] for par in parent])
    path.append('H')
else:
    path.extend([par[1] for par in parent])
    path.append('L')

print(path)