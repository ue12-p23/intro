---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  encoding: '# -*- coding: utf-8 -*-'
  notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version, -jupytext.text_representation.format_version,
    -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
    -language_info.file_extension, -language_info.mimetype, -toc
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Calysto Bash
  language: bash
  name: calysto_bash
language_info:
  help_links:
  - text: MetaKernel Magics
    url: https://metakernel.readthedocs.io/en/latest/source/README.html
  name: bash
nbhosting:
  title: vs-code et Python
---

Licence CC BY-NC-ND, Thierry Parmentelat & Valérie Roy

```{code-cell}
---
editable: true
slideshow:
  slide_type: ''
tags: [raises-exception]
---
%%python
from IPython.display import HTML
HTML(filename="_static/style.html")
```

# Python

+++

xxx à recaser qlq part

+++

```{admonition} pour être sûr
:class: note

en théorie c'est tout ce qu'il y a à faire pour installer conda

toutefois certains élèves nous ont signalé un souci, aussi à ce stade on vous recommande de
* lancer un nouveau terminal
* et dedans lancer `conda init bash`
```

+++



+++

### lancer python en mode interactif

depuis `GitBash`, on va lancer un Python interactif et lui faire calculer $2^{100}$,
afficher un texte, puis quitter l'interpréteur.

***

<div class=outline>

<span class="red-pill">quelques limitations connues :</span>

* lancer simplement `python` dans `GitBash` ne fonctionne pas  
  (le programme n'affiche pas le prompt et semble boucler sans rien afficher)

* dans `GitBash` vous **devez** tapez à la place `python -i`  
  (le `-i` est pour *interactive*) pour avoir un interpréteur interactif

* depuis le terminal embarqué dans vscode, vous pouvez faire simplement `python`  
  (`python -i` fonctionne bien aussi d'ailleurs)

* depuis GitBash et le terminal vs-code, vous pouvez lancer normalement `ipython`  
  (dont on parle un peu plus bas)

</div>

***

```console
pensez à bien mettre le -i - voyez ci-dessus
$ python -i
>>> 2 ** 100
1267650600228229401496703205376
>>> print("hello world")
hello world
>>> exit()
```

+++

### créer et lancer un premier script

+++

dans le répertoire de votre choix, ouvrez *vs-code* et créez un fichier qui s'appelle
`fact.py` contenant ce texte (n'hésitez pas à copier-coller) :

```{code-cell}
cat ../demo/python/fact.py
```

et dans le même répertoire lancez python pour exécuter ce programme, et donc calculer et afficher le factoriel de deux nombres

```{code-cell}
python ../demo/python/fact.py 10
```

### afficher le numéro de version de Python

+++

c'est toujours utile d'être bien sûr de la version qu'on a sous la main (surtout avec les
environnments virtuels)

```{code-cell}
python --version
```

## installations complémentaires

+++

### tout en un: `pip install`

voici un bloc de commandes que vous pouvez copier-coller **dans le terminal**  
pour faire en un seul coup toutes les installations dont on aura besoin

par contre cela peut prendre un moment...

```bash
pip install ipython 
pip install numpy pandas matplotlib
pip install -U jupyter
pip install -U jupytext jupyterlab-myst

jupytext-config set-default-viewer
```

+++

#### pourquoi `pip install -U`

````{admonition} un mot à propos de notebook 7
:class: dropdown note

depuis Juillet 2023, la version de `jupyterlab` est la 4.x, et la version de `notebook` est la 7.x.

si vous avez installé votre environnement avant cette date, il se peut que vous ayez
des versions plus anciennes, typiquement `notebook` en 6.x et `jupyterlab` en 3.x;
et dans ce cas il est recommandé de mettre à jour votre installation,
c'est la raison pour laquelle les commandes ci-dessus contiennent `pip install -U`
qui signifie *mettre à jour*
````

+++

#### pourquoi `jupytext-config` 

````{admonition} à quoi sert la config jupytext ?
:class: dropdown note

en l'absence de cette dernière commande, vous pouvez toujours ouvrir les notebooks jupytext,
mais il faut passer par *Clic droit* → *Open with* → *Notebook*  
une fois que vous aurez exécuté la commande ci-dessus, vous pourrez ouvrir les notebooks
simplement en double-cliquant dessus
````

+++

### vérifier les librairies installées avec `pip list`

```bash
# pour obtenir la liste des librairies installées (possiblement beaucoup)
pip list
# pour voir la version installée de UNE librairie, par exemple
pip show numpy
```

+++

### micro-démo `ipython`

si vous devez taper du code Python directement dans le terminal, je vous recommande
d'utiliser la commande `ipython` plutôt que l'interpréteur standard `python`

voilà à quoi ça ressemblerait si on devait refaire le calcul de $2^{100}$ comme on l'a
fait plus haut


```console
$ ipython
Python 3.8.3 (default, Jul  2 2020, 11:26:31)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.16.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 2 ** 100
Out[1]: 1267650600228229401496703205376

In [2]: print("hello world")
hello world

In [3]: exit()
```

comme vous le voyez c'est presque pareil; simplement avec ipython c'est beaucoup plus
pratique dès qu'on va au delà de ce genre de session de démo, notamment pour

* remonter et modifier l'historique
* obtenir de l'aide en ligne
* utiliser la complétion

+++

### vérification de numpy

comme on l'a vu pour vérifier, vous pouvez d'abord, depuis le terminal, faire
```bash
pip show numpy
```
qui vous montrera en plus le numéro de version de `numpy`

+++

vous pouvez aussi importer la librairie `numpy` depuis `ipython`, ça donne une session qui
ressemble à ceci (vous ne devez pas avoir d'erreur du type `ModuleNotFound`)

```
$ ipython
Python 3.8.3 (default, Jul  2 2020, 11:26:31)
<blabla>

In [1]: import numpy

In [2]: numpy.__version__
Out[2]: '1.19.1'
```

+++

### vérification de jupyter

si tout s'est bien passé vous devez pouvoir voir les versions des différents morceaux de
Jupyter comme ceci :

```{code-cell}
jupyter --version
```

## la complétion

+++

ce qu'on appelle complétion, c'est la capacité d'un outil à vous aider à taper votre code;
exemple :

* on lance `ipython`
* on tape le début d'une commande, par exemple `import frac`
* à ce point, on appuie sur la touche `Tabulation`
* ipython se rend compte que le seul mot qui fait du sens dans ce contexte et qui commence
  par `frac` est `fractions`, du coup il remplit la commande

+++

la complétion est un outil **indispensable** pour ne pas perdre un temps précieux;
apprenez à la maitriser

notez d'ailleurs que **ça existe aussi dans le terminal**, typiquement très utile avec les
noms de fichiers, entre autres

+++

## *RTFEM*

+++

il est normal de faire des erreurs quand on code, tout le monde en fait

on verra un peu plus loin comment les détecter le plus tôt possible (grâce à des
extensions dans un éditeur de code)  
mais les cas où ça se produit quand même, la première chose à faire est bien entendu de
**lire le message d'erreur**

le langage Python s'efforce de vous donner des indications plutôt claires dans ces cas-là

+++

voici par exemple un fichier très proche de `fact.py` qu'on vient de faire tourner  
mais j'y ai intentionnellement glissé une petite erreur de syntaxe  
voici le code, et ce qui se produit si on essaie de le faire tourner

```{code-cell}
:cell_style: split

cat ../demo/python/fact-broken.py
```

```{code-cell}
:cell_style: split

python ../demo/python/fact-broken.py
```

je vous demande en exercice de trouver l'erreur en question

+++

en pratique il arrive qu'on se trouve face à des erreurs plus difficiles à diagnostiquer,
mais dans tous les cas **commencez par *RTFEM***  
ça va de soi mais ça va mieux en le disant, je suis certain qu'on aura l'occasion de le
rappeler pendant les cours de langage :)

+++

## `autoreload` avec IPython ou les notebooks

**le problème**: vous êtes dans `ipython` ou dans un notebook, et vous faites

```python
from my_module import my_function
my_function(...)
```

et puis ensuite un peu plus tard, vous modifiez `my_module.py` sous vs-code, et vous
voulez essayer la nouvelle version; votre première idée est de refaire l'import pour
recharger le module dans l'interpréteur

là attention, **un second `import` ne recharge pas le fichier** c'est le
comportement attendu, et souhaitable, car charger un module est coûteux; c'est
pourquoi l'interpréteur garde en mémoire les modules qu'il a déjà chargés, et du
coup vous pouvez ré-importer autant que vous voulez, vous allez toujours utiliser
le premier code, et non le nouveau

**la solution**: avec l'astuce suivante, vous n'aurez plus besoin de ré-importer,
vous pourrez juste ré-exécuter `my_function()` et vous utiliserez la dernière
version du module (pour autant que le nouveau module ne contienne pas d'erreur qui
empêche son chargement, bien entendu)

il vous suffit de copier-coller les lignes suivantes dans un terminal bash

```bash
mkdir -p ~/.ipython/profile_default
cat >> ~/.ipython/profile_default/ipython_config.py << EOF
c.InteractiveShellApp.exec_lines = []
c.InteractiveShellApp.exec_lines.append('%load_ext autoreload')
c.InteractiveShellApp.exec_lines.append('%autoreload 2')
EOF
```

````{admonition} pour les curieux
:class: dropdown note

pour ceux qui veulent comprendre, ce script

* commence par s'assurer que le dossier `.ipython/profile_default` existe sous le home directory
* puis dans ce dossier, il ajoute dans le fichier `ipython_config.py` les 3 lignes de configuration qui précèdent le `EOF` (c'est du Python bien sûr)
````
