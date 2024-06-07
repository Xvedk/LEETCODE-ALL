class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for word in dictionary:
            cur = trie
            for c in word:
                cur = cur.setdefault(c, {})
            cur["$"] = True

        
        new_s = []
        for word in sentence.split():
            cur = trie 
            rt = ""
            for c in word:
                if "$" in cur:
                    break
                if c not in cur:
                    break
                cur = cur[c]
                rt += c
            
            new_s.append(rt if "$" in cur else word)
        return " ".join(new_s)
