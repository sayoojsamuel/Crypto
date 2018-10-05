#!/usr/bin/python3
 
__author__ = 'spyx'
import PyPDF2
import sys
import optparse
 
parser = optparse.OptionParser()
parser.add_option('-f','--file',dest='file',help='encrypted file')
parser.add_option('-w','--wordlist',dest='word',help='wordlist file')
(options, args) = parser.parse_args()
if options.file == None or options.word == None:
    print('./pdfCracker.py -f [file] -w [wordlist file]')
    sys.exit()
 
file = options.file
word = options.word
 
wordlist = open(word)
 
pdf = PyPDF2.PdfFileReader(open(file,'rb'))
if not pdf.isEncrypted:
    print('No password')
else:
    for line in wordlist.readlines():
        if pdf.decrypt(line.rstrip()) :
            print('[+] PASSWORD: ' +line)
            sys.exit()
        print ("Brute "+line)
    print('[-] Password not found')
