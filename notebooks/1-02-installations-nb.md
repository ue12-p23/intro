---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version, -jupytext.text_representation.format_version,
    -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
    -language_info.file_extension, -language_info.mimetype, -toc
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
nbhosting:
  title: fast track installations
---

Licence CC BY-NC-ND, Thierry Parmentelat & Valérie Roy

```{code-cell} ipython3
:tags: [raises-exception]

%%python
from IPython.display import HTML
HTML(filename="_static/style.html")
```

# installations

ce notebook devrait vous permettre de faire toutes les installations nécessaires

```{contents}
:depth: 3
```

+++

## la liste des outils

````{admonition} la liste des outils
:class: admonition

il nous faut a minima

* le terminal - nous utilisons **`bash`**, qui est
  * natif sur les OS linux et MacOS,
  * et qui vient avec le produit `git for windows`
* **`code`**, l'éditeur de code Visual Studio Code, mieux connu comme vs-code
* **miniconda** pour **`python`** (et les environnements virtuels)
* **`jupyter`** pour les notebooks
  * on parlera un peu de *markdown* pour la mise en forme du texte,
  * et de $\LaTeX$ pour les formules mathématiques
* et enfin **`git`** pour la gestion de versions  
  c'est un outil super-utile pour le développement, c'est indispensable que vous sachiez l'utiliser
````

+++

## généralités

pour commencer voici quelques recommandations générales:

+++

### créez un nouveau terminal !

après avoir installé, disons par exemple vs-code, on va vérifier que ça a marché  
et pour ça on vous dit de taper dans le terminal `code .`  
mais en fait l'installation de vs-code modifie **la façon dont s'initialise** le terminal  
et du coup ça n'affecte pas les terminaux créés avant l'installation   
il faut donc prendre l'habitude de **lancer un nouveau terminal après une installation**  

ceci est notamment pertinent lorsque vous recevez une erreur comme  
`code: command not found`  
si ce symptôme persiste même après avoir essayé dans un nouveau terminal, c'est que l'installation s'est mal passée

````{admonition} le PATH (pour les curieux)
:class: dropdown tip

le `PATH` c'est le mécanisme qui permet au terminal de trouver les commandes

du coup quand on installe un nouveau logiciel, comme on va le faire tout de suite avec
*git for windows*, il est parfois nécessaire de modifier le `PATH` pour que les nouvelles
commandes deviennent accessibles depuis le terminal

ce n'est pas crucial de le savoir, mais si vous êtes curieux, sachez que

* `PATH` c'est ce qu'on appelle une variable d'environnement (ça veut dire qu'elle se
  propage d'un processus à l'autre),

* que c'est une liste de répertoires où sont cherchées les commandes

```bash
# un exemple sur linux/macos
# le ':' est un séparateur
$ echo $PATH
/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

* et qu'elle est le plus souvent définie/modifiée dans un fichier caché qui s'appelle `.bashrc` dans votre homedir

````

+++

### comment bien installer sur MacOS

sur Mac, quand vous installez une application - comme par exemple vs-code - il est trés important **de copier l'application dans le dossier `Applications`** - on aura l'occasion d'en reparler

+++

### ne pas installer en mode administrateur

quelle que soit la plateforme, on s'efforce dans tous les cas où c'est possible d'installer **en mode user** et non pas en mode administrateur; l'idée d'installer en mode administrateur c'est de faire l'installation pour plusieurs utilisateurs à la fois, mais dans notre cas ça n'a aucun intérêt; et par contre l'installation en mode administrateur vient avec pas mal d'inconvénients, et notamment de devoir rebasculer sans arrêt en mode administrateur...

+++

## installation de git (et bash sur Windows)

+++

````{admonition} Windows
:class: dropdown seealso

en installant ***git for windows*** on va faire d'une
pierre deux coups, et installer à la fois `bash` et `git`

* allez sur le site là  <https://gitforwindows.org/>
* téléchargez et lancez l'installation...
* vous pouvez prendre toutes les options par défaut

```{admonition} on peut prendre toutes les options par défaut
:class: dropdown tip

et entre autres, à la question ***Adjusting your PATH environment*** :  
choisissez au moins l'option recommandée (#2) - on peut prendre l'option (#3) si on veut importer plus d'outils dans le terminal, mais ce n'est pas strictement nécessaire pour le cours

![](media/fig-set-path-git-for-windows.png)
```
````

+++

````{admonition} Mac et Linux
:class: dropdown seealso

bash est préinstallé; pour git, utilisez ce lien:  
<https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git>

* rien de particulier à signaler sur linux, c'est sans doute déjà installé, et sinon c'est trivial
* par contre pour les Mac: **attention ça peut être long !!** la méthode recommandée passe par l'activation de Xcode, un peu de patience sera nécessaire..
````

+++

````{admonition} on vérifie
:class: important dropdown

vous devez pouvoir

* lancer un terminal `bash`  
  pour Windows, cherchez *bash* dans le menu Démarrer, et n'hésitez pas à faire en sorte que ce programme, *Git Bash*, reste dans la barre des tâches même lorsqu'il est inactif; ça vous facilitera la vie
* pour vérifier que c'est bien du `bash` - et pas du *PowerShell* par exemple, tapez
  ```bash
  echo $BASH_VERSION
  ```
  qui doit répondre
  ```
  5.2.15(1)-release        # c'est un juste exemple hein
  ```
* pour vérifer que vous avez bien installé `git`:
  ```bash
  $ git --version
  git version 2.41.0       # pareil, la réponse peut être différente chez vous
  ```
  **remarque**  
  dans cette forme, le `$` signifie que j'ai tapé `git --version`  
  et que ça m'a répondu `git version 2.41.0`  
  c'est pour abréger un peu  
  pensez bien à **ne pas taper le `$` vous même**  
  car bien sûr ça va marcher beaucoup moins bien si vous le faites ;)
* si vous n'avez pas **au moins la version 2.23**, faites-vous connaitre; le mieux serait de mettre à jour pour obtenir une version plus récente, car certains éléments du cours sur git ne vont pas fonctionner chez vous...
````

+++

## exercice: le dossier `cours-info`

depuis le terminal on peut tout faire ! et pour commencer on va apprendre à créer un dossier  
c'est dans ce dossier qu'on vous invite à travailler pendant les cours d'info

* créez un nouveau terminal
* allez dans votre homedir en faisant simplement
  ```bash
  cd
  ```
  ```{admonition} à quoi ça sert ?
  :class: note dropdown
  
  sur mac et linux, c'est optionnel car le terminal démarre justement dans le homedir  
  par contre sur Windows c'est bien de prendre l'habitude de faire un premier `cd` au début du terminal car il arrive que le terminal démarre dans un autre dossier...
  ```
* créez un dosser `cours-info`
  ```bash
  mkdir cours-info
  ```
* allez dans ce dossier
  ```bash
  cd cours-info
  ```
* maintenant ouvrez votre **explorateur de fichiers**, et constatez qu'on a bien créé un dossier qui s'appelle `cours-info`

+++ {"jp-MarkdownHeadingCollapsed": true}

## installation de vs-code

nous demandons à **tous** les élèves d'installer et de savoir utiliser vs-code  
il s'agit d'un **éditeur de code**, c'est ce qu'on va utiliser pour écrire nos programmes  

```{admonition} pas de pyzo
:class: error

il y a eu **beaucoup de problèmes** les années passées avec les éditeurs de type *pyzo*  
ne les utilisez surtout pas dans nos cours, vous allez perdre un temps précieux et en faire perdre à vos enseignants pour des raisons inintéressantes, et extérieures à Python
```

````{admonition} installation (toutes plateformes)
:class: seealso dropdown

On y va. Le site est là <https://code.visualstudio.com/>. Vous voulez installer donc il va
falloir que vous alliez dans une section *download* ... vous la voyez ?  
à vous de jouer maintenant

```{admonition} pour les Mac
:class: warning dropdown

**Attention**  

on l'a signalé déjà rapidement, mais la bonne façon d'installer une appli sur MacOS en général est de la glisser-déplacer dans le dossier `Applications`  

aussi une fois que vous aurez téléchargé, et double cliqué sur le zip, vous allez voir un fichier de type `.app`, **qui se trouve dans votre dossier `Downloads`**  
**il est impératif** de glisser-déplacer ce fichier dans le dossier `Applications`  
si on ne le fait pas, ça semble fonctionner, mais on a des tas de problèmes assez retors par la suite

```
````


````{admonition} on vérifie
:class: important dropdown

* dans **un nouveau terminal** (voir + haut)  
  ```bash
  code --version
  1.84.2
  1a5daa3a0231a0fbba4f14db7ec463cf99d7768e
  x64
  ```
  qui doit afficher un numéro de version (et d'autres détails)  
* si à la place vous voyez  
  ```
  code: command not found
  ```
  d'abord vérifiez que vous avez bien essayé **dans un nouveau terminal** (oui je sais...)  
  et sinon [allez voir cette page](label-troubleshoot-code-command-not-found)
* lorsque ça fonctionne, prenez l'habitude de lancer vs-code comme ceci
  ```bash
  # first I want to choose in which folder I am going to work
  cd 
  cd cours-info
  code .
  ```
* et tant que vous y êtes, activez le mode *Auto Save*:  
  ⮑ dans le menu *File*, cliquez sur *Auto Save* (ça ajoute une check mark)  
  l'effet de ce réglage est que vos modifications sont sauvées toutes seules, pas besoin de *Control-S* sans arrêt
````

+++

## installation de miniconda (pour Python, IPython et Jupyter)

* il y a de très nombreuses distributions de Python disponibles
* notre choix : **miniconda**
  * relativement léger
  * permet d'installer en mode "user", c'est-à-dire sans droits administrateur
  * permet également de fabriquer des environnements virtuels (pas de panique, on n'utilisera pas ça tout de suite, mais c'est une possibilité qui devient vite intéressante)
* (ça va sans le dire mais ne prenez **surtout pas Python 2.7** !)

+++

```````{admonition} Windows
:class: seealso dropdown

``````{div}

`````{admonition} préparation
:class: seealso dropdown

````{div}
une première précaution, spécifique à Windows:  
il s'agit de contourner un bug dans l'installateur conda, qui se déclenche lorsqu'on choisit un dossier d'installation dans le nom duquel se trouve un caractère accentué ou un espace

du coup, nous allons pour commencer créer un dossier dont le nom est court et simple,
et **qui ne contient pas d'accent** (c'est très important que le chemin complet pour
accéder au dossier où on installe miniconda ne comporte pas d'accents.)

pour cela nous allons lancer la console Windows qui s'appelle `PowerShell`, et créer le
dossier `c:/miniconda`

en deux étapes, ça se présente comme ceci :

1. pour lancer la console `PowerShell`

```{image} media/fig-miniconda-powershell-locate.png
:width: 500px
```

2. on va créer maintenant le dossier dans lequel on installera ensuite miniconda,
et pour cela il y a une seule ligne à taper

```console
md c:/miniconda
```

```{image} media/fig-miniconda-powershell-md.png
:width: 500px
```

une fois la commande tapée vous pouvez sortir de PowerShell (utiliser la croix en haut à
droite par exemple)
````
`````



`````{admonition} download
:class: seealso dropdown

````{div}
cherchez sur google *`download miniconda`*  
vous allez trouver une page qui ressemble à ceci

```{image} media/fig-miniconda-download.png
:width: 500px
```

puisqu'on est sur Windows, on n'a pas le choix, téléchargez le `*.exe`  
(avant de le lancer, voyez l'étape suivante pour les réponses aux questions...)
````
`````



`````{admonition} les réponses aux questions
:class: seealso dropdown

````{div}
vous lancez le `.exe`  
et vous prenez toutes les options par défaut lorsqu'on vous pose une question  
**sauf pour les deux écrans qui suivent**

**(1) le choix du dossier où installer**  
sur cet écran vous remplacez le chemin qu'on vous propose par défaut, et vous
choisissez à la place le dossier qu'on a créé dans l'étape précédente, c'est-à-dire
`c:\miniconda`

```{image} media/fig-miniconda-set-install-dir.png
:width: 500px
```

<div style="height: 0.5cm"></div>

**(2) advanced options: *add to my PATH environment variable***  
il est important de **bien cocher la case ci-dessous** (malgré l'avertissement en rouge)

```{image} media/fig-miniconda-install.png
:width: 500px

```

si par mégarde vous êtes allé jusqu'au bout sans cocher cette case: relancez l'installation en faisant bien attention !
````
`````
``````
```````

+++

```````{admonition} MacOS
:class: seealso dropdown

``````{div}

`````{admonition} préparation: Intel ou M1 ?
:class: seealso dropdown

````{div}
c'est important que vous sachiez dire si votre Mac a une puce Intel ou M1 (en fait pour l'installation miniconda, M1 ou M2 c'est pareil..)  
et pour ça c'est simple, il suffit d'ouvrir le menu Pomme -> *About This Mac* où vous trouver l'information ici

```{image} media/fig-macos-about.png
:width: 400px
```
````
`````


`````{admonition} download
:class: seealso dropdown

````{div}
cherchez sur google *`download miniconda`*  
vous allez trouver une page qui ressemble à ceci

```{image} media/fig-miniconda-download.png
:width: 500px
```

vous téléchargez la seule entrée de type **`.pkg`** qui correspond à votre architecture  
une fois le download terminé, vous double-cliquez sur le `.pkg`  
il n'y a pas de choix particulier où on pourrait se tromper..
````
`````
``````
```````

+++

```````{admonition} Linux
:class: seealso dropdown

``````{div}
`````{admonition} download
:class: seealso dropdown

````{div}
cherchez sur google *`download miniconda`*  
vous allez trouver une page qui ressemble à ceci

```{image} media/fig-miniconda-download.png
:width: 500px
```

vous téléchargez la première entrée pour Linux (`Linux 64-bit`), les autres correspondent à des architectures différentes de celles qu'on trouve usuellement sur un ordi personnel
````
`````


`````{admonition} pour lancer l'installation
:class: seealso dropdown

````{div}
```bash
# just in case: go back to homedir
cd 
# go to the folder where download has ended up
cd Downloads
# making sure: list files that start with 'Miniconda3'
ls Miniconda3*
# very probably you will see only one file here, named 
# Miniconda3-latest-Linux-x86_64.sh
# (unless of course you download several times..)
#
# in any case, the way to actually run such a program is

bash Miniconda3-latest-Linux-x86_64.sh
```

les questions/réponses se passent dans le terminal, voici quelques trucs utiles:

- pendant le *License Agreement* on vous faire lire les conditions de la licence
  - pour avancer dans le document tapez *Espace*
  - pour abréger, tapez simplement *`q`*
- à la question  
  `Do you wish to update your shell profile to automatically initialize conda?`  
  on recommande de répondre `yes`
````
`````
``````
```````

+++

`````{admonition} on vérifie
:class: important dropdown

et on fait quoi pour vérifier ? on crée un **nouveau terminal** !

````{admonition} le prompt (rappel)
:class: dropdown

* les signes `$ ` ou `>>> ` ne font pas partie de ce que vous devez taper
* c'est juste une indication pour dire
  * avec `$ ` :  que la commande s'adresse au terminal  
  c-à-d à nouveau : GitBash sur Windows, Terminal sur MacOS,  
  et n'importe quel terminal bash sur linux

  * avec `>>> ` : que la commande s'adresse à l'interpréteur Python

ça signifie que ce que vous voyez ici correspond à ce qui sera affiché dans le terminal,
mais si vous suivez bien les indications vous n'avez pas à taper le `$` ou les `>>>`, ce
sera déjà affiché lorsque vous taperez vos commandes
````

````{admonition} quel python ?
:class: important dropdown

pour savoir si la commande `python` est connue, et si oui, où on l'a trouvée
```console
$ type python
```
(attention à ne pas coller le `$`, donc)  
qui doit vous répondre quelque chose comme
```console
# sur Windows avec notre setup vous devez avoir
python is /c/miniconda/python
# sur Mac par exemple je vois 
python is /c/Users/Thierry Parmentelat/miniconda3/python
```

si à ce stade vous avez un `python: not found` c'est que vous n'avez pas bien coché la case  
*Add Miniconda3 to my PATH environment variable*; dans ce cas le plus simple est de recommencer l'installation - [voir aussi ici](label-troubleshoot-python-command-not-found)

````

````{admonition} version de python
:class: important dropdown

pour savoir la version de python installée
```bash
$ python --version
Python 3.11.4
```
vous **devez** avoir une version 3.x, et **surtout pas** 2.7
````
  
`````

+++

## exercice: code + python

* créer un nouveau terminal
* aller dans le dossier `cours-info` (on fait comment déjà ?)
* lancez vs-code
  ```bash
  code .
  ```
* copiez-collez le code ci-dessous dans un fichier qui s'appelle `fact.py`
  ```python
  # une fonction qui calcule factorielle
  def fact(n):
      return 1 if n <= 1 else n * fact(n-1)


  # on affiche quelques résultats
  for n in [4, 25]:
      print(f"fact({n}) = {fact(n)}")
  ```
* exécutez le programme
  ```bash
  $ python fact.py
  fact(4) = 24
  fact(25) = 15511210043330985984000000
  ```


+++

## configuration git
[git - toutes les plateformes](label-setup-git)

+++

## configurations diverses

### autoreload

+++

## et pour se servir de tout cela

````{admonition} cloner le dépôt du cours
[clôner le dépôt du cours](label-clone-course)
````

````{admonition} ouvrir les notebooks sur votre ordi
[exécuter les notebooks sur votre ordinateur](label-notebooks-locally)
````

````{admonition} la checklist
[une vidéo et une liste de compétences](label-checklist)
````
