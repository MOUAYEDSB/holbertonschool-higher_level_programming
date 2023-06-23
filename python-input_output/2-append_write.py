#!/usr/bin/python3
"""Module for append_file method"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)"""
    i = 0
    with open(filename, 'a', encoding='utf-8') as file_to_add:
        file_to_add.write(text)
        for i in range(len(text)):
            i += 1
        return (i)
