import threading
import time

def worker(event, name):
    print('{} waiting for event...'.format(name))
    event.wait()
    print('{} event triggered at {}'.format(name, time.strftime('%H:%M:%S')))

event = threading.Event()

t1 = threading.Thread(target=worker, args=(event, 'Thread 1'))
t2 = threading.Thread(target=worker, args=(event, 'Thread 2'))

t1.start()
t2.start()

time.sleep(3)
print('Event is set at {}'.format(time.strftime('%H:%M:%S')))
event.set()

t1.join()
t2.join()
