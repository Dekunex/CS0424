#include <stdio.h>

int main ()
{
    printf("Salve, io sono il mago che ti calcola la media dei voti di scuola,\n");
    int italiano; 
    int matematica;
    int inglese;
    int informatica;
    float media;

    printf("vediamo se studi o meno...\n");

    printf("il tuo voto in italiano:");
    scanf("%d", &italiano);

    printf("il tuo voto a matematica:");
    scanf("%d", &matematica);

    printf("il tuo voto in inglese:");
    scanf("%d", &inglese);

    printf("il tuo voto in informatica:");
    scanf("%d", &informatica);

    media = (italiano + matematica + inglese + informatica) / 4;

    printf("bravo secchione, questa è la media: %.2f\n", media);

    return 0;

}