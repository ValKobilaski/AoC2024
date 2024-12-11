import pathlib
from typing import List
import copy


def read_input(path: str) -> List[int]:

    f_path = pathlib.Path(path).resolve()
    with open(f_path, "r") as f:
        f_input = f.read()

    block_arr = [int(num) for num in f_input]

    return block_arr


def get_seg_mask(block_arr: List[int]) -> List[bool]:

    seg_mask = []

    for i in range(len(block_arr)):
        if i % 2 == 0:
            seg_mask.extend([True] * block_arr[i])
        else:
            seg_mask.extend([False] * block_arr[i])

    return seg_mask


def check_sum(disk: List[int]):

    count = 0
    for i in range(len(disk)):
        count += disk[i] * i

    return count


def problem_1(block_arr: List[int]):

    evens = block_arr[0::2]

    disk = []
    unparted_data = []

    for i in range(len(evens)):
        unparted_data.extend([i] * evens[i])

    left_ptr = 0
    right_ptr = len(unparted_data) - 1

    seg_mask = get_seg_mask(block_arr)

    while len(seg_mask) > 0:

        normal_data = seg_mask.pop(0)
        if normal_data:
            disk.append(unparted_data[left_ptr])
            left_ptr += 1
        else:
            disk.append(unparted_data[right_ptr])
            right_ptr -= 1

    disk = disk[: sum(evens)]
    result = check_sum(disk)

    return result


def problem_2(block_arr: List[int]):

    idx = 0
    pages = []
    blank_space = []
    for i in range(len(block_arr)):
        if i % 2 == 0:
            pages.append((idx, [i // 2] * block_arr[i]))
            idx += block_arr[i]
        else:
            blank_space.append((idx, [0] * block_arr[i]))
            idx += block_arr[i]

    insertions = []

    for i in range(len(pages) - 1, 1, -1):
        page_len = len(pages[i][1])

        found_space = False

        for j in range(len(blank_space)):

            if not found_space:

                if page_len <= len(blank_space[j][1]):

                    insertions.append((blank_space[j][0], pages[i][1]))
                    blank_space[j] = (
                        blank_space[j][0] + page_len,
                        blank_space[j][1][page_len:],
                    )
                    pages.pop(i)
                    found_space = True

    empties_to_keep = []
    for blank in blank_space:
        if len(blank[1]) > 0:
            empties_to_keep.append(blank)
    blank_space = empties_to_keep

    disk_spaces = pages + insertions + blank_space
    disk_spaces.sort(key=lambda x: x[0])

    disk = []
    for disk_space in disk_spaces:
        disk.extend(disk_space[1])

    result = check_sum(disk)
    return result


def main():
    block_arr = read_input("Day9/input.txt")
    # result = problem_1(block_arr)
    result = problem_2(block_arr)
    print(result)


if __name__ == "__main__":
    main()
