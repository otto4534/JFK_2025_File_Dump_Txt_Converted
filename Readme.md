# 2025 JFK File Dump - TXT converted and associated tooling

---

## Overview
I ran the full set of 2343 pdf documents from https://www.archives.gov/research/jfk/release-2025  to text files through a text extraction algorithm. Results vary a bit. But in general, if the doc was decently human readable, it converts OK. This repo contains the converted .txt files. ***Note the file names exactly match the name of the associated .pdf file, making it possible to cross reference with the original.***
This repo also contains a useful string search tool that can scan all .txt files for a given string, as well as the original script used to perform the text extraction.

## Repo Map
This repo contains the following sub-folders

### 1. ZippedPackages
This folder contains the full set of 2343 .txt files, distributed over four .zip files.  Download these zip files and unzip in your desired directory.

### 2. StringSearchTool
This is a simple tool (available as standalone .exe and .py (python script)) which performs a string search over an arbitrary number of .txt files in a directory. It will also scan for .txt files in sub-directories. As noted, this initial version of the tool is very simple.  It will only return the file name of one or more files where the string was found. 

### 3. PDF_Text_Extraction_Tool
This folder contains the script used to perform the text extraction from the original .pdf files as well as some instruction on installing the necessary dependencies. 
