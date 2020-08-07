import pytesseract 
From PIL import Image 

# Correct way to avoid TesseractNotFound error 

# Declare path to tesseract is a must if running local machine for Python program 
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'

# Comment out path to tesseract if running Python program in Docker container 

# Common mistakes are 
# 1). Including local path into Dockerfile or even moving tesseract_cmd into current directory to make it work
# 2). Unable to locate the correct tesseract_cmd. One way to locate is using brew list tesseract command in terminal
