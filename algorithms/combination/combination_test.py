import unittest
from combination import combination

class Test(unittest.TestCase):
  def test_combination(self):
    arr = [1,2,3]
    expected = [[1,2], [2,3], [1,3]]
    result = combination(arr, 2)
    for el in list(result):
      self.assertIn(el, expected)





if __name__ == '__main__':  
    unittest.main()