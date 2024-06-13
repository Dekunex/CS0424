#include <stdio.h>
/*calcoliamo la moltiplicazione di due numeri dato da voi*/

int main ()
{
    /*inserimento di scritta iniziale di benvenuto tramite comando printf*/
    printf("Salve, io sono un mago. se mi dai 2 numeri ti faccio la moltiplicazione, vogliamo provare?\n");

    int primo_numero; 
    int secondo_numero;
    int moltiplicazione;

    printf("dammi il primo:\n");
    scanf("%d", &primo_numero);

    printf("ora il secondo:\n");
    scanf("%d", &secondo_numero);

    moltiplicazione = primo_numero * secondo_numero;
    printf("skatoooosh: %d\n", moltiplicazione);

    printf("ora esercitati da solo che tra poco andrò a fare il bagno allo stagno\n");
    
    return 0;
}
