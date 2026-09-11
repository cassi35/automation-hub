from queue import Queue
from threading import Thread
from dataclasses import dataclass


@dataclass
class Task:
    operation: str
    args: tuple
    result: Queue


class ExecutionQueue:
    def __init__(self, client):
        self.client = client
        self.queue = Queue()

        self.worker = Thread(
            target=self._worker,
            daemon=True,
        )
        self.worker.start()

    def _worker(self):
        while True:
            task = self.queue.get()

            try:
                method = getattr(self.client, task.operation)
                result = method(*task.args)
                task.result.put(result)
            except Exception as e:
                task.result.put(e)
            finally:
                self.queue.task_done()

    def call(self, operation, *args):
        result_queue = Queue()

        self.queue.put(
            Task(
                operation=operation,
                args=args,
                result=result_queue,
            )
        )

        result = result_queue.get()

        if isinstance(result, Exception):
            raise result

        return result

    def put(self, operation, *args):
        self.queue.put(
            Task(
                operation=operation,
                args=args,
                result=Queue(),
            )
        )