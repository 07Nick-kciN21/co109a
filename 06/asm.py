import re
import os



# 無符號版
dest = {"":"000","M":"001","D":"010",
        "MD":"011","A":"100","AM":"101",
        "AD":"110","AMD":"111"}

jump = {"":"000","JGT":"001","JEQ":"010",
        "JGE":"011","JLT":"100","JNE":"101",
        "JLE":"110","JMP":"111"}

comp = {"0":"0101010","1":"0111111","-1":"0111010",
        "D":"0001100","A":"0110000","!D":"0001101",
        "!A":"0110001","-D":"0001111","-A":"0110011",
        "D+1":"0011111","A+1":"0110111","D-1":"0001110",
        "A-1":"0110010","D+A":"0000010","D-A":"0010011",
        "A-D":"0000111","D&A":"0000000","D|A":"0010101",
        "M":"1110000","!M":"1110001","-M":"1110011",
        "M+1":"1110111","M-1":"1110010","D+M":"1000010",
        "D-M":"1010011","M-D":"1000111","D&M":"1000000",
        "D|M":"1010101"}
symb = {"R0":0,"R1":1,"R2":2,"R3":3,"R4":4,"R5":5,"R6":6,"R7":7,
        "R8":8, "R9":9, "R10":10, "R11":11,"R12":12,"R13":13,
        "R14":14,"R15":15,"SCREEN":16384, "KBD":24576, "SP":0, 
        "LCL":0, "ARG":2, "THIS":3, "THAT":4 }

# 轉換成二進位再補充0到16位
def put0(binum):
    binum = '0'*(16-len(binum)) + binum
    return binum

def bin_hex(bin):
    return hex(bin)

def pass1(Filename):
    print("============= PASS1 ================")
    inFile = open(Filename+'.asm','r')
    address = 0
    for i in inFile:
        if(i.startswith("//") != True and i.startswith("\n") != True):
            i = i.replace('\n','')
            print('{:>3}:{}'.format(str(address).zfill(2),i))
            address += 1

def pass2(Filename):
    print("============= PASS2 ================")
    inFile = open(Filename+'.asm','r')
    hackFile = open(Filename+'.hack','w')
    binFile = open(Filename+'.bin','w')
    ins = ''
    address=0
    for i in inFile:
        if(i.startswith("//") != True and i.startswith("\n") != True):# 過濾掉註解和換行字元
            i = i.replace('\n','')# 去掉換行字元
            if(i[0] == '@'):# 如果是A指令
                num = eval(i[1:])# 取得@後字元
                binum = bin(num)
                ins = binum[2:].zfill(16)
            else:# 如果是C指令
                D = False
                J = False
                ins1 = i.replace(";","=")# 把指令切割
                ins1 = ins1.split('=')
                if(i.find(';') != -1):# 如果有;代表有jump指令
                    J = True
                if(i.find('=') != -1):# 如果有=代表有dest指令
                    D = True
                if(J and D):
                    Dest = dest[ins1[0]]
                    Comp = comp[ins1[1]]
                    Jump = jump[ins1[2]]
                elif(J):
                    Dest = "000"
                    Comp = comp[ins1[0]]
                    Jump = jump[ins1[1]]
                else:
                    Dest = dest[ins1[0]]
                    Comp = comp[ins1[1]]
                    Jump = "000"
                ins = "111"+Comp+Dest+Jump
            hexcode = hex(int(ins,2))
            hexcode2 = hexcode[2:].zfill(4)
            print("{:>3}:{:<15}{:>20}  {}".format(str(address).zfill(2), i, ins, hexcode2))
            binFile.write(hexcode2+'\n')    
            hackFile.write(ins+'\n')
            address += 1
    hackFile.close()
                

def main():
    Filename = input()
    pass1(Filename)
    pass2(Filename)

main()