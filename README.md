File Extractor
This Python script helps in extracting various types of compressed files and viewing ASCII files by identifying their file types. It utilizes the file command to determine the file type and then performs extraction accordingly.

How to Use
Clone Repository:
git clone <repository_url>

Navigate to Directory:
cd <repository_directory>

Run the Script:
python file_extractor.py

Input File Name:
Enter the name of the file you want to analyze and extract.

Requirements
Python 3.x

Linux environment (tested on Kali Linux)

Functionality
The script prompts the user to input a filename.
It then determines the file type using the file command and redirects the output to output.txt.
The script reads the content of output.txt and searches for specific keywords to identify the file type.
If the file is a gzip, tar, bzip2, or Zip archive, it extracts the contents using relevant commands (gunzip, tar -xf, bunzip2, unzip).
If the file is identified as an ASCII text file, it displays the content of the file and terminates.
If none of the specified keywords are found in the file type description, it displays "BAD LUCK".

Note
This script is designed for Linux environments.
Ensure that the required commands (gzip, tar, bzip2, unzip) are installed and accessible in the system's PATH.
Use caution when extracting files, especially from untrusted sources, as this script does not implement any security checks.
