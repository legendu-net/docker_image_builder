#!/usr/bin/env python3
import json
from pathlib import Path
import subprocess as sp


def config_data_root(data_root: str) -> dict[str, str]:
    Path(data_root).mkdir(parents=True, exists_ok=True)
    settings = {}
    path = Path("/etc/docker/daemon.json")
    if path.is_file():
        with path.open("r", encoding="utf-8") as fin:
            settings = json.load(fin)
    settings["data-root"] = data_root
    with path.open("w", encoding="utf-8") as fout:
        json.dump(settings, fout, indent=4)
    return settings


def store_docker_on_mnt():
    sp.run(cmd="systemctl stop docker", shell=True, check=True)
    settings = config_data_root("/mnt/docker")
    print(settings)
    sp.run(cmd="systemctl start docker", shell=True, check=True)
    sp.run(cmd="docker info", shell=True, check=True)


if __name__ == "__main__":
    store_docker_on_mnt()

