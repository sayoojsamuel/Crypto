#Fixed key and fixed starting nonce! [with Counter increment]

from Crypto.Cipher import AES
from Crypto.Util import Counter
import os, string,time, thread, threading

KEY = os.urandom(16)
block_size = 16
def fixed_encrypt(pt):
	pt=pt.decode('base64')
	ctr = Counter.new(128, initial_value=0)
	aes = AES.new(KEY, AES.MODE_CTR, counter=ctr)
	return aes.encrypt(pt).encode('base64').replace('\n',"")
	
def decrypt(ct):
	ct=ct.decode('base64')
	ctr = Counter.new(128, initial_value=0)
        aes = AES.new(KEY, AES.MODE_CTR, counter=ctr)
	return aes.decrypt(ct).encode('base64').replace('\n','')
	
def xor(a,b):
	return "".join(chr(ord(i)^ord(j)) for i,j in zip(a,b))
#to clear screen
def clrscr():
	print(chr(27)+'[2j')
	print('\033c')
	print('\x1bc')

#raw_input with timeout
def raw_input_with_timeout(prompt, timeout=0.5):
    print prompt,    
    timer = threading.Timer(timeout, thread.interrupt_main)
    astring = None
    try:
        timer.start()
        astring = raw_input(prompt)
    except KeyboardInterrupt:
        pass
    timer.cancel()
    return astring

pt_list = open('20.txt').read().split()
ct_list = [fixed_encrypt(i) for i in pt_list]

#to find the length of smallest ciphertext
small=400
for i in pt_list:
	if(len(i)<small): small=len(i)
for i in range(len(ct_list)):
	ct_list[i]=ct_list[i][:small].decode('base64')


#no of blocks in the reduced ciphertext
block_len = ( small //16 ) -1

#blocks now store the blocks of different ct in block order
blocks = [[ct_list[i][j*16:(j+1)*16] for i in range(len(ct_list))] for j in range(block_len)]

#chars list supposed in plaintext
chars = 'I\'m rated"R.hiswng,ybvo/PpDJ-CuzckSlqf!BN;YWMAH?TFEx:KjLOZ4 '

#perform repeated key xor here, take block[0] and find the key used! this 
#to iterate over 4 columns in ct_list
chk_list=[]
for i in range(block_len):
	#to iterate over all the rows in ct_list 
	for j in range(block_size):
		keypos=""
		selections=""
		#to iterate over each byte in a single block
		for k in range(len(ct_list)):
			selections += blocks[i][k][j]
		for l in range(256):
			rets = xor(selections, chr(l)*16)
			if(all(_ in chars for _ in rets)): 
				keypos+=chr(l)
		chk_list+=[keypos]


#initially xoring with the first byte in possible chk_list
pt_guess = ct_list[:]
for i in range(len(ct_list)):
	pt_guess[i] = list(pt_guess[i])
	for j in range(48):
		pt_guess[i][j] = xor(ct_list[i][j],chk_list[j][0])
	pt_guess[i] = "".join(pt_guess[i])

clrscr()
for i in pt_guess:
	print i 

def change(place):
	ch = ''
	num = 0
	while(ch == ''):
		for i in range(len(ct_list)):
			pt_guess[i] = list(pt_guess[i])
			pt_guess[i][place] = xor(ct_list[i][place],chk_list[place][num%len(chk_list[place])])
			pt_guess[i] = "".join(pt_guess[i])
		clrscr()
		for _ in pt_guess: print _
		ch = raw_input("\nPlace :" + str(place)+" "+str(num) +"  Press enter for next, Space to Confirm: ")
		num +=1
	return
for i in range(42):
	change(i)




		

