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
:class: seealso dropdown

il nous faut a minima

* le terminal - nous utilisons **`bash`**, qui est
  * natif sur les OS linux et MacOS,
  * et qui vient avec le produit `git for windows`
* l'éditeur de code **VS-code** (Visual Studio Code)
* **miniconda** pour **Python** (et les environnements virtuels)
* **Jupyter** pour les notebooks
  * on parlera un peu de *markdown* pour la mise en forme du texte,
  * et de $\LaTeX$ pour les formules mathématiques
* et enfin **`git`** pour la gestion de versions  
  c'est un outil super-utile pour le développement, c'est indispensable que vous sachiez l'utiliser
````

+++

## généralités

pour commencer voici quelques recommandations générales:

* quelle que soit la plateforme, on s'efforce dans tous les cas où c'est possible d'installer **en mode user** et non pas en mode administrateur; l'idée d'installer en mode administrateur c'est de faire l'installation pour plusieurs utilisateurs à la fois, mais dans notre cas ça n'a aucun intérêt; et par contre l'installation en mode administrateur vient avec pas mal d'inconvénients, et notamment de devoir rebasculer sans arrêt en mode adminsitateur...

* sur Mac, quand vous installez une application - comme par exemple vs-code - il est trés important **de copier l'application dans le dossier `Applications`** - on aura l'occasion d'en reparler

* après avoir installé, disons par exemple vs-code, on va vérifier que ça a marché  
  et pour ça on vous dit de taper dans le terminal `code .`  
  mais en fait l'installation de vs-code modifie la façon **dont s'initialise** le terminal
  et du coup ça n'affecte pas les terminaux créés avant l'installation   
  du coup prenez l'habitude de **lancer un nouveau terminal après une installation**  

  ceci est notamment pertinent lorsque vous recevez une erreur comme  
  `code: command not found`  
  si ce symptôme persiste même après avoir essayé dans un nouveau terminal, c'est que l'installation s'est mal passée

  ````{admonition} le PATH (pour les curieux)
  :class: dropdown note

  le `PATH` c'est le mécanisme qui permet au terminal de trouver les commandes

  du coup quand on installe un nouveau logiciel, comme on va le faire tout de suite avec
  'git for windows', il est parfois nécessaire de modifier le `PATH` pour que les nouvelles
  commandes deviennent accessibles depuis le terminal

  ce n'est pas crucial de le savoir, mais si vous êtes curieux, sachez que

  * `PATH` c'est ce qu'on appelle une variable d'environnement (ça veut dire qu'elle se
    propage d'un processus à l'autre),

  * et que c'est une liste de répertoires où sont cherchées les commandes

  ```bash
  # un exemple sur linux/macos
  # le ':' est un séparateur
  $ echo $PATH
  /opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
  ```
  ````

+++

## installation de git (et bash sur Windows)

### Windows 

en installant ***git for windows*** on va faire d'une
pierre deux coups, et installer à la fois `bash` et `git`

* allez sur le site là  <https://gitforwindows.org/>
* téléchargez et lancez l'installation...
* vous pouvez prendre toutes les options par défaut

````{admonition} on peut prendre toutes les options par défaut
:class: dropdown seealso

et entre autres, à la question ***Adjusting your PATH environment*** :  
choisissez au moins l'option recommandée (#2), idéalement l'option #3

![](media/fig-set-path-git-for-windows.png)
````

+++

### Mac et Linux

bash est préinstallé; pour git, utilisez ce lien:  
<https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git>

* rien de particulier à signaler sur linux, c'est sans doute déjà installé, et sinon c'est trivial
* par contre pour les Mac: **attention ça peut être long !!** la méthode recommandée passe par l'activation de Xcode, un peu de patience sera nécessaire..

+++

***
***
***

+++

## installation de vs-code

[vs-code - toutes les plateformes](label-install-vscode)

+++

## installation de miniconda (pour Python, IPython et Jupyter)
[Python - toutes les plateformes](label-install-python)

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
