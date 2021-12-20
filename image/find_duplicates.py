#!/usr/bin/env python3
from argparse import ArgumentParser
from collections import defaultdict
from pathlib import Path

from imagehash import average_hash
from PIL import Image


def main(path_image, dir_search, recursive):
    hash_target = map_hash_to_paths(path_image, recursive=False)
    hash_search = map_hash_to_paths(dir_search, recursive=recursive)
    hash_duplicates = overlap_hashes(hash_target, hash_search)
    print_results(hash_target, hash_search, hash_duplicates)


def map_hash_to_paths(path_image, recursive=False):
    """Return mapping between hash and paths of all images with that hash"""
    hash_to_paths = defaultdict(list)

    if not Path(path_image).is_dir():
        return {hash_image(Path(path_image)): [Path(path_image)]}

    if recursive:
        paths = Path(path_image).glob("**/*.[jp][pn]*g")
    else:
        paths = Path(path_image).glob("*.[jp][pn]*g")

    for path in paths:
        hash_to_paths[hash_image(path)].append(path)

    return hash_to_paths


def hash_image(path_image):
    """Return the perceptual hash of an image given it's location"""
    with Image.open(path_image) as image:
        return str(average_hash(image))


def overlap_hashes(hash_target, hash_search):
    """Return a set of hashes common between the two mappings"""
    return set(hash_target).intersection(set(hash_search))


def print_results(hash_target, hash_search, hash_duplicates):
    """Print out which images are duplicates and their path"""

    if not hash_duplicates:
        print("No duplicates found")
    else:
        for hash_ in hash_duplicates:
            paths = " and ".join(map(str, hash_target[hash_]))
            path_duplicates = "\n".join(map(str, hash_search[hash_]))
            print(f"Found {len(hash_search[hash_])} duplicates for {paths}")
            print(path_duplicates)
            print()


def cli():
    parser = ArgumentParser(description="Find duplicate images")
    parser.add_argument(
        "path_target",
        type=str,
        help="path of image(s) to use for searching duplicates"
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

    main(args.path_target, args.dir_search, args.recursive)
