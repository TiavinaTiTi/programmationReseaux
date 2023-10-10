import socket

# Créez une socket serveur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(1)

print("Le serveur écoute sur le port 12345...")

# Attendez qu'un client se connecte
client_socket, client_address = server_socket.accept()
print(f"Connexion établie avec {client_address}")

# Boucle pour recevoir et envoyer des messages
while True:
    # Recevez le message du client
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
        break
    print(f"Client : {data}")

    # Envoyez une réponse au client
    message = input("Vous : ")
    client_socket.send(message.encode('utf-8'))

# Fermez la connexion
client_socket.close()
server_socket.close()
