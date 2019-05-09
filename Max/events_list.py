from time import time

events_list = []


class Event(object):#实现消息队列

    def __init__(self, *args, **kwargs):
        self.callback = lambda: None
        events_list.append(self)

    def set_callback(self, callback):
        self.callback = callback

    def is_ready(self):
        result = self._is_ready()

        if result:
            self.callback()

        return result


class SleepEvent(Event):

    def __init__(self, timeout):#重写time
        super(SleepEvent, self).__init__(timeout)
        self.timeout = timeout
        self.start_time = time()

    def _is_ready(self):
        return time() - self.start_time >= self.timeout


def sleep(timeout):
    return SleepEvent(timeout)


def run(tasks):#协程
    for task in tasks:
        _next(task)

    while len(events_list):
        for event in events_list:
            if event.is_ready():
                events_list.remove(event)
                break


def _next(task):
    try:
        event = next(task)
        event.set_callback(lambda: _next(task))  # 1
    except StopIteration:
        pass


def task(name):#main
    print(name, 1)
    yield sleep(1)
    print(name, 2)
    yield sleep(2)
    print(name, 3)


if __name__ == '__main__':
   run((task('hsfzxjy'), task('Jack')))