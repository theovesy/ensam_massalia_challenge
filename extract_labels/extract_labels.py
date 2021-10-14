import os.path
import sys
import csv

IMG_SIZE = (512.0,512.0)

# Extract objects data from a .csv file
def extract_line(filename):
	with open(filename, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		line_count = 0
		for row in reader:
			if line_count == 0:
				print(f'Detected columns : {", ".join(row)}')
				line_count += 1
			else:
				fill_obj_data_file(row)
				line_count += 1
		print(str(line_count) + " objects processed")

# Fill the .txt files needed by YOLO
def fill_obj_data_file(csv_line):
	full_img_name = str(csv_line[0])	# Name with extension
	img_name = full_img_name[:-4]		# Name w/ extension
	
	# Object box coordinates
	xmin = float(csv_line[1])
	ymin = float(csv_line[2])
	xmax = float(csv_line[3])
	ymax = float(csv_line[4])
	
	obj_class = 0	# Only one object type to detect
	
	# List containing current object data
	box_data = [str(obj_class), str((xmax + xmin)/(2*IMG_SIZE[0])), str((ymax + ymin)/(2*IMG_SIZE[1])), str((xmax - xmin)/IMG_SIZE[0]), str((ymax - ymin)/IMG_SIZE[1])] 
	
	# Append a data line for each object in an image
	with open("labels/" + img_name + ".txt", 'a') as f:
		f.write(' '.join(box_data) + "\n")
	
	# Read a train.txt file use by YOLO to know the path of each training image
	prev_img_name = None
	if os.path.isfile("train.txt"):
		with open("train.txt", 'r') as r_train:
			lines = r_train.readlines()			# Return a list with all the lines
			prev_img_name = lines[-1]			# Only the last one is necessary
			
	# Write a new line for each new image (one line by image and not by object)
	with open("train.txt", 'a') as a_train:
		if prev_img_name != full_img_name:
			a_train.write("data/obj/" + full_img_name + "\n")
		
	
def main(filename):
	extract_line(filename)
	print("Done !")

# Script command : python extract_labels.py <filename>
if __name__ == "__main__":
	if len(sys.argv) > 0:
		main(sys.argv[1])
	else:
		print("File name argument missing !")
		print("python extract_labels.py <filename>")
