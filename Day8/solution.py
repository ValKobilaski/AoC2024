import pathlib
import copy
from typing import List


def read_input(path: str) -> List[List[str]]:

    f_path = pathlib.Path(path).resolve()

    with open(f_path, "r") as f:
        lines = f.read().splitlines()

    for i in range(len(lines)):
        lines[i] = [char for char in lines[i]]

    return lines


def ant_arr_to_dict(ant_arr: List[List[str]]) -> dict:

    ant_dict = {}

    for i in range(len(ant_arr)):
        for j in range(len(ant_arr[0])):

            char = ant_arr[i][j]

            if char == ".":
                pass
            elif char in ant_dict.keys():
                ant_dict[char].append((i, j))
            else:
                ant_dict[char] = [(i, j)]

    return ant_dict


def get_antinodes(ant_dict: dict) -> dict:

    antinode_dict = {}

    for key in ant_dict.keys():
        ant_type = key
        antinodes = []
        ant_list = ant_dict[ant_type]

        for i in range(len(ant_list)):
            remaining_nodes = ant_list[:i] + ant_list[i + 1 :]
            ant_a = ant_list[i]
            for ant in remaining_nodes:
                ant_b = ant

                dist_r = ant_b[0] - ant_a[0]
                dist_c = ant_b[1] - ant_a[1]

                antinodes.append((ant_a[0] - dist_r, ant_a[1] - dist_c))

        antinode_dict[key] = set(antinodes)

    return antinode_dict


def filter_oob(height: int, width: int, antinode_dict: dict):
    new_antinode_dict = {}

    for key in antinode_dict:
        antis_to_keep = []
        antinode_set = antinode_dict[key]

        for antinode in antinode_set:
            if 0 <= antinode[0] <= height - 1:
                if 0 <= antinode[1] <= width - 1:
                    antis_to_keep.append(antinode)
        new_antinode_dict[key] = set(antis_to_keep)

    return new_antinode_dict


def filter_existing_antenas(antinode_dict, ant_dict):

    new_antinode_dict = copy.deepcopy(antinode_dict)

    for antinode_key in new_antinode_dict.keys():
        antinode_set = new_antinode_dict[antinode_key]

        for ant_key in ant_dict:
            ant_set = set(ant_dict[ant_key])
            new_antinode_dict[antinode_key] = antinode_set - ant_set
    return new_antinode_dict


def problem_1(ant_arr):

    count = 0

    height = len(ant_arr)
    width = len(ant_arr[0])
    ant_dict = ant_arr_to_dict(ant_arr)

    antinodes_dict = get_antinodes(ant_dict)
    antinodes_dict = filter_oob(height, width, antinodes_dict)
    antinodes_dict = filter_existing_antenas(antinodes_dict, ant_dict)

    antinodes = []
    print(antinodes_dict)

    for key in antinodes_dict:
        antinodes.extend(antinodes_dict[key])
    antinodes = set(antinodes)
    return len(antinodes)


def get_antinodes_with_harmonics(height: int, width: int, ant_dict: dict):

    antinode_dict = {}

    for key in ant_dict.keys():
        ant_type = key
        antinodes = []
        ant_list = ant_dict[ant_type]

        for i in range(len(ant_list)):
            remaining_nodes = ant_list[:i] + ant_list[i + 1 :]
            ant_a = ant_list[i]
            for ant in remaining_nodes:
                ant_b = ant

                dist_r = ant_b[0] - ant_a[0]
                dist_c = ant_b[1] - ant_a[1]

                antinode_r = ant_a[0]
                antinode_c = ant_a[1]

                while True:

                    if (0 <= antinode_r <= height - 1) and (
                        0 <= antinode_c <= width - 1
                    ):
                        antinodes.append((antinode_r, antinode_c))
                    else:
                        break
                    antinode_r = antinode_r - dist_r
                    antinode_c = antinode_c - dist_c

        antinode_dict[key] = set(antinodes)

    return antinode_dict


def problem_2(ant_arr):

    height = len(ant_arr)
    width = len(ant_arr[0])
    ant_dict = ant_arr_to_dict(ant_arr)

    antinodes_dict = get_antinodes_with_harmonics(height, width, ant_dict)
    # antinodes_dict = filter_oob(height, width, antinodes_dict)
    # antinodes_dict = filter_existing_antenas(antinodes_dict, ant_dict)

    antinodes = []
    print(antinodes_dict)

    for key in antinodes_dict:
        antinodes.extend(antinodes_dict[key])
    antinodes = set(antinodes)
    return len(antinodes)


def main():

    ant_arr = read_input("Day8/input.txt")
    # problem_1_input = copy.deepcopy(ant_arr)
    # result = problem_1(problem_1_input)
    # print(result)
    problem_2_input = copy.deepcopy(ant_arr)
    result = problem_2(problem_2_input)
    print(result)


if __name__ == "__main__":
    main()
