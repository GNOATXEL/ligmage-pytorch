# LigmageX

## Contexte

France, 2020 plus 2, un groupe d'étudiants assoiffés d'innovation se réunit autour d'une table. Un point les rassemble ; ils ont tous, sur leur ordinateur ou bien leur GSM entre autres, une panoplie bien garnie d'images, et plus particulièrement ce qu'on appelle des mèmes ou "memes" comme écrivent les djeunz, comme l'image ci-dessous.

<img src="https://cdn.discordapp.com/attachments/462263112926494740/1197894097311117383/aaaaaaaaaa.jpg?ex=65bcecd0&is=65aa77d0&hm=b83a4a8a53a7646407ff5f7e8d71dcc4e01fe45c11581725dd86d74905f49901&" alt="image" width="300" height="auto">

Ces mèmes sont donc des images à vocation humoristique, et peuplent les appareils de la plupart des jeunes de notre ère.

Cependant, si l'on s'intéresse à la provenance de ces images, nous observons qu'elles sont souvent téléchargées, un petit peu "à la fortune du pot" si on puit dire, et se retrouvent, par centaines voire milliers dans nos dossiers, avec des noms assez insolites, tout comme "ssstwitter.com_1703895035884.png", "000_33ET8FV.jpg" ou bien même "Capture d'écran 2023-10-04 205001.png".

C'est là qu'un problème survient : comment promptement retrouver le mème que l'on veut à un moment donné ? Étudiants entreprenants et motivés que nous sommes, notre cortex préfrontal s'est immédiatement activé, et une idée novatrice nous est venue : Ligmage.

Ligmage, nom issu de la contraction entre "Ligma" (un mème populaire sur la toile) et "Image", serait une application capable de retrouver des mèmes à partir de leur contenu.

Prenons l'exemple du mème envoyé plus haut. Le fichier s'appelle présentement "aaaaaaaaaa.jpg", impossible donc de le retrouver avec une simple recherche. Pas de panique, Ligmage va nous permettre de le retrouver grâce au contenu du mème, en cherchant "marteau" ou "orange man".

Mais quel sortilège peut bien permettre une telle prouesse ? Eh bien en fait c'est très simple, Ligmage utilise le réseau de neurones CLIP (d'OpenAI), qui reconnait objets et texte sur des images, et renvoie pour un mot donné un coefficient. Plus ce coefficient est haut, plus le mot correspond à l'image. Lorsque l'on rentre un mot dans Ligmage, l'application renvoie les images pour lesquelles le coefficient est le plus haut, et c'est ainsi qu'on retrouve des mèmes facilement malgré un nommage plus que douteux.

Cette application s'adresse donc surtout aux personnes ayant des mèmes sur leur appareil, les fonctionnalités se résumant pour l'instant à de la recherche et de la copie (pour pouvoir envoyer à ses camarades une image qui fait sourire 🤭), sans fonctionnalités permettant de les agencer à ce jour. Ces _features_ sont envisagées, afin de toucher éventail plus large de personnes, c'est à dire tout individu ayant des images sur son appareil. De plus, l'application n'est pour l'instant fonctionnelle que sur ordinateur, mais une portabilité sur natel est prévue.

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

Pour savoir comment fonctionne l'application, cliquez [ici](https://gitlab.istic.univ-rennes1.fr/meminov/ligmagex/-/blob/main/USERMANUAL.md?ref_type=heads&plain=0)

## Contributeurs
Axel MARTIN

Alexandre LECOMTE

Ivann VYSLANKO
