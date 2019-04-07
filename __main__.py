import unittest
from unit_test import deployment_unittest

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(deployment_unittest)
    unittest.TextTestRunner(verbosity=2).run(suite)