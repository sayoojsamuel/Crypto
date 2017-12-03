#Byte at a time attack on ECB - cryptopals 12
from Crypto.Cipher import AES
def encrypts(inp):
	secret="Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK".decode('base64')
	
	message=inp+secret
	message+=(16-len(message)%16) * chr(16-len(message)%16)
	k="YELLOW SUBMARINE"
	KEY=AES.new(k,AES.MODE_ECB)
	ct=KEY.encrypt(message)
	#print ct	
	return ct
 
#attack here

def bf():
	flag=""
	for k in range(1,10):	
		for j in range(15,-1,-1):

			inp=j * 'A'
			block1=encrypts(inp)
			for i in range(256):
				op_block=encrypts(inp+flag+chr(i))
				if (op_block[:16*k]==block1[:16*k]):
					#print chr(i)
					flag+=chr(i)
					break
	print flag

					
						
				
			






if __name__=="__main__":
	
	bf()
	

