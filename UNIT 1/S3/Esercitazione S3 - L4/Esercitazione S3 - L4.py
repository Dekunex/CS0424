import socket as so         #modulo socket con alias so , per poter utilizzare funzioni inerenti al socket

SRV_ADDR = "127.0.0.1"         #identificazione di indirizzo che utilizzeremo come ascolto 
SRV_PORT = 44444                #identificazione di porta per la connessione

s = so.socket(so.AF_INET, so.SOCK_STREAM)  #impostazione di un nuovo socket con i rispettivi AF_INET (IPV4) e SOCK_STREAM(TCP)
s.bind((SRV_ADDR, SRV_PORT)) #collegamento del Socket precedentemente creato al SRV_ADDR e SRV_PORT
s.listen(1)  # comando utilizzato per mettersi in ascolto (1) per specificare il numero massimo di connessioni.

print(f"Il server e' avviato su {SRV_ADDR}:{SRV_PORT}") 

connection, address = s.accept()  # accettazione di una connessione in entrata

print(f"Client in ascolto all'indirizzo {address}") # messaggio di avvertimento
connection.sendall(b" Ciao!\n faccio echo:\n") #ripetizione di messaggio
while True:  #inizia un ciclo infinito con il comunicante
    connection.sendall(b"$ ")
    data = connection.recv(1024)  #contenuto dei dati --> connessione per ricevere i dati ---> numero byte 
    if not data: break # se non ci sono dati esce dal ciclo e chiude la connessione
    connection.sendall(b"# ")
    command = data.decode('utf-8').replace("\n","") # decodifica dei dati 
    if(command == "ciao"):
        connection.sendall(b"Non abbiamo gia' stabilito il saluto?\n") #risposta se il comunicante ci dice "Ciao"
    elif(command == "ls"):
        connection.sendall(b"Ci hai provato?\n") #blocca esecuzione del comando " ls "
    else:
        connection.sendall(data)
    print(data.decode('utf-8')) #stampa i dati ricevuti
connection.close() #chiude la connessione

# Una backdoor è un accesso non consentito attuato di nascosto verso Software, Sistemi operativi o Dispositivi.
# E' utilizzata da hacker o creatori di malware per accedere a dati o per controllare i sistemi senza il consenso dei dell'utente leggittimo.


