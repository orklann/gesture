import json
from .job import Job

class Worker:
    def run(self, job_str):
        instance, args = self.resolve_job(job_str)

    def resolve_job(self, job_str):
        job_dict = json.loads(job_str)
        kclass = Job.class_by_name(job_dict["class"])
        instance = kclass()
        args = job_dict["args"]
        return (instance, args)

