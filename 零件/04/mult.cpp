#include<stdio.h>

int main()
{
    int x=10;
    int y=4;
    int i=1;
                
                
    loop:	 		
        if(i>y)		goto EXIT;        
        x += x;		
        i += 1;		
        goto loop;		

        
        EXIT:
        printf("%d", x);
        return 0;	
}
