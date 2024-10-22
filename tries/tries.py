class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.isWord
    
    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True


def main():
    trie = Trie()
    trie.insert("apple")
    trie.insert("ape")
    trie.insert("nope")

    print(trie.search("ape"))
    print(trie.startsWith("app"))
    print(trie.startsWith("apb"))


if __name__ == "__main__":
    main()