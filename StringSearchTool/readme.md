This folder contains 2 files. If you don't feel comfortable running the .exe.  Feel free to review and run the python script.


1. A python script 'StringSearch_MultiFile_With_GUI.py' which contains the source code for the
   executable StringSearch_MultiFile_With_GUI.exe

2. StringSearch_MultiFile_With_GUI.exe which provides a simplistic tool for scanning a set of text
   files for a specific string.
     -Settings
         -TXT Dump Directory - Specify the directory housing the .txt files.
          You can also specify a top level directory containing sub-folders.
          The application will scan each subfolder for .txt files as well as the
          top level directory. Click 'Browse' to locate directory via Windows browse mechanism.

         -Enter Search String - The key word or phrase that the found .txt files
          will be scanned for.  Click 'Scan' to initiate scan. Note that the 'Scan' button
          will be disabled until a directory is added to the 'TXT Dump Directory' field.

         -Write results to file - Check this box to write the scan results to a dedicated text
          file with naming convention 'StringMatches_<Search String>.txt'.
          This file will be written to the same directory that houses the .exe or .py script.

     -Processing
         -The TXT Dump Directory and associated sub-directories are scanned for any file ending in .txt
         -Upon finding at least one match of the Search String, the file name will be written to the
          status window of the user interface, and to an output text file (if Write results to file is enabled)
