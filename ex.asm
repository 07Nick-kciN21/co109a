@2
     M=0

    //LOOP:
        (loop)
        //if(R1==0) goto EXIT;

         @1
         D=M
         @exit
         D;JEQ 

        //R2+=R0;

         @0
         D=M
         @2
         M=M+D
         //R1--;
         @1
         M=M-1
        

        //goto LOOP;
        @loop
        0;JMP
    //EXIT:
    (exit)
    @exit
    0;JMP