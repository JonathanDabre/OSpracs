    pro_thread = threading.Thread(target=producer)
    con_thread = threading.Thread(target=consumer)
        
    pro_thread.start()
    con_thread.start()
        
    pro_thread.join()
    con_thread.join()