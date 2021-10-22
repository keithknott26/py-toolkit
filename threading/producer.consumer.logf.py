import multiprocessing

##########################
#multiprocessing functions
##########################
def q_reader(queue):
    msg = []
    ## Read from the queue; this will be spawned as a separate Process
    while True:
        try:
            message = queue.get(True, 180)
            msg.append(message)         # Read from the queue and do nothing
            #print debugStr, "Got Message: + " + str(message)
            if (message == 'DONE'):
                break
        except Exception as error:
            if debug:
                print debugStr, "q_reader(): Queue is now empty..." + str(error) 
            break
        #print debugStr, "Reading from queue..."
    #print debugStr, "q_reader(): Returning " + str(len(msg)) + " lines"
    return msg

def q_writer(queue, message):
    ## Write to the queue
    queue.put(message)

def info(title):
    print title
    print debugStr, 'module name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print debugStr,'parent process:', os.getppid()
    print debugStr,'process id:', os.getpid()
   