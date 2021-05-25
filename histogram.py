import unittest


class Histogram:
    def __init__(self, hist=None):
        self.hist = {} if hist is None else hist

    def __repr__(self):
        return f"Histogram({self.hist})"

    def bump(self, key):
        if key not in self.hist:
            self.hist[key] = 0
        self.hist[key] += 1

    def count_for(self, key):
        return self.hist.get(key, 0)

    def total_count(self):
        return sum(self.hist.values())

    def all_labels(self):
        return self.hist.keys()

    def mode(self):
        return max([(count, key) for (key, count) in self.hist.items()])[1]

    def ranking(self):
        return [(key, count) for (count,key) in reversed(sorted([(count, key) for (key, count) in self.hist.items()]))]


class TestHistogram(unittest.TestCase):
    def test_1(self):
        hist = Histogram()
        values = [10, 15, 20]
        for i in range(len(values)):
            for j in range(values[i]):
                hist.bump(i)

        for i in range(len(values)):
            self.assertEqual(hist.count_for(i), values[i])

        self.assertEqual(len(values), len(hist.all_labels()))
        self.assertEqual(sum(values), hist.total_count())
        self.assertEqual(2, hist.mode())
        self.assertEqual([(2, 20), (1, 15), (0, 10)], hist.ranking())
