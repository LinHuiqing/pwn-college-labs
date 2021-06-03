import socket

# To solve:
# 1. run /challenges/rev/level8_teaching1 in terminal 1
# 2. run this script in terminal 2

c = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) # for domain (/ non-network) socket
c.connect("hhyhi") # pipe opened by task

EXPECTED_RESULT = bytes([0xa2, 0xaa, 0xab, 0xad, 0xad, 0xae, 0xae, 0xae, 0xb0, 0xb3, 0xb4, 0xb6, 0xb7, 0xb9, 0xb9, 0xbb])

output = []

# reverse + sort => redundent operations
# XOR with 0xc3
for i in range(len(EXPECTED_RESULT)):
  output.append(EXPECTED_RESULT[i] ^ 0xc3)

# skip 9 bytes
output = b'_________' + bytes(output)

c.send(output)
c.close()