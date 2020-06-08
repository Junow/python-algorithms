import unittest
from binarySearch import binarySearch


class Test(unittest.TestCase):
  def testBinarySearch1(self):
    arr = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
    ]
    target = [
        1,
        3,
        5,
        9,
        0
    ]
    expected = [
        0,
        2,
        4,
        None,
        None,
    ]

    for i in range(5):
      result = binarySearch(arr[i], 0, len(arr[i])-1, target[i])
      self.assertIsNone
      self.assertEqual(result, expected[i])


if __name__ == '__main__':
  unittest.main()
