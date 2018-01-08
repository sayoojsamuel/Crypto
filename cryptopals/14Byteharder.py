#Byte at a time attack -Harder on ECB - cryptopals 14
from Crypto.Cipher import AES
def encrypts(inp):
	secret="Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK".decode('base64')
	random="This is just a random string"
	message=random+inp+secret
	message+=(16-len(message)%16) * chr(16-len(message)%16)
	k="YELLOW SUBMARINE"
	KEY=AES.new(k,AES.MODE_ECB)
	ct=KEY.encrypt(message)
	#print ct	
	return ct
 
#attack here

def bf():
	flag=""
	a=guess_random()
	for k in range(a[1]+1,40):	
		for j in range(15,-1,-1):
			inp=a[0] * 'a' +j * 'A'
			#print inp
			block1=encrypts(inp)
			for i in range(256):
				op_block=encrypts(inp+flag+chr(i))
				
				if (op_block[16*a[1]:16*k]==block1[16*a[1]:16*k]):
					#print chr(i)
					flag+=chr(i)
					break
	print flag

def guess_random():
	list=[]
	for j in range(5):
		inp1=""
		for i in range(16):
			first=encrypts(inp1)[j*16:(j+1)*16]
			inp1+="A"
			second=encrypts(inp1)[j*16:(j+1)*16]
			if first==second:
				list+=[len(inp1)-1]
				break

	out=[max(list),len(list)]
	return out
		
if __name__=="__main__":
	
	bf()
	
