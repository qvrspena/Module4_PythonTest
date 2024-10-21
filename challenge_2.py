#Vhan Randolp S Pena

import unittest
import re

def check_ip_and_mac(ip_add, mac_add):
    ip_pattern = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    mac_pattern = r'^(?:[0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}$'
    
    if re.match(ip_pattern, ip_add) and re.match(mac_pattern, mac_add):
        return True
    else:
        return False

class TestCheckIPAndMac(unittest.TestCase):
    def test_check_ip_and_mac(self):
        self.assertTrue(check_ip_and_mac("255.255.255.255", "00:1A:2B:3C:4D:5E"))
    def test_check_ip_and_mac2(self):
        self.assertTrue(check_ip_and_mac("192.168.45.25", "00:1A:2B:3C:4D:5A"))
    def test_check_ip_and_mac3(self):
        self.assertTrue(check_ip_and_mac("192.168.0.1", "00:1A:2B:3C:4D:5E"))
        
if __name__ == "__main__":
    unittest.main()
