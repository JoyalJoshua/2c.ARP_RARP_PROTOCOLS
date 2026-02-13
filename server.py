import socket

s=socket.socket()
s.bind(("127.0.0.1",8000))  
s.listen(5)
print("Server is listening on port 8000...")
conn,addr=s.accept()
print("Connection from:",addr)  

arp_table = {"10.23.45": "00:11:22:33:44:55", "10.23.46": "66:77:88:99:AA:BB"}

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print("Received request for IP:", data)
    
    mac_address = arp_table.get(data, "MAC Address not found")
    conn.send(mac_address.encode())
    
conn.close()
s.close()

