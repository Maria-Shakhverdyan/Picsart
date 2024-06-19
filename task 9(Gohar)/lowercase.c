#include <stdio.h>

char lower(char ch) {
    if (ch >= 'A' && ch <= 'Z') {
        return ch | (1 << 5);
    }
    return ch;
}

int main() {
    char str[100];

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    for (int i = 0; str[i] != '\0'; ++i) {
        str[i] = lower(str[i]);
    }

    printf("String in lowercase: %s", str);

    return 0;
}