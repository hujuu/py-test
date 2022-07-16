import qrcode
from csv import reader

with open('20220712164625.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    list_of_rows = list(csv_reader)

for row in list_of_rows:
    # QRコード化したい文字列を指定
    QR_STR = row[0]
    # QRコード画像ファイル名
    QR_FILE_NAME = f'qr_code/result_{row[0][-24:]}.png'
    # QRコードの設定
    qr = qrcode.QRCode(
        version=2,  # QRコードのバージョン(1~40)
        error_correction=qrcode.constants.ERROR_CORRECT_H  # 誤り訂正レベル(L：約7%,M：約15%,Q:約25%,H:約30%)
    )
    # QRコード化したい文字列を追加
    qr.add_data(QR_STR)
    # QRコード作成
    qr.make()
    # QRコードの画像化
    img = qr.make_image()
    # 画像ファイルを保存
    img.save(QR_FILE_NAME)
