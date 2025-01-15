from jupyter_client.localinterfaces import public_ips
from jupyterhub.auth import LocalAuthenticator
from firstuseauthenticator import FirstUseAuthenticator
c = get_config() # noqa
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000
c.Spawner.default_url = '/lab'
c.JupyterHub.hub_ip = public_ips()[0]
c.Authenticator.allow_all = True
c.Authenticator.allow_existing_users = True
c.JupyterHub.admin_access = True
c.Authenticator.admin_users = {'admin'}

# 驗證器
LocalAuthenticator.create_system_users = True
FirstUseAuthenticator.dbm_path = '/srv/jupyterhub/passwords.dbm'
FirstUseAuthenticator.create_users = True
class LocalNativeAuthenticator(FirstUseAuthenticator, LocalAuthenticator):
    pass
c.JupyterHub.authenticator_class = LocalNativeAuthenticator