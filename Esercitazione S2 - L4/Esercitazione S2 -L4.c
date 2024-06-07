#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define nome 50

void mostraMenu();
void nuovaPartita();
int DaiDomanda(const char* domanda, const char* opzioni[], char rispostaCorretta);

int main() {
    char scelta;

    while (1) {
        mostraMenu();
        scanf(" %c", &scelta);

        switch (scelta) {
            case 'A':
            case 'a':
                nuovaPartita();
                break;
            case 'B':
            case 'b':
                printf("Ok viandante, vai a giocare con le Barbie.\n");
                exit(0);
            default:
                printf("Scelta non valida. Riprova.\n");
        }
    }

    return 0;
}

void mostraMenu() {
    printf("\nSalve viandante, io sono il Mago ASR e ti aiuterò a trovare\n");
    printf("la leggendaria spada di Excalibur.\n");
    printf("\n");
    printf("\n");
    printf("Hai il coraggio di affrontare questa nuova avventura?\n");
    printf("\n");
    printf("A) Inizia avventura\n");
    printf("B) Scappa come un coniglio\n");
    printf("\n");
    printf("Mago ASR: sbrigate, che dopo devo annà a vede la Roma all'Olimpico..:\n");
}

void nuovaPartita() {
    int punteggio = 0;
    char nomeGiocatore[nome];

    printf("Comunque come ti chiami bello/a?: ");
    scanf("%s", nomeGiocatore);

    printf("\nPerfetto, %s! Annamo va...\n", nomeGiocatore);

    char* domanda1 = "trovi un fiore in mezzo al sentiero, che fai mo?:";
    printf("\n");
    char* opzioni1[] = {"A) Calpesta", "B) Raccogli", "C) me faccio li cavoli mia"};
    char risposta1 = 'C';
    char* domanda2 = "Incontri un Orso bruno che te vole magnà, che fai mo?";
    printf("\n");
    char* opzioni2[] = {"A) Corri", "B) Accarezza", "C) Urla"};
    char risposta2 = 'A';
    char* domanda3 = "Finalmente trovi ed estrai Excalibur, che fai mo? ";
    printf("\n");
    char* opzioni3[] = {"A) La tieni", "B) La vendi", "C) La regali"};
    char risposta3 = 'B';

    punteggio += DaiDomanda(domanda1, opzioni1, risposta1);
    punteggio += DaiDomanda(domanda2, opzioni2, risposta2);
    punteggio += DaiDomanda(domanda3, opzioni3, risposta3);

    printf("\n%s, In tutto ciò te metto come voto: %d\n", nomeGiocatore, punteggio);
}

int DaiDomanda(const char* domanda, const char* opzioni[], char rispostaCorretta) {
    char risposta;

    printf("\n%s\n", domanda);
    for (int i = 0; i < 3; i++) {
        printf("%s\n", opzioni[i]);
    }
    printf("\n");
    printf("MAGO ASR: Risponni: ");
    scanf(" %c", &risposta); // Aggiunto spazio prima di %c per gestire correttamente il newline

    if (risposta == rispostaCorretta || risposta == rispostaCorretta + ('a' - 'A')) {
        printf("Eddaje!\n");
        return 1;
    } else {
        printf("Annaggia!.... La risposta comunque era la %c.\n", rispostaCorretta);
        return 0;
    }
}