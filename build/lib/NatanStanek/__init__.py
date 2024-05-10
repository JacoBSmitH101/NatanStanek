# NatanStanek/__init__.py
import time
import random
def greet():
    print("Hello from NatanStanek!")

def DoesNatanSmell():
    print("Natan stinks")

def McDonaldsBreak(sec):
    time.sleep(sec)
    print("Break over, back to work!")

def DriveCar():
    num = random.randint(0, 10)
    if (num > 8):
        print("For once Natan is driving safely")
    else:
        print("Natan is driving like a maniac")
    time.sleep(2)
    print("Natan has fallen asleep at the wheel")

startTime = 0
def StartTest():
    global startTime
    startTime = time.time()


def EndTest(output = True):
    if (output):
        print("Test took: ", time.time() - startTime, " seconds")
    else:
        return time.time() - startTime

