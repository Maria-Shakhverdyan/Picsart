#include <stdio.h>

int reverseNumber(int num) {
    int reversedNum = 0;
    while (num > 0) {
        int remainder = num % 10;
        reversedNum = reversedNum * 10 + remainder;
        num /= 10;
    }
    return reversedNum;
}

int main() {
    int number = 0;

    do {
        printf("Enter an integer greater than 12: ");
        scanf("%d", &number);
        if (number <= 12) {
            printf("Number should be greater than 12. Try again.\n");
        }
    } while (number <= 12);

    int reversed = reverseNumber(number);

    printf("Reversed number: %d\n", reversed);

    return 0;
}
