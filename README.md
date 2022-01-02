# About Minitel

Minitel is a type of computer terminal intended for connection to the french Vidéotex service called Télétel, commercially operated in France between 1980 and 2012. Providing access to various services prefiguring those future Internet, and using for this the French network Transpac which itself foreshadowed the future Internet transmission infrastructure, it has raised France to the forefront of global telematics thanks to the first service in the world of free or paid supply of 'telematic information. It will be a considerable success and will remain popular for a long time.

# Minitel Image Viewer
## General
The goal of this project is to visualize any image (in color or in black and white) in 8 shades of gray on the Alcatel Minitel 2 using semi-graphic characters.  
The project is still in progress. 

## Use
### Prerequisites
Make sure to use Windows OS.  
On Python 3.x.x, install the serial library and cv2 library corresponding to your Python version.  

### Test
A test file is provided with the source code. To execute it, write the command below in a terminal at the root of the project :  
```
python src/image_to_semigraphic.py
```

### Error cases
- The serial connection between the computer and the Minitel is not correctly established:
``` 
Error opening port COM5 at 1200 bauds.
Error opening Minitel communication.
```
- The file path doesn't exist or the file is in a format that cannot be interpreted by cv2:
```
File at <your_path> doesn't exist or can't be read as an image.
Error opening the image.
```

### Expected result
Input image computer side:  
<img src="assets\happy.jpg"  width="200">  
<br />
Output image Minitel side:  
<img src="results\happy_result.jpg"  width="200">  

# Minitel Mouse
## General
The goal of this project is to add a mouse to the Minitel. When you move your computer mouse, the cursor will move on the Minitel terminal in proportion to the size of the main screen.  
The project is still in progress.

## Use
### Prerequisites
Make sure to use Windows OS.  
On Python 3.x.x, install the serial library corresponding to your Python version.  

### Test
A test file is provided with the source code. To execute it, write the command below in a terminal at the root of the project :  
```
python src/mouse_on_monitor.py
```

### Error case
- The serial connection between the computer and the Minitel is not correctly established:
``` 
Error opening port COM5 at 1200 bauds.
Error opening Minitel communication.
```

### Expected result
Output terminal Minitel:  
<img src="results\minitel_cursor.gif"  width="200">  

# Minitel Drawer
## General
The goal of this project is to be able to draw an image on the Minitel 2 terminal in 8 shades of gray using semi-graphic characters from a graphic interface on a computer connected in serial communication to the Minitel.  
The project is still in progress.

## Use
### Prerequisites
Make sure to use Windows OS.  
On Python 3.x.x, install the serial library and cv2 library corresponding to your Python version.  

### Test
A test file is provided with the source code. To execute it, write the command below in a terminal at the root of the project :  
```
python src/drawer_minitel.py
```

### Error cases
- The serial connection between the computer and the Minitel is not correctly established:
``` 
Error opening port COM5 at 1200 bauds.
Error opening Minitel communication.
```

### Expected result
Software computer side:  
<img src="results\minitel_drawer_software_screen.jpg"  width="200">  
<br />
Output image Minitel side:  
<img src="results\minitel_drawer_result.jpg"  width="200">  

# Bibliography
- https://github.com/eserandour/Minitel1B_Hard  
Thanks to this source code, it was possible for me to carry the basic options such as cleaning the screen or switching to semi-graphic mode. 
<br /> <br />
- https://wiki.labomedia.org/images/a/ad/STUM2.pdf  
With the Minitel 2 documentation, I was able to understand and implement the conversion of 6 pixels into a semi-graphic character.

<br /><br /><br /><br /><br /><br /><br />

# A propos du Minitel
Le Minitel est un type de terminal informatique destiné à la connexion au service français de Vidéotex baptisé Télétel, commercialement exploité en France entre 1980 et 2012. Donnant accès à des services variés préfigurant ceux du futur Internet, et utilisant pour cela le réseau français Transpac qui lui-même préfigurait la future infrastructure de transmission d'Internet, il a hissé la France au premier plan de la télématique mondiale grâce au premier service au monde de fourniture gratuite ou payante d’informations télématiques. Il sera un succès considérable et restera longtemps populaire.

# Visualisateur d'image Minitel
## Général
Le but de ce projet est de visualiser n'importe quelle image (en couleurs ou en noir et blanc) en 8 nuances de gris sur le Minitel 2 Alcatel grâce aux caractères semi-graphiques.  
Le projet est toujours en cours. 

## Utilisation
### Pré-requis
Assurez-vous d'utiliser le système d'exploitation Windows.  
Sur Python 3.x.x, installez la bibliothèque serial et cv2 correspondant à votre version Python.

### Test
Un fichier test est fourni avec le code source. Pour l'exécuter, écrivez la commande ci-dessous dans un terminal à la racine du projet :
```
python src/image_to_semigraphic.py
```

### Cas d'erreurs
- La connexion série entre l'ordinateur et le Minitel ne s'est pas établie correctement :
``` 
Error opening port COM5 at 1200 bauds.
Error opening Minitel communication.
```
- Le chemin du fichier n'existe pas ou le fichier est dans un format non interprétable par cv2 :
```
File at <your_path> doesn't exist or can't be read as an image.
Error opening the image.
```

### Résultat attendu
Image d'entrée côté ordinateur :  
<img src="assets\upssitech.jpg"  width="200">  
<br />
Image de sortie côté Minitel :  
<img src="results\upssitech_result.jpg"  width="200"> 

# Souris Minitel
## Général
Le but de ce projet est d'ajouter une souris au Minitel. Lorsque vous bougerez la souris de votre ordinateur, le curseur se déplacera alors sur le terminal du Minitel proportionnellement à la taille de l'écran principal.  
Le projet est toujours en cours.

## Utilisation
### Pré-requis
Assurez-vous d'utiliser le système d'exploitation Windows.  
Sur Python 3.x.x, installez la bibliothèque serial correspondant à votre version Python.

### Test
Un fichier test est fourni avec le code source. Pour l'exécuter, écrivez la commande ci-dessous dans un terminal à la racine du projet :
```
python src/mouse_on_monitor.py
```

### Cas d'erreur
- La connexion série entre l'ordinateur et le Minitel ne s'est pas établie correctement :  
``` 
Error opening port COM5 at 1200 bauds.
Error opening Minitel communication.
```

### Résultat attendu
Sortie terminal du Minitel :  
<img src="results\minitel_cursor.gif"  width="200">  

# Minitel Drawer
## Général
Le but de ce projet est de pouvoir dessiner une image sur le terminal du Minitel 2 en 8 nuances de gris à l'aide de caractères semi-graphiques depuis une interface graphique sur un ordinateur branché en communication série au Minitel.  
Le projet est toujours en cours.

## Utilisation
### Pré-requis
Assurez-vous d'utiliser le système d'exploitation Windows.  
Sur Python 3.x.x, installez la bibliothèque serial et cv2 correspondant à votre version Python.

### Test
Un fichier test est fourni avec le code source. Pour l'exécuter, écrivez la commande ci-dessous dans un terminal à la racine du projet :  
```
python src/drawer_minitel.py
```

### Cas d'erreur
- La connexion série entre l'ordinateur et le Minitel ne s'est pas établie correctement :  
``` 
Error opening port COM5 at 1200 bauds.
Error opening Minitel communication.
```

### Résultat attendu 
Image du logiciel côté ordinateur :  
<img src="results\minitel_drawer_software_screen.jpg"  width="200">  
<br />
Image de sortie côté Minitel :  
<img src="results\minitel_drawer_result.jpg"  width="200">  

# Bibliographie
- https://github.com/eserandour/Minitel1B_Hard  
Grâce à ce code source, il m'a été possible de porter les options de base comme le nettoyage de l'écran ou le passage en mode semi-graphique.
<br /> <br />
- https://wiki.labomedia.org/images/a/ad/STUM2.pdf  
Avec la documentation du Minitel 2, j'ai pu comprendre et implémenter la conversion de 6 pixels en un caractère semi-graphique.