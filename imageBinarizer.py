# For Windows
# This project is aimed to reduce the size of the pictures to make AI training more efficient and faster by using the binarization method.

import cv2
from os import remove, path, getcwd
from pngFileLister import hiddenList, subDirectory

try:
    with open(hiddenList, "r") as file: # Opens the temporary list which was created by pngFileLister.py
        for lineNumber, line in enumerate(file, start=1):
            print(f"Line {lineNumber}: {line.strip()}") # Prints the lines to the prompt

            img = cv2.imread(f"{line.strip()}", 0)
            imgCanny = cv2.Canny(img, 60, 60)  # Adjustable gradient values which allows to calibrate the edge detection.

            dim = (128, 128) # Raw image dimensions can be set from here.

            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

            filename = f"{line.strip()}"
            cv2.imwrite(path.join(getcwd() + "\\" + subDirectory, filename), imgCanny) # Saves the binarized pictures to the subdirectory which was created by pngFileLister.py
except FileNotFoundError:
    print(f"File not found: {hiddenList}")
except Exception as e:
    print(f"An error occurred: {e}")
remove(hiddenList)
