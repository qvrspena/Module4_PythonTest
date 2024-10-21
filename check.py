#Vhan Randolp S. Pena
import unittest

def check(x):
    if x >= 100:
        return True
    else:
        return False

class myTest(unittest.TestCase):
    def test(self):
        self.assertTrue(check(100))

if __name__ == '__main__':
    unittest.main()