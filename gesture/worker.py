import json
from .job import Job

class Worker:
    def run(self, job_str):
        instance, args = self.resolve_job(job_str)
        return self.execute_job(instance, args)

    def resolve_job(self, job_str):
        job_dict = json.loads(job_str)
        kclass = Job.class_by_name(job_dict["class"])
        instance = kclass()
        args = job_dict["args"]
        return (instance, args)

    def execute_job(self, instance, args):
        return instance.perform(*args)
