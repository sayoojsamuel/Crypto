import sys
from PyPDF2 import PdfFileReader

'''
Note that this script was tested on a PDF encrypted with 128 bit RC4 (most credit card statements) with 100% success. 
A wider implementation would be to loop something like qpdf with the passwords 
being generated using its --pasword='<password>' and --decrypt option.
'''


helpmsg = "Simple PDF brute force script\n"
helpmsg += "Cracks pwds of the format <first 4 chars of email>0000-9999."
helpmsg += "Example: snow0653\n\n"
helpmsg += "Usage: pdfbrute.py <encrypted_pdf_file> <email_address>"
if len(sys.argv) < 2:
        print (helpmsg)
        sys.exit()
        
pdffile = PdfFileReader(file(sys.argv[1], "rb"))
if pdffile.isEncrypted == False:
        print ("[!] The file is not protected with any password. Exiting.")
        exit

print ("[+] Attempting to Brute force. This could take some time...")

z = ""
for i in range(0,99999):
        z = str (i)
        while (len(z) < 5):
                z = "0" + z
        
        a = str(sys.argv[2][:1] + str(z))
        print (a)       
        if pdffile.decrypt(a) > 0:
                print ("[+] Password is: " + a)
                print ("[...] Exiting..")
                sys.exit()
