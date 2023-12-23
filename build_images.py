#!/usr/bin/env python3
"""Python script for building Docker images via GitHub Actions.
"""
from argparse import ArgumentParser, Namespace
from dockeree import DockerImageBuilder


REPOS = {
    "https://github.com/legendu-net/docker-gophernotes.git": "",
    "https://github.com/legendu-net/docker-rust-utils.git": "",
    "https://github.com/legendu-net/docker-rust-cicd.git": "",
    "https://github.com/legendu-net/docker-python-portable.git": "",
    "https://github.com/legendu-net/docker-vscode-server.git": "",
    "https://github.com/legendu-net/docker-gitpod.git": "",
    "https://github.com/legendu-net/docker-jupyterhub-pytorch.git": "",
    "https://github.com/legendu-net/docker-tensorboard.git": "",
    # "https://github.com/legendu-net/docker-conda-build.git": "",
    "https://github.com/legendu-net/docker-jupyterhub-kotlin.git": "",
    "https://github.com/legendu-net/docker-jupyterhub-ganymede.git": "",
    "https://github.com/legendu-net/docker-jupyterhub-sagemath.git": "",
    "https://github.com/legendu-net/docker-rustpython.git": "",
    # "https://github.com/legendu-net/docker-pypy.git": "",
    # "https://github.com/legendu-net/docker-jupyterhub-julia.git": "",
}
BRANCH_URLS = {
    "main": REPOS,
    "dev": REPOS,
    "blog": {
        # "https://github.com/legendu-net/docker-gitpod.git": "",
    },
    "rust_nightly": {
        # "https://github.com/legendu-net/docker-rust-utils.git": "",
    },
    "4.0": {
        "https://github.com/dclong/docker-jupyterhub.git": "",
    },
}


def parse_args(args=None, namespace=None) -> Namespace:
    """Parse command-line arguments."""
    parser = ArgumentParser(description="Build Docker images.")
    parser.add_argument(
        "--branch",
        dest="branch",
        required=True,
        help="The GitHub branch of repositories to build.",
    )
    parser.add_argument(
        "--repo",
        dest="repo",
        required=True,
        help="The leaf repository to build",
    )
    parser.add_argument(
        "--base",
        dest="base",
        required=True,
        help="The name of the base/root Docker image in dependency resolving.",
    )
    return parser.parse_args(args=args, namespace=namespace)


def main() -> None:
    """The main function of the script."""
    args = parse_args()
    branch_urls = BRANCH_URLS
    if args.repo:
        if not args.branch:
            args.branch = "dev"
        branch_urls = {args.branch: {args.repo: args.base}}
    builder = DockerImageBuilder(branch_urls)
    builder.build_images(remove=True)
    builder.save_graph()


if __name__ == "__main__":
    main()
