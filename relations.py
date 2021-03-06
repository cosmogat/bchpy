#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 03-12-2020
# alex
# relations.py

# relacions de conmutació per a la base niada o niuada
tamE = [2, 1, 2, 3, 6, 9, 18, 30, 56]
#tamE = [2, 1, 2, 3, 6, 9, 18, 30]
relE = [[[[[[0, 1, 0, 0]] for l in range(tamE[-1] + 1)] for k in range(len(tamE) + 1)] for j in range(tamE[-1] + 1)] for i in range(len(tamE) + 1)]

# relacions de conmutació per a composició d'ordre 1
tamZ = [1, 1, 2, 3, 6, 9, 18, 30, 56]
relZ = [[[[[[0, 1, 0, 0]] for l in range(tamZ[-1] + 1)] for k in range(len(tamZ) + 1)] for j in range(tamZ[-1] + 1)] for i in range(len(tamZ) + 1)]

# ordre 2 a 5
relE[1][1][1][2] = [[1, 1, 2, 1]]
relE[1][1][2][1] = [[1, 1, 3, 1]]
relE[1][2][2][1] = [[1, 1, 3, 2]]
relE[1][1][3][1] = [[1, 1, 4, 1]]
relE[1][1][3][2] = [[1, 1, 4, 2]]
relE[1][2][3][1] = [[1, 1, 4, 2]]
relE[1][2][3][2] = [[-1, 1, 4, 3]]
relE[1][1][4][1] = [[1, 1, 5, 1]]
relE[1][1][4][2] = [[-1, 1, 5, 3]]
relE[1][1][4][3] = [[1, 1, 5, 5]]
relE[1][2][4][1] = [[1, 1, 5, 2]]
relE[1][2][4][2] = [[1, 1, 5, 4]]
relE[1][2][4][3] = [[1, 1, 5, 6]]
relE[2][1][3][1] = [[-1, 1, 5, 2], [-1, 1, 5, 3]]
relE[2][1][3][2] = [[-1, 1, 5, 5], [-1, 1, 5, 4]]
# ordre 6
relE[1][1][5][1] = [[1, 1, 6, 1]]
relE[1][1][5][2] = [[1, 1, 6, 3]]
relE[1][1][5][3] = [[-2, 1, 6, 3], [1, 1, 6, 2]]
relE[1][1][5][4] = [[1, 1, 6, 4]]
relE[1][1][5][5] = [[1, 1, 6, 6]]
relE[1][1][5][6] = [[1, 1, 6, 8]]
relE[1][2][5][1] = [[1, 1, 6, 2]]
relE[1][2][5][2] = [[1, 1, 6, 5]]
relE[1][2][5][3] = [[-1, 3, 6, 6], [-1, 3, 6, 5], [-1, 1, 6, 4]]
relE[1][2][5][4] = [[1, 1, 6, 8], [-2, 1, 6, 7]]
relE[1][2][5][5] = [[1, 1, 6, 7]]
relE[1][2][5][6] = [[1, 1, 6, 9]]
relE[2][1][4][1] = [[-1, 1, 6, 2], [1, 1, 6, 3]]
relE[2][1][4][2] = [[-1, 3, 6, 6], [-1, 3, 6, 5]]
relE[2][1][4][3] = [[1, 1, 6, 8], [-1, 1, 6, 7]]
relE[3][1][3][2] = [[-2, 3, 6, 6], [-1, 1, 6, 4], [1, 3, 6, 5]]
# ordre 7
relE[1][1][6][1] = [[1, 1, 7, 1]]
relE[1][1][6][2] = [[1, 1, 7, 3]]
relE[1][1][6][3] = [[1, 1, 7, 5]]
relE[1][1][6][4] = [[1, 1, 7, 7]]
relE[1][1][6][5] = [[1, 1, 7, 9]]
relE[1][1][6][6] = [[1, 1, 7, 11]]
relE[1][1][6][7] = [[1, 1, 7, 13]]
relE[1][1][6][8] = [[1, 1, 7, 15]]
relE[1][1][6][9] = [[1, 1, 7, 17]]
relE[1][2][6][1] = [[1, 1, 7, 2]]
relE[1][2][6][2] = [[1, 1, 7, 4]]
relE[1][2][6][3] = [[1, 1, 7, 6]]
relE[1][2][6][4] = [[1, 1, 7, 8]]
relE[1][2][6][5] = [[1, 1, 7, 10]]
relE[1][2][6][6] = [[1, 1, 7, 12]]
relE[1][2][6][7] = [[1, 1, 7, 14]]
relE[1][2][6][8] = [[1, 1, 7, 16]]
relE[1][2][6][9] = [[1, 1, 7, 18]]
relE[2][1][5][1] = [[-1, 1, 7, 2], [1, 1, 7, 3]]
relE[2][1][5][2] = [[1, 1, 7, 9], [-1, 1, 7, 6]]
relE[2][1][5][3] = [[-1, 3, 7, 9], [2, 1, 7, 6], [-1, 1, 7, 7], [-1, 1, 7, 4], [-1, 3, 7, 11]]
relE[2][1][5][4] = [[-1, 1, 7, 8], [1, 1, 7, 15], [-2, 1, 7, 13]]
relE[2][1][5][5] = [[-1, 1, 7, 12], [1, 1, 7, 13]]
relE[2][1][5][6] = [[-1, 1, 7, 16], [1, 1, 7, 17]]
relE[3][1][4][1] = [[-2, 1, 7, 3], [1, 1, 7, 2], [1, 1, 7, 5]]
relE[3][1][4][2] = [[-2, 3, 7, 9], [2, 1, 7, 6], [-1, 1, 7, 7], [-2, 3, 7, 11], [-1, 1, 7, 4]]
relE[3][1][4][3] = [[1, 1, 7, 15], [1, 1, 7, 12], [-2, 1, 7, 13]]
relE[3][2][4][1] = [[-1, 1, 7, 9], [2, 1, 7, 6], [-1, 1, 7, 4]]
relE[3][2][4][2] = [[-1, 3, 7, 12], [-1, 1, 7, 15], [1, 1, 7, 8], [-1, 3, 7, 10], [2, 1, 7, 13]]
relE[3][2][4][3] = [[2, 1, 7, 16], [-1, 1, 7, 17], [-1, 1, 7, 14]]
# ordre 8
relE[1][1][7][1] = [[1, 1, 8, 1]]
relE[1][1][7][2] = [[1, 1, 8, 3]]
relE[1][1][7][3] = [[1, 1, 8, 5]]
relE[1][1][7][4] = [[1, 1, 8, 7]]
relE[1][1][7][5] = [[-3, 1, 8, 3], [3, 1, 8, 5], [1, 1, 8, 2]]
relE[1][1][7][6] = [[1, 1, 8, 10]]
relE[1][1][7][7] = [[1, 1, 8, 12]]
relE[1][1][7][8] = [[1, 1, 8, 14]]
relE[1][1][7][9] = [[1, 1, 8, 16]]
relE[1][1][7][10] = [[1, 1, 8, 18]]
relE[1][1][7][11] = [[-2, 1, 8, 9], [-3, 1, 8, 7], [-1, 1, 8, 6], [1, 1, 8, 4], [-2, 1, 8, 16], [-2, 1, 8, 12], [8, 1, 8, 10]]
relE[1][1][7][12] = [[1, 1, 8, 21]]
relE[1][1][7][13] = [[3, 1, 8, 21], [7, 3, 8, 17], [-5, 3, 8, 20], [-1, 1, 8, 18], [-2, 1, 8, 13], [2, 1, 8, 14], [-1, 1, 8, 11]]
relE[1][1][7][14] = [[1, 1, 8, 24]]
relE[1][1][7][15] = [[-1, 1, 8, 8], [-4, 1, 8, 20], [-2, 1, 8, 18], [6, 1, 8, 21], [4, 1, 8, 17], [-6, 1, 8, 13], [6, 1, 8, 14]]
relE[1][1][7][16] = [[1, 1, 8, 27]]
relE[1][1][7][17] = [[3, 1, 8, 26], [1, 1, 8, 27], [1, 3, 8, 19], [-8, 1, 8, 23], [4, 3, 8, 22], [2, 1, 8, 24], [-2, 1, 8, 15]]
relE[1][1][7][18] = [[3, 1, 8, 29], [-3, 1, 8, 28], [1, 1, 8, 25]]
relE[1][2][7][1] = [[1, 1, 8, 2]]
relE[1][2][7][2] = [[1, 1, 8, 4]]
relE[1][2][7][3] = [[1, 1, 8, 6]]
relE[1][2][7][4] = [[1, 1, 8, 8]]
relE[1][2][7][5] = [[1, 1, 8, 9]]
relE[1][2][7][6] = [[1, 1, 8, 11]]
relE[1][2][7][7] = [[1, 1, 8, 13]]
relE[1][2][7][8] = [[1, 1, 8, 15]]
relE[1][2][7][9] = [[1, 1, 8, 17]]
relE[1][2][7][10] = [[1, 1, 8, 19]]
relE[1][2][7][11] = [[1, 1, 8, 20]]
relE[1][2][7][12] = [[1, 1, 8, 22]]
relE[1][2][7][13] = [[1, 1, 8, 23]]
relE[1][2][7][14] = [[1, 1, 8, 25]]
relE[1][2][7][15] = [[1, 1, 8, 26]]
relE[1][2][7][16] = [[1, 1, 8, 28]]
relE[1][2][7][17] = [[1, 1, 8, 29]]
relE[1][2][7][18] = [[1, 1, 8, 30]]
relE[2][1][6][1] = [[-1, 1, 8, 2], [1, 1, 8, 3]]
relE[2][1][6][2] = [[1, 1, 8, 7], [-1, 1, 8, 6]]
relE[2][1][6][3] = [[-1, 1, 8, 9], [1, 1, 8, 10]]
relE[2][1][6][4] = [[-1, 1, 8, 13], [1, 1, 8, 14]]
relE[2][1][6][5] = [[1, 1, 8, 18], [-1, 1, 8, 17]]
relE[2][1][6][6] = [[1, 1, 8, 21], [-1, 1, 8, 20]]
relE[2][1][6][7] = [[-1, 1, 8, 23], [1, 1, 8, 24]]
relE[2][1][6][8] = [[-1, 1, 8, 26], [1, 1, 8, 27]]
relE[2][1][6][9] = [[2, 1, 8, 29], [-3, 1, 8, 28], [1, 1, 8, 25]]
relE[3][1][5][1] = [[1, 1, 8, 2], [-2, 1, 8, 3], [1, 1, 8, 5]]
relE[3][1][5][2] = [[1, 1, 8, 9], [-2, 1, 8, 10], [1, 1, 8, 16]]
relE[3][1][5][3] = [[-4, 3, 8, 9], [-1, 1, 8, 7], [4, 3, 8, 6], [4, 3, 8, 10], [1, 3, 8, 16], [-1, 3, 8, 4], [-1, 3, 8, 12]]
relE[3][1][5][4] = [[-1, 1, 8, 8], [-2, 3, 8, 20], [-2, 3, 8, 17], [-1, 1, 8, 13], [2, 1, 8, 11]]
relE[3][1][5][5] = [[1, 1, 8, 21], [-2, 3, 8, 20], [-1, 1, 8, 18], [7, 3, 8, 17], [2, 1, 8, 14], [-2, 1, 8, 13], [-1, 1, 8, 11]]
relE[3][1][5][6] = [[4, 1, 8, 26], [-1, 1, 8, 27], [-2, 1, 8, 15], [-8, 1, 8, 23], [4, 3, 8, 22], [1, 3, 8, 19], [2, 1, 8, 24]]
relE[3][2][5][1] = [[-1, 1, 8, 7], [2, 1, 8, 6], [-1, 1, 8, 4]]
relE[3][2][5][2] = [[-1, 1, 8, 18], [2, 1, 8, 17], [-1, 1, 8, 11]]
relE[3][2][5][3] = [[-1, 1, 8, 8], [-2, 3, 8, 20], [1, 3, 8, 21], [1, 3, 8, 18], [-2, 3, 8, 17], [-2, 1, 8, 13], [2, 1, 8, 11], [1, 1, 8, 14]]
relE[3][2][5][4] = [[-1, 1, 8, 27], [2, 1, 8, 26], [-4, 1, 8, 23], [-1, 1, 8, 15], [2, 1, 8, 24]]
relE[3][2][5][5] = [[2, 1, 8, 23], [-1, 1, 8, 22], [-1, 1, 8, 24]]
relE[3][2][5][6] = [[-1, 1, 8, 29], [2, 1, 8, 28], [-1, 1, 8, 25]]
relE[4][1][4][2] = [[2, 1, 8, 6], [-2, 1, 8, 10], [1, 1, 8, 16], [-1, 1, 8, 4]]
relE[4][1][4][3] = [[-1, 1, 8, 8], [1, 1, 8, 18], [-3, 1, 8, 17], [3, 1, 8, 11]]
relE[4][2][4][3] = [[1, 1, 8, 27], [-3, 1, 8, 26], [-1, 3, 8, 19], [6, 1, 8, 23], [-1, 3, 8, 22], [-2, 1, 8, 24], [2, 1, 8, 15]]
# ordre 9
relE[1][1][8][1] = [[1, 1, 9, 1]]
relE[1][1][8][2] = [[1, 1, 9, 3]]
relE[1][1][8][3] = [[1, 1, 9, 5]]
relE[1][1][8][4] = [[1, 1, 9, 7]]
relE[1][1][8][5] = [[1, 1, 9, 9]]
relE[1][1][8][6] = [[1, 1, 9, 11]]
relE[1][1][8][7] = [[1, 1, 9, 13]]
relE[1][1][8][8] = [[1, 1, 9, 15]]
relE[1][1][8][9] = [[1, 1, 9, 17]]
relE[1][1][8][10] = [[1, 1, 9, 19]]
relE[1][1][8][11] = [[1, 1, 9, 21]]
relE[1][1][8][12] = [[1, 1, 9, 23]]
relE[1][1][8][13] = [[1, 1, 9, 25]]
relE[1][1][8][14] = [[1, 1, 9, 27]]
relE[1][1][8][15] = [[1, 1, 9, 29]]
relE[1][1][8][16] = [[1, 1, 9, 7], [9, 4, 9, 13], [6, 1, 9, 6], [-9, 4, 9, 4], [4, 1, 9, 17], [-1, 1, 9, 19], [1, 4, 9, 23], [-11, 2, 9, 11], [-15, 4, 9, 10]]
relE[1][1][8][17] = [[1, 1, 9, 32]]
relE[1][1][8][18] = [[1, 1, 9, 34]]
relE[1][1][8][19] = [[1, 1, 9, 36]]
relE[1][1][8][20] = [[3, 2, 9, 8], [6, 1, 9, 20], [3, 2, 9, 34], [3, 1, 9, 21], [-3, 2, 9, 31], [-4, 1, 9, 32], [-3, 2, 9, 18], [-3, 2, 9, 27], [3, 2, 9, 25], [-3, 2, 9, 24], [-3, 2, 9, 15], [-3, 1, 9, 12]]
relE[1][1][8][21] = [[1, 1, 9, 39]]
relE[1][1][8][22] = [[1, 1, 9, 41]]
relE[1][1][8][23] = [[1, 1, 9, 43]]
relE[1][1][8][24] = [[1, 1, 9, 45]]
relE[1][1][8][25] = [[1, 1, 9, 47]]
relE[1][1][8][26] = [[1, 1, 9, 49]]
relE[1][1][8][27] = [[3, 1, 9, 49], [-2, 1, 9, 22], [-3, 1, 9, 40], [-3, 1, 9, 28], [2, 3, 9, 41], [1, 1, 9, 33], [2, 3, 9, 36], [-1, 1, 9, 35], [2, 1, 9, 38], [3, 1, 9, 26], [-4, 1, 9, 43], [-1, 1, 9, 29], [1, 1, 9, 45], [1, 1, 9, 16]]
relE[1][1][8][28] = [[1, 1, 9, 52]]
relE[1][1][8][29] = [[7, 1, 9, 50], [-6, 1, 9, 51], [4, 1, 9, 52], [1, 3, 9, 37], [-12, 1, 9, 44], [1, 3, 9, 42], [8, 1, 9, 46], [-3, 1, 9, 47], [-3, 1, 9, 30]]
relE[1][1][8][30] = [[1, 1, 9, 55]]
relE[1][2][8][1] = [[1, 1, 9, 2]]
relE[1][2][8][2] = [[1, 1, 9, 4]]
relE[1][2][8][3] = [[1, 1, 9, 6]]
relE[1][2][8][4] = [[1, 1, 9, 8]]
relE[1][2][8][5] = [[1, 1, 9, 10]]
relE[1][2][8][6] = [[1, 1, 9, 12]]
relE[1][2][8][7] = [[1, 1, 9, 14]]
relE[1][2][8][8] = [[1, 1, 9, 16]]
relE[1][2][8][9] = [[1, 1, 9, 18]]
relE[1][2][8][10] = [[1, 1, 9, 20]]
relE[1][2][8][11] = [[1, 1, 9, 22]]
relE[1][2][8][12] = [[1, 1, 9, 24]]
relE[1][2][8][13] = [[1, 1, 9, 26]]
relE[1][2][8][14] = [[1, 1, 9, 28]]
relE[1][2][8][15] = [[1, 1, 9, 30]]
relE[1][2][8][16] = [[1, 1, 9, 31]]
relE[1][2][8][17] = [[1, 1, 9, 33]]
relE[1][2][8][18] = [[1, 1, 9, 35]]
relE[1][2][8][19] = [[1, 1, 9, 37]]
relE[1][2][8][20] = [[1, 1, 9, 38]]
relE[1][2][8][21] = [[1, 1, 9, 40]]
relE[1][2][8][22] = [[1, 1, 9, 42]]
relE[1][2][8][23] = [[1, 1, 9, 44]]
relE[1][2][8][24] = [[1, 1, 9, 46]]
relE[1][2][8][25] = [[1, 1, 9, 48]]
relE[1][2][8][26] = [[1, 1, 9, 50]]
relE[1][2][8][27] = [[1, 1, 9, 51]]
relE[1][2][8][28] = [[1, 1, 9, 53]]
relE[1][2][8][29] = [[1, 1, 9, 54]]
relE[1][2][8][30] = [[1, 1, 9, 56]]
relE[2][1][7][1] = [[-1, 1, 9, 2], [1, 1, 9, 3]]
relE[2][1][7][2] = [[1, 1, 9, 7], [-1, 1, 9, 6]]
relE[2][1][7][3] = [[1, 1, 9, 11], [-1, 1, 9, 10]]
relE[2][1][7][4] = [[-1, 1, 9, 14], [1, 1, 9, 15]]
relE[2][1][7][5] = [[3, 1, 9, 6], [-1, 1, 9, 4], [1, 1, 9, 17], [-3, 1, 9, 10]]
relE[2][1][7][6] = [[-1, 1, 9, 20], [1, 1, 9, 21]]
relE[2][1][7][7] = [[1, 1, 9, 25], [-1, 1, 9, 24]]
relE[2][1][7][8] = [[-1, 1, 9, 28], [1, 1, 9, 29]]
relE[2][1][7][9] = [[1, 1, 9, 32], [-1, 1, 9, 31]]
relE[2][1][7][10] = [[-1, 1, 9, 35], [1, 1, 9, 36]]
relE[2][1][7][11] = [[1, 2, 9, 8], [1, 2, 9, 18], [3, 2, 9, 34], [-2, 1, 9, 20], [3, 1, 9, 21], [1, 2, 9, 31], [-4, 1, 9, 32], [-3, 2, 9, 27], [3, 2, 9, 25], [1, 2, 9, 24], [3, 1, 9, 14], [-3, 2, 9, 15], [-2, 1, 9, 12]]
relE[2][1][7][12] = [[-1, 1, 9, 40], [1, 1, 9, 41]]
relE[2][1][7][13] = [[-3, 1, 9, 40], [5, 3, 9, 38], [2, 1, 9, 26], [-7, 3, 9, 33], [1, 1, 9, 35], [-2, 1, 9, 28], [1, 1, 9, 43], [1, 1, 9, 22]]
relE[2][1][7][14] = [[-1, 1, 9, 46], [1, 1, 9, 47]]
relE[2][1][7][15] = [[6, 1, 9, 26], [1, 1, 9, 49], [2, 1, 9, 35], [-4, 1, 9, 33], [-6, 1, 9, 40], [4, 1, 9, 38], [1, 1, 9, 16], [-6, 1, 9, 28]]
relE[2][1][7][16] = [[-1, 1, 9, 51], [1, 1, 9, 52]]
relE[2][1][7][17] = [[-1, 1, 9, 42], [-7, 1, 9, 51], [4, 1, 9, 50], [4, 1, 9, 52], [-4, 1, 9, 44], [6, 1, 9, 46], [-3, 1, 9, 47], [-1, 1, 9, 30]]
relE[2][1][7][18] = [[3, 1, 9, 53], [-3, 1, 9, 54], [1, 1, 9, 55], [-1, 1, 9, 48]]
relE[3][1][6][1] = [[-2, 1, 9, 3], [1, 1, 9, 2], [1, 1, 9, 5]]
relE[3][1][6][2] = [[-2, 1, 9, 11], [1, 1, 9, 10], [1, 1, 9, 13]]
relE[3][1][6][3] = [[-3, 1, 9, 6], [1, 1, 9, 4], [1, 1, 9, 19], [-2, 1, 9, 17], [3, 1, 9, 10]]
relE[3][1][6][4] = [[-2, 1, 9, 25], [1, 1, 9, 24], [1, 1, 9, 27]]
relE[3][1][6][5] = [[1, 1, 9, 34], [1, 1, 9, 31], [-2, 1, 9, 32]]
relE[3][1][6][6] = [[3, 1, 9, 15], [-2, 1, 9, 8], [-3, 1, 9, 34], [-4, 1, 9, 20], [1, 1, 9, 31], [5, 1, 9, 12], [1, 1, 9, 39], [-3, 1, 9, 25], [-6, 1, 9, 21], [8, 1, 9, 32], [1, 1, 9, 18], [1, 1, 9, 24], [-3, 1, 9, 14], [3, 1, 9, 27]]
relE[3][1][6][7] = [[-1, 1, 9, 22], [-2, 1, 9, 43], [3, 1, 9, 40], [-5, 3, 9, 38], [-1, 1, 9, 35], [7, 3, 9, 33], [2, 1, 9, 28], [-2, 1, 9, 26], [1, 1, 9, 45]]
relE[3][1][6][8] = [[1, 1, 9, 49], [-2, 1, 9, 22], [3, 1, 9, 28], [-2, 1, 9, 38], [3, 1, 9, 40], [2, 3, 9, 41], [2, 3, 9, 36], [-3, 1, 9, 35], [5, 1, 9, 33], [-1, 1, 9, 29], [-4, 1, 9, 43], [-3, 1, 9, 26], [1, 1, 9, 45]]
relE[3][1][6][9] = [[-5, 1, 9, 30], [-5, 1, 9, 51], [10, 1, 9, 50], [1, 1, 9, 52], [5, 3, 9, 42], [-20, 1, 9, 44], [10, 1, 9, 46], [2, 3, 9, 37], [-2, 1, 9, 47]]
relE[3][2][6][1] = [[-1, 1, 9, 7], [2, 1, 9, 6], [-1, 1, 9, 4]]
relE[3][2][6][2] = [[2, 1, 9, 14], [-1, 1, 9, 12], [-1, 1, 9, 15]]
relE[3][2][6][3] = [[-1, 1, 9, 21], [2, 1, 9, 20], [-1, 1, 9, 18]]
relE[3][2][6][4] = [[2, 1, 9, 28], [-1, 1, 9, 26], [-1, 1, 9, 29]]
relE[3][2][6][5] = [[-1, 1, 9, 33], [2, 1, 9, 35], [-1, 1, 9, 36]]
relE[3][2][6][6] = [[2, 1, 9, 40], [-1, 1, 9, 38], [-1, 1, 9, 41]]
relE[3][2][6][7] = [[2, 1, 9, 46], [-1, 1, 9, 44], [-1, 1, 9, 47]]
relE[3][2][6][8] = [[2, 1, 9, 51], [-1, 1, 9, 50], [-1, 1, 9, 52]]
relE[3][2][6][9] = [[-6, 1, 9, 53], [5, 1, 9, 54], [-1, 1, 9, 55], [2, 1, 9, 48]]
relE[4][1][5][1] = [[3, 1, 9, 3], [-3, 1, 9, 5], [-1, 1, 9, 2], [1, 1, 9, 9]]
relE[4][1][5][2] = [[1, 1, 9, 7], [9, 1, 9, 6], [-11, 2, 9, 11], [-13, 4, 9, 4], [-4, 1, 9, 19], [7, 1, 9, 17], [9, 4, 9, 13], [1, 4, 9, 23], [-27, 4, 9, 10]]
relE[4][1][5][3] = [[-4, 1, 9, 6], [5, 4, 9, 4], [3, 2, 9, 11], [3, 1, 9, 19], [-4, 1, 9, 17], [-5, 4, 9, 13], [-1, 4, 9, 23], [15, 4, 9, 10]]
relE[4][1][5][4] = [[-1, 1, 9, 8], [-1, 1, 9, 34], [1, 1, 9, 31], [2, 1, 9, 12], [-4, 1, 9, 20], [2, 1, 9, 32], [1, 1, 9, 18]]
relE[4][1][5][5] = [[1, 1, 9, 8], [1, 1, 9, 34], [3, 1, 9, 14], [-2, 1, 9, 15], [-3, 1, 9, 32], [3, 1, 9, 21], [-3, 1, 9, 12]]
relE[4][1][5][6] = [[-6, 1, 9, 33], [4, 1, 9, 35], [-1, 1, 9, 36], [-1, 1, 9, 16], [4, 1, 9, 22]]
relE[4][2][5][1] = [[-2, 1, 9, 6], [1, 1, 9, 4], [2, 1, 9, 11], [-1, 1, 9, 13]]
relE[4][2][5][2] = [[-1, 1, 9, 34], [2, 1, 9, 32], [-2, 1, 9, 20], [1, 1, 9, 18]]
relE[4][2][5][3] = [[-1, 1, 9, 8], [1, 1, 9, 15], [-2, 3, 9, 34], [-2, 1, 9, 21], [1, 1, 9, 31], [3, 1, 9, 12], [2, 1, 9, 32], [1, 3, 9, 39], [-3, 1, 9, 25], [-2, 1, 9, 14], [1, 1, 9, 24], [-1, 1, 9, 18], [2, 1, 9, 27]]
relE[4][2][5][4] = [[2, 1, 9, 22], [-1, 1, 9, 49], [-2, 3, 9, 36], [-2, 1, 9, 26], [-2, 3, 9, 41], [3, 1, 9, 40], [1, 1, 9, 35], [-1, 1, 9, 33], [1, 1, 9, 29], [-2, 1, 9, 38], [1, 1, 9, 28], [1, 1, 9, 45], [-1, 1, 9, 16]]
relE[4][2][5][5] = [[-2, 1, 9, 40], [1, 1, 9, 38], [2, 1, 9, 43], [-1, 1, 9, 45]]
relE[4][2][5][6] = [[-1, 1, 9, 52], [-6, 1, 9, 50], [4, 1, 9, 51], [-1, 3, 9, 37], [-8, 1, 9, 46], [-1, 3, 9, 42], [12, 1, 9, 44], [2, 1, 9, 47], [3, 1, 9, 30]]
relE[4][3][5][1] = [[1, 1, 9, 8], [3, 1, 9, 14], [-1, 1, 9, 15], [-3, 1, 9, 12]]
relE[4][3][5][2] = [[-3, 1, 9, 33], [3, 1, 9, 35], [-1, 1, 9, 36], [1, 1, 9, 22]]
relE[4][3][5][3] = [[-1, 1, 9, 40], [1, 1, 9, 38], [1, 3, 9, 41], [1, 3, 9, 36], [-1, 1, 9, 35], [1, 1, 9, 33], [3, 1, 9, 26], [-3, 1, 9, 28], [-2, 1, 9, 22], [1, 1, 9, 29], [1, 1, 9, 16]]
relE[4][3][5][4] = [[1, 1, 9, 30], [-1, 1, 9, 52], [3, 1, 9, 51], [-3, 1, 9, 50], [-6, 1, 9, 46], [6, 1, 9, 44], [2, 1, 9, 47]]
relE[4][3][5][5] = [[-3, 1, 9, 44], [3, 1, 9, 46], [1, 1, 9, 42], [-1, 1, 9, 47]]
relE[4][3][5][6] = [[-8, 1, 9, 53], [6, 1, 9, 54], [-1, 1, 9, 55], [3, 1, 9, 48]]

# ordre 2 a 5
relZ[1][1][2][1] = [[1, 1, 3, 2]]
relZ[1][1][3][1] = [[1, 1, 4, 2]]
relZ[1][1][3][2] = [[1, 1, 4, 3]]
relZ[1][1][4][1] = [[1, 1, 5, 2]]
relZ[1][1][4][2] = [[1, 1, 5, 3]]
relZ[1][1][4][3] = [[1, 1, 5, 4]]
relZ[2][1][3][1] = [[1, 1, 5, 5]]
relZ[2][1][3][2] = [[1, 1, 5, 6]]
# ordre 6
relZ[1][1][5][1] = [[1, 1, 6, 2]]
relZ[1][1][5][2] = [[1, 1, 6, 3]]
relZ[1][1][5][3] = [[1, 1, 6, 4]]
relZ[1][1][5][4] = [[1, 1, 6, 5]]
relZ[1][1][5][5] = [[1, 1, 6, 6]]
relZ[1][1][5][6] = [[1, 1, 6, 7]]
relZ[2][1][4][1] = [[1, 1, 6, 8]]
relZ[2][1][4][2] = [[1, 1, 6, 9]]
relZ[2][1][4][3] = [[1, 1, 6, 7]]
relZ[3][1][3][2] = [[-1, 1, 6, 6], [1, 1, 6, 9]]
# ordre 7
relZ[1][1][6][1] = [[1, 1, 7, 2]]
relZ[1][1][6][2] = [[1, 1, 7, 3]]
relZ[1][1][6][3] = [[1, 1, 7, 4]]
relZ[1][1][6][4] = [[1, 1, 7, 5]]
relZ[1][1][6][5] = [[1, 1, 7, 6]]
relZ[1][1][6][6] = [[1, 1, 7, 7]]
relZ[1][1][6][7] = [[1, 1, 7, 8]]
relZ[1][1][6][8] = [[1, 1, 7, 9]]
relZ[1][1][6][9] = [[1, 1, 7, 10]]
relZ[2][1][5][1] = [[1, 1, 7, 11]]
relZ[2][1][5][2] = [[1, 1, 7, 12]]
relZ[2][1][5][3] = [[1, 1, 7, 13]]
relZ[2][1][5][4] = [[1, 1, 7, 14]]
relZ[2][1][5][5] = [[1, 1, 7, 15]]
relZ[2][1][5][6] = [[1, 1, 7, 16]]
relZ[3][1][4][1] = [[1, 1, 7, 17]]
relZ[3][1][4][2] = [[1, 1, 7, 18]]
relZ[3][1][4][3] = [[2, 1, 7, 10], [-1, 1, 7, 7], [-1, 1, 7, 13]]
relZ[3][2][4][1] = [[-1, 1, 7, 12], [1, 1, 7, 9]]
relZ[3][2][4][2] = [[1, 1, 7, 10], [-1, 1, 7, 13]]
relZ[3][2][4][3] = [[-1, 1, 7, 14], [1, 1, 7, 8]]
# ordre 8
relZ[1][1][7][1] = [[1, 1, 8, 2]]
relZ[1][1][7][2] = [[1, 1, 8, 3]]
relZ[1][1][7][3] = [[1, 1, 8, 4]]
relZ[1][1][7][4] = [[1, 1, 8, 5]]
relZ[1][1][7][5] = [[1, 1, 8, 6]]
relZ[1][1][7][6] = [[1, 1, 8, 7]]
relZ[1][1][7][7] = [[1, 1, 8, 8]]
relZ[1][1][7][8] = [[1, 1, 8, 9]]
relZ[1][1][7][9] = [[1, 1, 8, 10]]
relZ[1][1][7][10] = [[1, 1, 8, 11]]
relZ[1][1][7][11] = [[1, 1, 8, 12]]
relZ[1][1][7][12] = [[1, 1, 8, 13]]
relZ[1][1][7][13] = [[1, 1, 8, 14]]
relZ[1][1][7][14] = [[1, 1, 8, 15]]
relZ[1][1][7][15] = [[1, 1, 8, 16]]
relZ[1][1][7][16] = [[1, 1, 8, 17]]
relZ[1][1][7][17] = [[1, 1, 8, 18]]
relZ[1][1][7][18] = [[1, 1, 8, 19]]
relZ[2][1][6][1] = [[1, 1, 8, 20]]
relZ[2][1][6][2] = [[1, 1, 8, 21]]
relZ[2][1][6][3] = [[1, 1, 8, 22]]
relZ[2][1][6][4] = [[1, 1, 8, 23]]
relZ[2][1][6][5] = [[-1, 1, 8, 9], [2, 1, 8, 15]]
relZ[2][1][6][6] = [[1, 1, 8, 24]]
relZ[2][1][6][7] = [[1, 1, 8, 25]]
relZ[2][1][6][8] = [[1, 1, 8, 26]]
relZ[2][1][6][9] = [[1, 1, 8, 27]]
relZ[3][1][5][1] = [[1, 1, 8, 28]]
relZ[3][1][5][2] = [[1, 1, 8, 29]]
relZ[3][1][5][3] = [[1, 1, 8, 19]]
relZ[3][1][5][4] = [[3, 1, 8, 11], [-3, 1, 8, 14], [-1, 1, 8, 8], [1, 1, 8, 23]]
relZ[3][1][5][5] = [[1, 1, 8, 30]]
relZ[3][1][5][6] = [[-2, 1, 8, 24], [1, 1, 8, 16], [1, 1, 8, 27]]
relZ[3][2][5][1] = [[-1, 1, 8, 21], [1, 1, 8, 12]]
relZ[3][2][5][2] = [[1, 1, 8, 13], [-1, 1, 8, 22]]
relZ[3][2][5][3] = [[1, 1, 8, 14], [-1, 1, 8, 23]]
relZ[3][2][5][4] = [[1, 1, 8, 9], [-1, 1, 8, 15]]
relZ[3][2][5][5] = [[-1, 1, 8, 24], [1, 1, 8, 16]]
relZ[3][2][5][6] = [[1, 1, 8, 17], [-1, 1, 8, 25]]
relZ[4][1][4][2] = [[-1, 1, 8, 18], [1, 1, 8, 29]]
relZ[4][1][4][3] = [[2, 1, 8, 13], [-1, 1, 8, 10], [-1, 1, 8, 22]]
relZ[4][2][4][3] = [[2, 1, 8, 14], [-1, 1, 8, 11], [-1, 1, 8, 23]]
# ordre 9
relZ[1][1][8][1] = [[1, 1, 9, 2]]
relZ[1][1][8][2] = [[1, 1, 9, 3]]
relZ[1][1][8][3] = [[1, 1, 9, 4]]
relZ[1][1][8][4] = [[1, 1, 9, 5]]
relZ[1][1][8][5] = [[1, 1, 9, 6]]
relZ[1][1][8][6] = [[1, 1, 9, 7]]
relZ[1][1][8][7] = [[1, 1, 9, 8]]
relZ[1][1][8][8] = [[1, 1, 9, 9]]
relZ[1][1][8][9] = [[1, 1, 9, 10]]
relZ[1][1][8][10] = [[1, 1, 9, 11]]
relZ[1][1][8][11] = [[1, 1, 9, 12]]
relZ[1][1][8][12] = [[1, 1, 9, 13]]
relZ[1][1][8][13] = [[1, 1, 9, 14]]
relZ[1][1][8][14] = [[1, 1, 9, 15]]
relZ[1][1][8][15] = [[1, 1, 9, 16]]
relZ[1][1][8][16] = [[1, 1, 9, 17]]
relZ[1][1][8][17] = [[1, 1, 9, 18]]
relZ[1][1][8][18] = [[1, 1, 9, 19]]
relZ[1][1][8][19] = [[1, 1, 9, 20]]
relZ[1][1][8][20] = [[1, 1, 9, 21]]
relZ[1][1][8][21] = [[1, 1, 9, 22]]
relZ[1][1][8][22] = [[1, 1, 9, 23]]
relZ[1][1][8][23] = [[1, 1, 9, 24]]
relZ[1][1][8][24] = [[1, 1, 9, 25]]
relZ[1][1][8][25] = [[1, 1, 9, 26]]
relZ[1][1][8][26] = [[1, 1, 9, 27]]
relZ[1][1][8][27] = [[1, 1, 9, 28]]
relZ[1][1][8][28] = [[1, 1, 9, 29]]
relZ[1][1][8][29] = [[1, 1, 9, 30]]
relZ[1][1][8][30] = [[1, 1, 9, 31]]
relZ[2][1][7][1] = [[1, 1, 9, 32]]
relZ[2][1][7][2] = [[1, 1, 9, 33]]
relZ[2][1][7][3] = [[1, 1, 9, 34]]
relZ[2][1][7][4] = [[1, 1, 9, 35]]
relZ[2][1][7][5] = [[1, 1, 9, 36]]
relZ[2][1][7][6] = [[1, 1, 9, 37]]
relZ[2][1][7][7] = [[1, 1, 9, 38]]
relZ[2][1][7][8] = [[1, 1, 9, 39]]
relZ[2][1][7][9] = [[1, 1, 9, 40]]
relZ[2][1][7][10] = [[1, 1, 9, 41]]
relZ[2][1][7][11] = [[1, 1, 9, 42]]
relZ[2][1][7][12] = [[1, 1, 9, 43]]
relZ[2][1][7][13] = [[1, 1, 9, 44]]
relZ[2][1][7][14] = [[-3, 1, 9, 26], [3, 1, 9, 39], [1, 1, 9, 18]]
relZ[2][1][7][15] = [[1, 1, 9, 45]]
relZ[2][1][7][16] = [[1, 1, 9, 46]]
relZ[2][1][7][17] = [[1, 1, 9, 47]]
relZ[2][1][7][18] = [[1, 1, 9, 48]]
relZ[3][1][6][1] = [[1, 1, 9, 49]]
relZ[3][1][6][2] = [[1, 1, 9, 50]]
relZ[3][1][6][3] = [[1, 1, 9, 51]]
relZ[3][1][6][4] = [[1, 1, 9, 52]]
relZ[3][1][6][5] = [[4, 1, 9, 12], [4, 1, 9, 24], [-6, 1, 9, 15], [-1, 1, 9, 9], [-1, 1, 9, 36]]
relZ[3][1][6][6] = [[1, 1, 9, 53]]
relZ[3][1][6][7] = [[2, 1, 9, 41], [-2, 1, 9, 25], [-1, 1, 9, 44], [1, 1, 9, 17]]
relZ[3][1][6][8] = [[1, 1, 9, 54]]
relZ[3][1][6][9] = [[-1, 1, 9, 53], [1, 1, 9, 31], [1, 1, 9, 48]]
relZ[3][2][6][1] = [[-1, 1, 9, 33], [1, 1, 9, 21]]
relZ[3][2][6][2] = [[1, 1, 9, 22], [-1, 1, 9, 34]]
relZ[3][2][6][3] = [[1, 1, 9, 23], [-1, 1, 9, 35]]
relZ[3][2][6][4] = [[1, 1, 9, 24], [-1, 1, 9, 36]]
relZ[3][2][6][5] = [[2, 1, 9, 16], [-1, 1, 9, 37], [-1, 1, 9, 10]]
relZ[3][2][6][6] = [[1, 1, 9, 25], [-1, 1, 9, 38]]
relZ[3][2][6][7] = [[1, 1, 9, 26], [-1, 1, 9, 39]]
relZ[3][2][6][8] = [[-1, 1, 9, 40], [1, 1, 9, 27]]
relZ[3][2][6][9] = [[-1, 1, 9, 41], [1, 1, 9, 28]]
relZ[4][1][5][1] = [[1, 1, 9, 55]]
relZ[4][1][5][2] = [[1, 1, 9, 56]]
relZ[4][1][5][3] = [[2, 1, 9, 30], [-1, 1, 9, 19], [-1, 1, 9, 51]]
relZ[4][1][5][4] = [[3, 1, 9, 14], [-3, 1, 9, 23], [-1, 1, 9, 11], [1, 1, 9, 35]]
relZ[4][1][5][5] = [[-1, 1, 9, 47], [1, 1, 9, 54]]
relZ[4][1][5][6] = [[-2, 1, 9, 40], [1, 1, 9, 27], [1, 1, 9, 43]]
relZ[4][2][5][1] = [[-1, 1, 9, 50], [1, 1, 9, 29]]
relZ[4][2][5][2] = [[1, 1, 9, 30], [-1, 1, 9, 51]]
relZ[4][2][5][3] = [[-1, 1, 9, 52], [1, 1, 9, 20]]
relZ[4][2][5][4] = [[3, 1, 9, 15], [-3, 1, 9, 24], [-1, 1, 9, 12], [1, 1, 9, 36]]
relZ[4][2][5][5] = [[-1, 1, 9, 53], [1, 1, 9, 31]]
relZ[4][2][5][6] = [[-2, 1, 9, 41], [1, 1, 9, 28], [1, 1, 9, 44]]
relZ[4][3][5][1] = [[-2, 1, 9, 22], [1, 1, 9, 34], [1, 1, 9, 13]]
relZ[4][3][5][2] = [[-2, 1, 9, 23], [1, 1, 9, 14], [1, 1, 9, 35]]
relZ[4][3][5][3] = [[-2, 1, 9, 24], [1, 1, 9, 15], [1, 1, 9, 36]]
relZ[4][3][5][4] = [[-3, 1, 9, 16], [1, 1, 9, 37], [2, 1, 9, 10]]
relZ[4][3][5][5] = [[-2, 1, 9, 25], [1, 1, 9, 38], [1, 1, 9, 17]]
relZ[4][3][5][6] = [[-2, 1, 9, 26], [1, 1, 9, 18], [1, 1, 9, 39]]

def corxetErel(i, j, k, l):
    if (i > len(tamE)) or (k > len(tamE)) or (j > tamE[i - 1]) or (l > tamE[k - 1]) or (i == k and j == l):
        return [[0, 1, 0, 0]]
    elif (k < i) or (k == i and l < j):
        klij = relE[k][l][i][j]
        inreves = []
        for m in range(len(klij)):
            inreves.append([-klij[m][0], klij[m][1], klij[m][2], klij[m][3]])
        return inreves
    return relE[i][j][k][l]

def corxetZrel(i, j, k, l):
    if (i > len(tamZ)) or (k > len(tamZ)) or (j > tamZ[i - 1]) or (l > tamZ[k - 1]) or (i == k and j == l):
        return [[0, 1, 0, 0]]
    elif (k < i) or (k == i and l < j):
        klij = relZ[k][l][i][j]
        inreves = []
        for m in range(len(klij)):
            inreves.append([-klij[m][0], klij[m][1], klij[m][2], klij[m][3]])
        return inreves
    return relZ[i][j][k][l]
