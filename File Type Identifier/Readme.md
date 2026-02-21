# File Type Identifier

## Project Description

File Type Identifier is a security tool that checks the real file type of a file using its internal binary signature also known as a magic number or file signature.

Normally, we identify files by their extensions, such as:
- photo.jpg  
- document.pdf  
- video.mp4  

The attackers can easily rename a file:

virus.exe → photo.jpg  

- Even though the file looks like an image, it may still be an executable file internally.
- This tool reads the hidden binary header of a file to determine its true file type and compares it with the file extension.
- If the extension does not match the actual file type, the tool displays a warning.
- This helps detect disguised malware and improves file upload security.

--- 

## Requirements for this Project

- Basic knowledge of Python  
- Understanding of file extensions  
- Basic understanding of cybersecurity concepts  
- Python installed on your system  

---

## Software Requirements
I have used VS Code for this Project 
- Python 3.8 or higher
- Git (optional, for version control)  
- Command Prompt or Terminal  

---

## Python Libraries Used

filetype library is used to detect the real file type from binary signature

Install dependencies using:
- pip install filetype 

---

## Importants 

This project is important in cybersecurity because:

- Attackers often disguise malware by changing file extensions.  
- Many systems trust file extensions without checking the real file content.  
- This tool verifies the actual file type using binary inspection.  

This Tool can be used in:

- Security Operations Center environments  
- Secure file upload systems  
- Malware analysis  
- Digital forensics  

---

## How to Run

1. Clone the file identifier.py 
2. Install the requirements  
3. Run the scanner  

Example:

python file identifier.py

<img width="820" height="370" alt="image" src="https://github.com/user-attachments/assets/1567d405-3608-44bc-9421-93fb62ed27f4" />

If a file extension does not match its real type, the tool will display:
- WARNING: Extension does NOT match real file type.

---

## Repository Structure

MagicNumber-File-Scanner/
- scanner.py  
- README.md  
- samples/  
  - safe file.md 
  - Insecure file.md
---

## Futures that can be added later for Improvements

- Add SHA256 hashing  
- Add logging to CSV  
- Add a quarantine folder for suspicious files  

---

## Author
### RUTHRAN-SEC
