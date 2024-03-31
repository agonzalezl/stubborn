import subprocess
from pathlib import Path

from poetry.core.packages.package import Package
from poetry.factory import Factory

from .dependency_pairs import DEPENDENCY_PAIRS


def apply_dependency_constrain(dependency_name: str, constraint: str):
    command = f"poetry add {dependency_name}@{constraint} --lock"
    subprocess.run(command, shell=True)


def search(packages:list[Package], package_name: str)->Package:
    for package in packages:
        if package_name == package.name:
            return package
    return None

def get_missmatched_packages(poetry_path: str) -> list[list]:
    poetry = Factory().create_poetry(Path(poetry_path))
    repository = poetry.locker.locked_repository()

    missmatched_packages = []

    for package_name, type_package_name in DEPENDENCY_PAIRS.items():
        package = search(repository.packages, package_name)
        type_package = search(repository.packages, type_package_name)
        if not package or not type_package:
            continue

        if (
            package.version.major != type_package.version.major
            or package.version.minor != type_package.version.minor
        ):
            missmatched_packages.append(
                [
                    package_name,
                    package.version,
                    type_package_name,
                    type_package.version,
                ]
            )

    return missmatched_packages
