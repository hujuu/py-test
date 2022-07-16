from multiprocessing import Process, Queue
import qrcode
from csv import reader

with open('20220712164625.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    list_of_rows = list(csv_reader)


def count_primes(list_rows: list, queue: Queue) -> None:
    primes = 0
    for row in list_rows:
        QR_STR = row[0]
        QR_FILE_NAME = f'qr_code/result_{row[0][-24:]}.png'
        qr = qrcode.QRCode(
            version=2,  # QRコードのバージョン(1~40)
            error_correction=qrcode.constants.ERROR_CORRECT_H  # 誤り訂正レベル(L：約7%,M：約15%,Q:約25%,H:約30%)
        )
        qr.add_data(QR_STR)
        qr.make()
        img = qr.make_image()
        img.save(QR_FILE_NAME)
    queue.put(primes)


if __name__ == '__main__':
    queue1 = Queue()
    process1 = Process(target=count_primes, args=(list_of_rows[0:7999], queue1))
    process1.start()

    queue2 = Queue()
    process2 = Process(target=count_primes, args=(list_of_rows[8000:15999], queue2))
    process2.start()

    queue3 = Queue()
    process3 = Process(target=count_primes, args=(list_of_rows[16000:25000], queue2))
    process3.start()

    process1.join()
    print(queue1.get())
    process2.join()
    print(queue2.get())
    process3.join()
    print(queue3.get())
