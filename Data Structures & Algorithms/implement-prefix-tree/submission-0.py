class Node:
    def __init__(self) -> None:
        self.connections = [None] * 26
        self.endOfWord = False
class PrefixTree:

    def __init__(self):
        self.trie = Node()

    def insert(self, word: str) -> None:
        curr = self.trie
        word = word.lower()
        for letter in word:
            index = ord(letter) - ord("a")
            if curr.connections[index] == None:
                curr.connections[index] = Node()
            curr = curr.connections[index]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.trie
        word = word.lower()
        for letter in word:
            index = ord(letter) - ord("a")
            if curr.connections[index] == None:
                return False
            curr = curr.connections[index]
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        prefix = prefix.lower()
        for letter in prefix:
            index = ord(letter) - ord("a")
            if curr.connections[index] == None:
                return False
            curr = curr.connections[index]
        return True
    
            

        
        