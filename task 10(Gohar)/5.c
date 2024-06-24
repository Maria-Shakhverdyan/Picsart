#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char *str = 0;
    int length = 0;

    printf("Enter a string: ");
    
    int maxLength = 100;

    str = (char *)malloc(maxLength * sizeof(char));
    if (str == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    fgets(str, maxLength, stdin);

    length = strlen(str);
    if (str[length - 1] == '\n') {
        str[length - 1] = '\0';
        length--;
    }

    printf("Reversed string: ");
    for (int i = length - 1; i >= 0; i--) {
        putchar(str[i]);
    }
    printf("\n");

    free(str);

    return 0;
}
