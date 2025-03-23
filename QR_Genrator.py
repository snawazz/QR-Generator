import qrcode 
from PIL import Image
#import qrcode.constants

# Ask the user whether they want to generate a QR code for UPI or other data
choice = input("To generate a QR code of UPI, Type 'UPI' or for other data, Type 'OTHER' : ")
massage = choice.lower()

# If the user selects UPI, prompt for UPI ID and format it as a UPI payment link
if "upi" in massage:
    upi = input("Enter your UPI here : ")
    qr_data = (f"upi://pay?pa={upi}&cu=INR")

# If the user selects "OTHER", prompt for any general data to encode
elif "other" in massage:
    qr_data = input("Enter your DATA here : ")

# Exit if the input is neither "UPI" nor "OTHER"
else:
    raise SystemExit("Invalid choice")   

# Ask the user for a filename to save the generated QR code
qr_name = input("Give a filename to save your QR code : ")   
# Ask the image format jpg or png
file_format = input("File format jpg/png :")
# Create a QRCode object with specific settings
qr = qrcode.QRCode(version= 2,  # Determines the size and complexity of the QR code
                   error_correction = qrcode.constants.ERROR_CORRECT_H,  # High error correction level
                   box_size=20,  # Size of each box in the QR grid
                   border= 2)  # Border width of the QR code

# Add data to the QR code
qr.add_data(qr_data)

# Generate the QR code image
qr.make(fit= True)

# Create an image from the QR code object with specific colors
QR = qr.make_image(fill_color = "black", back_color = "white")

# Save the generated QR code image with the user-defined name
QR.save(f"{qr_name}.{file_format}")
