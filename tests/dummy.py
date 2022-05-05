from gesture.job import Job

class DummyJob(Job):
    def perform(self, count):
        return count
