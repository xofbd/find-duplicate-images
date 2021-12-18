import re

from image import __version__


def test_version():
    """"
    GIVEN -
    WHEN pyproject.toml is parsed for the version
    THEN the version matches what's in __init__.py
    """

    with open('pyproject.toml', 'r') as f:
        toml = f.read()

    version = re.search(r'^version = "(.+)"$', toml, re.MULTILINE).group(1)

    assert version == __version__
