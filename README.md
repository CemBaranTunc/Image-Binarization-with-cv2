This project is aimed to reduce the size of the pictures to make AI training more efficient and faster by using the binarization method.

The pngFileLister.py creates a hidden temporary file to write-down (line by line) all png extensioned files where located in the same directory as the script is.
After the list being created, the script creates a sub-directory to store processed pictures which will be later created by imageBinarizer.py
imageBinarizer.py processes the images and saves them to the created sub-directory.
After all binarized pictures being saved to the targeted sub-directory, the script deletes the hidden temporary file.

Deep Note: Eyes and mouth areas of people from the original pictures are censored due to the legal concerns.
