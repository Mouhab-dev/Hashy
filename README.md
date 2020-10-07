# Hashy  ![Python](https://img.shields.io/badge/-Python-black?style=flat&logo=Python) ![version](https://img.shields.io/badge/version-v1.0-blueviolet) ![platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-green)

CLI program for generating hash values for files or strings (i.e. passwords).

## Table of contents
* [General info](#general-info)
* [Libraries](#libraries)
* [Setup](#setup)
* [Usage](#usage)
* [Test](#test)

## General info
This project is a CLI (Command Line Interface) to hash individual files, compare between two files for integrity check or hash strings.

## Libraries
Project is created with:
* hashlib library.
* argparse library.
* python 3.6 or higher.

## Setup
To run this project, install all the required libraries first then run the python script:

```
$ pip install hashlib
$ pip install argparse
$ python hashy.py -hf (hash functions) [-f <file path> | -cf <file path> <file path> | -s <string>]
```

## Usage
Run the following command to display help message
```
hashy.py -h
```
or
```
hashy.py --help
```
A help message will appear with all required arguments the program needs to run:
```
usage: hashy.py [-h] [-v] -hf MD5:SHA1:blake2b [MD5:SHA1:blake2b ...]       
                (-cf <file path> <file path> | -f <file path> | -s "String")

hashy v1.0 is a CLI program to hash files, strings and databases.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         display current version of Hashy
  -hf MD5:SHA1:blake2b [MD5:SHA1:blake2b ...]
                        the required hash function.
  -cf <file path> <file path>
                        check hash of two files for a match using the provided
                        hash function.
  -f <file path>        calculate hash for a file using the provided hash
                        function.
  -s "String"           calculate hash for a string using the provided hash
                        function (string inside " " is a must).
```
* -hf is essential for the script to run
* -cf / -f / -s :
only one of the previous arguments followed by the appropriate input is required to run the script.

## Test



