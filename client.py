import socket

# Créez une socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))

# Boucle pour envoyer et recevoir des messages
while True:
    message = input("Vous : ")
    client_socket.send(message.encode('utf-8'))

    # Recevez la réponse du serveur
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Serveur : {data}")

# Fermez la connexion
client_socket.close()
