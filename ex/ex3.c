#include <stdio.h>

int main(){
    int n=0;                    //@0, M=1
    loop:
        n++;                    //@0, M=M+1
        if(n == 10)
            goto EXIT;
        printf("n=%d\n", n);
        goto loop;              //@loop, 0;JMP
    EXIT:
        return 0;
}