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
  title: introduction
---

Licence CC BY-NC-ND, Thierry Parmentelat & Valérie Roy

```{code-cell} ipython3
:tags: [raises-exception]

%%python
from IPython.display import HTML
HTML(filename="_static/style.html")
```

# les supports de cours

+++

## dépôt git

comme on l'a vu, les contenus de cours vous sont exposés au travers d'un **dépôt git** (hébergé sur <https://github.com>)

en général il y aura **un dépôt par bloc de cours** (typiquement, un pour cette introduction, un pour le cours Python numérique, un pour votre cours de langage, …)

du côté **github.com**, les cours du premier semestre sont exposés sous une **organisation** (c'est un terme propre à github pour structurer l'espace de noms des dépôts, il y en a plusieurs dizaines de millions...) qui s'appelle `ue12-p23`; ça signifie que vous pouvez retrouver tous les cours à cette adresse

<https://github.com/ue12-p23/>

+++

## les contenus sur votre ordi

une des premières choses que nous apprendrons, ce sera donc 

* comment copier ces contenus sur votre ordinateur, en *clonant* le dépôt depuis github vers votre ordinateur
* comment ensuite lire ces contenus (principalement des notebooks donc) sur votre ordinateur

+++

## supports HTML cherchables 

les contenus des notebooks sont également publiés sur *nbhosting* dans un format `HTML`; il s'agit bien sûr d'une version statique (on ne peut plus modifier le code), mais par contre on peut y faire des recherches globalement, ce qui est pratique dans les cours qui contiennent beaucoup de notebooks

le point d'entrée se situe ici:

<https://nbhosting.inria.fr/public/mines-p23/>

+++

## `nbhosting`

enfin les années précédentes, nous avions utilisé une plateforme hébergée sur <https://nbhosting.inria.fr>, où les notebooks étaient accessibles en *live* (code modifiable et exécutable) sans installation préalable; 
il s'agissait essentiellement d'une facilité pour les premiers cours, de sorte que l'on puisse avancer avant que toute la promo soit entièrement bien installée sur les ordis perso.

il devrait être entendu que le mode d'utilisation "normal" des notebooks est **en local sur votre ordi**,
aussi cette année 2023, nous allons essayer de nous passer totalement de nbhosting; 
on pourra envisager de donner un accès à ce service aux élèves qui auraient des difficultés insurmontables avec leurs installations

+++

## la checklist

s'agissant de cette introduction, [voyez aussi la checklist](label-checklist) qui contient la **liste des compétences requises**, ainsi qu'une **vidéo de démonstration** sur YouTube
