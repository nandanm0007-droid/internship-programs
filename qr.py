import qrcode
link = "https://milanainfotech.in/"
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4,
)
qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill_color="Black", back_color="white")
img.save("qrcode.png")
print("QR code saved as qrcode.png")
