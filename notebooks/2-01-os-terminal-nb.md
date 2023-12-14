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
  title: OS & terminal
---

Licence CC BY-NC-ND, Thierry Parmentelat & Valérie Roy

```{code-cell}
:tags: [raises-exception]

%%python
from IPython.display import HTML
HTML(filename="_static/style.html")
```

+++ {"slideshow": {"slide_type": ""}}

# OS & terminal

* votre OS (Operating System), c'est Windows, MacOS, ou linux
* quelques différences (très) visibles
* mais en réalité de très nombreux concepts communs

````{admonition} à quoi ça sert ?
:class: dropdown

* calculette  
  * un programme a accès à toutes les ressources
  * exemple : je range X dans la case mémoire 1
* ordinateurs
  * plein de programmes **en même temps**
  * accessoirement plein d'utilisateurs
````

+++ {"slideshow": {"slide_type": ""}}

````{admonition} rôle de l'OS
:class: dropdown

* fournir de l'**isolation** entre les programmes
  * si deux programmes différents utilisent la case mémoire 1  
    pour ranger une donnée, ça ne va pas le faire !

* permettre la **concurrence**
  * faire tourner plusieurs programmes en même temps  
    sur un nombre fini de processeurs  

  * lancez sur mac (\*) Activity Monitor   
    typiquement **plusieurs dizaines** de programmes

* fournir de l'**isolation** entre les utilisateurs


(\*) ou alors:  *Task Manager* sous Windows, et *top* sous linux
````

+++ {"slideshow": {"slide_type": ""}}

````{admonition} notion de **processus** (en anglais *process*)
:class: dropdown

* chaque programme qui tourne constitue un ***process***
* les process sont isolés les uns des autres  
  * notamment la mémoire
* l'OS fait tourner tous les programmes  
  * dans un mode ***chacun son tour***
  * à relativement haute fréquence
  * c'est le travail du *scheduler*
````

+++ {"tags": []}

````{admonition} soyons précis (pour les curieux)
:class: dropdown

le terme *OS* - *Operating System* a plein de significations différentes dans le langage
courant

* Windows et MacOS : incluent une interface graphique
* linux : l'interface graphique est plus clairement séparée, on a le choix

**mais** nous ici lorsqu'on parle d'OS, on désigne **seulement** ce qu'on appelle aussi le
**noyau**

c'est-à-dire techniquement :

* le **seul** programme dans l'ordinateur qui a **accès direct** aux périphériques
* qui "fait tourner" les programmes en leur donnant tour à tour accès au processeur
* et qui fait en sortes qu'ils soient **isolés les uns des autres**
* tous les autres programmes (*user land*) accèdent à ces ressources au travers
  d'**abstractions**

  * mémoire : **mémoire virtuelle**  
    la case mémoire '1' est redirigée vers un bout de mémoire allouée au programme  

  * **système de fichiers**  
    le disque dur est accessible au travers de dossiers et fichiers

  * **interface réseau** etc…
````

+++

## le terminal

le premier outil que nous allons voir c'est ce qu'on appelle le terminal;  
un terminal qu'est-ce que c'est ?

le terminal c'est tout simplement un programme (processus) qui permet de lancer d'autres programmes

ça peut paraitre moins pratique que de cliquer sur les icones du bureau...  
**MAIS** c'est **beaucoup plus puissant** parce que
- d'abord c'est de cette manière qu'on accède à des ressources distantes (cloud, cluster de calcul, ...)
- et surtout c'est un peu comme un langage de programmation, on peut faire en une ligne ce qui prendrait des heures avec un cliquodrome !

+++

### `bash`

il y a plein de types de terminal selon les systèmes d'exploitation, mais pour que nous
travaillions tous ensemble sur le même objet, nous allons choisir un terminal qui
s'appelle ``bash``

* `bash` vient avec l'installation de base sur MacOS et lzinux
* sur Windows, il faut l'installer séparément, on l'a vu avec ***git for
  windows***

+++

## dossiers et fichiers

le contenu du disque dur est organisé en **dossiers** et **fichiers**

le **dossier** est juste un cas particulier de fichier  

* qui **contient d'autres fichiers** (ou dossiers, donc)  
* au lieu de contenir des données

termes synonymes :

* dossier, répertoire, *folder*, *directory*: c'est tout pareil
* fichier, *file*: idem ce sont des synonymes

+++

### répertoire utilisateur (*home directory*)

chaque utilisateur possède un répertoire (synonyme de dossier),  
qui est la racine de l'arbre dans lequel il peut ranger ses affaires  
indépendamment du système d'exploitation

pour y aller le plus simple est de faire simplement `cd` sans paramètre

```{admonition} nouveau terminal

en principe, un terminal qui vient d'être créé a comme dossier courant le home directory  
c'est le cas sur MacOS et Linux  
toutefois sur Windows, en pratique ce n'est pas toujours le cas en fonction de votre setup  
aussi si vous êtes dans ce cas-là, prenez l'habitude de faire `cd` avant toute chose dans le terminal
```

```{code-cell}
# sans paramètre je vais tout en haut de mon espace
# c'est mon home-directory

cd
```

```{code-cell}
# pour voir où il est
# pwd = print working directory

pwd
```

### répertoire courant et chemins relatifs

tous les programmes (processus) ont ce qu'on appelle un répertoire courant

dans le terminal on peut le voir avec la commande `pwd` comme on vient de le faire 

c'est uniquement une **commodité** pour ne pas avoir à retaper le chemin complet depuis la
racine des dossiers

voyons ça sur un exemple; je vous invite à expérimenter tout ceci dans votre propre terminal  
(et sans taper les `$ ` évidemment)

`````{admonition} screenshot
:class: note

````{div}
```{image} media/fig-bash-relative-paths.png
:width: 600px
```
````
`````

`````{admonition} à noter sur cet exemple
````{div}
* la commande `ls` permet d'afficher le contenu d'un dossier
  ou de vérifier si un fichier existe
* vous voyez que, parce qu'on est dans le dossier `intro`  
  on n'a **pas besoin** de taper **tout le chemin** qui mène à `README.md`  
  c'est parce que `README.md` est considéré comme **relatif** au dossier courant  
* une fois que je change de dossier en allant dans `demo/python`, je ne **trouve plus** le fichier `README.md`
  if faut que je dise bien qu'il est en fait deux étages plus haut
  en indiquant `../../README.md` (car `..` signifie le dossier parent)
* je peux faire tourner le programme `fact.py`
  sans précider le dossier de `fact.py`
  car il est dans le même dossier que moi
* je *peux aussi* bien sûr lancerle même programme en donnant son **chemin absolu**
  remarquez que cette forme marcherait alors quel que soit mon dossier courant !
* remarquez enfin que le programme `python` a été trouvé comme étant en fait `/c/miniconda/python`
  c'est grâce à cette fameuse variable `PATH` que le programme d'installation de conda a modifiée pour nous
````
`````

+++

### `.` et `..`

par convention:

* `.` désigne le répertoire courant
* `..` désigne le répertoire "au dessus" du répertoire courant  
  on l'utilise pour fabriquer des chemins du genre de

      ls ../frere/neveu

pour "remonter" dans l'arborescence des dossiers, je peux donc utiliser un chemin relatif  
comme on l'a fait un peu plus haut d'ailleurs

+++

### `cd -` (avancé)

enfin, une astuce utile c'est pour **revenir en arrière** avec `cd -`  
avec cette commande, vous retournez au dossier où vous étiez avant le dernier `cd`

```bash
$ pwd
/c/Users/Jean Mineur
$ cd cours-info/intro
$ pwd
/c/Users/Jean Mineur/cours-info/intro
$ cd -
$ pwd 
/c/Users/Jean Mineur
$ cd - 
$ pwd
/c/Users/Jean Mineur/cours-info/intro
```

+++

## organisation en dossiers: quelques conseils

quelques conseils pour organiser votre travail en dossiers

+++

### un raccourci vers `cours-info`

le *homedir*, c'est une racine tentante pour mettre ses affaires, mais souvent il y a pas
mal de fourbis dès le départ; sur Windows par exemple si vous regardez son contenu
(faites-le !), vous verrez que c'est pas mal encombré

c'est pourquoi on vous a demandé de créer un dossier `cours-info` dans lequel on va ranger vos différents dossiers: chaque cours dans un repo, puis au besoin un dossier par exercice ou TP ou hackaton, etc...

je vous recommande de passer 5 minutes pour ajouter ce dossier dans les **raccourcis de votre explorateur de fichiers*
de cette façon vous y aurez un accès direct en un clic, comme ceci

```{image} media/fig-quick-access-cours-info.png
:width: 600px
```

+++

### ne pas abuser sur la profondeur des arbres  

dans tous les cas, évitez de couper les cheveux en 4 en créant plein de sous-répertoires, genre :

~~`/User/jeanmineur/Desktop/git/mines/première-année/info/ue12/numerique`~~

+++

### noms de fichiers

c'est assez facile (avec l'explorateur de fichiers notamment) de créer des fichiers dont
le nom contient des caractères biscornus, comme des espaces ou des accents

mais après ça devient rapidement compliqué de les utiliser, dans le terminal notamment

c'est pourquoi on recommande d'**éviter les espaces et les accents** dans les noms de
fichiers

+++ {"tags": []}

### affichez les extensions dans les noms de fichier

dans l'explorateur Windows par défaut, si vous créez un fichier `foo.txt` on va vous
montrer dans l'explorateur de fichiers une entrée qui s'affiche avec simplement `foo`

par défaut, on a jugé que c'était "plus simple" de ne pas montrer l'extension, ici `.txt`  
personnellement je ne trouve pas ça très pratique…

voici comment on peut changer ce comportement, pour voir les noms de fichier en entier,
i.e. comme avec le terminal


```{image} media/fig-show-extensions-1.png
:width: 600px
```

```{image} media/fig-show-extensions-2.png
:width: 600px
```

+++

## quelques commandes `bash` utiles

+++

### commandes utiles

+++

voici pour résumer un rappel des commandes bash les plus simples et les plus utiles

| commande | fonction |
|-:|:-|
| `cd` | changer de dossier courant |
| `pwd` | afficher le dossier courant |
| `ls` | lister les fichiers et dossiers dans le dossier courant |
| `mkdir` | créer un dossier |
| `rm` | supprimer des fichiers - **attention** ils sont supprimés pour de bon et non pas placés dans la corbeillle |
| `echo un message` | pour afficher du texte |
| `cat unfichier` | pour afficher le contenu d'un (ou plusieurs) fichier |

+++

### redirections

plutôt que d'afficher la résultat d'une commande dans le terminal, il est parfois pratique de rediriger cela dans un fichier

par exemple si j'écris dans le terminal

  ```bash
  # je crée ou j'écrase le fichier foo.txt
  echo "un petit fichier bidon" > foo.txt
  ```

ce qui va se passer c'est que je vais créer (ou écraser) le fichier `foo.txt` pour y ranger dedans la chaine  
`un petit fichier bidon\n`

le dernier cararactère (`\n`) correspond à un **saut de ligne**

+++

### *globbing*

si j'ai plusieurs fichiers qui se terminent en `.txt`, je peux les lister avec la notation en `*` comme ceci

  ```bash
  # je crée (ou j'écrase) un second fichier bar.txt
  $ echo "un autre fichier bidon" > bar.txt
  ```

de là je peux lister tous les fichiers qui se terminent en .txt

  ```bash
  $ ls *.txt
  bar.txt foo.txt
  ```
ou tous ceux qui commencent par un f

   ```bash
   $ ls f*
   foo.txt
   ```

ou toute combinaison du même genre

   ```bash
   $ ls f*txt
   foo.txt
   ```

+++

#### à n'importe quelle profondeur

  ```bash
  # si je veux chercher tous les fichiers en *.txt
  # à n'importe quelle profondeur sous mon dossier courant

  ls **/*.txt
  ```

+++ {"tags": ["level_intermediate"]}

#### les crochets `[]` (avancé)

  ```bash
  # on peut aussi utiliser les [] 
  # ici tous les fichiers qui commencent par un f ou un b et qui finissent en .txt

  ls [fb]*.txt
  ```
