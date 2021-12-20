import pytest

from image.find_duplicates import (
    hash_image,
    map_hash_to_paths,
    overlap_hashes,
    print_results
)


def assert_equal_dicts(dict_1, dict_2):
    """
    Assert that two dicts that map keys to lists are equal

    The two dicts must share the same keys their values should be lists that
    contain the same elements.
    """

    assert set(dict_1) == set(dict_2)

    for key in dict_1:
        assert sorted(dict_1[key]) == sorted(dict_2[key])


def test_hash_image(path_image_medium, hash_coffee):
    """
    GIVEN a path to an image of the coffee cup
    WHEN the average hash is taken
    THEN the hash value matches the expected value
    """
    assert hash_image(path_image_medium) == hash_coffee


@pytest.mark.parametrize(
    'path_target,recursive,case',
    [
        ('tests/data/coffee_medium.jpg', False, 0),
        ('tests/data/target', True, 1),
        ('tests/data/photos', True, 2),
    ]
)
def test_map_hash_to_paths(
        recursive,
        path_target,
        case,
        hash_to_paths_mapping_cases
):
    """
    GIVEN a target path
    WHEN map_hash_to_paths is called
    THEN the correcting mapping of hash to paths with that hash is returned
    """
    hash_to_paths = map_hash_to_paths(path_target, recursive=recursive)

    assert_equal_dicts(hash_to_paths, hash_to_paths_mapping_cases[case])


def test_overlap_hashes(hash_target, hash_search, hash_duplicates):
    """
    GIVEN the hash-path mapping of the both the target and search
    WHEN overlap_hashes is called
    THEN the set of the common hashes between the two mappings is returned
    """
    assert overlap_hashes(hash_target, hash_search) == hash_duplicates


@pytest.mark.parametrize('case', [0, 1])
def test_print_results(
        case,
        result_string_cases,
        print_results_expected,
        capsys,
):
    """
    GIVEN the resulting hash-to-paths and overlap hashes
    WHEN print_results is called with those outputs
    THEN a message of the number of duplicates and their paths is printed
    """
    print_results(**result_string_cases[case])
    output = capsys.readouterr().out

    assert output == print_results_expected[case]
