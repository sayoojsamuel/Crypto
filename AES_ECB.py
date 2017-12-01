#AES Electronic Code Book Encode
from Crypto.Cipher import AES
print "Enter the Message"
pt =  raw_input()
# to pad the given message
m=16 - len(pt)%16
pt+=m * chr(m)
print pt
'''
if (m==16):
	pt+= 16 * chr(16)
else:
	pt+= m* chr(m)
'''


key=AES.new("The key is color",AES.MODE_ECB)
ct=key.encrypt(pt)
print ct





