#!/usr/bin/env python3
from argparse import ArgumentParser
from pathlib import Path

from imagehash import average_hash
from PIL import Image


def main(path_image, dir_search, recursive):
    hash_target = hash_image(path_image)
    duplicate_images = search_duplicates(
        hash_target,
        dir_search,
        recursive=recursive
    )
    print_results(duplicate_images)


def hash_image(path_image):
    """Return the perceptual hash of an image given it's location"""
    with Image.open(path_image) as image:
        return str(average_hash(image))


def search_duplicates(hash_target, dir_search, recursive=False):
    """Return list of paths of all duplicate images"""
    results = [
        path for path in Path(dir_search).glob("*.[jp][pn]*g")
        if hash_target == hash_image(path)
    ]

    if recursive:
        for dir_ in Path(dir_search).iterdir():
            if dir_.is_dir():
                results += search_duplicates(hash_target, dir_, recursive=True)

    return results


def print_results(duplicate_images):
    """Print out the paths of the identified duplicate images"""
    for path in duplicate_images:
        print(path)


def cli():
    parser = ArgumentParser(description="Find duplicate images")
    parser.add_argument(
        "path_image",
        type=str,
        help="path of image to use for searching duplicates"
    )
    parser.add_argument(
        "dir_search",
        type=str,
        help="directory to look for duplicate images"
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="search directories recursively"
    )
    args = parser.parse_args()

    main(args.path_image, args.dir_search, args.recursive)
