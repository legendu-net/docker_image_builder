#!/usr/bin/env python3
import dsutil.docker
images = [
    "https://github.com/dclong/docker-python-portable.git",
    "https://github.com/dclong/docker-vscode-server.git",
    "https://github.com/dclong/docker-gitpod.git",
    "https://github.com/dclong/docker-jupyterhub-julia.git",
    "https://github.com/dclong/docker-jupyterhub-pytorch.git",
]
# build the dev branch which generates the next tag
builder = dsutil.docker.DockerImageBuilder(images)
builder.build()
