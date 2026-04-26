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
file_path = None
resized = None
root = tb.Window(themename="vapor")
#root=tk.Tk()
root.title("Morphological operations")
root.iconbitmap(r"imageProcessing_output_24.ico")
root.geometry("500x500")

def nothing(x):
    pass
def erosion():
    global file_path, resized
    title_trackbar_element_shape = 'Element:\n 0: Rect \n 1: Cross \n 2: Ellipse \n 3: Diamond'
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    resized = cv2.resize(img, (1900, 1000))
    if img is None:
        print("Error: Could not find or open image.")
        exit()
    window_name = 'Erosion'
    cv2.namedWindow(window_name)
    cv2.createTrackbar(title_trackbar_element_shape, window_name, 0, 3, nothing)
    cv2.createTrackbar('Kernel Size', window_name, 0, 12, nothing)
    while True:
        try:
            element_size = cv2.getTrackbarPos(title_trackbar_element_shape, window_name)
            kernel_size = cv2.getTrackbarPos('Kernel Size', window_name)*2+1
        except:
            break  # window closed → avoid crash
        if element_size == 0:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        elif element_size == 1:
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))
        elif element_size == 2:
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
        elif element_size == 3:
            kernel = cv2.getStructuringElement(cv2.MORPH_DIAMOND, (kernel_size, kernel_size))
        result = cv2.erode(resized, kernel)   
        cv2.imshow('Erosion', result) 
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

def dilation():
    global file_path, resized
    title_trackbar_element_shape = 'Element:\n 0: Rect \n 1: Cross \n 2: Ellipse \n 3: Diamond'
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    resized = cv2.resize(img, (1900, 1000))
    if img is None:
        print("Error: Could not find or open image.")
        exit()
    window_name = 'Dilation'
    cv2.namedWindow(window_name)
    cv2.createTrackbar(title_trackbar_element_shape, window_name, 0, 3, nothing)
    cv2.createTrackbar('Kernel Size', window_name, 0, 12, nothing)
    while True:
        try:
            element_size = cv2.getTrackbarPos(title_trackbar_element_shape, window_name)
            kernel_size = cv2.getTrackbarPos('Kernel Size', window_name)*2+1
        except:
            break  # window closed → avoid crash
        if element_size == 0:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        elif element_size == 1:
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))
        elif element_size == 2:
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
        elif element_size == 3:
            kernel = cv2.getStructuringElement(cv2.MORPH_DIAMOND, (kernel_size, kernel_size))
        result = cv2.dilate(resized, kernel)   
        cv2.imshow('Dilation', result) 
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

def opening():
    global file_path, resized
    title_trackbar_element_shape = 'Element:\n 0: Rect \n 1: Cross \n 2: Ellipse \n 3: Diamond'
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    resized = cv2.resize(img, (1900, 1000))
    if img is None:
        print("Error: Could not find or open image.")
        exit()
    window_name = 'Opening'
    cv2.namedWindow(window_name)
    cv2.createTrackbar(title_trackbar_element_shape, window_name, 0, 3, nothing)
    cv2.createTrackbar('Kernel Size', window_name, 0, 12, nothing)
    while True:
        try:
            element_size = cv2.getTrackbarPos(title_trackbar_element_shape, window_name)
            kernel_size = cv2.getTrackbarPos('Kernel Size', window_name)*2+1
        except:
            break  # window closed → avoid crash
        if element_size == 0:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        elif element_size == 1:
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))
        elif element_size == 2:
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
        elif element_size == 3:
            kernel = cv2.getStructuringElement(cv2.MORPH_DIAMOND, (kernel_size, kernel_size))
        result = cv2.morphologyEx(resized, cv2.MORPH_OPEN, kernel)   
        cv2.imshow('Opening', result) 
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

def closing():
    global file_path, resized
    title_trackbar_element_shape = 'Element:\n 0: Rect \n 1: Cross \n 2: Ellipse \n 3: Diamond'
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    resized = cv2.resize(img, (1900, 1000))
    if img is None:
        print("Error: Could not find or open image.")
        exit()
    window_name = 'Closing'
    cv2.namedWindow(window_name)
    cv2.createTrackbar(title_trackbar_element_shape, window_name, 0, 3, nothing)
    cv2.createTrackbar('Kernel Size', window_name, 0, 12, nothing)
    while True:
        try:
            element_size = cv2.getTrackbarPos(title_trackbar_element_shape, window_name)
            kernel_size = cv2.getTrackbarPos('Kernel Size', window_name)*2+1
        except:
            break  # window closed → avoid crash
        if element_size == 0:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        elif element_size == 1:
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))
        elif element_size == 2:
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
        elif element_size == 3:
            kernel = cv2.getStructuringElement(cv2.MORPH_DIAMOND, (kernel_size, kernel_size))
        result = cv2.morphologyEx(resized, cv2.MORPH_CLOSE, kernel)   
        cv2.imshow('Closing', result) 
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

def gradient():
    global file_path, resized
    title_trackbar_element_shape = 'Element:\n 0: Rect \n 1: Cross \n 2: Ellipse \n 3: Diamond'
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    resized = cv2.resize(img, (1900, 1000))
    if img is None:
        print("Error: Could not find or open image.")
        exit()
    window_name = 'Gradient'
    cv2.namedWindow(window_name)
    cv2.createTrackbar(title_trackbar_element_shape, window_name, 0, 3, nothing)
    cv2.createTrackbar('Kernel Size', window_name, 0, 12, nothing)
    while True:
        try:
            element_size = cv2.getTrackbarPos(title_trackbar_element_shape, window_name)
            kernel_size = cv2.getTrackbarPos('Kernel Size', window_name)*2+1 
        except:
            break  # window closed → avoid crash
        if element_size == 0:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        elif element_size == 1:
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))
        elif element_size == 2:
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
        elif element_size == 3:
            kernel = cv2.getStructuringElement(cv2.MORPH_DIAMOND, (kernel_size, kernel_size))
        result = cv2.morphologyEx(resized, cv2.MORPH_GRADIENT, kernel)   
        cv2.imshow('Gradient', result) 
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()


#file upload with 100MB
def upload_file():
    # 1. Open File Dialog
    global file_path
    file_path = filedialog.askopenfilename(
        title="Select File",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
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

btn_upload = tk.Button(root, font=("Courier", 10),text="Select Image File (Max 100MB)", command=upload_file)
btn_upload.pack(pady=20)

label_status = tk.Label(root, font=("Courier", 10),text="Not Selected")
label_status.pack(pady=10)


#dropdown menu code

# Define options
options = ["Erosion", "Dilation", "Opening", "Closing", "Gradient"]


# Create Combobox
combo = ttk.Combobox(root, font=("Courier", 10),values=options, state="readonly")
combo.set("Erosion")  # Set default value
combo.pack(pady=20)

# Function to get selected value
def on_selection_change():
    #global resized
    #print(f"Selected: {combo.get()}")
    selected=combo.get()
    if selected == options[0]:
        erosion()
        
    elif selected == options[1]:
        dilation()

    elif selected == options[2]:
        opening()
        
    elif selected == options[3]:
        closing()

    elif selected == options[4]:
        gradient()
    
btn = tk.Button(root, font=("Courier", 10), text="Apply Operation", command=on_selection_change)
btn.pack()

root.mainloop()
