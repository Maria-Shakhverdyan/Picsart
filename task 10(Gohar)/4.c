#include <stdio.h>
#include <stdbool.h>

bool areArraysEqual(int arr1[], int arr2[], int size) {
    for (int i = 0; i < size; i++) {
        if (arr1[i] != arr2[i]) {
            return false;
        }
    }
    return true;
}

int main() {
    int arr1[] = {1, 2, 3, 4, 5};
    int arr2[] = {1, 2, 3, 4, 5};
    int size1 = sizeof(arr1) / sizeof(arr1[0]);
    int size2 = sizeof(arr2) / sizeof(arr2[0]);

    if (size1 != size2) {
        printf("Arrays are not of the same size.\n");
        return 0;
    }

    if (areArraysEqual(arr1, arr2, size1)) {
        printf("Arrays are equal.\n");
    } else {
        printf("Arrays are not equal.\n");
    }

    return 0;
}
