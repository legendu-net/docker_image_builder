#!/usr/bin/env python3
import datetime
import dsutil.docker

repos = {
    "https://github.com/dclong/docker-python-portable.git": "",
    "https://github.com/dclong/docker-pypy.git": "",
    "https://github.com/dclong/docker-vscode-server.git": "",
    "https://github.com/dclong/docker-gitpod.git": "",
    "https://github.com/dclong/docker-jupyterhub-julia.git": "",
    "https://github.com/dclong/docker-jupyterhub-pytorch.git": "",
}
branch_urls = {
    "main": repos,
    "dev": repos,
    "debian": {},
}
builder = dsutil.docker.DockerImageBuilder(branch_urls)
# builder.build_images(push=False, remove=False)
builder._build_graph()
builder.save_graph(f"graphs/{datetime.date.today()}.yaml")
