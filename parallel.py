from threading import Thread
from threading import Lock 

def _do_working_thread(lock, iterator, func, callback, args):
    while True:
        try:
            lock.acquire()
            item = iterator.next()
        except StopIteration:
            break
        finally:
            lock.release()
        ret, data = func(item, args)
        callback(item, ret, args, data)

def parallel_map(array, func, callback, args, thread_num):
    iterator = iter(array)
    threads = []
    lock = Lock()
    for i in range(thread_num):
        th = Thread(target = _do_working_thread, args = (lock, iterator, func, callback, args))
        th.start()
        threads.append(th)
    for th in threads:
        th.join()


if __name__ == '__main__':
    def func(item ,args):
        print item
        import time
        print item
        time.sleep(1)
        return True, None

    def callback(item, ret, args, data):
        print item, ret

    l = range(10)
    parallel_map(l, func, callback, None, 2)
