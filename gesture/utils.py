import time
import threading

class ArgumentError(Exception):
    pass

class Thread(threading.Thread):
    def run(self):
        self.exc = None
        try:
            super().run()
        except Exception as e:
            self.exc = e

    def join(self):
        threading.Thread.join(self)
        if self.exc:
            raise self.exc

def validate(item):
    if not (isinstance(item, dict) and "class" in item and "args" in item):
        raise ArgumentError("Job must be a dict with 'class' and 'args' keys: `%s`" % item)
    if not isinstance(item["args"], list):
        raise ArgumentError("Job args must be a list: `%s`" % item)
    if not isinstance(item["class"], str):
        raise ArgumentError("Job class must be a str representation of the class name: `%s`" % item)
    if 'at' in item and not isinstance(item['at'], float):
        raise ArgumentError("Job 'at' must be a float timestamp: `%s`" % item)

def normalize_item(item):
    validate(item)
    # `created_at` is the key to make two same jobs different, so in general
    # we have two same jobs in Redis.
    item["created_at"] = time.time()
    return item

def safe_thread(function):
    def watchdog():
        try:
            function()
        except Exception as e:
            # TODO: Add handler to exception
            raise e

    thread = Thread(target=watchdog)
    thread.start()
    return thread
