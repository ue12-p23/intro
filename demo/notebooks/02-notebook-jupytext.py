# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # jupytext

# %% [markdown]
# on peut sauver les notebooks dans un format `.py` plutôt que le format natif `.ipynb`
#
# avantages:
#
# * se prête beaucoup mieux à la gestion de version (git)
# * peut s'exécuter dans vscode
# * et si il faut, on peut exécuter le fichier directement
#
# le seul inconvénient par rapport à un `.ipynb` est qu'on ne peut pas sauver la valeur de sortie des cellules une fois qu'elles sont évaluées

# %% [markdown]
# # installation

# %% [markdown]
# comme toujours on installe ça avec
#
# ```
# pip install jupytext
# ```
#
# **Attention** bien sûr si vous ne l'avez pas fait, vous pouvez qund même ouvrir ces fichiers avec jupyter, mais ça ne rend pas bien du tout

# %%
print("je suis un notebook en jupytext")

# %% [markdown]
# **exercice 1**
#
# exécutez ce notebook depuis le terminal

# %% [markdown]
# **exercice 2**
#
# créez un nouveau notebook jupytext en vous inspirant de 
# ![](create-a-text-notebook.png)
