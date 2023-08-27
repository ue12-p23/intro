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

# introduction

bienvenue dans le premier cours d'informatique de **UE12**  
*Unité d'Enseignement de l'informatique du premier semestre*

+++

## objectifs pour cette introduction

+++

ce cours d'introduction vise à présenter, et à vous faire installer, les outils de base
pour le cours d'informatique; il ne présente **aucune difficulté** mais vous êtes invité·e
malgré tout à le suivre **avec une grande attention** car tous ces éléments sont
**cruciaux pour la suite**

+++

notez que

* le cours est **coopératif**, et pas compétitif  
  ceux qui savent déjà **aident leurs camarades**

* voyez aussi la liste des compétences requises - [notebook
  `2-01-checklist-nb.md`](https://nbhosting.inria.fr/builds/ue12-p23-intro/handouts/latest/2-01-checklist-nb.html) qui contient notamment [une vidéo YouTube en guise de checklist](https://youtu.be/i_ZcP7iNw-U)

* à terminer pour la prochaine fois si nécessaire

+++

## les supports de cours

le plus souvent, les supports de cours sont fournis **sous forme de notebooks**; ce sont des documents hybrides contenant **du texte** (mis en page grâce à *markdown*) et du **code** directement **exécutable**; on peut également y inclure des équations mathématiques, et des média externes (images, vidéos, sons, ...)

+++

### dépôt git

ces contenus vous sont exposés au travers d'un **dépôt git** (hébergé sur <https://github.com>)

en général il y aura **un dépôt par bloc de cours** (typiquement, un pour cette introduction, un pour le cours Python numérique, un pour votre cours de langage, …)

du côté **github.com**, les cours du premier semestre sont exposés sous une **organisation** (c'est un terme propre à github pour structurer l'espace de noms des dépôts, il y en a plusieurs dizaines de millions...) qui s'appelle `ue12-p23`; ça signifie que vous pouvez retrouver tous les cours à cette adresse

<https://github.com/ue12-p23/>

+++

### les contenus sur votre ordi

une des premières choses que nous apprendrons, ce sera donc 

* comment copier ces contenus sur votre ordinateur, en *clonant* le dépôt depuis github vers votre ordinateur
* comment ensuite lire ces contenus (principalement des notebooks donc) sur votre ordinateur

+++

### supports HTML cherchables 

les contenus des notebooks sont également publiés sur *nbhosting* dans un format `HTML`; il s'agit bien sûr d'une version statique (on ne peut plus modifier le code), mais par contre on peut y faire des recherches globalement, ce qui est pratique dans les cours qui contiennent un grand nombre de notebooks

le point d'entrée se situe ici:

<https://nbhosting.inria.fr/public/mines-p23/>

+++

### `nbhosting`

enfin les années précédentes, nous avions utilisé une plateforme hébergée sur <https://nbhosting.inria.fr>, où les notebooks étaient accessibles en *live* (code modifiable et exécutable) sans installation préalable; 
il s'agissait essentiellement d'une facilité pour les premiers cours, de sorte que l'on puisse avancer avant que toute la promo soit entièrement bien installée sur les ordis perso.

il devrait être entendu que le mode d'utilisation "normal" des notebooks est **en local sur votre ordi**,
aussi cette année 2023, nous allons essayer de nous passer totalement de nbhosting dans ce mode (il continue à servir les versions html, mais pas d'accès avec login); 
on pourra envisager de donner un accès à ce service aux élèves qui auraient des difficultés insurmontables avec leurs installations

+++

---
