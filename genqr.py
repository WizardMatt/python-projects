import qrcode

def generate_qr(data, filename="qrcode.png"):
    """Generates and saves a QR Code."""
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"✅ QR Code saved as {filename}")

# Get user input
text = input("Enter text or URL to generate QR Code: ")
generate_qr(text)


