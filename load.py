import itertools
import threading
import time
import sys
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rLoading......' + c)
        sys.stdout.flush()
        time.sleep(0.1)
def load_start():
	t = threading.Thread(target=animate)
	t.start()
load_start()
time.sleep(3)
done = True