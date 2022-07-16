from multiprocessing import Process, Queue


def count_primes(num: int, queue: Queue) -> None:
    primes = 0
    for i in range(2, num + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes += 1
    queue.put(primes)


if __name__ == '__main__':
    queue1 = Queue()
    process1 = Process(target=count_primes, args=(100000, queue1))
    process1.start()

    queue2 = Queue()
    process2 = Process(target=count_primes, args=(100000, queue2))
    process2.start()

    process1.join()
    print(queue1.get())
    process2.join()
    print(queue2.get())
