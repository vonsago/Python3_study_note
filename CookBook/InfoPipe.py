#!/usr/bin/env python
# coding=utf-8
'''
> File Name: InfoPipe.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 五  3/30 11:57:23 2018
'''

from os import walk
import fnmatch
import gzip
import bz2
import re

'''
---note 1 ---walk
Generate the file names in a directory tree by walking the tree either top-down or bottom-up. For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).

---note 2 ---fnmatch
This module provides support for Unix shell-style wildcards, which are not the same as regular expressions (which are documented in the re module). The special characters used in shell-style wildcards are:

*	matches everything
?	matches any single character
[seq]	matches any character in seq
[!seq]	matches any character not in seq

'''


def gen_find(filepat, top): '''
    Find all filenames in a directory tree that match a shell wildcard pattern
    '''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames): '''
Open a sequence of filenames one at a time producing a file object. The file is closed immediately when proceeding to the next iteration. '''
for filename in filenames:
    if filename.endswith('.gz'):
        f = gzip.open(filename, 'rt')
    elif filename.endswith('.bz2'):
        f = bz2.open(filename, 'rt')
    else:
        f = open(filename, 'rt')
     yield f
     f.close()

def gen_concatenate(iterators): '''
Chain a sequence of iterators together into a single sequence. '''
    for it in iterators:
        yield from it

def gen_grep(pattern, lines): '''
Look for a regex pattern in a sequence of lines '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line): yield line
'''
http://www.dabeaz.com/generators/
'''
if __name__ = '__main__':
    lognames = gen_find('access-log*', 'www') files = gen_opener(lognames)
    lines = gen_concatenate(files)
    pylines = gen_grep('(?i)python', lines) for line in pylines:
    print(line)
