
import pathlib
from typing import List, Tuple
import itertools

def readinput(path):
    f_path = pathlib.Path(path).resolve()

    with open(f_path) as f:
        input = f.read().splitlines()
    
    return input

def add_padding(input : List[str], pad_len = 1, char = '.'):
    length = len(input)
    width = len(input[0])

    for i in range(length):
        input[i] = (char*pad_len) + input[i] + (char * pad_len)

    for i in range(pad_len):
        input.insert(0,char*(width + (2 * pad_len)))
        input.append(char*(width + (2 * pad_len)))

    return input

def rec_search(input, remaining : str, current : List[Tuple[str,int, int]], pos_c, pos_r) -> List[Tuple[str,int, int]]:

    #base case, we found all letters
    if len(remaining) == 0:
        return current

    #found next letter at current pos
    if input[pos_c][pos_r] == remaining[0]:

        next_current = [(input[pos_c][pos_r], pos_c, pos_r)]

        #found letter after second
        if len(current) > 0:
            first_letter = current[-1]
            direction_c = pos_c - first_letter[1]
            direction_r = pos_r - first_letter[2]

            # Continue search in current direction
            return rec_search(input,
                                remaining[1:],
                                current + next_current,
                                pos_c + direction_c,
                                pos_r + direction_r)
        #found second letter
        else:
            sol = [rec_search(input, remaining[1:], current + next_current, pos_c - 1, pos_r), #search up
                    rec_search(input, remaining[1:], current + next_current, pos_c, pos_r + 1), #search right
                    rec_search(input, remaining[1:], current + next_current, pos_c + 1, pos_r), #search down
                    rec_search(input, remaining[1:], current + next_current, pos_c, pos_r - 1), #search left
                    rec_search(input, remaining[1:], current + next_current, pos_c - 1 , pos_r + 1), #search up-right
                    rec_search(input, remaining[1:], current + next_current, pos_c + 1, pos_r + 1), #search down-right
                    rec_search(input, remaining[1:], current + next_current, pos_c + 1, pos_r - 1), #search down-left
                    rec_search(input, remaining[1:], current + next_current, pos_c -1, pos_r - 1)] #search up-left
            sol =  list(filter(lambda search : search is not None, sol))
            if sol == []:
                return None
            else:
                return sol

    else:
        return None

def problem_1(input: List[str]) -> int:
    input = add_padding(input)
    finds = []
    for i in range(len(input)):
        for j in range(len(input)):
            finds.append(rec_search(input,'XMAS',[], i, j))
    finds = list(filter(lambda search : search is not None, finds))
    finds = list(itertools.chain.from_iterable(finds))
    return len(finds)

def filter_diagonals(finds : List[Tuple[str, int, int]]):

    diag_finds = []

    for find in finds:
        m = find[0]
        a = find[1]

        diff_c = a[1] - m[1]
        diff_r = a[2] - m[2]

        if (abs(diff_c) + abs(diff_r)) >= 2:
            diag_finds.append(find)

    return diag_finds

def count_matching_As(finds : List[Tuple[str, int, int]]):

    A_dict = {}
    count = 0

    for find in finds:
        A_col = find[1][1]
        A_row = find[1][2]
        if (A_col,A_row) not in A_dict:
            A_dict[(A_col,A_row)] = [find]
        else:
            A_dict[(A_col,A_row)].append(find)
    
    for key in A_dict.keys():
        if len(A_dict[key]) == 2:
            count += 1

    return count


def problem_2(input : List[str]) -> int:
    input = add_padding(input)
    finds = []
    for i in range(len(input)):
        for j in range(len(input)):
            finds.append(rec_search(input,'MAS',[], i, j))
    finds =list(filter(lambda search : search is not None, finds))
    finds = list(itertools.chain.from_iterable(finds))

    finds = filter_diagonals(finds)
    result = count_matching_As(finds)
    return result




def main():
    input = readinput("Day4/input.txt")
    #result = problem_1(input)
    #print(result)
    result = problem_2(input)
    print(result)

if __name__ == '__main__':
    main()