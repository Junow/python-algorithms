import unittest
from LIS import lisNlogN, lisNSquare

class Test(unittest.TestCase):
  def test_LIS(self):
    INPUT = [
      [4, 7, 10, 3, 1, 8, 7, 2, 5, 7],
      [7, 9, 10, 8, 2, 3, 7],
      [7, 10, 8, 10, 1, 2, 9, 9, 1, 10],
      [2, 8, 3, 10, 5, 1, 5, 2, 3],
      [10, 6, 5, 9, 10, 9, 3, 4, 7, 1],
      [5, 8, 10, 3, 9, 1, 5, 8, 5, 6],
      [3, 2, 8, 2, 10, 1, 2, 2, 3],
      [3, 8, 10, 1, 5, 7, 9, 8, 9, 6],
      [4, 3, 4, 9, 1, 3, 7],
      [8, 6, 8, 9, 5, 1, 4, 4, 6, 3]
    ]
    OUTPUT=[
        4,
        3,
        4,
        3,
        3,
        3,
        3,
        5,
        3,
        3,
    ]
    for i in range(10):
      self.assertEqual(lisNlogN(INPUT[i]), OUTPUT[i])

if __name__ == '__main__':  
    unittest.main()


