import threading
import time

# Fonction exécutée par le premier thread
def thread1_function():
    for i in range(5):
        print("Thread 1 - Compteur :", i)
        time.sleep(1)  # Pause d'une seconde entre chaque itération

# Fonction exécutée par le deuxième thread
def thread2_function():
    for i in range(5):
        print("Thread 2 - Compteur :", i)
        time.sleep(0.5)  # Pause de demi-seconde entre chaque itération

# Créez deux threads
thread1 = threading.Thread(target=thread1_function)
thread2 = threading.Thread(target=thread2_function)

# Démarrez les threads
thread1.start()
thread2.start()

# Attendez que les threads se terminent
thread1.join()
thread2.join()

print("Tous les threads sont terminés.")
