# --------
FROM nbhosting/minimal-notebook

# NOTE
# we cannot use jupyter nbextension enable/disable
# because we provide our own nbconfig/notebook.json
# and that is where is stored the enabled/disabled extensions
RUN true \
 && pip install -U --pre jupyterlab notebook jupyterlab-myst jupytext \
 && pip install -U git+https://github.com/mwouts/jupyterlab-jupytext.git@jupyterlab4 \
 && pip install jupyterlab-courselevels jupyterlab-nbhosting \
 && pip install -U ipythontutor nbautoeval  \
 && pip install numpy pandas matplotlib seaborn \
 && pip install calysto_bash \
 && true
