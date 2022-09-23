#Import hacks for compatibility
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

# Merge Sort Tests
import unittest
from bubble_sort import bubble_sort

class TestSelectionSort(unittest.TestCase):
    def test_already_sorted(self):
        N = 1000
        arr = list(range(1, N+1))
        
        self.assertEqual(
             arr,
             bubble_sort(arr)
         )

    def test_reverse_sorted(self):
         N = 1000
         arr = list(range(1, N+1))[::-1]


         self.assertEqual(
             list(range(1, N+1)),
             bubble_sort(arr)
         )

    def test_empty(self):
         arr = []

         self.assertEqual(
             arr,
             bubble_sort(arr)
         )

    def test_one_element(self):
         arr = [1]

         self.assertEqual(
             arr,
             bubble_sort(arr)
         )

if __name__ == "__main__":
    unittest.main()