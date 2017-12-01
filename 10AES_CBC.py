#AES Electronic Codebook Decode
from Crypto.Cipher import AES


ef = open ("10.txt", 'r')
content=ef.read()
ct=content.decode('base64')
iv="\x00\x00\x00 &c"
key=AES.new('YELLOW SUBMARINE',AES.MODE_CBC,iv)
pt=key.decrypt(ct)
print pt






