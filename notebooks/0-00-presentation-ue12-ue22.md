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

# présentation générale des ue12 et ue22 d'informatique

Unités d'Enseignement du premier et du second semestre

+++ {"jp-MarkdownHeadingCollapsed": true}

## nos objectifs

+++ {"jp-MarkdownHeadingCollapsed": true}

**prise d'autonomie** dans l'**utilisation des ressources digitales**  
pas de salle informatique  
le premier objectif est que vous sachiez **rapidement utiliser votre propre ordinateur** pour travailler

> vous devez apporter votre portable (et son chargeur) **à toutes les séances d'informatique**
----

**prise d'autonomie** dans le **numérique et la programmation**  
avec pour cela un focus sur quelques outils (du moment)  

> ces outils serviront aux autres enseignements (mathématiques, machine-learning...)
---

nos cours sont introductifs, seul un **travail personnel entre les cours** vous permettra  
**d'assimiler** les rudiments et d'**acquérir** quelques automatismes (nécessaires à la programmation)

> ne pas travailler l'informatique pour vous consacrer aux autres matières plus fondamentales/exigentes n'est pas un bon choix

> vous avez déjà un bon niveau en informatique ? venez-nous voir, vous éviterez de perdre votre temps

---

ces quelques compétences en informatiques sont **incontournables** quel que soit vos futurs métiers  

> il vous faudra aussi les tenir à jour

---

en cas de **dificulté**: compréhension, charge de travail, rapidité des cours (trop/pas assez), motivation, problème de portable...

> contacter valerie.roy@minesparis.psl.eu

+++

## le programme des enseignements sur l'année (8 ECTS)

2 ECTS = 9 séances de 3 heures

+++

### premier semestre (4 ECTS)

**PE** *Programmation Élémentaire* (2 ECTS)

||séances|contenu|
|---|---|---|
|python-numérique|5 | pandas, numpy, matplotlib| 
|git| 2 | système de gestion de versions de projets|
|hackaton | 1 | réaliser du code en groupe (min 2 max 4)| 

**AP** *Apprentissage de la Programmation* (2 ECTS)

|langage (au choix) |séances|contenu|
|---|---|---|
|python-avancé|9 | approfondissements du langage Python| 
|c++| 9 | découverte d'un langage compilé de haut niveau|
|hackaton | 2 | réaliser du code en groupe de 4| 

**

+++ {"jp-MarkdownHeadingCollapsed": true}

### second semestre (4 ECTS)

**PFC** *Programme fiables et concurrents* (2 ECTS)

||séances|contenu|
|---|---|---|
| rudiments de Web|5 | html, css, javascript| 
|réseau| 2 | |
|site Web | 1 | réaliser un site web en flask| 
|hackaton | 1 | réaliser un code en groupe de 4| 

**PI** *Projet Informatique* (2 ECTS) en groupe de 4 élèves
- implication des alumins et d'enseignants-chercheurs-ingénieurs de l'école qui proposent et encadrent des sujets
- parfois sur un domaine que vous ne connaissez pas
- parfois avec des techniques que vous ne connaissez pas (encore) 

| |séances|contenu|
|---|---|---|
|travail en groupe| 6 | libérées| 
|propriété intellectuelle/industrielle| 1 | conférence|
|soutenances | 2 | présentation des projets en groupe| 


+++ {"jp-MarkdownHeadingCollapsed": true}

## les cours

### les supports de cours
Ce sont des **notebooks** formés de
* cellules de textes: les explications (en `markdown`)
* cellules de code: que vous exécutez et pouvez modifier

> les contenus des notbooks sont également publiés dans leur version textuelle (statique) dans laquelle vous pouvez facilement faire des recherches  
> <https://nbhosting.inria.fr/public/mines-p23/>

qui contiennent
* les notions de base à connaître
* quelques notions intermédiaires
* des notions avancées (pour ceux qui vont plus vite)

> en cours: on commence les apprentissages ensemble en parcourant des *notebooks*

> à-la-maison: vous terminez les notebooks commencés et vous relisez les notebooks déjà vus


### ce qu'on attend de vous
* que vous soyez présents à tous les cours (ils sont obligatoires)
* que vous préveniez votre enseignant en cas d'absence (avant si cela vous est possible)
  il vous indiquera quoi rattraper
* que vous soyez à l'heure (un contrôle continu sera fait en début de séance)

### votre comportement

soyez constructif, coopératifs
*  vis-à-vis des autres élèves en les aidant sans être compétitif
*  vis-à vis de vos enseignants en leur posant des questions, en leur disant si ils vont trop/pas assez vite...  
  aidez les à comprendre où vous en êtes


### pour savoir où vous en êtes ?

*pour le fun* (non noté)
> un hackaton pour vous apprendre à travailler ensemble

un contrôle continu noté (quiz ou exercices au début de chaque cours)

un mini-projet de programmation (noté et personnel)

### à savoir

> les enseignants ne pourront pas attribuer de note de contrôle continu aux élèves trop souvent absents (qui iront donc rattrapage)

> si vous êtes absent parce que vous connaissez déjà parfaitement toutes ces notions: contacter valerie.roy@minesparis.psl.eu

+++

## Les 2 langages <span style="color:blue">python</span> et <span style="color:blue">C++</span>

vous prendez un de ces langages au choix
> un formulaire vous sera envoyé pour le choix du langage

### <span style="color:blue">Python</span>

- simple, lisible et *élégant*, interprété
- très grand nombre de librairies
- prototypage rapide
- applications web, data-science, machine-learning

#### <span style="color:blue">C++</span>

- haut-niveau et proche de la machine, typé, compilé, très performant
- plus difficile d'accès que <span style="color:blue">python</span> et plus exigeant mais vous apporte une compréhension fine de ce qui se passe en machine
- de belles constructions (templates)
- logiciels scientifiques, OS, BdD, moteurs de rendus, logiciels de
  micro-contrôleurs (tout ce qui doit aller vite)
