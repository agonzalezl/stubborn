from typing import Optional

import typer
from typing_extensions import Annotated

from .main import report_missmatched_versions


def main(
    major: Annotated[
        Optional[str], typer.Argument(help="Alert on major version missmatch")
    ] = True,
    minor: Annotated[
        Optional[str], typer.Argument(help="Alert on minor version missmatch")
    ] = True,
    patch: Annotated[
        Optional[str], typer.Argument(help="Alert on patch version missmatch")
    ] = False,
    path: Annotated[
        Optional[str],
        typer.Argument(help="Path to poetry root path", show_default="os.getcwd()"),
    ] = None,
):
    report_missmatched_versions(major, minor, patch, path)


if __name__ == "__main__":
    typer.run(main)
