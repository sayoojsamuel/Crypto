#attack on IV in AES_CBC
from Crypto.Cipher import AES
import os
key=os.urandom(16)
iv="I am A random IV"
def AES_CBC(string):
	global iv
	global key
	obj=AES.new(key,AES.MODE_CBC,iv)
	ct=obj.encrypt(string)
	return ct
def decrypt(ct):
	global iv
	global key
	obj=AES.new(key,AES.MODE_CBC,iv)
	pt=obj.decrypt(ct)
	return pt
def xor(str1, str2):
	return "".join(chr(ord(a) ^ ord(b)) for a,b in zip(str1,str2))
if __name__=="__main__":
	
	pt=[]
	pt+=[16 * "0"] 
	
	ct=[]
	ct+=[AES_CBC(pt[0])]
	pt+=[xor(pt[0],ct[0])]
	ct+=[AES_CBC(pt[0]+pt[1])[16:32]]
	print "plaintext blocks :" + str(pt)
	print "ciphertext blocks :" + str(ct)
	guess_iv=xor(decrypt(ct[1]),pt[0])
	print "The iv value is :\v " + guess_iv
	print guess_iv==iv


	
