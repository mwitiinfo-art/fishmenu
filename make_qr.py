"""Make a printable QR code for your menu link.

Setup (once):   pip install "qrcode[pil]"
Run:            python make_qr.py https://mwitiinfo-art.github.io/fish-menu/
Creates:        menu-qr.png (for printing / sharing) and menu-qr.svg (sharp at any size)
"""
import sys

try:
    import qrcode
    import qrcode.image.svg
except ImportError:
    sys.exit('Missing library. Run:  pip install "qrcode[pil]"')

url = sys.argv[1] if len(sys.argv) > 1 else input("Paste your menu link (https://...): ")
url = url.strip()
if not url.startswith("https://"):
    sys.exit("The link must start with https://")

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=20, border=4)
qr.add_data(url)
qr.make(fit=True)

qr.make_image(fill_color="black", back_color="white").save("menu-qr.png")
qr.make_image(image_factory=qrcode.image.svg.SvgPathImage).save("menu-qr.svg")
print("Saved menu-qr.png and menu-qr.svg for:", url)
print("Scan it with your phone before printing.")