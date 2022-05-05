import time
from .client import Client

class NoClassError(Exception):
    pass

class Job:
    class_map = {}

    @classmethod
    def class_by_name(cls, name):
        if name in cls.class_map:
            return cls.class_map[name]
        for klass in cls.__subclasses__():
            if klass.__name__ == name:
                cls.class_map[klass.__name__] = klass
                return klass
        raise NoClassError("No class definition found for %s" % name)

    @classmethod
    def perform_async(cls, *args):
        payload = {"class": cls.__name__, "args": list(args)}
        payload["at"] = time.time()
        client = Client()
        client.push(payload)
