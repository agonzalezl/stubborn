import os

from .poetry_missmatch import get_missmatched_packages


def main():
    missmatched_packages = get_missmatched_packages(os.getcwd())

    if not missmatched_packages:
        return

    print("Dependency issue found:")

    for missmatched_package in missmatched_packages:
        print(
            f"{missmatched_package[0]}@{missmatched_package[1]} \
                vs {missmatched_package[2]}@{missmatched_package[3]}"
        )
