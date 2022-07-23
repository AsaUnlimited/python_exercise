from dataclasses import dataclass


@dataclass(frozen=True)
class Player:
    name: str
    sign: str


if __name__ == '__main__':
    player1 = Player('ameerah', '5')

    print(player1.name)

# class Player:
# def __init__(self, name: str, sign: str) -> None
#     self.name = name
#     self.sign = sign
