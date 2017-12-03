# won,lost,Draw
# Assignment 2 CS562
# Author - Neha M
# Date - 1/12/2017

import os
import numpy as np


score = np.zeros((32,3))
dir_name = 'Results/'

for file_ in os.listdir(dir_name):
	player1 = int(file_.split('_')[0])
	player2 = int(file_.split('_')[1])

	path = dir_name + file_
	f = open(path,'r')
	a = f.readlines()
	
	if len(a)!=0:
		a = a[-1]
		print (a)

	if "Draw" in a:
		score[player1-1][2] += 1 
		score[player2-1][2] += 1 

	elif "Loser" in a:
		i = int(a.split('_')[1])
		if i == 1:
			score[player1-1][1] += 1			
			score[player2-1][0] += 1	
		else:
			score[player1-1][0] += 1			
			score[player2-1][1] += 1

print score	

for i in range (0,32):
	print score[i][0] + score[i][1] + score[i][2]

np.savetxt('a',score)					