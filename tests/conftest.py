from pathlib import Path

import pytest


@pytest.fixture
def path_image_medium():
    return Path('tests') / 'data' / 'coffee_medium.jpg'


@pytest.fixture
def hash_coffee():
    return '38387e23073f3737'


@pytest.fixture
def hash_fox():
    return 'ffffbe3c3c040008'


@pytest.fixture
def hash_to_paths_mapping_cases(hash_coffee, hash_fox):
    case_0 = {
        hash_coffee: [Path('tests/data/coffee_medium.jpg')],
    }

    case_1 = {
        hash_coffee: [Path('tests/data/target/coffee_small.jpg')],
        hash_fox: [Path('tests/data/target/fox_small.jpg')],
    }

    case_2 = {
        hash_coffee: [
            Path('tests/data/photos/coffee_small.jpg'),
            Path('tests/data/photos/another/coffee_small.png'),
            Path('tests/data/photos/another/coffee_water_marked.jpg'),
            Path('tests/data/photos/another/directory/coffee_small.jpg'),
            Path('tests/data/photos/another/folder/coffee_low_res.jpg'),
            ],
        hash_fox: [Path('tests/data/photos/fox_small.jpg')],
        }

    return [case_0, case_1, case_2]


@pytest.fixture
def hash_target():
    return {
        'abcd': [Path('some/path/image.jpg')],
        'edfg': [Path('some/other/path/image.jpg')]
    }


@pytest.fixture
def hash_search():
    return {
        'abcd': [Path('search/image.jpg'), Path('search/path/image.jpg')]
    }


@pytest.fixture
def hash_search_other():
    return {'xyz': [Path('not/this/one/image.jph')]}


@pytest.fixture
def hash_duplicates():
    return {'abcd'}


@pytest.fixture
def result_string_cases(
        hash_target,
        hash_search,
        hash_search_other,
        hash_duplicates
):
    return [
        {
            'hash_target': hash_target,
            'hash_search': hash_search,
            'hash_duplicates': hash_duplicates,
        },
        {
            'hash_target': hash_target,
            'hash_search': hash_search_other,
            'hash_duplicates': set(),
        }
    ]


@pytest.fixture
def print_results_expected():
    return [
        (
            'Found 2 duplicates for some/path/image.jpg\n'
            'search/image.jpg\n'
            'search/path/image.jpg\n\n'
        ),
        'No duplicates found\n'
    ]
