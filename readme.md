# Database pour YOLO

Yolo utilise un format different pour les bounding box que celui fourni par le challenge :

Il lui faut pour chaque image un fichier texte avec les coordonnées des rectangles dedans avec ce format :

```
<object-class> <x_center> <y_center> <width> <height>
```

Pour nous object-class sera simplement 0 parce qu'on ne veux reconnaitre qu'un type d'objet.
x_center et y_center sont les coordonnées du centre de la bounding box
width et height sont la largeur et la hauteur de la bounding box divisée par la largeure ou longueur totale de l'image. Sachant que chaque image fait 512x512.

J'ai fait la conversion avec le script python yolodataset.py inclu dans ce repo. Les fichiers générés sont dans le dossier labels.
