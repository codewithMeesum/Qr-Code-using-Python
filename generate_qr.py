import qrcode
qr=qrcode.make("https://www.instagram.com/learningdailyai/")
qr.save("qrcode.png")
print ("QR code generated and saved as qrcode.png")