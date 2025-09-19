class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.isWord=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()


    def addWord(self, word: str) -> None:
        node=self.root
        for ch in word:
            i = ord(ch)-97
            if node.children[i] is None:
                node.children[i]=TrieNode()
            node= node.children[i]
        node.isWord=True

    def search(self, word: str) -> bool:
        def dfs(node,idx):
            if node is None:
                return False
            if idx==len(word):
                return node.isWord
            ch=word[idx]
            if ch =='.':
                for child in node.children:
                    if child and dfs(child,idx+1):
                        return True
                return False
            else:
                return dfs(node.children[ord(ch)-97],idx+1)
        return dfs(self.root,0)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)