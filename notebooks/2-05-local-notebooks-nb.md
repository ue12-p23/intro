---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  formats: md:myst
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
  title: notebooks en local
---

+++ {"editable": true, "slideshow": {"slide_type": ""}, "tags": []}

Licence CC BY-NC-ND, Thierry Parmentelat & Valérie Roy

```{code-cell}
%%python
from IPython.display import HTML
HTML(filename="_static/style.html")
```

(label-notebooks-locally)=
# notebooks en local

Les notebooks sont de petits *cahiers* d'exercices exécutables. Ils sont très pratiques
pour expliquer pas à pas ce qu'on fait, comme dans ces cours mais ils ne servent pas
uniquement aux cours.

Nous allons vous montrer dans cette section comment installer et lancer `jupyter`,
**localement sur votre ordi**, pour créer des notebooks avec des cellules de texte
et des cellules de code...

+++

## dépendances supplémentaires

si vous êtes en train de lire un cours que vous avez cloné depuis github, et que celui-ci contient un fichier `requirements.txt`, alors tapez également cette commande

```bash
pip install -r requirements.txt
```

et de cette façon, vous aurez déjà toutes les librairies utilisées à l'intérieur des notebooks (typiquement numpy, pandas, et autres éventuellement plus exotiques)

+++

## utilisation de base

pour lancer un serveur jupyter vous tapez dans le terminal la commande

```bash
jupyter lab
```

````{note} notebook classic
:class: dropdown

si on préfère on peut aussi lancer ceci - c'est une interface un peu plus simple, mais le principe est grosso-modo le même

```bash
jupyter notebook
```
````

quelle que soit l'option choisie, le terminal va afficher plein de messages genre ceci

![](media/jlab-001-blob.png)

mais ça aura aussi pour effet, bien plus intéressant, d'ouvrir une fenêtre ou un onglet dans votre navigateur Web

![](media/jlab-002-welcome.png)

+++

### le processus serveur

en fait là on fait deux choses complémentaires

* on lance un programme (le serveur Jupyter) qui tourne dans le terminal
* on demande au browser de créer une page qui interagit avec ce serveur

du coup ça signifie que **le serveur Jupyter doit tourner en permanence**

* si vous le tuez depuis le terminal, le notebook dans le browser va cesser de fonctionner
* ça signifie aussi que cette session du terminal n'est plus utilisable pour autre chose…

+++

## micro-démo Jupyter lab

depuis le navigateur, vous pouvez vous déplacer dans le cours  
pour commencer allez dans le dossier `demo/notebooks` où vous verrez ceci

![](media/jlab-003-in-demo.png)

+++

### créer un notebook

créez un nouveau notebook, et appelez-le `foo` (*File* -> *Rename Notebook...*), vous devez voir maintenant ceci

![](media/jlab-004-new-notebook-foo.png)

+++

### créer des cellules mixtes

à présent arrangez-vous pour créer une nouvelle cellule, de sorte à avoir une cellule de texte suivie d'une cellule de code, comme ceci

![](media/jlab-005-mixed-cells.png)

+++

### gérer l'affichage

vous pouvez libérer de la place et supprimer le browser de fichiers sur la gauche

essayez de cliquer sur les boutons de la barre de gauche pour comprendre la logique

remarquez la troisième icône ![](media/jlab-006-toc-icon.png), qui permet d'afficher la table des matières

![](media/jlab-006-more-space.png)

+++

### mode édition ou commande

chaque cellule est dans un des deux modes :

* édition : pour changer le contenu d'une cellule (le texte que vous tapez va directement dans la cellule)
* commande : cette fois quand vous tapez un caractère il est interprété comme une commande
* pour sortir du mode édition : tapez `Escape` ou encore `Control-M`

voici à quoi ressemblent **nos deux cellules en mode 'commande'**

![](media/jlab-007-command-mode.png)

et maintenant **les mêmes en mode 'édition'** - la différence est un peu subtile 

![](media/jlab-007-edit-mode.png)

+++

### raccourcis utiles

autant prendre rapidement l'habitude d'utiliser les raccourcis clavier - ça va tellement plus vite !

parmi les plus fréquemment utilisés, il y a :

* `Shift-Entrée`: pour évaluer la cellule courante et passer à la suivante
* `⌥-Entrée`: pour évaluer la cellule et en insérer une dessous`
* `Control-M M` pour passer la cellule courante en `Markdown`
* `Control-M Y` pour passer la cellule courante en `Code` (y comme pYthon)

il y a aussi des raccourcis pratiques pour créer directement des sections

* `Control-M 1` met la cellule en markdown, et insère si nécessaire un `#` au début de la
  cellule; on crée ainsi une cellule de titre de rang 1
* `Control-M 2` : de rang 2, etc…

pour une liste exhaustive, à partir du menu, faites *Help* → *Keyboard Shortcuts*

````{note}
en fait, le préfixe `Control-M` est un raccourci pour **revenir en mode commande**  
et donc quand on dit que, par exemple, `Control-M M` fait passer en `Markdown`, il faut comprendre qu'en mode commande, la lettre `M` fait passer en `Markdown`; on ajoute juste le `Control-M` pour être sûr que la séquence marche dans les deux modes, mais si on est déjà en mode commande on n'a pas besoin de taper le `Control-M`
````

+++

### la palette

mimée sur celle de vs-code, il y a ici aussi une palette, que l'on invoque avec `Shift-Ctrl-C` (`Shift-Command-C` sur Mac)

c'est extrêmement utile pour trouver des commandes un peu évoluées, qui ne sont pas forcément toutes accessibles au travers d'un bouton dans l'interface

![](media/jlab-008-palette.png)

+++

### sélection multiple

* en général on a exactement **une** cellule courante
* mais avec `Shift-⬆` ou `Shift-⬇` on peut sélectionner plusieurs cellules contigües

![](media/jlab-009-multiple-selection.png)

c'est utile pour par exemple les déplacer toutes ensemble

+++

### déplacer les cellules

parlant de déplacer les cellules, on peut le faire à la souris comme ceci

![](media/jlab-010-move-cells.gif)

+++

## lire le cours localement (sur votre portable)

+++

### prérequis (rappels)

+++

#### indispensable

pour pouvoir ouvrir un notebook du cours - n'importe lequel - il faut avoir fait ceci

```console
pip install jupytext jupyterlab-myst
```

autrement, vous allez avoir un affichage bizarre…

+++

#### utile pour ce notebook

pour pouvoir exécuter les notebooks en bash (dont celui-ci, donc), il vous faut également
faire

```bash
pip install -r requirements.txt
```

````{note}
évidemment, pour pouvoir faire ceci, il faut d'abord avoir cloné le repo, car c'est dans le repo que se trouve le fichier `requirements.txt`
````

+++

### y'a plus qu'à

+++

à ce stade vous avez tout ce qu'il faut pour tout mettre ensemble, c'est-à-dire :

* cloner le repo du cours
* lancer jupyter à la racine

+++

puis vous pouvez

* ouvrir un des notebooks de démonstration (dans le dossier `demo/notebooks`)
  (je ne recommande pas forcément de commencer avec le présent notebook, car il utilise un
  kernel `bash` qui n'est pas standard…)
* l'exécuter localement
* et vous amuser à le modifier

+++

je vous demande surtout de

* ouvrir le notebook de checklist, qui résume les compétences attendues
* et vérifier que vous avez bien tout installé
* et si vous êtes en avance, attaquez-vous à l'exercice qui figure à la fin de la
  checklist
