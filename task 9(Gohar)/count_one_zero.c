#include <stdio.h>
 
int main()
{
    int count0 = 0, count1 = 0;
    int number;
    
    printf("Enter the number: ");
    scanf("%d", &number);
    
    while (number > 0) {
        if(number & 1) {
            ++count1;
        } else {
            ++count0;
        }
        number >>= 1;
    }
    
    printf("Count of 0s: %d\n", count0);
    printf("Count of 1s: %d\n", count1);
    
    return 0;
}