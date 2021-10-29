# Utilisation de Darknet & Yolo_v4 pour la détection d'antennes réseau sur des images satellites

Réalisé pour le Orange MassalIA Challenge

https://github.com/AlexeyAB/darknet

Il faut déplacer les fichiers de darknet_massalia/ vers la racine darknet/ de AlexeyAB pour notre utilisation.


## Commande d'entrainement :
./darknet detector train <data_file> <config_file> <pretrained_weight_file>

Fichier pré-entrainé : https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137

## Dans notre cas la commande d'entrainement est :
./darknet detector train data/obj.data cfg/yolo-obj.cfg yolov4.conv.137 -map


Commande de test :
