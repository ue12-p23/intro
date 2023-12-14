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
  title: installations
---

Licence CC BY-NC-ND, Thierry Parmentelat & Valérie Roy

```{code-cell} ipython3
:tags: [raises-exception]

%%python
from IPython.display import HTML
HTML(filename="_static/style.html")
```

# cloner et lire le cours

une fois que vous avez fait toutes les installations, la première chose que l'on va faire, c'est de *cloner* le cours, et de s'assurer que vous pouvez lire les notebooks **localement sur votre ordi**

c'est intéressant, d'abord pour vérifier que tout est bien en place (ce n'est pas grave si on ne vérifie pas forcément tout), et ce sera surtout utile pour le prochain cours puisque c'est comme cela que vous serez amené à travailler

+++

## cloner le cours


### trouver la bonne URL

à ce stade vous pouvez naviguer jusqu'au cours; pour cela, repartez de l'organisation qui va bien:

<https://github.com/ue12-p23/>

allez éventuellement à l'onglet *Repositories*, cliquez sur le cours `intro`

```{image} media/github-orga.png
:width: 600px
:align: center
```

dans cette page, on va aller copier l'URL du cours; pour cela suivez ceci:

```{image} media/github-choose-ssh.png
:width: 600px
:align: center
```

une fois que vous aurez cliqué sur l'icône "copier-coller" (étape 3), vous aurez copié dans votre presse-papier la chaine `git@github.com:ue12-p23/intro.git`; (si vous avez un truc qui commence en `https://` c'est que vous n'avez pas bien choisi `SSH`

```{admonition} prenez toujours SSH
:class: warning

à partir de maintenant, prenez l'habitude de toujours choisir le mode d'authentification *`SSH`* lorsque vous clônez un repo !
```

+++

### cloner le dépôt du cours

et maintenant vous allez pouvoir cloner, c'est-à-dire copier, le dépôt du cours

il vous suffit pour ça de faire (lisez bien jusqu'au bout avant de copier-coller)

```bash
cd
cd cours-info
git clone # et ici vous collez le presse-papier
          # ce qui donne
git clone git@github.com:ue12-p23/intro.git
```

````{admonition} attention toutefois
:class: warning

c'est important de **bien se mettre dans le bon dossier** avant de faire le `git clone` car sinon le cours va bien être créé mais pas là où vous pensez...
````

````{admonition} un autre nom ?
:class: dropdown

pour choisir un autre nom que `intro` pour le dossier contenant le clone, faites par exemple

```bash
git clone https://github.com/ue12-p23/intro ue12-p23-intro
```
````

````{admonition} si ça échoue ?
:class: dropdown
si vous n'arrivez pas à cloner le repo, il y a pas mal de documentation sur github, je vous propose de commencer avec ceci pour vérifier votre setup SSH:

<https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection>
````

````{admonition} on vérifie le clone
:class: important dropdown

pour vérifier que tout s'est bien passé :

  ```bash
  # bien sûr si vous avez utilisé la deuxième forme
  # votre répertoire local s'appelle ue12-p23-intro et pas juste intro
  cd intro

  # le répertoire est rempli avec la dernière version du cours
  cat README.md
  ```
````

````{admonition} suivre les évolutions futures
:class: tip dropdown

pour terminer cette micro-introduction:  
imaginez que demain je publie des modifications dans ce dépôt

alors pour mettre à jour votre dépôt local, il vous suffira de faire

  ```bash
  # toujours dans le même répertoire bien sûr
  git pull
  ```

qui va **fusionner** vos éventuelles modifications avec les miennes !

on creusera tout ceci dans le cours dédié à git dans quelques semaines
````

+++

## lire les notebooks

le `git clone` a pour effet de créer un dossier qui s'appelle `intro` dans lequel vous pouvez vous déplacer en faisant

  ```bash
  # au cas où vous n'y seriez pas déjà
  cd ~/cours-info
  cd intro
  ```

et une fois dans le bon dossier vous tapez
```
jupyter lab
```


à ce stade on se contente de vérifier que cette commande ouvre un onglet dans votre navigateur web  

vous trouverez [dans ce notebook](label-notebooks-locally) plus de détails sur comment utiliser Jupyter

+++

## la checklist

ça peut valoir la peine de consacrer 10 minutes à visionner une vidéo qui montre comment tous ces outils s'utilisent en vrai; [vous la trouverez, ainsi qu'une liste de compétences, dans ce notebook](label-checklist)
