#!/usr/bin/env python3
from dockeree import DockerImageBuilder


repos = [
    "https://github.com/dclong/docker-python-portable.git",
    "https://github.com/dclong/docker-vscode-server.git",
    "https://github.com/dclong/docker-gitpod.git",
    "https://github.com/dclong/docker-jupyterhub-julia.git",
    "https://github.com/dclong/docker-jupyterhub-pytorch.git",
    "https://github.com/dclong/docker-jupyterhub-sagemath.git",
    "https://github.com/dclong/docker-tensorboard.git",
    "https://github.com/dclong/docker-rust-utils.git",
    "https://github.com/dclong/docker-evcxr_jupyter.git",
    #"https://github.com/dclong/docker-rustpython.git",
    #"https://github.com/dclong/docker-pypy.git",
]
branch_urls = {
    "main": repos,
    "dev": repos,
    "debian": [
        #"https://github.com/dclong/docker-jupyterhub-ds.git",
        #"https://github.com/dclong/docker-vscode-server.git",
        #"https://github.com/dclong/docker-rustpython.git",
    ],
    "22.04": [
        "https://github.com/dclong/docker-vscode-server.git",
    ],
    "centos7": [
        "https://github.com/dclong/docker-rust.git",
    ],
}
builder = DockerImageBuilder(branch_urls)
builder.build_images(remove=True)
builder.save_graph()

