#include <stdio.h>
#include <stdbool.h>

bool checkBit(int number, int pos) {
    return (number & (1 << pos)) != 0;
}

int main() {
    int number, pos;
    
    printf("Enter a number: ");
    scanf("%d", &number);
    
    printf("Enter position: ");
    scanf("%d", &pos);
    
    if (checkBit(number, pos)) {
        printf("The %d-th bit of %d is 1.\n", pos, number);
    } else {
        printf("The %d-th bit of %d is 0.\n", pos, number);
    }
    
    return 0;
}
