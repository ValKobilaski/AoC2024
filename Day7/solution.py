import pathlib
from typing import List, Tuple
from copy import deepcopy

def read_input(path : str) ->  List[Tuple[int, List]]:

    f_path = pathlib.Path(path)
    with open(f_path,'r') as f:
        lines = f.read().splitlines()

    answers = []
    numbers = []

    for line in lines:
        answer, number = line.split(':')
        answers.append(int(answer))
        numbers.append([int(x) for x in number.split()])
    
    input = list(zip(answers,numbers))
    return input

def parse_ops(op: str):
    if op == '+':
        return 
def rec_eqn_solver(nums : List[int], with_concat) -> List[int]:

    #base case
    if len(nums) == 1:
        return nums
    
    num_1 = nums.pop(0)
    num_2 = nums.pop(0)

    summation = rec_eqn_solver([num_1 + num_2] + nums, with_concat)
    product = rec_eqn_solver([num_1 * num_2] + nums, with_concat)
    if with_concat:
        concat = rec_eqn_solver([concat_ints(num_1, num_2)] + nums, with_concat)
    
    if with_concat:
        return summation + product + concat
    else:
        return summation + product

def problem_1(input : List[Tuple[int, List]]) -> int:

    count = 0
    
    for calibration in input:
        result, nums  = calibration

        all_combs = rec_eqn_solver(nums, False)
        if result in all_combs:
            count += result
    
    return count

def concat_ints(num_a : int, num_b : int):

    a_str = str(num_a)
    b_str = str(num_b)
    combine = a_str + b_str

    return int(combine)

def problem_2(input : List[Tuple[int, List]]) -> int:
    count = 0
    
    for calibration in input:
        result, nums  = calibration

        all_combs = rec_eqn_solver(nums, True)
        if result in all_combs:
            count += result
    
    return count

def main():
    input = read_input('Day7/input.txt')
    problem_1_input = deepcopy(input)
    result = problem_1(problem_1_input)
    print(result)
    problem_2_input = deepcopy(input)
    result = problem_2(problem_2_input)
    print(result)


if __name__ =='__main__':
    main()