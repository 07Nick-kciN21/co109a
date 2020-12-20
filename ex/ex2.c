#include <stdio.h>

int main(){
    int n=0;
    loop:
        n++;
        if(n == 10)
            goto EXIT;
        printf("n=%d\n", n);
        goto loop;
    EXIT:
        return 0;
}