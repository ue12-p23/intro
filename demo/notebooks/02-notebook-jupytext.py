# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     formats: py:percent
#     notebook_metadata_filter: 'all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version,
#
#       -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
#
#       -language_info.file_extension, -language_info.mimetype, -toc'
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
# ---

# %% [markdown]
# # jupytext

# %% [markdown]
# on peut sauver les notebooks dans un format `.py` plutôt que le format natif `.ipynb`
#
# avantages:
#
# 1. se prête beaucoup mieux à la gestion de version (git)
# 1. on peut exécuter le fichier directement avec `python lefichier.py`
# 1. et si il faut, on peut aussi l'exécuter dans vscode
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

# %%
print("je suis un notebook en jupytext")

# %% [markdown]
# **exercice 1**
#
# ouvrez ce notebook dans jupyter; il doit apparaitre comme un notebook, et non pas comme un simple fichier .py

# %% [markdown]
# **exercice 2**
#
# toujours dans jupyter, exécutez le code ci-dessous, et sauvez le notebook  
# ouvrez alors le fichier dans vs-code et vérifiez que la sortie (notamment la courbe) ne sont pas sauvées dans le fichier

# %%
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib ipympl

X = np.linspace(-5, 5)
Y = X**3
plt.plot(X, Y);
