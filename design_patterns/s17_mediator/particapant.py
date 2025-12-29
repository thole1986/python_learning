class Mediator:
    def __init__(self):
        self.participants = []
        
    def register(self, participant):
        self.participants.append(participant)
        
    def broadcast(self, sender, value):
        for participant in self.participants:
            if participant != sender:
                participant.value += value

class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator
        mediator.register(self)

    def say(self, value):
        self.mediator.broadcast(self, value)
        
mediator = Mediator()

p1 = Participant(mediator)
p2 = Participant(mediator)

p1.say(3)
print(p1.value, p2.value)   # 0 3

p2.say(2)
print(p1.value, p2.value)   # 2 3
