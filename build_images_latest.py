#!/usr/bin/env python3
import dsutil

images = [
    "https://github.com/dclong/docker-python-portable.git",
    "https://github.com/dclong/docker-vscode-server.git",
    "https://github.com/dclong/docker-gitpod.git",
    "https://github.com/dclong/docker-jupyterhub-julia.git",
    "https://github.com/dclong/docker-jupyterhub-pytorch.git",
]
# build the master branch which generates the latest tag
builder = dsutil.docker.DockerImageBuilder(images, branch="master")
builder.build()
