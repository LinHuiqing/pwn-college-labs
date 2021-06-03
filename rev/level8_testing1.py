import socket

# To solve:
# 1. run /challenges/rev/level8_testing1 in terminal 1
# 2. run this script in terminal 2

c = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) # for domain (/ non-network) socket
c.connect("rtbwy") # pipe opened by task

EXPECTED_RESULT = bytes([0x64, 0x70, 0x77, 0x67, 0x66, 0x66, 0x62, 0x70])

output = list(EXPECTED_RESULT)

# swap index 1 and 2
output[1], output[2] = output[2], output[1]

# swap index 5 and 7
output[5], output[7] = output[7], output[5]

# reverse
output = output[::-1]

# skip 0xc (int => 12) bytes
output = b'____________' + bytes(output)

c.send(output)
c.close()