# NOTES:
# This initially feels like a graph problem but buildling the entire graph
# may not be necessary. Likely we can reach the solution by keeping a 3 line
# buffer of the input and moving through it.


from dataclasses import dataclass, field



@dataclass
class Buffer:
    data: list[str] = field(default_factory=list)
    bounds: tuple[int, int] = (0, 0)

    def init_buffer(self, input: list):
        self.bounds = (0, 2)
        self.data[1:] = input[:2]
        for i in range(len(self.data)):
            self.data[i] = self.data[i].rstrip()

    def slide(self, input: list) -> list[str]:
        if self.bounds[0] == 0:
            self.bounds = (self.bounds[0] + 1, self.bounds[1] + 2)
        else:
            self.bounds = (self.bounds[0] + 1, self.bounds[1] + 1)
        self.data = input[self.bounds[0]:self.bounds[1]]

        for i in range(len(self.data)):
            self.data[i] = self.data[i].rstrip()

        return self.data


class PartScanner:

    cursor: int
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '+', '=', '?', '/']

    def __init__(self, input: list):
        self.buffer = Buffer(data=[""]*3)
        self.buffer.init_buffer(input)
        self.cursor = 0
        self.invalid_parts = []
        self._validate_parts()

    def update(self, input: list) -> list[str]:
        self.buffer.slide(input)
        self._validate_parts()

    def _validate_parts(self):
        i: int = 0
        while i < len(self.buffer.data[1]):
            part_loc, j = self._next_part(i)
            # not sure why exclusion of second clause causes blank parts to be
            # added to invalid_parts
            if (not self._validate_part(part_loc)) and \
               (part_loc[1]-part_loc[0] >= 1):
                self.invalid_parts.append(int(self.buffer.data[1][part_loc[0]:part_loc[1]]))
            i = j

    def _next_part(self, cursor) -> [int, int]:
        part_loc: [int, int] = [0, 0]
        if self.buffer.data[1][cursor] == ".":
            cursor += 1
        elif self.buffer.data[1][cursor].isdigit():
            part_loc[0] = cursor
            while self.buffer.data[1][cursor].isdigit() and cursor < len(self.buffer.data[1])-1:
                cursor += 1
            else:
                part_loc[1] = cursor
                cursor += 1
        else:
            cursor += 1
        return part_loc, cursor

    def _validate_part(self, part_loc: [int, int]) -> bool:
        valid: bool = False
        for line in self.buffer.data:
            for i in line[part_loc[0]-1:part_loc[1]+1]:
                if i in self.symbols:
                    valid = True
                    return valid
        return valid


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = f.readlines()

    scanner = PartScanner(input)

    while scanner.buffer.bounds[1] < len(input)+1:
        scanner.update(input)
    print(scanner.invalid_parts)
    print(sum(scanner.invalid_parts))