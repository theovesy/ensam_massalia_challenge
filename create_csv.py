import os.path
import glob
import sys
import csv

IMG_SIZE = (512.0,512.0)

# Extract data from .txt files in <path>
def extract_txt(csv_name, path):
    # List all text files in path
    txt_files = glob.glob(path + "*.txt")
    for file in txt_files:
        with open(file, 'r') as textfile:
            data_lines = textfile.readlines()
            img_name = os.path.split(file)[1]                    # img name w/ path
            img_name = os.path.splitext(img_name)[0] + ".png"    # img name with the right extension
            fill_csv(csv_name, img_name, data_lines)

# Fill the .csv with object data
def fill_csv(csv_name, img_name, data_lines):
    with open(csv_name, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        line_count = 0
        for line in data_lines:
            data_list = [img_name] + line.split()[1:]   # data line to write in the csv file
            data_list[1],data_list[2], data_list[3], data_list[4] = convert2aboslute(data_list)     # absolute coordinates
            data_list[-1] = float(data_list[-1]) / 100  # 0 < score < 1
            data_list[-1] = str("%.2f" % data_list[-1]) # convert to str with only 2 decimals
            writer.writerow(data_list)
            line_count += 1
        print(str(line_count) + "line(s) writen for " + img_name)

# Convert relative coordinates of the center of the box to absolute coordinates of the corners
def convert2aboslute(relative):
    L, l = IMG_SIZE[0], IMG_SIZE[1]
    x, y, w, h = float(relative[1]),float(relative[2]), float(relative[3]), float(relative[4])
    xmin = int(L * (x - 0.5 * w))
    xmax = int(L * (x + 0.5 * w))
    ymin = int(l * (y - 0.5 * h))
    ymax = int(l * (y + 0.5 * h))
    
    return str(xmin), str(ymin), str(xmax), str(ymax)

def init_csv():
    # Avoid to overwrite old results
    i = 0
    while os.path.isfile("results" + str(i) + ".csv"):
        i += 1
    csv_name = "results" + str(i) + ".csv" 
    print("File " + csv_name + " created !")

    # Write the first line
    with open(csv_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(["filename", "xmin", "ymin", "xmax", "ymax", "score"])

    return csv_name

def main(path):
    csv_name = init_csv()
    extract_txt(csv_name, path)
    print("Done !")	

# Script command : python create_csv.py <path to .txt test results>
if __name__ == "__main__":
	if len(sys.argv) > 0:
		main(sys.argv[1])
	else:
		print("Folder path argument missing !")
		print("python create_csv.py <path to .txt test results>")
