import qrcode
import os

QR_CODE_FOLDER = "qr_codes"

if not os.path.exists(QR_CODE_FOLDER):
    os.makedirs(QR_CODE_FOLDER)

def generate_qr_code(numero: int):
    qr_data = f"Participant {numero}"
    qr_filename = f"{numero}.png"
    path = os.path.join(QR_CODE_FOLDER, qr_filename)

    img = qrcode.make(qr_data)
    img.save(path)

    return path
