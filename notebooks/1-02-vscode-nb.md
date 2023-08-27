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
:tags: [raises-exception]

%%python
from IPython.display import HTML
HTML(filename="_static/style.html")
```

# vs-code

## éditeur de code

+++

pour pouvoir facilement modifier le contenu de nos fichiers texte, comme tout à l'heure le
fichier `foo.txt`, on va utiliser un programme qui s'appelle un **éditeur de code**

en effet, il **ne faut pas** utiliser un **outil comme Word** pour éditer des programmes:
c'est un éditeur de texte, et pas un éditeur de code !

> l'enseignant lance Visual Studio Code et le montre très très rapidement

+++

### installation éditeur de code

+++

nous demandons à **tous** les élèves d'installer et de savoir utiliser vs-code

et **ATTENTION** il y a eu **beaucoup de problèmes** les années passé avec les éditeurs de type *pyzo*, ne les utilisez surtout pas dans nos cours, vous allez perdre un temps précieux et en faire perdre à vos enseignants pour des raisons inintéressantes et extérieures à Python

+++

On y va. Le site est là <https://code.visualstudio.com/>. Vous voulez installer donc il va
falloir que vous alliez dans une section *download* ... vous la voyez ? à vous de jouer
maintenant

+++

### micro-démo vs-code

+++

Que vous ayez réussi à installer visual studio code sur votre portable ou pas encore,
suivez maintenant ce que montre l'enseignant.

Si vous avez rencontré des problèmes imprévus lors de l'installation (ce qui n'est pas
rare en informatique), venez nous voir plus tard pour que nous vous aidions.

+++

> micro démo de Visual Code sur le fichier `foo.txt`

* depuis le terminal, aller dans le bon répertoire et lancer
  ```
  code .
  ```

***

* manipulations simples
  * afficher/cacher l'explorateur de fichiers
  * modifier `foo.txt`, sauver la version modifiée
  * créer un nouveau fichier `bar.txt`, le sauver
  * observer le contenu des fichiers depuis le terminal avec `cat`
  * montrer comment se manifeste la fin de ligne

***

* montrer des manipulations élémentaires de fenêtres
  * afficher les deux fichiers côte à côte
  * puis l'un au dessus de l'autre

***

* montrer comment :
  * chercher une extension  (prétexte : l'extension 'Markdown All in One' et/ou Python)
  * installer/désinstaller
  * activer/désactiver une nouvelle extension

***

* montrer comment :
  * passer d'une application à une autre avec `⌥ ⇥` (Alt-Tab)
  * typiquement pour basculer entre vscode et terminal

***

* de retour dans vs-code, montrer la palette :
  * `⇧ ⌘ P` Shift-Command-P (mac)
  * `⇧ ⌃ P` Shift-Control-P (windows)

* sur Windows, pour choisir 'bash' comme terminal
  * utiliser la palette et taper
  * `Select Default Shell`

* montrer comment lancer le terminal
  * Control \` - la deuxième fois on le ferme

+++

pour plus de détails, voir aussi  
<https://code.visualstudio.com/docs/getstarted/userinterface>

+++

exercice :

* refaire les manipulations vous-mêmes une fois l'installation de l'éditeur de code
  terminée.

+++ {"tags": []}

````{note}
il est recommandé, avec vs-code, de prendre l'habitude d'ouvrir un **répertoire** plutôt
qu'un fichier

si vous ouvrez un fichier (par exemple par un clic droit sur le fichier dans l'explorateur
de fichiers), vs-code va vous ouvrir le fichier dans une fenêtre déjà ouverte - souvent ça
va arriver comme un cheveu sur la soupe, dans un autre répertoire; si votre objectif c'est
d'ouvrir une nouvelle fenêtre, préfèrez ouvrir tout un dossier

pour cela, vous pouvez soit 

* taper `code .` dans le terminal comme on l'a vu (et ici le `.` correspond au dossier courant)
* ou utiliser le clic droit depuis l'explorateur Windows, mais sur le dossier lui-même et non le fichier
````

+++

## markdown

+++

c'est un format simple, léger et bien pensé pour mettre en forme facilement vos textes, il
est devenu le couteau suisse pour écrire des documents

* avec un minimum de présentation
  * sections
  * listes
  * gras, italique, code
  * liens
  * maths
* toujours dans un **fichier texte** (à nouveau, ≠ Word)

+++

format **très populaire** en ce moment, supporté e.g. :

* dans les notebooks, justement,
* dans discourse
* dans github
* sur whatsapp (en partie), …

et plus généralement dans tous les sites web de forums/blogs, où on peut entrer du texte
directement depuis le navigateur

+++

### micro-démo sous vs-code

> sous vs-code

* créer un fichier `foo.md`
* remarquer la petite icône ![](media/fig-vscode-markdown.png)
  * afficher côte à côte le markdown brut et rendu
* rapide survol
  * sections
  * listes avec et sans numérotation
  * gras, italique
* insister sur les plusieurs façons de mettre du code,
  * soit `inline` sans saut de ligne, ou alors
  * avec des "triple ticks" <code>```</code>
  * avec 4 espaces de marge
* images et liens
  * montrer le code markdown de cette cellule notebook

cheatsheet <https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf>

+++

### mathjax

+++

on peut aussi écrire des maths en markdown  
ça se fait en utilisant le langage $\LaTeX$  
c'est un peu abscons au début mais on s'y habitue vite  
parce que c'est vraiment très joli

***

$$
\forall \epsilon \in \mathbb{R}^+, \exists\alpha\in\mathbb{R}^+,
\forall x, |x-x_0| < \alpha\implies |f(x)-f(x_0)| < \epsilon
$$

***

$$
\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}
$$

+++

#### *inline*

à la base markdown utilise pour ça le signe `$`

si vous voulez mettre des maths dans un paragraphe (on dit *inline*), vous utilisez un
seul `$` au début et à la fin de l'équation; c-a-d si vous écrivez

```latex
voici une petite équation $y = x^2 +2x +1$ au milieu de la ligne
```

vous obtenez

voici une petite équation $y = x^2 +2x +1$ au milieu de la ligne

+++

#### paragraphe séparé

pour mettre une équation dans un paragraphe séparé on double le dollar de début et de fin

du coup

```latex
$$
\forall x \in \mathbb{R}, \forall \epsilon \in \mathbb{R}^+, \exists\alpha\in\mathbb{R}^+ \\
 |x'-x| < \alpha\implies |f(x')-f(x)| < \epsilon
$$
```

se présentera comme ceci :

$$
\forall x \in \mathbb{R}, \forall \epsilon \in \mathbb{R}^+, \exists\alpha\in\mathbb{R}^+ \\
 |x'-x| < \alpha\implies |f(x')-f(x)| < \epsilon
$$

+++

au passage, vous remarquez que les commandes $\LaTeX$  commencent par `\`

+++

#### les mots du jargon $\LaTeX$

+++

ça dépasse complètement notre périmètre que d'essayer de faire le tour de $\LaTeX$; je
préfère commencer par quelques exemples qui devraient vous permettre de démarrer

+++ {"cell_style": "split"}

$$
\forall x\in \mathbb{R},
\; \exists y \leq \epsilon
$$

+++ {"cell_style": "split"}

```
\forall x \in \mathbb{R},
\; \exists y \leq \epsilon
```

+++ {"cell_style": "split"}

$$x_1=\frac{-b+\sqrt{b^2-4ac}}{2a}$$

+++ {"cell_style": "split"}

```
x_1=\frac{-b+\sqrt{b^2-4ac}}{2a}
```

+++ {"cell_style": "split"}

$$
A_{m,n} =
 \begin{pmatrix}
  a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
  a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
  \vdots  & \vdots  & \ddots & \vdots  \\
  a_{m,1} & a_{m,2} & \cdots & a_{m,n}
 \end{pmatrix}
$$

+++ {"cell_style": "split"}

```
$$
A_{m,n} =
 \begin{pmatrix}
  a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
  a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
  \vdots  & \vdots  & \ddots & \vdots  \\
  a_{m,1} & a_{m,2} & \cdots & a_{m,n}
 \end{pmatrix}
$$
```

+++ {"cell_style": "split"}

$$
\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}
$$

+++ {"cell_style": "split", "slideshow": {"slide_type": ""}}

```
\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}
```

+++ {"tags": ["level_intermediate"]}

ceux qui veulent creuser peuvent

* s'exercer avec un outil en ligne <https://www.codecogs.com/latex/eqneditor.php>

* commencer par cet article 
<https://www.physicsoverflow.org/15329/mathjax-basic-tutorial-and-quick-reference>

* approfondir avec celui-ci <https://en.wikibooks.org/wiki/LaTeX/Mathematics>
