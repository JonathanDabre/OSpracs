import time
from multiprocessing import Process, Lock, Value

def add_five(total, lock):
    for i in range(100):
        time.sleep(0.005) #takes argument in seconds
        lock.acquire() #sets the lock, doesn't allow other processes to use 
        print('a')
        total.value += 5
        lock.release() #resets the lock, allow other processes to use
        
    

def sub_four(total, lock):
    for i in range(100):
        time.sleep(0.005) # 5 miliseconds
        lock.acquire()
        print('b')
        total.value -= 4
        lock.release()  
        
if __name__ == "__main__":
    lock = Lock() #built-in lock variable, from class Lock
    total = Value('i', 500)  #buil-in shared variable from class Value, 'i' indicates integer
    
    addProcess = Process(target=add_five, args=(total, lock))
    subProcess = Process(target=sub_four, args=(total, lock))
    
    addProcess.start()
    subProcess.start()
    
    addProcess.join()
    subProcess.join()
    
    print(total.value)
    