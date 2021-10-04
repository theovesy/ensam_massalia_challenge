import sys
import csv

IMG_SIZE = (512.0,512.0)

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
				
def fill_obj_data_file(csv_line):
	img_name = str(csv_line[0][:-4])
	
	# Object box coordinates
	xmin = float(csv_line[1])
	ymin = float(csv_line[2])
	xmax = float(csv_line[3])
	ymax = float(csv_line[4])
	
	obj_class = 0	# Only one object type to detect
	
	box_data = [str(obj_class), str((xmax + xmin)/2), str((ymax + ymin)/2), str((xmax - xmin)/IMG_SIZE[0]), str((ymax - ymin)/IMG_SIZE[0])] 
	
	with open("labels/" + img_name + ".txt", 'a') as f:
		f.write(' '.join(box_data) + "\n")

def main(filename):
	extract_line(filename)

if __name__ == "__main__":
	if len(sys.argv) > 0:
		main(sys.argv[1])
	else:
		print("File name argument missing !")
		print("python extract_labels.py <filename>")
