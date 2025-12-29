class Token:
    def __init__(self, value=0):
        self.value = value


class Memento(list):
    pass


class TokenMachine:
    def __init__(self):
        self.tokens = []

    def add_token_value(self, value):
        return self.add_token(Token(value))

    def add_token(self, token):
        self.tokens.append(token)
        memento = Memento(t.value for t in self.tokens)
        return memento

    def revert(self, memento):
        self.tokens.clear()

        # Khôi phục từ snapshot
        for value in memento:
            self.tokens.append(Token(value))
            
machine = TokenMachine()

t = Token(10)
m1 = machine.add_token(t)

t.value = 20
m2 = machine.add_token(t)

print([token.value for token in machine.tokens])
# [20, 20]

machine.revert(m1)
print([token.value for token in machine.tokens])
# [10] ✅ CHÍNH XÁC
