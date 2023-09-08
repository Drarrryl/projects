import threading
import queue
import datetime
import time

class myThread(threading.Thread):
    def __init__(self, in_queue, out_queue):
        threading.Thread.__init__(self)
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        while True:
            item = self.in_queue.get() #blocking till something is available in the queue
            print("Running lines of code.")
            processed_data = item + str(datetime.now()) + 'Processed'
            self.out_queue.put(processed_data)


IN_QUEUE = queue.Queue()
OUT_QUEUE = queue.Queue()

#starting 10 threads to do your work in parallel 
for i in range(1):
    t = myThread(IN_QUEUE, OUT_QUEUE)
    t.setDaemon(True)
    t.start()

#now populate your input queue
for i in range(3000):
    IN_QUEUE.put("string to process")

while not IN_QUEUE.empty():
    print("Data left to process - ", IN_QUEUE.qsize())
    time.sleep(10)

#finally printing output
while not OUT_QUEUE.empty():
    print(OUT_QUEUE.get())