@16384
D=A
@i
M=D
(WHILE2)
@24576
D=A 
@i 
D=M-D
@END2  
D;JGE
@color 
M=0
@24576
D=M
@NEXT  
D;JGE
@color
M=-1
(NEXT)
@color 
D=M
@I 
A=M
M=D
@i
M=M+1
@WHILE2
0;JMP 
(END2)
@WHILE1
0;JMP