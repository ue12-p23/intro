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

## la complétion

```{code-cell}

```

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
