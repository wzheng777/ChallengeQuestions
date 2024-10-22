
class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class PronunciationFinder:
    def __init__(self):
        # Assume the dictonary is like this
        self.dict = {
        'ABACUS': ['AE', 'B', 'AH', 'K', 'AH', 'S'],
        'BOOK': ['B', 'UH', 'K'],
        'THEIR': ['DH', 'EH', 'R'],
        'THERE': ['DH', 'EH', 'R'],
        'TOMATO.': ['T', 'AH', 'M', 'AA', 'T', 'OW'],
        'TOMATO': ['T', 'AH', 'M', 'EY', 'OW'],
        }
        self.trie = None

    def build_pronun_trie(self):
        root = TrieNode()
        for word, pronuns in self.dict.items():
            node = root
            for pro in pronuns:
                if pro not in node.children:
                    node.children[pro] = TrieNode()
                node = node.children[pro]
            node.words.append(word)

        self.trie = root

    def dfs(self, index, phonence, memo):
        if index == len(phonence):
            return [[]]
        if index in memo:
            return memo[index]
        
        results = []
        node = self.trie
        i = index
        while i < len(phonence) and phonence[i] in node.children:
            node = node.children[phonence[i]]
            i += 1
            if node.words:
                # Found words ending here
                for word in node.words:
                    # Recurse for the remaining phonemes
                    for seq in self.dfs(i, phonence, memo):
                        results.append([word] + seq)
        memo[index] = results
        return results
    
    def find_word_with_pronoun(self, phonence):
        if not phonence or not self.dict:
            return []
        self.build_pronun_trie()
        if not self.trie:
            return
        memo = {}

        return self.dfs(0, phonence, memo)
    
def main():
    finder = PronunciationFinder()
    phonence = ['DH', 'EH', 'R', 'DH', 'EH', 'R']

    combos = finder.find_word_with_pronoun(phonence)

    for combo in combos:
        print(combo)

if __name__ == "__main__":
    main()


    