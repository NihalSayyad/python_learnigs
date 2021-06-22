import multiprocessing

result = []

def calc_square(numbers, q):
    for idx, n in enumerate(numbers):
        q.put(n*n)


if __name__ == '__main__':
    numbers = [2,3,4,5]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(numbers,q))

    p.start()
    p.join()
    print(q)
    while not q.empty():
        print(q.get())