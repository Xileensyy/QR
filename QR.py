import qrcode

url = "https://transportesnarvaez.cl/"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="white", back_color="black")
img.save("qr_code.png")