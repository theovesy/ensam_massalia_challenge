#!/usr/bin/python3

# Se lance avec une commande du type
# python yolodataset.py <nom du fichier csv>

import sys
import csv

img_size = (512, 512)

# Pour recuperer les arguments dans l'appel du script
def get_args(i):
    return sys.argv[i]

# Pour generer les lignes a ajouter dans les fichiers texte de chaque image
def yolo_line(row):
    line = "0 "
    line += str(((int(row[3])+int(row[1]))/2)/img_size[0])
    line += " "
    line += str(((int(row[4])+int(row[2]))/2)/img_size[1])
    line += " "
    line += str((int(row[3])-int(row[1]))/(img_size[0]))
    line += " "
    line += str((int(row[4])-int(row[2]))/(img_size[1]))
    return line

# Fonction principale
def write_files():
    # On ouvre le fichier cvs fourni et on le separer en liste pour chaque ligne
    source = open(get_args(1), 'r')
    source_rows = csv.reader(source, delimiter=',')

    # Pour chaque ligne du csv on ajoute dans le fichier lié a l'image correspondante
    for row in source_rows:
        with open("labels/" + row[0][:-4] + ".txt", 'a') as writer:
            writer.write(yolo_line(row) + "\n")

    source.close()

# On lance le tout
write_files()
