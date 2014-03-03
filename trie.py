class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, value):
        self.__add(self.root, value)

    def search(self, query, results_to_return=[]):
        if len(query) == 0:
            return

        self.__search(self.root, query, '', results_to_return)

    def __add(self, node, value):
        if len(value) == 0:
            node.is_word = True
            return

        key = value[0]
        new_value = value[1:]

        if key in node.children:
            self.__add(node.children[key], new_value)
        else:
            new_node = Node()
            node.children[key] = new_node
            self.__add(new_node, new_value)

    def __search(self, node, query, results='', results_to_return=[]):
        if len(query) > 0:
            key = query[0]
            query = query[1:]
            if key in node.children:
                results = results + key
                self.__search(node.children[key], query, results, results_to_return)
        else:
            if node.is_word:
                results_to_return.append(results)

            for key in node.children.keys():
                self.__search(node.children[key], '', results + key, results_to_return)
