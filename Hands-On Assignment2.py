import qrcode

# Prompting the user to enter the destination link
url = input("Enter the URL: ")

# Setting up QR grid dimensions and quiet zone padding
qr = qrcode.QRCode(
    version=1,     # Smallest standard grid size
    box_size=10,   # Pixel size per module/square
    border=4       # Minimum margin required for scanner detection
)

qr.add_data(url)
qr.make(fit=True)  # Auto-adjust size if url exceeds version capacity

# Rendering image with high-contrast colors
qr_image = qr.make_image(
    fill_color="black",
    back_color="white"
)

# destination path to save the output
save_path = (
    "/Users/vattikunta/Desktop/Masters_Assignments/"
    "Advanced Artificial Intelligence/qr_code.png"
)
qr_image.save(save_path)

print("QR code generated successfully!")
print(f"Saved to: {save_path}")