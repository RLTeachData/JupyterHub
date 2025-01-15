# Introduction
使用 Dockerfile Compose 製作 JupyterHub
# Build step by step
- Build image with the docker-compose
```bash
cd JupyterHub
docker-compose build
```
- Create compose
```
docker-compose up -d
```
- Check process
```
docker-compose ps
docker-compose logs
```
- open your website and input your `ip:port`
