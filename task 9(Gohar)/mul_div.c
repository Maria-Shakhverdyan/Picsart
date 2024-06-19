#include <stdio.h>

int multiply(int number, int power) {
    return number << power;
}

int division(int number, int power) {
    return number >> power;
}

int main() {
    int number, power;

    printf("Enter number: ");
    scanf("%d", &number);

    printf("Enter power: ");
    scanf("%d", &power);

    int multiplied = multiply(number, power);
    printf("Multiply result %d\n", multiplied);

    int divided = division(number, power);
    printf("Division result %d\n", divided);

    return 0;
}
