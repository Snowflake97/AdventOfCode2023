from CommonTools.DataReader import read_from_file
from Day2.Parser import Parser

colors = ["green", "blue", "red"]

def get_games():
    lines = read_from_file("data.txt")
    games = []
    for line in lines:
        parser = Parser(line.strip(), colors)
        games.append(parser)

    return games


def get_impossible_games(games):
    possible_games = []
    for game in games:
        print(game)
        for subset in game.subsets:
            if not(int(subset["red"]) <= 12 and int(subset["green"]) <= 13 and int(subset["blue"]) <= 14):
                possible_games.append(int(game.game_id))

    possible_games = list(set(possible_games))
    possible_games.sort()
    return possible_games

games = get_games()
impossible_games = get_impossible_games(games)
possible_games = list(range(1, 101))
possible_games = list(filter(lambda x: x not in impossible_games, possible_games))
print(sum(possible_games))
