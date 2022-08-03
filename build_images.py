#!/usr/bin/env python3
from dockeree import DockerImageBuilder


repos = [
    "https://github.com/legendu-net/docker-gophernotes.git",
    "https://github.com/legendu-net/docker-rust-utils.git",
    "https://github.com/legendu-net/docker-python-portable.git",
    "https://github.com/legendu-net/docker-vscode-server.git",
    "https://github.com/legendu-net/docker-gitpod.git",
    "https://github.com/legendu-net/docker-jupyterhub-pytorch.git",
    "https://github.com/legendu-net/docker-tensorboard.git",
    "https://github.com/legendu-net/docker-conda-build.git",
    "https://github.com/legendu-net/docker-jupyterhub-kotlin.git",
    "https://github.com/legendu-net/docker-jupyterhub-sagemath.git",
    #"https://github.com/legendu-net/docker-rustpython.git",
    #"https://github.com/legendu-net/docker-pypy.git",
    #"https://github.com/legendu-net/docker-jupyterhub-julia.git",
]
branch_urls = {
    "main": repos,
    "dev": repos,
    "debian": [
        #"https://github.com/legendu-net/docker-jupyterhub-ds.git",
        #"https://github.com/legendu-net/docker-vscode-server.git",
        #"https://github.com/legendu-net/docker-rustpython.git",
    ],
    "centos7": [
        #"https://github.com/legendu-net/docker-rust.git",
    ],
}
builder = DockerImageBuilder(branch_urls)
builder.build_images(remove=True)
builder.save_graph()

