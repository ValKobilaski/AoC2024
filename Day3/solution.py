import re
import pathlib

def read_input(path:str):
    f_path = pathlib.Path(path).resolve()
    with open(f_path,'r') as f:
        input = f.read()
    return input


def evaluate_mul(mul_string):
    nums = mul_string[4:-1]
    nums = nums.split(',')
    return (int(nums[0]) * int(nums[1]))

def problem_1(input):
    if input == "":
        return 0
    muls = re.findall("mul\(\d{1,3},\d{1,3}\)", input)
    sum = 0
    for mul in muls:
        sum += evaluate_mul(mul)
    return sum

def problem_2(input):

    input = input.replace('\n','')
    flags =re.findall(r"do\(\)|don't\(\)",input)
    flags = [x == "do()" for x in flags]
    flags.insert(0,True)
    segments = re.split(r"do\(\)|don't\(\)",input)
    parsed = zip(flags, segments)

    sum = 0
    for string in parsed:
        if string[0]:
            sum += problem_1(string[1])
    return sum

def main():

    input = read_input('Day3/input.txt')
    #print(len(re.findall("\\n", input)))
    result = problem_1(input)
    #print(result)
    result = problem_2(input)
    print(result)


if __name__ == "__main__":
    main()