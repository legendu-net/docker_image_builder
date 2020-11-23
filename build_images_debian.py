#!/usr/bin/env python3
import dsutil

images = ["https://github.com/dclong/docker-jupyterhub-ds.git"]
builder = dsutil.docker.DockerImageBuilder(images, branch="debian")
builder.build()
