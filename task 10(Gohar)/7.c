#include <stdio.h>
#include <stdlib.h>

int main() {
    char *str = 0;
    int length = 0;

    int maxLength = 100;

    str = (char *)malloc(maxLength * sizeof(char));
    if (str == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    printf("Enter a string: ");
    fgets(str, maxLength, stdin);

    length = 0;
    while (str[length] != '\0') {
        if (str[length] == '\n') {
            str[length] = '\0';
            break;
        }
        length++;
    }

    for (int i = 0; i < length; i++) {
        if (str[i] >= 'a' && str[i] <= 'z') {
            str[i] = str[i] - 'a' + 'A';
        }
    }

    printf("Uppercase string: %s\n", str);

    free(str);

    return 0;
}
