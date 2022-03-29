import threading
import time

def Driving():
    for i in range(10):
        print('กำลังขับรถ...', i)
        time.sleep(1)

def Meeting():
    for i in range(10):
        print('กำลังประชุม...',i)
        time.sleep(0.5)

task1 = threading.Thread(target=Driving)
task2 = threading.Thread(target=Meeting)

task1.start()
task2.start()

# task1.join()
# task2.join()

print('ขับรถถึงแล้วและประชุมเสร็จแล้ว')

#Driving()
#Meeting()