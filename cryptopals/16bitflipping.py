# to perform CBC_Bitflipping

from Crypto.Cipher import AES

#to encrypt
def encrypt(message):
	message=message.replace('=','?')
	message=message.replace(';','?')
	message= "comment1=cooking%20MCs;userdate=" + message + ";comment2=%20like%20a%20pound%20of%20bacon"
	message+=(16-len(message)%16) * chr(16-len(message)%16)
	KEY=AES.new('YELLOW SUBMARINE', AES.MODE_CBC, "I AM RANDOM IVEE")
	ct=KEY.encrypt(message)
	return ct

#to decrypt
def decrypt(ct):
	KEY=AES.new('YELLOW SUBMARINE', AES.MODE_CBC, "I AM RANDOM IVEE")
	message=KEY.decrypt(ct)
	if ";admin=true;" in message:
		print "You are admin now"
	else:
		print "You must be admin to get access"

# applying Bitflipping
cipher_list=[]
payload=';admin=true;'
ct=encrypt(payload)


for k in range(len(ct)/16):
	cipher_list.append(ct[16*k : 16*(k+1)])
block=list(cipher_list[1])
block[0]= chr(ord(block[0]) ^ ord('?') ^ ord(';'))
block[6]= chr(ord(block[6]) ^ ord('?') ^ ord('='))
block[11]= chr(ord(block[11]) ^ ord('?') ^ ord(';'))
cipher_list[1]=''.join(block)
ct=''.join(cipher_list)
#todecrypt
decrypt(ct)





	
