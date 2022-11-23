#include <stdio.h>
#include <stdlib.h>

int main() {

    int i;
    int pieces[6];
    int correct[6] = {1, 1, 2, 2, 2, 8};

    for (i = 0; i < 6; i++) {
        scanf("%d", &pieces[i]);
        pieces[i] = correct[i] - pieces[i];  
    }

    for (i = 0; i < 6; i++) {
        printf("%d ", pieces[i]);
    }

    return 0;

}