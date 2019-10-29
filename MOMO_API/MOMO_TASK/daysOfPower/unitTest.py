import unittest 
from daysOfPower import calculate 

class TestDaysOfPower(unittest.TestCase): 

    def test_daysOfPower(self):         
        self.assertEqual(calculate([{2:1000},{5:500},{3:1500}, {2:2000}],50000), [10,47000,3000]) 

        
  
if __name__ == '__main__': 
    unittest.main() 