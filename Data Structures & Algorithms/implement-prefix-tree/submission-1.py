class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}


class PrefixTree:

    def __init__(self):
        self.trie = Node('*')

    def insert(self, word: str) -> None:
        curNode = self.trie
        for c in word:
            if c not in curNode.children:
                curNode.children[c] = Node(c)
            curNode = curNode.children[c]

        curNode.children['*'] = '*'

    def search(self, word: str) -> bool:
        curNode = self.trie
        for c in word:
            if c in curNode.children:
                curNode = curNode.children[c]
                continue
            else:
                return False

        return '*' in curNode.children
        
    def startsWith(self, prefix: str) -> bool:
        curNode = self.trie
        for c in prefix:
            if c in curNode.children:
                curNode = curNode.children[c]
                continue
            else:
                return False

        return True