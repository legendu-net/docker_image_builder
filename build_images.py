#!/usr/bin/env python3
"""Python script for building Docker images via GitHub Actions.
"""
from argparse import ArgumentParser, Namespace
import json
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
        "--branch-urls",
        dest="branch_urls",
        required=True,
        help="A JSON representation of dic[branch, dict[repo_git_url, base_image_name]].",
    )
    return parser.parse_args(args=args, namespace=namespace)


def main() -> None:
    """The main function of the script."""
    args = parse_args()
    args.branch_urls = "".join(
        line
        for line in args.branch_urls.strip().split("\n")
        if not line.strip().startswith("#")
    ).strip()
    print(args.branch_urls)
    branch_urls = json.loads(args.branch_urls) if args.branch_urls else BRANCH_URLS
    builder = DockerImageBuilder(branch_urls)
    builder.build_images(remove=True)
    builder.save_graph()


if __name__ == "__main__":
    main()
