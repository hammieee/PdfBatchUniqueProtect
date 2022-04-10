# import PdfFileWriter and PdfFileReader
# class from PyPDF2 library
from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

if len(sys.argv) == 3:
    # create a PdfFileWriter object
    out = PdfFileWriter()

    # Open our PDF file with the PdfFileReader
    filename = sys.argv[1]
    file = PdfFileReader("C:/Users/tomwo/Desktop/pdf/"+filename)

    # Get number of pages in original file
    num = file.numPages

    # Iterate through every page of the original
    # file and add it to our new file.
    for idx in range(num):
        
        # Get the page at index idx
        page = file.getPage(idx)
        
        # Add it to the output file
        out.addPage(page)


    # Create a variable password and store
    # our password in it.
    password = sys.argv[2]

    # Encrypt the new file with the entered password
    out.encrypt(password)

    # Open a new file in the "protected" directory
    with open("C:/Users/tomwo/Desktop/pdf/protected/"+filename, "wb+") as f:
        
        # Write our encrypted PDF to this file
        out.write(f)
