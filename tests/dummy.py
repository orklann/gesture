from gesture.job import Job

class DummyJob(Job):
    def perform(count):
        return count
