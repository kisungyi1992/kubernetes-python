import unittest
from unit_test import deployment_unittest
from unit_test import serviceaccount_unittest

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(deployment_unittest)
    suite = unittest.TestLoader().loadTestsFromModule(serviceaccount_unittest)
    unittest.TextTestRunner(verbosity=2).run(suite)