import socket
import logging
logging.basicConfig(level=logging.INFO,filename = "client.log", filemode="w", format="%(asctime)s - %(message)s")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 1035))
logging.info("Client connected")
print(client.recv(1024).decode())
while True:
    print(client.recv(1024).decode())
    request = input()
    client.send(request.encode())
    logging.info(f"Client sent : {request}")
    if request == "quit":
        break
    data = client.recv(1024).decode()
    logging.info(f"Client received : {data}")
    print(data)
client.close()
logging.info("Client disconnected")


