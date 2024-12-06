import pathlib
from typing import List, Tuple

def read_input(path : str) -> Tuple[List[Tuple[int, int]], List[int]]:

    rules = []
    books = []

    f_path = pathlib.Path(path).resolve()

    with open (f_path,'r') as f:
        lines = f.read().splitlines()

    reading_rules = True
    line_count = 0

    while reading_rules:
        str_to_parse = lines[line_count]
        if str_to_parse == '':
            reading_rules = False
        else:
            rules.append(parse_rule(str_to_parse))
        line_count += 1
    while line_count < len(lines):
        books.append(parse_books(lines[line_count]))
        line_count += 1

    return(rules, books)

def parse_rule(rule_str : str) -> Tuple[int,int]:
    rule_str = rule_str.split('|')
    rule = tuple([int(rule_str[0]), int(rule_str[1])])
    return rule

def parse_books(book_str : str) -> List[int]:
    book_str = book_str.split(',')
    book = [int(x) for x in book_str]
    return book


def book_to_dict(book : List[int]) -> dict:
    book_dict = {}
    for i in range(len(book)):
        if book[i] in book_dict.keys():
            book_dict[book[i]].append(i)
        else:
            book_dict[book[i]] = i
    return book_dict

def valid_update(book : list,  rule_set : dict) -> bool:

    book_dict = book_to_dict(book)

    for page in book[1:]:
        if page in rule_set.keys():
            for rule in rule_set[page]:
                before = page
                after = rule[1]

                if after in book_dict.keys():
                    if book_dict[before] > book_dict[after]:
                        return False
                    
    return True

    


def problem_1(rules : List[Tuple[int, int]],books : List[int]):

    count = 0

    rule_set = {}
    for rule in rules:
        if rule[0] in rule_set.keys():
            rule_set[rule[0]].append(rule)
        else:
            rule_set[rule[0]] = [rule]

    for book in books:
        is_valid = valid_update(book, rule_set)
        if is_valid:
            count += book[len(book)//2]

    return count

def fix_book(book : list,  rule_set : dict) -> list:

    book_dict = book_to_dict(book)

    for page in book[1:]:
        if page in rule_set.keys():
            for rule in rule_set[page]:
                before = page
                after = rule[1]

                if after in book_dict.keys():
                    if book_dict[before] > book_dict[after]:
                        book[book_dict[page]],book[book_dict[after]] = book[book_dict[after]], book[book_dict[page]]
                        return fix_book(book, rule_set)
    return book

def problem_2(rules : List[Tuple[int, int]],books : List[int]):

    count = 0

    rule_set = {}
    for rule in rules:
        if rule[0] in rule_set.keys():
            rule_set[rule[0]].append(rule)
        else:
            rule_set[rule[0]] = [rule]

    for book in books:
        is_valid = valid_update(book, rule_set)
        if is_valid:
            pass
        else:
            new_book = fix_book(book, rule_set)
            count += new_book[len(book)//2]

    return count

def main():
    rules, books = read_input('Day5/input.txt')
    results = problem_1(rules, books)
    print(results)
    results = problem_2(rules, books)
    print(results)

if __name__ == '__main__':
    main()
