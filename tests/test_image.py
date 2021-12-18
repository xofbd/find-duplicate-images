from pathlib import Path

import pytest

from image.find_duplicates import hash_image, print_results, search_duplicates


def test_hash_image(path_image_medium, hash_target):
    """
    GIVEN a path to an image
    WHEN the perceptual hash is taken
    THEN the hash value matches the expected value
    """
    assert hash_image(path_image_medium) == hash_target


@pytest.mark.parametrize(
    'recursive,expected',
    [(
        False,
        [Path('tests/data/photos/coffee_small.jpg')]
    ),
     (
         True,
         [
             Path('tests/data/photos/coffee_small.jpg'),
             Path('tests/data/photos/another/coffee_small.png'),
             Path('tests/data/photos/another/coffee_water_marked.jpg'),
             Path('tests/data/photos/another/directory/coffee_small.jpg'),
             Path('tests/data/photos/another/folder/coffee_low_res.jpg'),
         ]
     )
    ]
)
def test_search_duplicates(recursive, expected, hash_target, dir_search):
    """
    GIVEN a the hash of a target image and search directory
    WHEN the search_duplicates function is called
    THEN the list of the paths of the duplicate images is returned
    """
    duplicates = search_duplicates(
        hash_target,
        dir_search,
        recursive=recursive
    )

    assert not (set(duplicates) - set(expected))


@pytest.mark.parametrize(
    'duplicate_images,print_string',
    [
        (
            [Path('tests/data/photos/coffee_small.jpg')],
            'tests/data/photos/coffee_small.jpg\n'
        ),
        ([], '')
    ]
)
def test_print_results(duplicate_images, print_string, capsys):
    """
    GIVEN a list of paths representing duplicate files
    WHEN print_results is called with those list of paths
    THEN their paths are printed
    """
    print_results(duplicate_images)
    captured = capsys.readouterr()

    assert captured.out == print_string
