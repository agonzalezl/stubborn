import os

from .poetry_missmatch import get_missmatched_packages


def report_missmatched_versions(major, minor, patch, path):

    if not path:
        path = os.getcwd()

    missmatched_packages = get_missmatched_packages(path, major, minor, patch)

    if not missmatched_packages:
        return

    print("Dependency issue found:")

    for missmatched_package in missmatched_packages:
        print(
            f"{missmatched_package[0]}@{missmatched_package[1]} \
                vs {missmatched_package[2]}@{missmatched_package[3]}"
        )
