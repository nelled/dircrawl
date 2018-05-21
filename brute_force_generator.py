import itertools
import string


class BruteForceGenerator:
    ALPHABET = string.ascii_letters + string.digits

    def __init__(self, min_len=3, max_len=5):
        self.max_len = max_len
        self.min_len = min_len

    def generator(self):
        for s in range(self.min_len, self.max_len + 1):
            for comb in itertools.combinations(BruteForceGenerator.ALPHABET, s):
                yield ''.join(comb)


if __name__ == '__main__':
    bfg = BruteForceGenerator(2, 3)
    for c in bfg.generator():
        print(''.join(c))
