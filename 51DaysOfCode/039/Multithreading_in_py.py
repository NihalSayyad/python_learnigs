import time
import threading

def calc_square(number):
    print('Calculate squares')
    for n in number:
        time.sleep(0.2)
        print('Square: ', n*n)

def calc_cube(number):
    print('Calculate Cube')
    for n in number:
        time.sleep(0.2)
        print('Cube', n*n*n)

arr = [2,3,8,9]

t = time.time()
calc_square(arr)
calc_cube(arr)
print("Done in : ", time.time()-t)

print("--------------------------------------------")
t = time.time()
t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()
print("Done in : ", time.time()-t)