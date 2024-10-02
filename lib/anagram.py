class Anagram:
    def __init__(self, word: str):
        self.word = word

    def match(self, candidates: list) -> list:
        # Sort the letters of the initialized word
        sorted_word = sorted(self.word)
        matches = []
        
        for candidate in candidates:
            # Sort the letters of the candidate
            if sorted(candidate) == sorted_word:
                matches.append(candidate)

        return matches
