import pathlib
from typing import List, Callable
import warnings

def read_input(path) -> List[List[int]]:

    input = []

    f_path = pathlib.Path(path).resolve()
    with open(f_path, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.split()
        input.append([int(x) for x in line])
    return input

def all_asc_or_desc(arr: list) -> bool:
    if len(arr) < 2:
        warnings.warn('USER Warning: all_asc_or_desc was called on list of size < 2')
        return True
    
    #handle neither asc or desc case
    if arr[1] == arr[0]:
        return False

    is_asc = arr[1] > arr[0]

    #is ascending
    if is_asc:
        for i in range(1,len(arr)):
            if arr[i] <= arr[i-1]:
                return False
    #is descending
    else:
        for i in range(1,len(arr)):
            if arr[i] >= arr[i-1]:
                return False
        
    return True


def diff_of_1_to_3(arr : list):
    if len(arr) < 2:
        warnings.warn('USER Warning: diff_of_1_to_3 was called on list of size < 2')
        return True
    
    for i in range(1, len(arr)):
        diff = abs(arr[i] - arr[i-1])
        if not (1 <= diff <= 3):
            return False
    return True

def is_safe(arr: list, constraints : List[Callable[[list],bool]]):
    for constraint in constraints:
        if constraint(arr) == False:
            return False
    return True

def problem_1(arrs : List[List[int]]):
    # Horribly inefficient but very modular ;)

    count = 0
    constraints = [all_asc_or_desc, diff_of_1_to_3]

    for arr in arrs:
        if is_safe(arr, constraints):
            count += 1
    return count

def is_safe_dampener(arr) -> bool:


    dampened = False

    #handle exceptions
    if len(arr) < 2:
        return True
    if arr[1] == arr[0]:
        return False
    
    is_asc = arr[1] > arr[0]

    for i in range(1, len(arr)):
        if is_asc:
            diff = arr[i] - arr[i-1]
            if not(1 <= diff <= 3):
                return is_safe(arr[:i] + arr[i+1:], [all_asc_or_desc, diff_of_1_to_3])
        else:
            diff = arr[i] - arr[i-1]
            if not(-3 <= diff <=-1):
                return is_safe(arr[:i] + arr[i+1:], [all_asc_or_desc, diff_of_1_to_3])
    return True
    

def problem_2(arrs) -> int:
    #efficient but not modular :(
    count = 0
    constraints = [all_asc_or_desc, diff_of_1_to_3]

    for arr in arrs:
        if not(is_safe(arr, constraints)):
            #Get all versions of array without a single element
            minus_ones = [arr[:i] + arr[i+1:] for i in range(len(arr))]
            #check if any are safe
            if any(map(lambda x: is_safe(x, constraints), minus_ones)):
                count += 1
        else:
            count += 1

    return count

            


def main():
    input = read_input('Day2/input.txt')
    result = problem_1(input)
    print(result)
    result = problem_2(input)
    print(result)


if __name__ == '__main__':
    main()