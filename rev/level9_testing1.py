import socket

# from bin ninja: int32_t rax_5 = socket(AF_INET, SOCK_STREAM, 0)
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # for network socket
# port no from htons(0xb7d2) => 47058
c.connect(("localhost", 47058))

EXPECTED_RESULT = bytes([0x62, 0x63, 0x64, 0x66, 0x66, 0x68, 0x6b, 0x6e, 0x6e, 0x70, 0x73, 0x74, 0x74, 0x75, 0x79])

# ends with sorting => other shifting operations don't matter
# skip 8 bytes
output = b'________' + EXPECTED_RESULT

c.send(output)
c.close()