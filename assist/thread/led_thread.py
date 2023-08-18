import threading

def thread(fun1, fun2, args2, event):

    stop_event = threading.Event()

    # roof function
    roof_f = threading.Thread(target=fun1, args=(stop_event,))
    # result function
    result_f = threading.Thread(target=fun2, args=(args2,))

    # function start
    result_f.start()
    roof_f.start()

    result_f.join()
    stop_event.set()
    event()
    roof_f.join()

    return
    