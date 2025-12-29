class Game:
    def __init__(self):
        self.rats = []


class Rat:
    def __init__(self, game):
        self.game = game
        self.attack = 1
        self.game.rats.append(self)
        self.update_attack()  # cập nhật attack dựa trên số lượng rat hiện tại
        
    def update_attack(self):
        # Mỗi rat có attack = số lượng rat hiện tại
        for rat in self.game.rats:
            rat.attack = len(self.game.rats)
    
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Khi rat rời game, loại nó khỏi danh sách
        self.game.rats.remove(self)
        # Cập nhật attack của các rat còn lại
        self.update_attack()
        
def test_three_rats_one_dies():
    game = Game()

    rat = Rat(game)
    assert rat.attack == 1

    rat2 = Rat(game)
    assert rat.attack == 2
    assert rat2.attack == 2

    with Rat(game) as rat3:
        assert rat.attack == 3
        assert rat2.attack == 3
        assert rat3.attack == 3

    assert rat.attack == 2
    assert rat2.attack == 2
    print("All tests passed!")

test_three_rats_one_dies()
