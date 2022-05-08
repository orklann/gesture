import pathlib
import sys

# Make it work to import parent pacakage
cwd = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(cwd))

from gesture.job import Job

class SimpleJob(Job):
    def perform(self, count):
        print(count)
