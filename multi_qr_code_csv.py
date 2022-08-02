from multiprocessing import Process
import qrcode
from csv import reader

with open('20220712164625.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    list_of_rows = list(csv_reader)


def count_primes(list_rows: list) -> None:
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
    return QR_STR


if __name__ == '__main__':
    process1 = Process(target=count_primes, args=(list_of_rows[0:12500],))
    process1.start()

    process2 = Process(target=count_primes, args=(list_of_rows[12500:25000],))
    process2.start()

    process1.join()
    process2.join()
