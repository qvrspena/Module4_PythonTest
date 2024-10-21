#Create a test to check if the device is a router, a personal computer, a switch, or a server
#Vhan Randolp S Pena

import unittest

def check_device(device_type):
    return device_type


class DeviceCheck(unittest.TestCase):
    def test_check_device(self):
        valid_devices = ["router", "personal computer", "switch", "server"]
        self.assertIn(check_device("router"), valid_devices)
        self.assertIn(check_device("switch"), valid_devices)
        

if __name__ =="__main__":
    unittest.main()