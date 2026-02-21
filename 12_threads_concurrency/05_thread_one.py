import threading
import time

def boil_milk():
    print(f"Boiling milk...")
    time.sleep(2)
    print(f"Milk Boiled...")

def toast_bun():
    print(f"Toasting bun...")
    time.sleep(3)
    print(f"Done with bun toast...")

def make_tea():
    print(f"Making tea...")
    time.sleep(1)
    print(f"Tea is ready to serve...")
    
start = time.time()

t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)
t3 = threading.Thread(target=make_tea)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

end = time.time()

print(f"Breakfast is ready in {end - start:.2f} seconds")
