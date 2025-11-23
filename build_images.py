#!/usr/bin/env -S uv run
# /// script
# requires-python = "==3.13"
# dependencies = [
#     "dockeree",
# ]
# ///
"""Python script for building Docker images via GitHub Actions."""

from argparse import ArgumentParser, Namespace
from dockeree import DockerImageBuilder


REPOS = {
    "https://github.com/legendu-net/docker-gophernotes": "",
    "https://github.com/legendu-net/docker-rust-utils": "",
    "https://github.com/legendu-net/docker-rust-cicd": "",
    "https://github.com/legendu-net/docker-python-portable": "",
    "https://github.com/legendu-net/docker-vscode-server": "",
    # "https://github.com/legendu-net/docker-gitpod": "",
    "https://github.com/legendu-net/docker-jupyterhub-ds": "",
    "https://github.com/legendu-net/docker-jupyterhub-pytorch": "",
    "https://github.com/legendu-net/docker-tensorboard": "",
    # "https://github.com/legendu-net/docker-conda-build": "",
    "https://github.com/legendu-net/docker-jupyterhub-kotlin": "",
    "https://github.com/legendu-net/docker-jupyterhub-ganymede": "",
    # "https://github.com/legendu-net/docker-jupyterhub-sagemath": "",
    "https://github.com/legendu-net/docker-rustpython": "",
    # "https://github.com/legendu-net/docker-pypy": "",
    # "https://github.com/legendu-net/docker-jupyterhub-julia": "",
}
BRANCH_URLS = {
    "main": REPOS,
    "dev": REPOS,
    "rust_nightly": {
        # "https://github.com/legendu-net/docker-rust-utils": "",
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
        "--root-image-name",
        dest="root_image_name",
        required=True,
        help="The name of the base/root Docker image in dependency resolving.",
    )
    parser.add_argument(
        "--remove-images",
        dest="remove_images",
        action="store_true",
        help="Remove a Docker image when it's not needed (for building other images).",
    )
    return parser.parse_args(args=args, namespace=namespace)


def main() -> None:
    """The main function of the script."""
    args = parse_args()
    branch_urls = BRANCH_URLS
    if args.repo:
        if not args.branch:
            args.branch = "dev"
        branch_urls = {args.branch: {args.repo: args.root_image_name}}
    builder = DockerImageBuilder(branch_urls)
    builder.build_images(remove=args.remove_images)
    builder.save_graph()


if __name__ == "__main__":
    main()
