# Assignment 2 CS562
# Author - Neha M
# Date - 1/12/2017

import subprocess
import os
import psutil
import time, signal


def start_match(player1,player2,output):

	output= "Results/"+output

	command = "python Assign2.py {} {} >{}".format(player1,player2,output)
	print ("Process started")
	p = subprocess.Popen([command],shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, preexec_fn=os.setsid)
	print (p.communicate())

	if check_pid == 'True':
		os.killpg(os.getpgid(p.pid), signal.SIGTERM)
	print ("Process Stopped\n")


def check_pid(pid):        
    """ Check For the existence of a unix pid. """
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True


if __name__ == '__main__':
	
	dir_name = '/home/neha/AI_Asgn/Archive/AI_Assign2_submissions/'
	list_items = os.listdir(dir_name)
	list_ignore = ['run','Assign2','MyPlayer','OtherPlayer']

	for player1 in list_items: 
		abspath = dir_name + player1
		name1 = player1.split(".")[0]
		
		if os.path.isfile(abspath) and name1 not in list_ignore and player1.split('.')[1] != 'pyc':
			print ("Currently running " + player1)
			for player2 in list_items:
				name2 = player2.split(".")[0]
				if name2!=name1 and os.path.isfile(dir_name + player2) and name2 not in list_ignore and player2.split('.')[1] != "pyc":
					print ("Competing with " + player2)
					start_match(name1 , name2 , name1+"_"+name2)

		
