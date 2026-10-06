import qrcode

def generate_qrcode():
    """
    Generate a QR Code from a user-provided URL and save it as a PNG image.

    The function prompts the user for the URL to encode and the desired output filename.
    The generated QR code is saved with a '.png' extension.
    """
    qr_link = input("Enter link of which qr code will be generated:\n").strip()
    qr_code_file = input("Enter file name to be saved as:\n").strip()
    img = qrcode.make(qr_link)
    img.save(qr_code_file+".png")
    print(f"QR Code Generated, Saved as {qr_code_file}.png")

generate_qrcode()

