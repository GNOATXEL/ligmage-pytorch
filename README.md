# LigmageX

## Installation

1. Installer python (ex [miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html))
2. Cloner le project
3. Puis dans votre environnement python, installer le modèle et les librairies suivantes : 

Le modèle : open-clip
```
pip install open_clip_torch
```

Les librairies Pyside6 et filetype :
```
pip install PySide6
```
```
pip install filetype
```

Il est possible que la version de Pillow installée automatiquement pose des problèmes d'incompatibilité, pour pallier ce problème vous pouvez modifier sa version par la commande suivante :
```
pip install pillow==<version>
```

## Fonctionnement

1. Ouvrir le projet
2. Run gui.py (le projet télécharge des données du modèle pour une première utilisation)
3. Choisissez un répertoire d'image et un mot-clé pour la recherche
4. Cliquez sur "Chercher"

L'application vous renverra les 3 images du répertoire correspondant le plus au mot-clé choisi. Vous pouvez cliquer sous un bouton sous chaque image pour la copier.

## Contributeurs
Axel MARTIN

Alexandre LECOMTE

Ivann VYSLANKO
