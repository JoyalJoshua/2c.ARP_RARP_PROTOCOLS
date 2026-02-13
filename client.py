import socket
s = socket.socket()
s.connect(("127.0.0.1", 8000))

ip_address = input("Enter IP address to resolve: ")
s.send(ip_address.encode())
mac_address = s.recv(1024).decode()
print("MAC Address:", mac_address)  
s.close()   