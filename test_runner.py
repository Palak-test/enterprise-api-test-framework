#!/usr/bin/env python3
"""
Basic test runner for enterprise-api-test-framework
"""
import sys
import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    tests = loader.discover('src')
    testRunner = unittest.runner.TextTestRunner()
    result = testRunner.run(tests)
    sys.exit(not result.wasSuccessful())
