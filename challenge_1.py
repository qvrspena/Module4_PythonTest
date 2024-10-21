#Create a test to check if the location of the R1 is TIP_Manila and the IP address is 192.168.45.25 and the subnet mask is 255.255.255.0.
#Vhan Randolp S Pena

import unittest

def check_R1(location, ip_add, subnet_mask):
    if (location == "Manila") and (ip_add == "192.168.45.25") and (subnet_mask == "255.255.255.0"):
        return True
    else:
        return False

class R1(unittest.TestCase):
    def test_check_R1(self):
        self.assertTrue(check_R1("Manila", "192.168.45.25", "255.255.255.0"))


if __name__ =="__main__":
    unittest.main()