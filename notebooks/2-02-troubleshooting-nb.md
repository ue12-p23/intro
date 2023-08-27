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
  title: troubleshooting
---

Licence CC BY-NC-ND, Thierry Parmentelat & Valérie Roy

```{code-cell} ipython3
%%python
from IPython.display import HTML
HTML(filename="_static/style.html")
```

# troubleshooting

les erreurs les plus fréquentes lors des installations

si vous ne trouvez pas la réponse ici: **commencez par demander à google** en précisant bien votre contexte: le nom de l'OS, le logiciel qui ne fonctionne pas comme attendu, et le message d'erreur; il y a de très grandes chances que vous trouviez votre réponse sur `stackoverflow.com`

dans tous les cas, essayez d'abord de trouver par vous même avant de demander de l'aide à vos camarades ou aux professeurs

+++

## `python: command not found`

+++

* tapez dans votre terminal

  ```bash
  conda init bash
  ```
  avant de lancer un nouveau terminal et de réessayez

  <div class=note>
    
  (si vous êtes sur mac, il se peut que votre shell soit `zsh` et pas `bash`; pas de souci pour suivre le cours avec `zsh`, mais par contre vous devez peut-être taper ici `conda init zsh`)
    
  </div>

* si ce n'est pas cela, le plus probable est que vous n'avez pas bien coché la case `mettre à jour $PATH` lors de l'installation de miniconda; réinstallez, relancez un terminal, et réessayez

+++

## `code: command not found`

+++

* lancez code par les menus, puis dans la palette, tapez `shell command: install 'code' command in PATH`
  comme toujours, relancez un nouveau terminal et réessayez

+++

## `ModuleNotFoundError: No module named 'bidule'`

+++

vous avez installé un module (n'importe lequel, disons `numpy`) depuis le terminal  
**MAIS** depuis python, vous essayez de l'importer et il n'est pas trouvé...

dans 99% des cas, c'est parce que vous avez plusieurs environnements Python différents; vous installez dans un, et vous exécutez dans un autre...

vérifiez bien des deux cotés de quel python il s'agit, en tapant par exemple `type python`

```{code-cell} ipython3
# le ! c'est une commande 'magic' qui dit à ipython d'exécuter du bash...
!type python
```

il faut bien sûr que ce soit le même python des deux cotés (à nouveau, là où vous installez et là où vous exécutez)

+++

souvenez-vous aussi que sous VS-code vous avez un menu pour choisir justement l'environnement Python à utiliser
