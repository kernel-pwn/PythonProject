# Used to perform multiple tasks concurrently (multitasking)
# Good for I/O bound tasks like reading files or fetching data from APIs
# Threading.Thread(target-my_function)

import threading
import  time

def walk_dog(name, last):
    time.sleep(8)
    print(f"finished walking dog {name} {last}")

def take_out_trash():
    time.sleep(2)
    print("finished taking out trash")

def get_mail():
    time.sleep(4)
    print("finished getting mail")

chore1 = threading.Thread(target=walk_dog, args=("scooby","doo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

time.sleep(1)
print("all done")