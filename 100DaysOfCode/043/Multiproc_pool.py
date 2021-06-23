from multiprocessing import Pool
import time

def f(n):
    time.sleep(0.5)
    return n*n

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9,10]
    t = time.time()
    p = Pool()
    result = p.map(f, array)
    print(result)
    print("Done in ", str(time.time() - t))

    t= time.time()
    result = []
    for i in array:
        result.append(f(i))
    print(result)
    print("Done in ", str(time.time() - t))