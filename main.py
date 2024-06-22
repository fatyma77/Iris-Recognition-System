import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from scipy.ndimage import gaussian_filter

def load_image(prompt):
    file_path = filedialog.askopenfilename(title=prompt, filetypes=[("JPEG files", "*.jpg")])
    return file_path

def safe_power(arr, gamma):
    arr = np.clip(arr, 0, None)  # Ensure no negative values
    arr_max = np.max(arr)
    if arr_max == 0:
        return arr  # Avoid division by zero
    normalized = arr / arr_max
    return np.power(normalized, gamma)

def apply_fft_filter(image, low, band1, band2):
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    rows, cols = image.shape
    crow, ccol = rows // 2 , cols // 2

    low_pass = np.ones((rows, cols), np.uint8)
    band_pass = np.ones((rows, cols), np.uint8)

    for u in range(rows):
        for v in range(cols):
            d = np.sqrt((u - crow) ** 2 + (v - ccol) ** 2)
            if d > low:
                low_pass[u, v] = 0
            if d > band2 or d < band1:
                band_pass[u, v] = 0

    fshift_low = fshift * low_pass
    fshift_band = fshift * band_pass

    img_back_low = np.fft.ifft2(np.fft.ifftshift(fshift_low))
    img_back_band = np.fft.ifft2(np.fft.ifftshift(fshift_band))

    return np.abs(img_back_low), np.abs(img_back_band)

def process_images(file1, file2):
    if not file1 or not file2:
        messagebox.showerror("Error", "Please select both images.")
        return

    # Image 1
    i = cv2.imread(file1)
    i = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
    g = cv2.cvtColor(i, cv2.COLOR_RGB2GRAY)
    c = g[40:140, 30:240]
    r = cv2.resize(c, (256, 256), interpolation=cv2.INTER_NEAREST)
    f = gaussian_filter(r, sigma=3)
    S1 = cv2.Sobel(f, cv2.CV_64F, 1, 1, ksize=3)
    gamma = 0.8
    y = safe_power(S1, gamma)
    low = 62
    band1 = 15
    band2 = 60
    g_downsampled = cv2.resize(g, (500, 500), interpolation=cv2.INTER_NEAREST)
    r1, _ = apply_fft_filter(g_downsampled, low, band1, band2)
    N = f

    # Image 2
    ii = cv2.imread(file2)
    ii = cv2.cvtColor(ii, cv2.COLOR_BGR2RGB)
    gg = cv2.cvtColor(ii, cv2.COLOR_RGB2GRAY)
    cc = gg[40:140, 30:240]
    rr = cv2.resize(cc, (256, 256), interpolation=cv2.INTER_NEAREST)
    ff = gaussian_filter(rr, sigma=3)
    SS1 = cv2.Sobel(ff, cv2.CV_64F, 1, 1, ksize=3)
    yy = safe_power(SS1, gamma)
    gg_downsampled = cv2.resize(gg, (500, 500), interpolation=cv2.INTER_NEAREST)
    _, r2 = apply_fft_filter(gg_downsampled, low, band1, band2)
    NN = ff

    # Compare images
    result = "SAME IRIS" if np.array_equal(N, NN) else "DIFFERENT IRIS"
    messagebox.showinfo("Iris Recognition Result", result)

if __name__ == "__main__":
    file1 = load_image('Select 1st Image')
    file2 = load_image('Select 2nd Image')

    if file1 and file2:
        process_images(file1, file2)
    else:
        messagebox.showerror("Error", "Please select both images.")
