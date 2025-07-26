# qr_generator.py
import qrcode

def generate_qr_code(data, filename="ticket.png"):
    qr_code = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr_code.add_data(data)
    qr_code.make(fit=True)
    img = qr_code.make_image(fill='black', back_color='white')
    img.save(filename)
