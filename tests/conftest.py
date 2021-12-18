from pathlib import Path

import pytest


@pytest.fixture
def dir_search():
    return Path('tests') / 'data' / 'photos'


@pytest.fixture
def path_image_small(dir_search):
    return dir_search / 'coffee_small.jpg'


@pytest.fixture
def path_image_medium():
    return Path('tests') / 'data' / 'coffee_medium.jpg'


@pytest.fixture
def hash_target():
    return '38387e23073f3737'
