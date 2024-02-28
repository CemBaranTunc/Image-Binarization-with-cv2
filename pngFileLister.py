# For Windows
# This project is aimed to reduce the size of the pictures to make AI training more efficient and faster by using the binarization method.

from os import listdir, getcwd, remove, makedirs

def findPngFiles(directory="."):
    pngFiles = [file for file in listdir(directory) if file.lower().endswith(".png")]
    return pngFiles

hiddenList = "_list.tmp"  # The file path will be chosen as the same directory with pngFileLister.py

try:
    try:
        remove(hiddenList) # Removes the list.tmp file if it hasn't removed after previous iteration or if a file with the same name exists in the same directory by any chance.
    except Exception:
        pass
    subDirectory = "processedPictures"
    makedirs(subDirectory, exist_ok=True) # Creates the directory
    with open(hiddenList, "w") as outputFile: # Creates the list.tmp in the same directory as pngFileLister.py
        if findPngFiles(getcwd()): # Detects and writes every single png file in the same directory in a list form.
            for pngFile in findPngFiles(getcwd()):
                outputFile.write(pngFile + "\n")
        else:
            outputFile.write("No PNG files found in the current directory.")
            print("No PNG files found in the current directory. Results saved to", hiddenList)
except Exception as e:
    print(f"An error occurred: {e}")
import imageBinarizer # Jumping to the imageBinarizer.py script after file list is created