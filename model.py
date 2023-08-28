import qrcode
from PIL import Image
import io

class QRCodeGenerator:
    def generate_qr_code(self, url):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")
        
        img_bytes = io.BytesIO()
        qr_image.save(img_bytes, format="PNG")
        return img_bytes.getvalue()
