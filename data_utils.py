import numpy as np


def read_tracking_data3D(data_dir):
	Tracking3D = []
	f=open(data_dir, 'r')
	for line in f:
		elements = line.split(',')
		Tracking3D.append(list(map(float, elements)))
	f.close()

	Tracking3D = np.array(Tracking3D) # list can not read by index while arr can be
	Tracking3D = np.squeeze(Tracking3D)
	print(Tracking3D.shape)
	restore = np.copy(Tracking3D)
	return Tracking3D, restore


def read_tracking_data3D_nan(data_dir):
	Tracking3D = []
	f=open(data_dir, 'r')
	for line in f:
		elements = line[:-1].split(',')
		for x in range(len(elements)):
			if elements[x] == "NaN":
				elements[x] = '0'
		Tracking3D.append(list(map(float, elements)))
	f.close()

	Tracking3D = np.array(Tracking3D) # list can not read by index while arr can be
	Tracking3D = np.squeeze(Tracking3D)
	print(Tracking3D.shape)
	restore = np.copy(Tracking3D)
	return Tracking3D, restore


def find_full_matrix(Tracking2D, frame_length, overlap=False):
	count = 0
	list_full = []
	for i, frame in enumerate(Tracking2D):
		if frame[frame==0].shape[0] == 0:
			count += 1
			if count >= frame_length:
				list_full.append([i - frame_length + 1, i + 1])
				if not overlap:
					count = 0
	return list_full
