#Cryptopas S3e18 AES mode CTR

from Crypto.Cipher import AES
from Crypto.Util import Counter
import os
import binascii


key = "YELLOW SUBMARINE"
message = "This is a message from test 1 " 





def int_of_string(s):
    return int(binascii.hexlify(s), 16)
def encrypt_message(key, plaintext):
    iv = os.urandom(16)
    ctr = Counter.new(128, initial_value=int_of_string(iv))
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return iv + aes.encrypt(plaintext)
def decrypt_message(key, ciphertext):
    iv = ciphertext[:16]
    ctr = Counter.new(128, initial_value=int_of_string(iv))
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return aes.decrypt(ciphertext[16:])



#Method 1 using the above functions (No padding)
ct=encrypt_message(key, message)
pt=decrypt_message(key, ct)
print "[+] decrypting1: ",pt

#Method 2 without padding #may return error + not so secure
secret = os.urandom(16)
secret = "\x00" * 16
obj = AES.new(key, AES.MODE_CTR, counter=lambda: secret)
ct = obj.encrypt("2nd message12345")
print "\nThe Cipher text is\n " + ct, len(ct)

pt = obj.decrypt(ct)
print "[+] Decrypting2 : " + pt

