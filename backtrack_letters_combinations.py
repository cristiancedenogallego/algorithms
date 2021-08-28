class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if (len(digits) == 0):
            return []
        
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        comb = []
        
        def backtrack(index, path):
            # Se completo
            if len(path) == len(digits):
                comb.append("".join(path))
                return
    
            possible_letters = letters[digits[index]]
            for l in possible_letters:
                path.append(l)
                backtrack(index + 1, path)
                path.pop()
            
        backtrack(0, [])
            
        return comb
