import socket
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.56.1", 9999))  

file_path = "image.png"
file_name = "received_image.png"
file_size = os.path.getsize(file_path)

client.send(file_name.encode())
client.send(str(file_size).encode())

with open(file_path, "rb") as file:
    while chunk := file.read(1024):
        client.sendall(chunk)

client.close()
print("File sent successfully!")