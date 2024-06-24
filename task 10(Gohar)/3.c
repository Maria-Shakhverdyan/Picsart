#include <stdio.h>

int main() {
    int arr1[] = {1, 2, 3, 4, 5};
    int arr2[] = {6, 7, 8, 9, 10};
    int size = sizeof(arr1) / sizeof(arr1[0]);
    int result[2 * size];

    for (int i = 0; i < size; i++) {
        result[i] = arr1[i];
    }

    for (int i = 0; i < size; i++) {
        result[size + i] = arr2[i];
    }

    printf("Resulting array: ");
    for (int i = 0; i < 2 * size; i++) {
        printf("%d ", result[i]);
    }
    printf("\n");

    return 0;
}
