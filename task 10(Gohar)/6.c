#include <stdio.h>

int stringLength(const char *str) {
    int length = 0;
    while (str[length] != '\0') {
        length++;
    }
    return length;
}

int main() {
    char str[100];

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    int length = 0;
    while (str[length] != '\0') {
        if (str[length] == '\n') {
            str[length] = '\0';
            break;
        }
        length++;
    }

    int len = stringLength(str);

    printf("Length of the string: %d\n", len);

    return 0;
}
