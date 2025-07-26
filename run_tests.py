import unittest
import os

TEST_DIR = r"D:\LoginWare-internship\bus_projects"

def run_tests():
    loader = unittest.TestLoader()
    suite = loader.discover(TEST_DIR, pattern='test_*.py')  # Looks for test_*.py files
    
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
