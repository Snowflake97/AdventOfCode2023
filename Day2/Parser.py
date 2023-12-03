import re


class Parser:
    def __init__(self, game, colors):
        self.game = game.strip()
        self.colors = colors
        self.game_id = self.get_game_id()
        self.subsets = self.get_subsets()
        self.minimal_required_color_cubes = self.get_minimal_required_color_cubes()

    def __str__(self):
        return "Game: {} \nSubsets: \n{}".format(self.game_id, self.return_subsets_nicely())

    def get_game_id(self):
        return re.findall(r'(Game )(\d+)(:)', self.game)[0][1]

    def get_subsets(self):
        subsets_list = []
        subsets = re.findall(r'(Game \d+: )(.*)', self.game)[0][1].split(";")
        for subset in subsets:
            subset_dict = {}
            subset = subset.strip()
            for color in self.colors:
                if color in subset:
                    color_number = re.findall(r'(\d+) ({})'.format(color), subset)[0][0]
                else:
                    color_number = 0

                subset_dict[color] = color_number
            subsets_list.append(subset_dict)

        return subsets_list

    def return_subsets_nicely(self):
        output = ""
        for pos, subset in enumerate(self.subsets):
            output = output + "{:2}* Subset {}: \n".format("", pos + 1)
            for color in self.colors:
                output = output + "{:4}-{} : {}\n".format("", color, subset[color])
        return output

    def get_minimal_required_color_cubes(self):
        max_values_dict = {}
        for color in self.colors:
            max_values_dict[color] = 0

        for subset in self.subsets:
            for color in self.colors:
                if int(subset[color]) > int(max_values_dict[color]):
                    max_values_dict[color] = int(subset[color])

        return max_values_dict
