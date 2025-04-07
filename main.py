# import libraries
import threading
import random
from time import sleep


# we have an object 'Box'
class Box:
    def __init__(self):
        self.lock = threading.Lock()
        self.box_count = 0
        self.box_num = random.randint(1, 60)

    def increment(self, worker_type):
        with self.lock:
            if self.box_num > 0:
                self.box_count += 1
                self.box_num -= 1
                print(f'{threading.current_thread().name}: {worker_type} worker moved a box. total box is {self.box_count}')
                return True
            else:
                return False


# The function for workers(Aghaye Hashemiiii?!) that how much time they spend
def worker(box, worker_type):
    if worker_type == 'young':
        transport_time = 4
    else:
        transport_time = random.randint(5,  8)
    while box.box_num > 0:

        # load balancing among threads
        sleep(3)
        sleep(transport_time)

        # box moved
        if box.increment(worker_type):
            # Return time spent by the worker
            sleep(transport_time/2)
            # print(f'{threading.current_thread().name}: {worker_type} worker moved a box. total box is {box.box_count}')
        else:
            break

# shop simulation
def main():
    box = Box()
    box_num = box.box_num
    if box_num < 20:
        worker_num = 2
    elif 20 <= box_num < 40:
        worker_num = 3
    else:
        worker_num = 4

    threads = []

    for i in range(worker_num):
        worker_type = random.choice(['young', 'old'])
        thread = threading.Thread(target=worker, args=(box, worker_type))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Total boxes moved: {box.box_count}')


main()
