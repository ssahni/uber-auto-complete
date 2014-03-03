from flask import Flask
from flask import request
from flask import jsonify
from trie import Trie

app = Flask(__name__)

trie = Trie()


def init_cities():
    with open('cities.txt') as cities:
        for city in cities:
            trie.add(city.strip())


@app.route("/add", methods=['GET'])
def add():
    if 'word' not in request.args:
        return 'Please specify a word'

    word_to_add = request.args.get('word').encode('utf-8')
    if word_to_add == '':
        return 'Please specify a word'

    trie.add(word_to_add)
    return 'OK'


@app.route("/search", methods=['GET'])
def search():
    query = ''
    if 'q' in request.args:
        query = request.args.get('q').encode('utf-8')

    results = []
    trie.search(query, results)
    return jsonify(results=results)

if __name__ == "__main__":
    init_cities()
    app.run()
