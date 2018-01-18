#CBC Padding oracle attack, cryptopals 17 Set 3
import os
import random
from Crypto.Cipher import AES
#key=os.urandom(16)
key="sayoojsamuel4444" #remove this after completuin of code
def encrypt():
	a=open("17.txt").readlines()
	#pt=a[random.randint(0,len(a)-1)].rstrip('\n')
	#pt=a[0].rstrip('\n')   # remove this line after test successa
	pt="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	pad=16-len(pt)%16
	pt+=pad * chr(pad)
	#iv=os.urandom(16)
	iv="sayoojsamuel4444"
	obj=AES.new(key,AES.MODE_CBC,iv)
	ct=obj.encrypt(pt)
	return [ct,iv]
def decrypt(ct,iv):
	obj=AES.new(key,AES.MODE_CBC, iv)
	pt=obj.decrypt(ct)
	return pad_check(pt)

def pad_check(string, block=16):
	pad=string[len(string)-1]
	intpad=ord(pad)
	try:
		for i in range(intpad):
			if(string[::-1][i]!=pad):
				raise
		string=string.rstrip(pad)
		#print "The string after padding removal is :\n" + string
		return True

	except:
		#print "Padding is wrong"
		return False


#second approach to attack
def att_2():
	a=encrypt();
	n=len(a[0])/16
	ctr=[]
	ctr+=16* '\x00'
	block=16
	block-=1
	pt=[]
	ptorg=[]
	pt+=16 * "\x00"
	ct=[a[0][l*16:(l+1)*16] for l in range(len(a[0])/16)]
	print ct
	for i in range(256):
		att="".join(ctr[:15])+chr(i)
		att+=ct[n-1]
		temp=decrypt(att,a[1])
		if(temp):
			pt[block]=chr(i)
			ptorg= 1 ^ ord(ct[n-1][block]) ^ i
			break
	print chr(ptorg)

if __name__=="__main__":
	att_2()

	'''
	a=encrypt();
	n=len(a[0])/16
	ctr=[]
	rate=16
	ctr+=16 * '\x00'
	pt=[]
	pt+=16 * '\x00'
	for j in range(16):
		rate-=1
		for i in range(1,256):
			#rate-=1
			att="".join(ctr[:rate])+chr(i)+"".join(ctr[rate+1:])
			print [att]
			att=att+a[0][(n-1) * 16 : n * 16]
			temp=decrypt(att,a[1])
			#print "printing temp:",temp
			if(temp):
				pt[rate]=chr(i)
				print "Check on ",i
				break
	print "The pt value is ",pt
   	'''
