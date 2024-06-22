# Iris-Recognition-System
This Python application demonstrates iris recognition using image processing techniques and a graphical user interface (GUI) built with tkinter. Iris recognition is a biometric identification method that uses the unique patterns in the iris of the human eye.

**Features**

1. Image Processing: Uses OpenCV and numpy for image manipulation, including grayscale conversion, cropping, resizing, Gaussian smoothing, edge detection (Canny and Sobel), and FFT-based filtering.
2. Graphical User Interface: Built with tkinter for selecting image files and displaying the results.
3. Iris Comparison: Compares two iris images to determine if they belong to the "same iris" or "different iris".
4. Gamma Correction: Applies gamma correction to enhance image contrast before processing.
5. FFT Filtering: Uses FFT to filter frequency components of iris images.
6. Error Handling: Provides error messages if image files are not selected or operations fail.

**Usage**
1. Select Images:
Run the script and select two JPEG images of irises.
2. Process Images: The system processes the images by performing various image processing steps.
3. Result: Displays whether the selected irises are "SAME IRIS" or "DIFFERENT IRIS" based on their unique patterns.


**Requirements**
1. Python 3.x
2. Libraries: numpy, cv2 (OpenCV), tkinter, PIL (Pillow), scipy
   
**How to Run**
1. Clone the repository.
2. Install the required libraries (pip install -r requirements.txt).
3. Run the script (python iris_recognition.py).
4. Follow the GUI prompts to select the iris images and view the result.
   
**Contributions**

Contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests.
