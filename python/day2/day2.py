from dataclasses import dataclass, field


@dataclass
class Game:
    id: int
    subgames: list[dict]
    maxes: dict[str, int] = field(init=False)

    def __post_init__(self):
        self.maxes = {}
        for subgame in self.subgames:
            for move in subgame:
                if move not in self.maxes:
                    self.maxes[move] = 0
                self.maxes[move] = max(self.maxes[move], subgame[move])


def parse_subgames(input: str) -> list[dict]:
    subgames = []
    for subgame in input.split(';'):
        sg = {}
        for move in subgame.split(','):
            move = move.strip().split(' ')
            sg[move[1]] = int(move[0])
        subgames.append(sg)
    return subgames


def parse_game(input: str) -> Game:
    game = input.split(':')
    id = int(game[0].replace('Game ', ''))
    subgames = parse_subgames(game[1])

    return Game(id, subgames)


def possible_game(game: Game, constraints: dict[str, int]) -> bool:
    for move in constraints:
        if move not in game.maxes:
            return False
        if game.maxes[move] > constraints[move]:
            return False
    return True


def part1():
    constraints = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    possible_ids = []

    with open('input.txt') as f:
        for line in f:
            game = parse_game(line)
            if possible_game(game, constraints):
                possible_ids.append(game.id)

    return sum(possible_ids)

def part2():

    with open('input.txt') as f:
        sum = 0
        for line in f:
            game = parse_game(line)
            power = game.maxes["red"] * game.maxes["green"] * game.maxes["blue"]
            sum += power

    return sum

if __name__ == '__main__':
    print(part1())
    print(part2())