import numpy as np
import re
import os

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

def pass1(Filename):
    print("============= PASS1 ================")
    inFile = open(Filename + '.asm','r')
    x = 16
    address = 0
    lab2 = re.compile(r'[\w\W]+[^\)]')
    lab3 = re.compile(r'[\D][\w\W]*')
    for i in inFile:
        if(i.startswith("//") != True and i.startswith("\n") != True):
            i = i.replace('\n','')
            i = i.replace(' ','')
            i = i.split('//')[0]#去掉註解
            print('{}:{}'.format(str(address).zfill(2),i))
            # 確認他是(字串)格式
            if(i[0] == '('):
                # 取得()內字串
                label1 = lab2.search(i[1:]).group()
                if(label1 != None):
                    symb[label1] = address
                    print("symbol:{} address={}".format(label1, symb[label1]))
            elif(i[0] == '@'):
                # 取得符號字串，不要數字開頭
                label3 = lab3.match(i[1:])
                if(label3 != None):
                    label4 = label3.group()
                    symb.setdefault(label4, x)#放入字典
                    x += 1
                address += 1
            else:
                address += 1
    inFile.close()
    # print(symb)

def pass2(Filename):
    print("============= PASS2 ================")
    inFile = open(Filename+'.asm','r')
    hackFile = open(Filename+'.hack','w')
    binFile = open(Filename+'.bin','wb')
    ins = ''
    address=0
    at1 = re.compile(r'[\D][\w\W]*')# @i
    # at2 = re.compile(r'[^@][\d]')# @12
    for i in inFile:
        # 過濾掉註解和換行字元
        if(i.startswith("//") != True and i.startswith("\n") != True):
            # 去掉換行字元和空白
            i = i.replace('\n','')
            i = i.replace(' ','')
            i = i.split('//')[0]
            if(i[0] == '('):
                print(i)
            else:
                # 如果是A指令
                if(i[0] == '@'):
                    # 取得@後字元
                    if(at1.match(i[1:]) != None):#是否為符號
                        num = symb[at1.match(i[1:]).group()]
                    else:#是否為數字
                        num = eval(i[1:])# 取得@後字元
                    binum = bin(num)
                    ins = binum[2:].zfill(16)
                    # print('{}:{:<20}{:>20}'.format(str(address).zfill(2), i ,ins))
                    address += 1
                # 如果是C指令
                else:
                    D = False
                    J = False
                    # 把指令切割
                    ins1 = i.replace(";","=")
                    ins1 = ins1.split('=')
                    # 如果有;代表有jump指令
                    if(i.find(';') != -1):
                        J = True
                    # 如果有=代表有dest指令
                    if(i.find('=') != -1):
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
                    # print("{}:{:<20}{:>20}".format(str(address).zfill(2), i, ins))
                bincode = int(ins,2)#轉換成2進位數字
                hexcode = hex(bincode)#轉換成16進位
                int_bytes = bincode.to_bytes(2, 'big')#轉換成bin檔可讀入的格式
                print("{}:{:<15}{:>20}  {}".format(str(address).zfill(2), i, ins, hexcode[2:].zfill(4)))
                binFile.write(int_bytes)
                hackFile.write(ins+'\n')
                address += 1
    inFile.close()
    hackFile.close()
    binFile.close()
                


def main():
    Filename = input()
    pass1(Filename)
    pass2(Filename)

main()

