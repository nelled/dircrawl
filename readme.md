---
author:
- |
    Daniel Nelle\
    dnelle\@uni-potsdam.de\
    759780
title: |
    Lab No. 1\
    Software Security summer term 2018
---

\maketitle
Description
===========

The program is modeled after *DirBuster* as suggested in the exercise
and does roughly the same thing: Based on a word list or via brute force
it fires requests at a webserver in order to find out whether certain
files/ directories exist. This gives hackers information about possible
attack vectors. The responses to the HTTP requests are analyzed to
determine if the generated request was successful and therefore a
certain file/ directory exists on the server. The application is written
in Python and uses its Threading library to speed up execution time.
Through lists in the config file the HTTP codes of interest as well as
file extensions to be used for file name generation can be manipulated.
Every word from the wordlist/ bruteforce generator is treated as a
directory once and as a file once for each file extension in the list.
In order to descend further into the directory structure of a server,
successful requests are re-added to the queue with another layer of
words attached. If, i. e. http://www.foo.com/existing\_directory/
returns HTTP code 200, all possible combinations of this address with
all words from the word list (as directories AND files with extensions
appended) will be added to the queue until the maximum depth is reached.
The program is written in Python3 and will probably not work with an
older interpreter.

Usage
=====

Flags
-----

The program allows certain flags to be passed in order to change its
behavior:

-url

:   URL of website we want to attack. URL has to be in
    http://\<address\> format in order for the program to work.

-words

:   Path to file with words, every word in a new line.

-threads

:   Number of threads to be used. Default is 20.

-depth

:   Maximum depth of the URL. Might not work 100%, but is intended to
    limit execution time. Default is 2.

-bruteforce

:   Use bruteforce instead of word list. Minimum and maximum length of
    the words generated as well as the alphabet to be used can be set in
    the program.

Example calls
-------------

``` {#lst:orgcode language="c" caption="Original code" label="lst:orgcode"}
dircrawl.py -url http://sans.org -words ./wordlists/own_list.txt
dircrawl.py -url http://localhost/dvwa -words ./wordlists/own_list.txt
dircrawl.py -url http://localhost/dvwa -bruteforce
```
