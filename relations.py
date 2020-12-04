#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 03-12-2020
# alex
# relations.py

# relacions de conmutació per a la base anidada
tamE=[2, 1, 2, 3, 6, 9]
relE=[[[[[[0, 1, 0, 0]] for l in range(tamE[-1] + 1)] for k in range(len(tamE) + 1)] for j in range(tamE[-1] + 1)] for i in range(len(tamE) + 1)]
relE[1][1][1][2] = [[1, 1, 2, 1]]
relE[1][1][2][1] = [[1, 1, 3, 1]]
relE[1][1][3][1] = [[1, 1, 4, 1]]
relE[1][1][3][2] = [[1, 1, 4, 2]]
relE[1][1][4][1] = [[1, 1, 5, 1]]
relE[1][1][4][2] = [[-1, 1, 5, 3]]
relE[1][1][4][3] = [[1, 1, 5, 5]]
relE[1][2][2][1] = [[1, 1, 3, 2]]
relE[1][2][3][1] = [[1, 1, 4, 2]]
relE[1][2][3][2] = [[-1, 1, 4, 3]]
relE[1][2][4][1] = [[1, 1, 5, 2]]
relE[1][2][4][2] = [[1, 1, 5, 4]]
relE[1][2][4][3] = [[1, 1, 5, 6]]
relE[2][1][3][1] = [[-1, 1, 5, 3], [-1, 1, 5, 2]]
relE[2][1][3][2] = [[-1, 1, 5, 4], [-1, 1, 5, 5]]
relE[1][1][5][1] = [[1, 1, 6, 1]]
relE[1][1][5][2] = [[1, 1, 6, 3]]
relE[1][1][5][3] = [[1, 1, 6, 3], [-1, 1, 6, 2]]
relE[1][1][5][4] = [[1, 1, 6, 4]]
relE[1][1][5][5] = [[1, 1, 6, 6]]
relE[1][1][5][6] = [[1, 1, 6, 8]]
relE[1][2][5][1] = [[1, 1, 6, 2]]
relE[1][2][5][2] = [[1, 1, 6, 5]]
relE[1][2][5][3] = [[-1, 3, 6, 5], [-1, 3, 6, 6]]
relE[1][2][5][4] = [[1, 1, 6, 7], [-1, 1, 6, 8]]
relE[1][2][5][5] = [[1, 1, 6, 7]]
relE[1][2][5][6] = [[1, 1, 6, 9]]
relE[2][1][4][1] = [[1, 1, 6, 3], [-1, 1, 6, 2]]
relE[2][1][4][2] = [[-1, 3, 6, 5], [-1, 3, 6, 6]]
relE[2][1][4][3] = [[1, 1, 6, 8], [-1, 1, 6, 7]]

def corxetErel(i, j, k, l):
    if (i > len(tamE)) or (k > len(tamE)) or (j > tamE[i - 1]) or (l > tamE[k - 1]):
        return [[0, 1, 0, 0]]
    return relE[i][j][k][l]
