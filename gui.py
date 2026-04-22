import tkinter as tk
from tkinter import ttk
from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
import os
import cv2
import numpy as np

root = tb.Window(themename="vapor")
#root=tk.Tk()
root.title("Morphological operations")
root.iconbitmap(r"imageProcessing_output_24.ico")
root.geometry("500x500")


#file upload with 100MB
def upload_file():
    # 1. Open File Dialog
    global file_path
    file_path = filedialog.askopenfilename(
        title="Select File",
        filetypes=[("All Files", "*.*")]
    )
  
    if not file_path:
        return

    # 2. Check File Size (100MB = 100 * 1024 * 1024 bytes)
    file_size = os.path.getsize(file_path)
    limit = 100 * 1024 * 1024
    
    if file_size > limit:
        messagebox.showerror("Error", "File size exceeds 100MB limit!")
        return

    # 3. Process the file (Example: display path)
    label_status.config(text=f"Selected: {os.path.basename(file_path)}")
    print(f"Uploading: {file_path} (Size: {file_size} bytes)")

btn_upload = tk.Button(root, font=("Helvetica", 10),text="Select Image File (Max 100MB)", command=upload_file)
btn_upload.pack(pady=20)

label_status = tk.Label(root, text="")
label_status.pack(pady=10)


#dropdown menu code

# Define options
options = ["Erosion", "Dilation", "Opening", "Closing"]


# Create Combobox
combo = ttk.Combobox(root, font=("Helvetica", 10),values=options, state="readonly")
combo.set("Erosion")  # Set default value
combo.pack(pady=20)

# Function to get selected value
def on_selection_change():
    #print(f"Selected: {combo.get()}")
    selected=combo.get()
    if selected == options[0]:
        # Load the input image in grayscale
        img = cv2.imread(file_path, 0)
        resized = cv2.resize(img, (1900, 1000)) # (width, height)
        # Define the kernel (e.g., 5x5 matrix of ones)
        # Larger kernels result in more significant erosion
        kernel = np.ones((5, 5), np.uint8)
        erosion = cv2.erode(resized, kernel, iterations=1)
        cv2.imshow('Original', resized)
        cv2.imshow('Erosion', erosion)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif selected == options[1]:
        img = cv2.imread(file_path, 0) # Read in grayscale
        resized = cv2.resize(img, (1900, 1000)) # (width, height)
        # 2. Define the kernel (structuring element)
        # A 5x5 kernel of ones will expand the foreground by roughly 2 pixels in each direction
        kernel = np.ones((5, 5), np.uint8)

        # 3. Apply dilation
        # iterations=1 defines how many times the operation is repeated
        dilated_img = cv2.dilate(resized, kernel, iterations=1)

        # 4. Display results
        cv2.imshow('Original', resized)
        cv2.imshow('Dilated', dilated_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif selected == options[2]:
        # 1. Load the input image (grayscale or binary is recommended)
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        resized = cv2.resize(image, (1900, 1000)) # (width, height)
        # 2. Define the kernel (structuring element)
        # A 5x5 rectangular kernel is common; larger kernels remove more noise.
        kernel = np.ones((5, 5), np.uint8)

        # 3. Apply the Opening operation
        # Opening = Erosion followed by Dilation
        opening = cv2.morphologyEx(resized, cv2.MORPH_OPEN, kernel)

        # 4. Display the results
        cv2.imshow('Original Image', resized)
        cv2.imshow('Opening Result (Noise Removed)', opening)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif selected == options[3]:
        img = cv2.imread(file_path, 0)  # Load in grayscale
        resized = cv2.resize(img, (1900, 1000)) # (width, height)
        # Define a structuring element (kernel)
        # Larger kernels remove larger holes
        kernel = np.ones((5,5), np.uint8)

        # Perform the closing operation
        # cv2.MORPH_CLOSE specifies dilation followed by erosion
        closing = cv2.morphologyEx(resized, cv2.MORPH_CLOSE, kernel)

        # Display the results
        cv2.imshow('Original', resized)
        cv2.imshow('Closing Result', closing)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    
    

btn = tk.Button(root, font=("Helvetica", 10), text="Submit", command=on_selection_change)
btn.pack()

root.mainloop()