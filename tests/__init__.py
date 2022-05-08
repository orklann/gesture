import unittest
from .utils import clear_set, clear_list
import redis

def stopTestRun(self):
    """
    https://docs.python.org/3/library/unittest.html#unittest.TestResult.stopTestRun
    Called once after all tests are executed.

    :return:
    """
    r = redis.Redis()
    clear_set(r, "schedule")
    clear_list(r, "queue")
    print("")
    print("Clean up redis!")

setattr(unittest.TestResult, 'stopTestRun', stopTestRun)
