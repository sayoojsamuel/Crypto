# to perform CTR_Bitflipping
from Crypto.Cipher import AES
from Crypto.Util import Counter
import binascii
import os


#ctr = Counter.new(128, initial_value=int_of_string(iv))

def int_of_string(s):
    return int(binascii.hexlify(s), 16)

#encrypt function
def encrypt_ctr(message):
	message=message.replace('=','?')
	message=message.replace(';','?')
	message= "comment1=cooking%20MCs;userdate=" + message + ";comment2=%20like%20a%20pound%20of%20bacon"
	#iv ="I AM RANDOM IVEE"
	message+=(16-len(message)%16) * chr(16-len(message)%16)
	print message
	#ctr = Counter.new(128, initial_value=int_of_string(iv))
	KEY=AES.new('YELLOW SUBMARINE', AES.MODE_CTR, counter=ctr)
	ct=KEY.encrypt(message)
	return ct

#to decrypt
def decrypt_ctr(ct):
	#iv ="I AM RANDOM IVEE"
	#ctr = Counter.new(128, initial_value=int_of_string(iv))
	KEY=AES.new('YELLOW SUBMARINE', AES.MODE_CTR, counter=ctr)
	message=KEY.decrypt(ct)
	print message
	if ";admin=true;" in message:
		print "You are admin now"
	else:
		print "You must be admin to get access"

# applying Bitflipping
cipher_list=[]
payload=';admin=true;'
iv ="I AM RANDOM IVEE"
ctr = Counter.new(128, initial_value=int_of_string(iv))


ct=encrypt_ctr(payload)
decrypt_ctr(ct)

for k in range(len(ct)/16):
	cipher_list.append(ct[16*k : 16*(k+1)])
block=list(cipher_list[1])
block[0]= chr(ord(block[0]) ^ ord('?') ^ ord(';'))
block[6]= chr(ord(block[6]) ^ ord('?') ^ ord('='))
block[11]= chr(ord(block[11]) ^ ord('?') ^ ord(';'))
cipher_list[1]=''.join(block)
ct=''.join(cipher_list)

decrypt_ctr(ct)



