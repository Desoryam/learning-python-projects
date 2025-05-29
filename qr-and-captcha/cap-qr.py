import qrcode
import base64

with open("image/img1.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

qr = qrcode.QRCode(version=2, box_size=10, border=5)

qr.add_data(encoded_string)

qr.make()


img = qr.make_image(fill_color="black", back_color="white")

img.save("output/MYQR1.png")

print("QR code generated successfully!")