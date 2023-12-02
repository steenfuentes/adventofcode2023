

def part1():
    with open('input.txt') as f:
        loc_sum: int = 0
        for line in f:
            digits = [int(d) for d in line if d.isdigit()]
            digit_str = int(str(digits[0]) + str(digits[-1]))
            loc_sum += digit_str
        print(f"Part 1: {loc_sum}")


def part2():

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

    class Node:
        def __init__(self):
            self.children = [None]*26
            self.terminal = False
            self.value = None

    class Processor:
        def __init__(self):
            self.root = Node()

        def ch_idx(self, ch):
            return ord(ch) - ord('a')

        def insert(self, word):
            curr = self.root
            for ch in word:
                idx = self.ch_idx(ch)
                if not curr.children[idx]:
                    curr.children[idx] = Node()
                curr = curr.children[idx]
            curr.terminal = True
            curr.value = d_dict[word]

        def build_trie(self, words):
            for word in words:
                self.insert(word)

        def calibrate_line(self, input) -> int:
            curr: Node = self.root
            ch: str
            digits = []

            for ch in input:
                if ch.isdigit():
                    digits.append(int(ch))
                    curr = self.root
                elif ch.isalpha():
                    idx = self.ch_idx(ch)
                    curr = curr.children[idx]
                    if curr is not None and curr.terminal:
                        digits.append(curr.value)
                        curr = self.root

                    elif curr is None and self.root.children[idx] is not None:
                        curr = self.root.children[idx]

                    elif curr is None:
                        curr = self.root

            cal_val = int(str(digits[0]) + str(digits[-1]))
            print(f"Calibration value: {cal_val}")
            return cal_val

    with open('input.txt') as f:
        processor = Processor()
        processor.build_trie(list(d_dict.keys()))

        loc_sum: int = 0
        for line in f:
            loc_sum += processor.calibrate_line(line)

        print(f"Part 2: {loc_sum}")


if __name__ == '__main__':
    part1()
    part2()