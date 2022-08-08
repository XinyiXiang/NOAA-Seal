"""
this script is used to extrct YOLO conforming style labels
<object-class-id> <x> <y> <width> <height>

Command:
python3 label.py <Training.csv>

In referenced to BOSSTraining.csv under Polar/Training
"""

INPUT_CSV_PATH = "../../Downloads/boss_training.csv"
OUTPUT_CSV_PATH = "../../Downloads/boss_training_output.csv"

import os
import argparse

import pandas as pd

def label(lines):
	df = pd.DataFrame(columns=['file_name','obj_class_id', 'x', 'y', 'width', 'height'])


	for row in lines:
		full_name = row.split(",")[6]

		df = df.append(
			{'file_name': row.split(",")[0].split(".")[0], 
			'obj_class_id': full_name.split("_")[1], 
			'x': row.split(",")[2], 
			'y': row.split(",")[3], 
			'width':int(row.split(",")[4])-int(row.split(",")[2]), 
			'height':int(row.split(",")[5])-int(row.split(",")[3])},
			ignore_index = True
		)

	res = df.to_csv(OUTPUT_CSV_PATH)

	return res

if __name__ == "__main__":
	
	# Extract class id, x-coor, y-coor, width and height from train file csv
	with open(INPUT_CSV_PATH) as file:
		train_csv_lines = file.readlines()

	label(train_csv_lines)