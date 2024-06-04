import qrcode 
from PIL import Image
import qrcode.constants


qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data('https://www.youtube.com/watch?v=y_I2YOP91Is')
qr.make(fit=True)
img=qr.make_image(fill_color='blue',back_color='white')
img.save('python_miniproject.png')
print("type of the image: ",type(img))