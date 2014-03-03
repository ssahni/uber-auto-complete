uber-auto-complete
==================

uber-auto-complete is an implementation of an efficient data structure (trie) used to store words which can later be queried by partial prefixes. The final result of a query is a list of all possible matching words.

Insertion time of a new word in the worst case is O(n) where n is the length of the word being inserted. Retrieval time of a list of possible matching words given a query in the worst case is O(n log m) where n is the length of the query and m is the number of elements in the trie.

uber-auto-complete is a simple Flask based web application that has two endpoints: add and search. add allows a word to be inserted into the trie via a GET request. search returns a json encoded list of results based on the query provided via a GET request.

**Queries are case-sensitive**

Prerequisites
----
* [Python] - Python 2.7.6
* [virtualenv] - Tool to create isolated Python environments (optional)
* [pip] - Tool for installing and managing Python packages
* [flask] - Micro web application framework for Python

Files
-----------
* autocomplete.py - Main server entry point. stores an in-memory trie of the top 100 populous cities in the world. Exposes two HTTP GET endpoints to add to the trie and search the trie.
* trie.py - The data structure used to store the words (or cities in this case). There are two classes in this module: Node and Trie. The Trie class contains a single attribute: the root Node object. The Node class has two attributes: children and is_word. children is a dictionary which stores characters as the keys and more Node objects as their values. is_word is a flag which denotes if the node is the final character of a word. autocomplete.py uses the Trie class to store the list of cities.
* trie_tests.py - A suite of unit tests written to specifically test the correctness of trie.py.
* requirements.txt - A list of packages to install that are necessary to run uber-auto-complete
* cities.txt - A list of the top 100 most populous cities in the world (http://thegeographist.wordpress.com/2013/11/26/largest-cities-world-population/)

Running the Server
-----------
**It is recommended that virtualenv is used, however it is not necessary. uber-auto-complete has been tested with Python 2.7.6**
```sh
$ pip install -r requirements.txt
$ python autocomplete.py
```

Running the Tests
-----------
```sh
$ python trie_tests.py
```

cURL Requests
-----------
* curl http://localhost:5000/search?q={query} - Response should be a list of json encoded results
* curl http://localhost:5000/add?word={word_to_add} - Response should either be "OK" if the word was added or "Please specify a word" if no word was specified via the query string.

[Python]:http://www.python.org/download/releases/2.7.6
[virtualenv]:http://www.virtualenv.org/en/latest/
[pip]:https://pypi.python.org/pypi/pip
[flask]:http://flask.pocoo.org/
