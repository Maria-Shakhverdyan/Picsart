#include <stdio.h>

int main() {
    int intVar = 42;
    char charVar = 'A';
    int arrVar[3] = {1, 2, 3};

    int *intPtr = &intVar;
    char *charPtr = &charVar;
    int (*arrPtr)[3] = &arrVar;

    printf("Address stored in intPtr: %p\n", (void*)intPtr);
    printf("Address stored in charPtr: %p\n", (void*)charPtr);
    printf("Address stored in arrPtr: %p\n", (void*)arrPtr);

    return 0;
}
