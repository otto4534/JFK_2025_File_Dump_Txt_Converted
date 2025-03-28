# String Search Tool Documentation

This folder contains 2 files. If you don't feel comfortable running the `.exe`, feel free to review and run the Python script.

## Contents

1. **Python Script**: `StringSearch_MultiFile_With_GUI.py`  
   Contains the source code for the executable `StringSearch_MultiFile_With_GUI.exe`.

2. **Executable File**: `StringSearch_MultiFile_With_GUI.exe`  
   Provides a simplistic tool for scanning a set of text files for a specific string.

---

## Settings

### **TXT Dump Directory**
- Specify the directory housing the `.txt` files.  
- You can also specify a top-level directory containing sub-folders.  
- The application will scan each subfolder for `.txt` files as well as the top-level directory.  
- Click **`Browse`** to locate the directory using the Windows browse mechanism.

### **Enter Search String**
- Enter the key word or phrase to scan for within the `.txt` files found.  
- Click **`Scan`** to initiate the scan.  
- **Note**: The **`Scan`** button will be disabled until a directory is added to the **TXT Dump Directory** field.

### **Write Results to File**
- Check this box to write the scan results to a dedicated text file.  
- The file will be named `StringMatches_<Search String>.txt`.  
- The file will be saved to the same directory as the `.exe` or `.py` script.

---

## Processing

1. The **TXT Dump Directory** and associated sub-directories are scanned for any file ending in `.txt`.  
2. Upon finding at least one match for the **Search String**, the file name will:
   - Be displayed in the status window of the user interface.
   - Be written to an output text file (if **Write results to file** is enabled).

