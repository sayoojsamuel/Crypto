#CBC Padding oracle attack, cryptopals 17 Set 3
import os
import random
from Crypto.Cipher import AES
key=os.urandom(16)


def xor(a,b):
	return "".join(chr(ord(i) ^ ord(j)) for i,j in zip(a,b))
def xor3(a,b,c):
	return "".join(chr(ord(i) ^ ord(j) ^ ord(k)) for i,j,k in zip(a,b,c))

def encrypt():
	a=open("17.txt").readlines()



	#pt=random.choice(a).rstrip("\n").decode("base64")
	pt=a[9].rstrip("\n").decode("base64")
	print pt
	pad=16-len(pt)%16
	pt+=pad * chr(pad)
	iv=os.urandom(16)

	obj=AES.new(key,AES.MODE_CBC,iv)
	ct=obj.encrypt(pt)
	return [ct,iv]

def decrypt(ct,iv):
	obj=AES.new(key,AES.MODE_CBC, iv)
	pt=obj.decrypt(ct)
	return pad_check(pt)
 
def pad_check(string, block=16):
	pad=string[len(string)-1]
	if(pad=='\x00'):
		return False
	intpad=ord(pad)
	try:
		for i in range(intpad):
			if(string[::-1][i]!=pad):
				raise
		string=string.rstrip(pad)
		#print "the string after padding removal is :\n" + string
		return True
	except:
		#print "Padding is wrong"
		return False


def exploit():
	#takes the list output
	out=encrypt()

	ct=out[0]
	iv=out[1]
	
	#to get the number of blocks (includes iv)
	nblock=len(ct)/16 + 1
	block_size=16

	#to break the ct into ct list
	ctl=[iv]
	ptl=[]
	for i in range(nblock):
		ctl+=[ct[i*block_size : (i+1)*block_size]] 
	flag=""
	for i in range(nblock-1,-1,-1):
			
		#to create 1 block attack
		brute="\x00"*block_size
		ptblock=""
		for j in range(15,-1,-1):
			pad = chr(16-j)
			for k in range(256):
				mod = xor3(ctl[i-1],"\x00"*j + pad *(16-j) ,brute[:j]+chr(k)+ptblock)
				att = mod + ctl[i]
				print " mod : ", len(brute[:j]+chr(k)+ptblock)
				if(decrypt(att,iv)):
					print chr(k)
					ptblock=chr(k)+ptblock

		
		flag=ptblock+flag
		print "-------"
	print flag
		
if __name__=="__main__"	:
	exploit()
