# DecodeImage
Convert a text file of numbers to the pixels of an image

This is intended to be used with the FLiR Lepton camera and the [Arduino code](https://github.com/josepbordesjove/FLiR-lepton) (commit 8e64a19) that runs on an Arduino Due.
For instructions and setup, see the project's readme.

Paste the pixel data from the camera into a .csv file and place the file in the DecodeImage project directory.  Make sure the correct file name is referenced from line 13 of DecodeData.py, and run the script to produce and save the image.
