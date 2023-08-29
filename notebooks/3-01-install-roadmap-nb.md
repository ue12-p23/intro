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

# fast track

ce notebook est un résumé des installations qu'il va nous falloir faire

+++

## les outils

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

+++

## les installations

voici un parcours accéléré pour faire toutes les installations:

````{admonition} installation de git (et bash sur Windows)
* **(Windows seulement)** [installation de git for windows (git + bash)](label-install-git-for-windows)
* **(tous sauf Windows)** [installation git seul](label-install-git-others)
````

puis ensuite, pour tous les OS

````{admonition} installation de vs-code
[toutes les plateformes](label-install-vscode)
````

````{admonition} installation de miniconda (pour Python, IPython et Jupyter)
[toutes les plateformes](label-install-python)
````

````{admonition} configuration git
[toutes les plateformes](label-setup-git)
````

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
