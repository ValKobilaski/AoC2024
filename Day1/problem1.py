import random
import pathlib
from typing import Tuple

def quick_sort(arr: list) -> list:

    if len(arr) <= 1:
        return arr
    
    else:
    
        #Select pivot
        pivot_idx = random.randint(0, len(arr)-1)
        pivot = arr[pivot_idx]

        #Swap Pivot to end of arr
        arr[pivot_idx], arr[-1] = arr[-1], arr[pivot_idx]
        pivot_idx = len(arr)-1

        #init pointers
        left_idx = 0
        right_idx = len(arr) - 2

        #Partiioning step
        found_left = False
        found_right = False
        while left_idx <= right_idx:
            #if val at left_ptr should go after pivot
            if(arr[left_idx] >= pivot):
                found_left = True
            else:
                left_idx += 1
            
            #if val at right_ptr should go before pivot
            if(arr[right_idx] < pivot):
                found_right = True
            else:
                right_idx -=1

            #if found valid swap
            if found_left and found_right:
                arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]
                found_left = False
                found_right = False
        #Move back pivot to original position
        arr[left_idx], arr[pivot_idx] = arr[pivot_idx], arr[left_idx]
        #Recurse on each partition
        return quick_sort(arr[:left_idx]) + [arr[left_idx]] + quick_sort(arr[left_idx + 1:])

def _test_quick_sort(n = 50):
    arr_len = 50
    for i in range(n):
        rand_arr = [random.randint(0, 100)]
        qs_arr = quick_sort(rand_arr)
        if (qs_arr == sorted(rand_arr)):
            pass
        else:
            print("Error, quick sort failed:")
            print(qs_arr)
            print(sorted(rand_arr))
            return
    print("Quicksort test Succeded!")


def read_input(path : str) -> Tuple[list,list]:
    f_path = pathlib.Path(path).resolve()

    with open (f_path, 'r') as f:
        f_lines = f.readlines()
    arr_a = []
    arr_b = []
    for line in f_lines:
        split_line = line.split("   ")
        arr_a.append(int(split_line[0]))
        arr_b.append(int(split_line[1])) 
    return(arr_a, arr_b)

def test_read_input():
    pass


def problem_1(arr_a, arr_b):

    sorted_arr_a = quick_sort(arr_a)
    sorted_arr_b = quick_sort(arr_b)

    zipped_arrs = zip(sorted_arr_a, sorted_arr_b)
    diffs = [abs(elem_a - elem_b) for (elem_a, elem_b) in zipped_arrs]
    answer = sum(diffs)
    return answer
    
def problem_2(arr_a, arr_b):

    lens = len(arr_a)
    count = 0

    arr_a = quick_sort(arr_a)
    arr_b = quick_sort(arr_b)

    ptr_a = 0
    ptr_b = 0

    while ptr_a < lens and ptr_b < lens:

        #arr_a val is less than arr_b val, move on in arr_a
        if(arr_a[ptr_a] < arr_b[ptr_b]):
            ptr_a += 1

        #arr_a val is greater than arr_b val, move on in arr_b
        elif(arr_a[ptr_a] > arr_b[ptr_b]):
            ptr_b += 1

        else:
            #count_consecutive matches
            ptr_cons = ptr_b
            while(arr_a[ptr_a] == arr_b[ptr_cons]):
                count+=arr_a[ptr_a]
                ptr_cons += 1
            ptr_a +=1

    return count
                
            



def main():
    arr_a, arr_b = read_input('Day1/input.txt')

    result = problem_1(arr_a, arr_b)
    print(result)
    
    result = problem_2(arr_a, arr_b)
    print(result)


if __name__ == '__main__':
    main()