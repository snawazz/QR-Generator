import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import qrcode
from PIL import Image

def generate_qr_code():
     
    choice = choice_var.get()
    # Get data from Text widget from the first character ("1.0") to the end (tk.END)
    data = data_entry.get("1.0", tk.END).strip()
    file_format = format_var.get()

    # Input Validation
    if not data:
        messagebox.showerror("Error", "The data field cannot be empty. Please enter a UPI ID or other data.")
        return

    
    if choice == "upi":
        qr_data = f"upi://pay?pa={data}&cu=INR"
    else: 
        qr_data = data

    try:
        # Create QR Code
        qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=20,
            border=2
        )
        qr.add_data(qr_data)
        qr.make(fit=True)

        # Create an image of qr
        qr_image = qr.make_image(fill_color="black", back_color="white")

        # Ask user where to save the file
        file_path = filedialog.asksaveasfilename(
            defaultextension=f".{file_format}",
            filetypes=[
                (f"{file_format.upper()} files", f"*.{file_format}"),
                ("All Files", "*.*")
            ],
            title="Save QR Code As"
        )

        # If the user cancels the save dialog, file_path will be empty
        if not file_path:
            return

        qr_image.save(file_path)
        messagebox.showinfo("Success", f"Your QR code has been saved successfully!\n\nPath: {file_path}")
        # Clear the text field after successful generation
        data_entry.delete("1.0", tk.END)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while generating the QR code: {e}")

def update_input_prompt(*args):
    """Updates the label text based on the radio button selection."""
    if choice_var.get() == "upi":
        input_label.config(text="Enter Your UPI ID:")
    else:
        input_label.config(text="Enter Data or URL:")

# main window setup 
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("450x500") 
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# styles
style = ttk.Style()
style.configure("TFrame", background="#f0f0f0")
style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 11))
style.configure("TRadiobutton", background="#f0f0f0", font=("Helvetica", 10))
style.configure("TButton", font=("Helvetica", 11, "bold"), padding=10)
style.configure("Header.TLabel", font=("Helvetica", 16, "bold"))


# Main Frame
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(expand=True, fill="both")

# UI Elements

# Header
header_label = ttk.Label(main_frame, text="QR Code Generator", style="Header.TLabel")
header_label.pack(pady=(0, 20))

# Choice Frame (UPI or Other)
choice_frame = ttk.Frame(main_frame)
choice_frame.pack(fill="x", pady=5)

ttk.Label(choice_frame, text="1. Select QR Code Type:").pack(side="left", anchor="w")

choice_var = tk.StringVar(value="other")
choice_var.trace_add("write", update_input_prompt)

upi_radio = ttk.Radiobutton(choice_frame, text="UPI", variable=choice_var, value="upi")
upi_radio.pack(side="right", padx=(0, 20))
other_radio = ttk.Radiobutton(choice_frame, text="Other Data/URL", variable=choice_var, value="other")
other_radio.pack(side="right")


# Data Input Frame
input_frame = ttk.Frame(main_frame)
input_frame.pack(fill="x", pady=10, ipady=5)

input_label = ttk.Label(input_frame, text="2. Enter Data or URL:")
input_label.pack(anchor="w", pady=(0, 5))

data_entry = tk.Text(input_frame, font=("Helvetica", 12), height=8, wrap="word", relief="solid", borderwidth=1)
data_entry.pack(fill="x")

# Format Selection Frame
format_frame = ttk.Frame(main_frame)
format_frame.pack(fill="x", pady=15) 

ttk.Label(format_frame, text="3. Select Image Format:").pack(side="left", anchor="w")

format_var = tk.StringVar(value="png")

png_radio = ttk.Radiobutton(format_frame, text="PNG", variable=format_var, value="png")
png_radio.pack(side="right", padx=(0, 20))
jpg_radio = ttk.Radiobutton(format_frame, text="JPG", variable=format_var, value="jpg")
jpg_radio.pack(side="right")


# Generate Button 
generate_button = ttk.Button(main_frame, text="Generate & Save QR Code", command=generate_qr_code)
generate_button.pack(pady=(25, 10), fill="x")

root.mainloop()

