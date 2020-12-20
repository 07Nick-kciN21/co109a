```cpp

WHILE1:
    int i=16384;            //@16384, D=A, @i, M=D

    WHILE2:                 //(WHILE2)           16384-24576  < 0
        if(i >= 24576)      //@24576, D=A, @i, D=M-D
            goto END2       //@END2,  D;JGE
        int color = 0;      //@color, M=0
        if(M[24576]==0)     //@24576, D=M
            goto NEXT       //@NEXT,  D;JGE
        color = -1;         //@color, M=-1
    NEXT:                   //(NEXT)
        N[i] = color;       //@color, D=M, @I, A=M, M=D
        i++;                //@i,     M=M+1 
        goto WHILE2         //@WHILE2,0;JMP 
    END2;                   //(END2)

    goto WHILE1             //@WHILE1,0;JMP
```