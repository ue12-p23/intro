# --------
FROM nbhosting/minimal-notebook

# NOTE
# we cannot use jupyter nbextension enable/disable
# because we provide our own nbconfig/notebook.json
# and that is where is stored the enabled/disabled extensions
# jupyterlab-nbhosting not ready
RUN true \
 && pip install -U jupyterlab notebook jupytext jupyterlab-myst \
 && pip install -U jupyterlab-courselevels \
 && pip install -U ipythontutor nbautoeval  \
 && pip install numpy pandas matplotlib seaborn \
 && pip install calysto_bash \
 && true
