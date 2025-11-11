
class Sentence:
    class Token:
        def __init__(self):
            self.capitalize = False
        
    def __init__(self, plain_text):
        self.words = plain_text.split()
        self.tokens = {}  # Chỉ lưu các token cho các từ cần chỉnh sửa.
    
    def __getitem__(self, index):
        if index not in self.tokens:
            self.tokens[index] = self.Token()
        return self.tokens[index]
    
    def __str__(self):
        result = []
        for i, word in enumerate(self.words):
            if i in self.tokens and self.tokens[i].capitalize:
                result.append(word.upper())
            else:
                result.append(word)
        return ' '.join(result)


if __name__ == '__main__':
    sentence = Sentence('hello world')
    print("sentence[1].capitalize", sentence[1].capitalize)
    sentence[1].capitalize = True
    print(sentence)  # Output: hello WORLD
