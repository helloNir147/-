import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.56.1", 9999))
server.listen()

client, addr = server.accept()
file_name = client.recv(1024).decode()
print("File name received:", file_name)
file_size = client.recv(1024).decode()
print("File size received:", file_size)

file = open(file_name, 'wb')
file_bytes = b""
done = False
total_received = 0
file_size = int(file_size)
print("Receiving file...")

while not done:
    data = client.recv(1024)
    if file_bytes[-5:] == b"<END>":
        done = True
        file_bytes = file_bytes[:-5]
    else:
        file_bytes += data
        total_received += len(data)
        percent_done = (total_received / file_size) * 100
        print(f"Progress: {percent_done:.2f}%", end='\r')

file.write(file_bytes)
file.close()
client.close()
server.close()
print("\nFile received successfully!")