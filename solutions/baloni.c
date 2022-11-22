#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main() {

    int i, j;
    int n;
    int h;
    int arrows;
    int *heights;
    int *popped;

    scanf("%d", &n);

    heights = (int *) malloc(sizeof(int) * n);
    popped = (int *) calloc(n, sizeof(int));

    for (i = 0; i < n; i++) {
        scanf("%d", &heights[i]);    
    }

    arrows = 0;

    for (i = 0; i < n; i++) {
        if (popped[i] == 1) {
            continue;
        }
        
        arrows++;
        h = heights[i] - 1;
        popped[i] = 1;

        for (j = i + 1; j < n; j++) {
            if (heights[j] == h && popped[j] == 0) {
                popped[j] = 1;
                h -= 1;
            }
        }
    }

    printf("%d\n", arrows);
    
    return 0;

}