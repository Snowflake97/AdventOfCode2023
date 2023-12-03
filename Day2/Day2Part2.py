from CommonTools.DataReader import read_from_file
from Day2.Parser import Parser
import math

colors = ["green", "blue", "red"]


def get_games():
    lines = read_from_file("data.txt")
    games = []
    for line in lines:
        parser = Parser(line.strip(), colors)
        games.append(parser)

    return games


def get_sum_of_multiplications_of_minimal_cubes(games):
    value = 0
    for game in games:
        game_minimal_number_of_cubes = list(game.minimal_required_color_cubes.values())
        value = value + math.prod(game_minimal_number_of_cubes)

    return value


games = get_games()
print(get_sum_of_multiplications_of_minimal_cubes(games))
