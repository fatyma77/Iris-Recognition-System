# Iris-Recognition-System
This Python application demonstrates iris recognition using image processing techniques and a graphical user interface (GUI) built with tkinter. Iris recognition is a biometric identification method that uses the unique patterns in the iris of the human eye.

Features
Image Processing: Uses OpenCV and numpy for image manipulation, including grayscale conversion, cropping, resizing, Gaussian smoothing, edge detection (Canny and Sobel), and FFT-based filtering.
Graphical User Interface: Built with tkinter for selecting image files and displaying the results.
Iris Comparison: Compares two iris images to determine if they belong to the "same iris" or "different iris".
Gamma Correction: Applies gamma correction to enhance image contrast before processing.
FFT Filtering: Uses FFT to filter frequency components of iris images.
Error Handling: Provides error messages if image files are not selected or operations fail.
Usage
Select Images: Run the script and select two JPEG images of irises.
Process Images: The system processes the images by performing various image processing steps.
Result: Displays whether the selected irises are "SAME IRIS" or "DIFFERENT IRIS" based on their unique patterns.
Requirements
Python 3.x
Libraries: numpy, cv2 (OpenCV), tkinter, PIL (Pillow), scipy
How to Run
Clone the repository.
Install the required libraries (pip install -r requirements.txt).
Run the script (python iris_recognition.py).
Follow the GUI prompts to select the iris images and view the result.
Contributions
Contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests.
