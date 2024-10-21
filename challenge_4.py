#Create a test to check if the subnet mask is correct using the given prefix
#Vhan Randolp S Pena

import unittest

def check_prefix(prefix_length):
    if not (0 <= prefix_length <= 32):
        return False

    octet = prefix_length // 8
    remainder = prefix_length % 8

    mask = [0] * 4

    octet_val = [0, 128, 192, 224, 240, 248, 252, 254, 255]

    for i in range(octet):
        mask[i] = 255

    if remainder > 0:
        mask[octet] = octet_val[remainder]

    return '.'.join(map(str, mask))

class TestSubnet(unittest.TestCase):
    def test_check_prefix(self):
        self.assertEqual(check_prefix(31), "255.255.255.254")

if __name__ =="__main__":
    unittest.main()