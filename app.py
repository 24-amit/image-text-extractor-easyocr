import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import tkinter as tk
from tkinter import filedialog
# from PIL import Image
import easyocr

root = tk.Tk()
root.withdraw() # Hide the main window

file_path = filedialog.askopenfilename(
    title="Select an image file",
    filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
)

if file_path:
    print(f"Selected file: {file_path}")
    # img = Image.open(file_path)
    # img.show()
else:
    print("No file selected.")

# Initialize the reader and read text
reader = easyocr.Reader(['en'])
result = reader.readtext(file_path)

# Print extracted text
print("Extracted Text using EasyOCR:")
for detection in result:
    print(detection[1])