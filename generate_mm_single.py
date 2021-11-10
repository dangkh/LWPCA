# generate missing gap in specific joint according to PLOS16
import numpy as np
from data_utils import *
from arguments import arg
import sys
import random
from datetime import datetime
import os

def generate_missing_joint_gap(n, m, joint = -1):
	LSHO = 9
	LKNE = 28 
	LWA = 14

	frames = 370
	matrix = np.ones((n,m))
	joints = np.arange(m//3)
	counter = 0
	total_numgap = 1
	start_missing_frame = random.randint(0, max(0,n-frames))
	print('start : ')
	while counter < total_numgap:
		print("start_missing_frame: ",start_missing_frame, ";")
		if joint == -1:
			missing_joint = np.random.randint(0,m//3)
		else:
			missing_joint = joint
		for frame in range(start_missing_frame, start_missing_frame+frames):
			matrix[frame, missing_joint*3] = 0
			matrix[frame, missing_joint*3+1] = 0
			matrix[frame, missing_joint*3+2] = 0
		old_start = start_missing_frame
		start_missing_frame = random.randint(old_start, min(n-frames, old_start+frames))
		counter+=1
	print("end.")
	counter = 0
	for x in range(n):
		for y in range(m):
			if matrix[x][y] == 0: counter +=1
	print("percent missing: ", 100.0 * counter / (n*m))
	return matrix

def process_gap_missing():
	
	test_location = arg.test_link
	gaps = {"LSHO": 9, "LKNE": 28, "LWA": 14, "random": -1}
	test_reference = arg.missing_index
	sample = np.copy(Tracking3D[test_reference[0]:test_reference[1]])

	for gap in gaps:
		link = test_location+ str(gap)+"/"
		if not os.path.isdir(link):
			os.mkdir(link)
		for times in range(50):
			print("current: ", times)
			missing_matrix = generate_missing_joint_gap(sample.shape[0], sample.shape[1], gaps[gap])		
			np.savetxt(test_location+"/"+str(gap)+"/"+str(times)+ ".txt", missing_matrix, fmt = "%d")
	return 

if __name__ == '__main__':

	Tracking3D, _  = read_tracking_data3D(arg.data_link)
	Tracking3D = Tracking3D.astype(float)
	process_gap_missing()
