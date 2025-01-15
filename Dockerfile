FROM jupyterhub/jupyterhub:latest

# 複製 JupyterHub 配置文件
COPY ./jupyterhub_config/jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

# 安裝依賴
RUN python3 -m pip install --upgrade pip
RUN pip install jupyter-server
RUN pip install jupyter-client
RUN pip install jupyterlab
RUN pip install jupyterhub-dummyauthenticator
RUN pip install jupyterhub-firstuseauthenticator

CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]