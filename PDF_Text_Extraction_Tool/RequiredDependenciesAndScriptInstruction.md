# Dependencies and Setup Instructions for the Script

## Required Python Modules
The following Python modules are required to run the script:
1. ### PyMuPDF (fitz)
   Used for reading and rendering PDF pages.
   Installation:
   pip install pymupdf

2. ### pytesseract
   Python wrapper for Tesseract OCR, used to extract text from images.
   Installation:
   pip install pytesseract
   Note: Tesseract OCR software must also be installed on your system (see instructions below).

3. ### Pillow
   Python Imaging Library (PIL), used for image manipulation.
   Installation:
   pip install pillow

4. ### io (Built-in Python module)
   Used to handle byte streams.
   No installation required; part of the Python standard library.

5. ### os (Built-in Python module)
   Provides directory and file manipulation functions.
   No installation required; part of the Python standard library.

## Installing Tesseract OCR
To use pytesseract, you need to install Tesseract OCR software on your system. Follow the instructions below:
 ### Windows:
  Download the installer from Tesseract's GitHub (https://github.com/tesseract-ocr/tesseract) or use the UB Mannheim Windows installer (https://github.com/UB-Mannheim/tesseract/wiki).
  After installation, add Tesseract to your system's PATH (e.g., C:\Program Files\Tesseract-OCR).

 ### macOS:
  Install via Homebrew:
  brew install tesseract

 ### Linux:
  Install via package manager (e.g., apt):
  sudo apt install tesseract-ocr

## Configuration
The script uses a custom configuration for Tesseract OCR:
--oem 1 --psm 6
Ensure Tesseract supports the selected mode (PSM = Page Segmentation Mode).

## Script Usage
1. Place all PDF files to be processed in the input directory (default is the "pdfs" folder in the script directory).
2. Ensure that Tesseract OCR is installed and accessible.
3. Run the script with Python (e.g., python script_name.py).
4. Text output files will be saved to the specified output directory.

Python Version
This script requires Python 3.x. It is recommended to use the latest stable version of Python.
"""
