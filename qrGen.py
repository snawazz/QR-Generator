import qrcode 
from PIL import Image

while True:
    try:
        print("\nTo exit Press -> CTRL + C")
        while True:
            choice = input("To generate a QR code of UPI, Type 'UPI' or for other data, Type 'OTHER' : ")
            message = choice.lower()
            
            if message == "other" or message == "upi":
                break
            else:
                print("\nInvalid input, please try again!\n")

        if "upi" in message:
            upi = input("\nEnter your UPI here : ")
            qr_data = (f"upi://pay?pa={upi}&cu=INR")

        elif "other" in message:
            qr_data = input("\nEnter your DATA here : ") 

        qr_name = input("\nGive a filename to save your QR code : ")  
        while True:
            # Ask the image format jpg or png
            file_format = input("\nFile format jpg/png :").strip().lower()
            if file_format == "jpg" or file_format == "png":
                break
            else:
                print("\nchoose reserved file format!")

        qr = qrcode.QRCode(version= 2, 
                        error_correction = qrcode.constants.ERROR_CORRECT_H,  
                        box_size=20,  
                        border= 2)  


        qr.add_data(qr_data)
        qr.make(fit= True)

        # Create the QR code with specific colors
        QR = qr.make_image(fill_color = "black", back_color = "white")

        QR.save(f"{qr_name}.{file_format}")
        print(f'your QR "{qr_name}.{file_format}" has created Successfully!')

        repeat = input("\nDo you want to generate another one (yes/no): ").strip().lower()

        if repeat != "yes":
            print("\nOkay Come back soon 😊")
            break

    except KeyboardInterrupt:
           print("\nProgram exited by User!")
           break
