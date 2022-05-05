import json

class Worker:
    def run(self, job_str):
        job_dict = json.loads(job_str)
        print(job_dict)
