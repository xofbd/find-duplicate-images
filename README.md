![Python](https://shields.io/badge/Python-3.8%20%7C%203.9-blue)
[![GitHub release](https://img.shields.io/github/v/release/xofbd/find-duplicate-images.svg)](https://github.com/xofbd/find-duplicate-images.svg/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![CI](https://github.com/xofbd/find-duplicate-images/workflows/CI/badge.svg?branch=master)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/xofbd/find-duplicate-images.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/xofbd/find-duplicate-images/context:python)

# Find Duplicate Images
This project provides a command line program to look for duplicate images of a given search image. For example, with a target image and a target directory, the program will look to see what images in the target directory are the same as the target image.

The application works by using a special [image hash function](http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html). A standard hash function such as [SHA-1](https://en.wikipedia.org/wiki/SHA-1) cannot be used because these hash functions rely on the images to be exactly the same. Small differences in bytes will result in a completely different hash value. In short, these image hash functions work by hashing an image that has been distilled down to its core structure by removing things such as high frequency details. This application is built using the [`ImageHash`](https://pypi.org/project/ImageHash/) Python package.

A common application for this tool is to sift through a collection of images for training a machine learning application where you don't want duplicates. You can imagine conglomerating images from various sources where duplicate images may exist but may have different quality and even have watermarks. Further, you want to prevent training images to be present in your test set.

## Prerequisites
1. Python 3
1. (optional) [Poetry](https://python-poetry.org/)

## Installation
There are several ways you can install the application:

* With Poetry and GNU Make: `make install`
* With just `Poetry`: `poetry install --no-dev`
* With `pip`: `pip install .`

## Usage
Once you have the application installed, in the command line run:
```
find_duplicates path_image dir_search
```
where `path_image` is the path of the target image, the image you are looking for duplicates, and `dir_search` is the directory you are looking for duplicates of the target.

## License
This project is distributed under the MIT license. Please see `LICENSE` for more information. The test images come from [Unsplash](https://unsplash.com), which provides freely usable images. You can read their license [here](https://unsplash.com/license). While attribution is not required by the license, it is encouraged.

* The photo of the [coffee](tests/data/coffee_medium.jpg) is by [Alex Padurariu](https://unsplash.com/@alexpadurariu?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).
* The photo of the [fox](tests/data/photos/fox_small.jpg) is by [Ray Hennessy](https://unsplash.com/@rayhennessy?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/fox?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).
