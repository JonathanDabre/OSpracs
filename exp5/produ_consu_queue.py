import queue
import threading
import time

q = queue.Queue(5) #module.TypeOfQueue(size)
#queue in python has built-in thread safe implementation, so we don't have to use lock variable explicitly
#It does locking by itself whenever felt necessary.

def producer():
    
    while True:
        if not q.full():
            #here we could have used lock acquire
            item = time.time()
            q.put(item)        
            print(f"Item Produced: {item}")
            #here we would have released the lock
            time.sleep(1)
        
def consumer():
    
    while True:
        if not q.empty():
            item = q.get()
            print(f"Item Consumed: {item}")
            time.sleep(2)
        
        
if __name__ == '__main__':
    
    pro_thread = threading.Thread(target=producer)
    con_thread = threading.Thread(target=consumer)
        
    pro_thread.start()
    con_thread.start()
        
    pro_thread.join()
    con_thread.join()
         
        