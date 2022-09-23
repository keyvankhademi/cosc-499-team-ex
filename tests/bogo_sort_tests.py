# Import hacks for compatibility
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

# Merge Sort Tests
import unittest
from ..bogo_sort import bogo_sort


class TestMergeSort(unittest.TestCase):
    def test_already_sorted(self):
        N = 5
        arr = list(range(1, N + 1))

        self.assertEqual(
            arr,
            bogo_sort(arr)
        )

    def test_reverse_sorted(self):
        N = 5
        arr = list(range(1, N + 1))[::-1]

        self.assertEqual(
            list(range(1, N + 1)),
            bogo_sort(arr)
        )

    def test_empty(self):
        arr = []

        self.assertEqual(
            arr,
            bogo_sort(arr)
        )

    def test_one_element(self):
        arr = [1]

        self.assertEqual(
            arr,
            bogo_sort(arr)
        )


if __name__ == "__main__":
    unittest.main()
