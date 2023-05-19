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
  title: roadmap
---

Licence CC BY-NC-ND, Thierry Parmentelat & Valérie Roy

```{code-cell} ipython3
:tags: [raises-exception]

%%python
from IPython.display import HTML
HTML(filename="_static/style.html")
```

# fast track

Ce notebook est un résumé des installations qu'il va nous falloir faire

## les outils

Il nous faut a minima

* le terminal - nous utilisons **`bash`**, qui est natif sur les OS linux et MacOS, et qui vient avec le produit `git for windows`
* l'éditeur de code **VS-code** (Visual Studio Code)
* **miniconda** pour **Python** (et les environnements virtuels)
* **Jupyter** pour les notebooks
  * et accessoirement, *markdown* pour la mise en forme du texte,
  * et les formules mathématiques en $\LaTeX$
* **`git`** pour la gestion de versions; c'est un outil super-utile pour le développement, c'est indispensable que vous sachiez l'utiliser

## roadmap

Voici un parcours accéléré pour faire toutes les installations:

```{admonition} installation de git
:class: dropdown
* **(Windows seulement)** git for windows (git + bash)
  <https://nbhosting.inria.fr/builds/ue12-p22-intro/handouts/latest/1-01-os-terminal-nb.html#installation-de-bash>

* **(tous sauf Windows)** installation git seul
  <https://nbhosting.inria.fr/builds/ue12-p22-intro/handouts/latest/1-03-git-setup-nb.html#installation>
```

puis ensuite, pour tous les OS

```{admonition} installation de vs-code
:class: dropdown

voir <https://nbhosting.inria.fr/builds/ue12-p22-intro/handouts/latest/1-02-vscode-python-nb.html#installation-editeur-de-code>
```

```{admonition} installation de miniconda
:class: dropdown

voir <https://nbhosting.inria.fr/builds/ue12-p22-intro/handouts/latest/1-02-vscode-python-nb.html#installation-de-base>
```

```{admonition} configuration git
:class: dropdown

voir <https://nbhosting.inria.fr/builds/ue12-p22-intro/handouts/latest/1-03-git-setup-nb.html#setup-git>
```

et pour se servir de tout cela

```{admonition} cloner le dépôt du cours
:class: dropdown

voir <https://nbhosting.inria.fr/builds/ue12-p22-intro/handouts/latest/1-03-git-setup-nb.html#cloner-le-depot-du-cours>
```

```{admonition} ouvrir les notebooks sur votre ordi
:class: dropdown

voir <https://nbhosting.inria.fr/builds/ue12-p22-intro/handouts/latest/1-04-local-notebooks-nb.html#notebooks-en-local>
```

