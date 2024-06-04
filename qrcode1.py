import qrcode1 

qr = qrcode1.QRCode(
    version=1,
    error_correction=qrcode1.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)
qr.add_data('https://www.youtube.com/watch?v=fjYnYF_mu78')
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("datascince youtube.png")
print("type of the image: ",type(img))
