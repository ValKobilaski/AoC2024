
import pathlib
from typing import List, Tuple
import copy
import tqdm

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

class agent():

    def __init__(self,map):
        self.map = copy.deepcopy(map)

        
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == '^':
                    row = i
                    col = j
                    self.map[i][j] = '.'
        self.r = row
        self.c = col
        self.dir = 0


    def scan_forward(self):
        
        if self.dir == 0:
            return self.map[self.r -1][self.c]
        elif self.dir == 1:
            return self.map[self.r][self.c + 1]
        elif self.dir ==2:
            return self.map[self.r + 1][self.c]
        else:
            return self.map[self.r][self.c - 1]

    def move_forward(self):

        if self.dir == 0:
            self.r -= 1
        elif self.dir == 1:
            self.c += 1
        elif self.dir ==2:
            self.r += 1
        else:
            self.c -= 1

    def turn_right(self):

        self.dir = (self.dir + 1) % 4

def problem_1(input):
    guard = agent(input)
    path = [(guard.r,guard.c)]
    infront = guard.scan_forward()
    while infront != "O":
        if infront == "#":
            guard.turn_right()
        elif infront == ".":
            guard.move_forward()
            path.append((guard.r, guard.c))
        
        infront = guard.scan_forward()
    uniq_states = set(path)
    return uniq_states

def project_right(guard: agent):

    guard_copy = copy.deepcopy(guard)
    guard_copy.turn_right()
    infront = guard_copy.scan_forward()
    while infront == '.':
        guard_copy.move_forward()
        infront = guard_copy.scan_forward()

    return ((guard_copy.r, guard_copy.c, guard_copy.dir))


def problem_2(input):

    count = 0
    max_steps = 100000
    path = list(problem_1(input))
    #path.remove((7,5))
    path.remove((90,52))

    for step in tqdm.tqdm(path[1:]):
        steps = 0
        cond_input = copy.deepcopy(input)
        cond_input[step[0]][step[1]] = '#'
        guard = agent(cond_input)

        infront = guard.scan_forward()
        while infront != "O":
            if infront == "#":
                guard.turn_right()
            elif infront == ".":
                guard.move_forward()

            infront = guard.scan_forward()
            steps +=1
            if max_steps == steps:
                count += 1
                break
    return count



def main():
    input = readinput('Day6/input.txt')
    input = add_padding(input,char='O')
    for i in range(len(input)):
        input[i] = [char for char in input[i]]
        
    result = problem_1(input)
    print(result)
    result = problem_2(input)
    print(result)

if __name__ == '__main__':
    main()