import time
import sys
import os

myString = "Follow white rabbit!"
clear = lambda: os.system('cls') # Windows
# clear = lambda: os.system('clear') - Linux
clear()
for i in myString:
    time.sleep(0.2)
    sys.stdout.write(i)
    sys.stdout.flush()