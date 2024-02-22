import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size = 12, border = 5,)
qr.add_data("https://www.facebook.com/pratigya.pandey.345")
qr.make(fit = True)
image = qr.make_image(fill_color = "blue",back_color= "white")
image.save("Pratigya_fb.png")