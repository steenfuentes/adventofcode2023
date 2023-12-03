import re
import timeit

def part1():
    with open('input.txt') as f:
        loc_sum: int = 0
        for line in f:
            digits = [int(d) for d in line if d.isdigit()]
            digit_str = int(str(digits[0]) + str(digits[-1]))
            loc_sum += digit_str

    return loc_sum


def part1rgx():
    with open('input.txt') as f:
        loc_sum: int = 0
        for line in f:
            digits = [int(d) for d in re.findall(r'\d', line)]
            digit_str = int(str(digits[0]) + str(digits[-1]))
            loc_sum += digit_str
    return loc_sum


d_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def part2trie():

    class Node:
        def __init__(self):
            self.children: list = [None]*26
            self.terminal: bool = False
            self.value: int  = None
            self.parent: Node  = None
            self.idx: int = None

    class Processor:
        def __init__(self):
            self.root = Node()

        def ch_idx(self, ch):
            return ord(ch) - ord('a')

        def insert(self, word):
            curr: Node = self.root
            for ch in word:
                idx = self.ch_idx(ch)
                if not curr.children[idx]:
                    curr.children[idx] = Node()
                    curr.children[idx].parent = curr

                curr = curr.children[idx]
                curr.idx = idx

            curr.terminal = True
            curr.value = d_dict[word]

        def build_trie(self, words):
            for word in words:
                self.insert(word)

        def calibrate_line(self, input) -> int:
            curr: Node = self.root
            next: Node = None
            prev: Node = None
            ch: str
            digits = []

            for ch in input:
                if ch.isdigit():
                    digits.append(int(ch))
                    next = self.root
                    curr = None
                elif ch.isalpha():
                    idx = self.ch_idx(ch)
                    next = curr.children[idx]

                    if next is not None and prev is not None:
                        if next.idx == prev.idx:
                            next = self.root

                    if next is not None and next.value is not None:
                        digits.append(next.value)
                        if self.root.children[idx] is not None:
                            next = self.root.children[idx]
                        else:
                            next = self.root

                    # elif next is None and self.root.children[idx] is not None:
                    #     next = self.root.children[idx]

                    elif next is None:
                        next = self.root

                prev = curr
                curr = next

            cal_val = int(str(digits[0]) + str(digits[-1]))
            return cal_val

    with open('input.txt') as f:
        processor = Processor()
        processor.build_trie(list(d_dict.keys()))

        loc_sum: int = 0
        for line in f:
            loc_sum += processor.calibrate_line(line)

    return loc_sum


def part2rgx():
    digits: dict[int, int] = {}

    with open('input.txt') as f:
        loc_sum: int = 0
        for line in f:
            lo = 999
            hi = -1
            digits = {}
            for i,ch in enumerate(line):
                if ch.isdigit():
                    digits[i] = int(ch)
                    lo = min(lo, i)
                    hi = max(hi, i)

            for k in d_dict.keys():
                for m in re.finditer(k, line):
                    digits[m.start()] = d_dict[k]
                    lo = min(lo, m.start())
                    hi = max(hi, m.start())

            loc_sum += int(str(digits[lo]) + str(digits[hi]))

    return loc_sum


if __name__ == '__main__':
    sum = part1()
    print(f"Part 1: {sum}", "time:",
          timeit.timeit("part1()", setup="from __main__ import part1",
                        number=100))

    sum = part1rgx()
    print(f"Part 1 w/ regex: {sum}", "time:",
          timeit.timeit("part1rgx()", setup="from __main__ import part1rgx",
                        number=100))

    sum = part2trie()
    print(f"Part 2 w/ trie: {sum}", "time:",
          timeit.timeit("part2trie()", setup="from __main__ import part2trie",
                        number=100))

    sum = part2rgx()
    print(f"Part 2 w/ regex: {sum}", "time:",
          timeit.timeit("part2rgx()", setup="from __main__ import part2rgx",
                        number=100))