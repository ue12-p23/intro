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
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
nbhosting:
  title: "notebook de d\xE9mo"
---

# micro-notebook de démonstration

+++

voici un petit notebook, principalement conçu pour votre démarrage en Jupyter  
vous êtes invités à l'ouvrir **sur votre ordinateur** une fois que vous avez installé les
outils, et cloné le cours

il utilise un kernel *Python* - ce qui le rend plus facile d'accès que le cours
d'introduction, qui requiert une installation supplémentaire car il utilise un kernel *bash*

et de toutes façons, l'énorme majorité des notebooks du cours sont en Python, c'est mieux
de commencer par là

+++

## markdown

+++

grâce à markdown, on peut produire des tas d'effets rien qu'en écrivant du texte; du **gras**, de
l'*italique*, `du code`

+++

lorsque vous faites `Entrée` dans une zone de texte vous passez en mode édition, vous
voyez le code markdown; lorsque vous évaluez la cellule le code markdown est transformé
(on dit qu'il est *rendu*) en HTML

+++

la plupart du temps on évalue les cellules avec `Shift-Enter` mais on peut aussi faire

* `Control-Enter` pour évaluer la cellule **sans passer à la suivante**
* `Alt-Enter` pour évaluer **et insérer une nouvelle cellule au dessous**

entrainez-vous à modifier une cellule

+++

on peut produire

* des listes
* à bullets

et aussi

1. des listes
1. à numéros
1. qui se numérotent toutes seules

+++

* on peut aussi
  * **imbriquer** les listes
  * pour produire
  * un peu de structure
* on **peut** imbriquer beaucoup
  * mais je vous conseille, de vous limiter
  * à une profondeur de 2 seulement,
    * donc ne faites pas comme ici..

+++

### liens hypertexte

+++

pour les liens hypertexte, on a plusieurs choix de présentation

* on peut simplement mettre l'URL telle quelle https://www.youtube.com/watch?v=i_ZcP7iNw-U  
  je vous recommande toutefois de prendre l'habitude de mettre l'URL entre des `<>` comme ici <https://www.youtube.com/watch?v=i_ZcP7iNw-U>
* on peut aussi [l'habiller un peu](https://www.youtube.com/watch?v=i_ZcP7iNw-U) et pour
  ça on utilise la notation markdown

      [le texte](url de la cible)

+++

**remarque** : passez la cellule en mode édition pour visualiser les URLs utilisées

+++

### images

+++

pour les images enfin, c'est un peu la même syntaxe que les liens, mais avec un `!`
devant, ça donne ceci

    ![](url de l'image)

par exemple comme ceci

* on peut insérer une image au format vectoriel (ici du svg)
  ![](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)
* en format bitmap (ici du png) ![](https://upload.wikimedia.org/wikipedia/commons/a/a1/IPy-logo.png)

***

+++

**remarque** : passez la cellule en mode édition pour visualiser les URLs utilisées

+++

## équations

+++

dans une cellule de texte, puisque c'est du markdown on peut écrire des équations

+++

### exemple

+++

on définit l'ensemble des triplets pythagoriciens comme :

$$
P = \{ (a, b, c) \in \mathbb{N^*}^3 \;/\; a^2 + b^2 = c^2 \}
$$

+++

pour générer cet ensemble on considère

* d'abord l'ensemble des complexes à parties réelles et imaginaires entières
$C_{\mathbb{N}} = \{z = n + im \;/\; (n, m) \in \mathbb{Z}^2\}$

* puis l'ensemble de leurs carrés $C_{\mathbb{N}}^2 = \{z^2, z\in C_{\mathbb{N}} \}$

vous vous convaincrez facilement - ce n'est pas du tout notre sujet ici - que cette
méthode permet d'énumérer des triplets pythagoriciens… (mais regardez la vidéo youtube
citée plus haut si vous voulez en savoir plus)

+++

## code

+++

la plupart des notebooks qu'on utilisera seront comme celui-ci **écrits pour Python**

```{code-cell} ipython3
# du coup dans une cellule de code
# on doit écrire du Python

def hey():
    print("bonjour le monde")
```

```{code-cell} ipython3
# quand vous évaluez ceci
# ça doit afficher le message

hey()
```

### exemple (suite)

+++

voici un petit bout de code Python qui utilise notre méthode pour énumérer les triplets
pythagoriciens; bien sûr vous n'avez pas encore le bagage pour tout comprendre, mais vous
pouvez déjà l'exécuter !

```{code-cell} ipython3
import math

def pythagore(N):
    """
    retourne un ensemble de triplets pythagoriciens obtenus en
    calculant le carré des complexes n + im
    avec 1 <= n <= N  et 1 <= m <= N
    """
    solutions = set()
    for n in range(1, N+1):
        for m in range(1, N+1):
            # on calcule (n + im) au carré
            z = (n + 1j*m) ** 2
            # on extrait ses parties réelle et imaginaire
            a, b = z.real, z.imag
            # on écarte les solutions sans intérêt
            if a and b:
                solution = int(abs(a)), int(abs(b))
                solutions.add(solution)
    # l'avantage d'utiliser un ensemble est qu'on n'a
    # pas besoin d'éliminer les doublons
    return solutions
```

```{code-cell} ipython3
len(pythagore(7))
```

```{code-cell} ipython3
# affichons ce qu'on a trouvé
for a, b in sorted(pythagore(7)):
    # en Python pour calculer x au carré
    # on peut - par exemple - écrire x**2
    c = math.sqrt(a**2 + b**2)
    # convert into int
    ci = int(c)
    print(f"({a}, {b}, {ci})\t{ci == c}, {a**2 + b**2 == ci**2}")
```

**exercice**

* amusez-vous à regarder ce que donne la méthode pour d'autres valeurs de N
* insérez ci-dessous une ou plusieurs cellules de code, et vérifiez un de ces triplets

+++

**indice** en Python vous pouvez comparer deux valeurs avec l'opérateur `==`; par exemple

```{code-cell} ipython3
# va renvoyer True, c'est exact que 2 + 3 = 5
2 + 3 == 5
```

## figures

+++

dans un notebook on peut aussi tracer des figures; ici encore, on verra les détails
bientôt, mais juste pour illustrer ce trait, voici comment dessiner la courbe de la
fonction $ f(x) = e^{-x^2} $ sur l'ntervalle $[\pi, \pi]$

```{code-cell} ipython3
# dès qu'on fait du calcul scientifique on utilise la librairie numpy
import numpy as np

# et pour dessiner on utilise matplotlib
import matplotlib.pyplot as plt

%matplotlib widget
```

```{code-cell} ipython3
def f(x):
    return np.exp(- x**2)
```

```{code-cell} ipython3
# tous les X qui nous intéressent
domain = np.linspace(-np.pi, np.pi, 200)

# tous les Y qui vont avec les X
image = f(domain)

# ya plus qu'à
plt.figure()
plt.plot(domain, image);
```

```{code-cell} ipython3
# si vous voulez changer la taille
plt.figure(figsize=(8, 3))
plt.plot(domain, image);
```

## code "inline"

+++

parfois le code qu'on cite dans un notebook n'est pas fait pour être exécuté

il y a plusieurs façons de faire cela, passez en mode édition pour les voir

+++

d'abord on peut mettre le code `print("hello world")` dans un paragraphe "normal", on appelle ça *inline*

+++

ensuite pour montrer du code dans un bloc à part, on à plusieurs choix

```python
# ma préférence
def hello():
    print("hello world")
```

ou encore, parfois pratique aussi, décaler de 4 espaces vers la droite; mais du coup on n'a pas les couleurs

    # moins utile mais bon...
    def hello():
        print('hello world")

+++

remarquez que toutes ces cellules sont des cellules *markdown* bien sûr, et pas des cellules de code

+++

## sections

+++

activez la table des matières (*`View -> Table of Contents`*)

voyez comment on crée les titres en markdown; pour cela, passez en édition sur les cellules qui contiennent ces titres
