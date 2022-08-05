"""
this script is used to extrct YOLO conforming style labels
<object-class-id> <x> <y> <width> <height>

Command:
python3 label.py <Training.csv>

In referenced to BOSSTraining.csv under Polar/Training
"""

import os
import argparse

import pandas as pd

def label(self, csv):
	df = pd.DataFrame(columns=['obj_class_id', 'x', 'y', 'width', 'height'])


	for row in csv:
		df = df.append({'obj_class_id': row.split(",")[6], 'x': row.split(",")[2], 'y':row.split(",")[3], 'width':row.split(",")[4]-row.split(",")[2], 'height':row.split(",")[5]-row.split(",")[3]}
			


if name == "__main__":
	
	# Extract class id, x-coor, y-coor, width and height from train file csv
	train_csv = pd.read_csv("C:\Users\polar\BOSS_Color_Training\training")

	label(train_csv)