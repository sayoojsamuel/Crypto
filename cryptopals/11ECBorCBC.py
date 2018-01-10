#to detect ECB vs CBC detection
import os
import string
import random
from Crypto.Cipher import AES
chars=string.printable
def keygen():	
	key = os.urandom(16)
	return key

def AES_ECB(string):
	obj = AES.new(keygen(), AES.MODE_ECB)
	ct = obj.encrypt(string)
	print "Trigger ECB"
	return ct
def AES_CBC(string):
	obj = AES.new(keygen(), AES.MODE_CBC, keygen())
	ct = obj.encrypt(string)
	print "Trigger CBC"
	return ct
def encrypt(string):
	a="".join([random.choice(chars) for i in range(random.randint(5,10))])
	b="".join([random.choice(chars) for i in range(random.randint(5,10))])
	string = a + string + b
	pad=16-len(string)%16
	string+=pad * chr(pad)
	ct=""
	if (random.randint(0,1)):
		ct=AES_ECB(string)
	else:
		ct=AES_CBC(string)
	return ct
if __name__=="__main__":
	enc="AES_CBC"
	att=60 * 'a'
	ct=encrypt(att)
	for k in range(len(ct)/16):
		if ( ct[k*16 : (k+1)*16] == ct[(k+1)*16 : (k+2)*16]):
			enc="AES_ECB"			
	print enc
		
		
	
	
