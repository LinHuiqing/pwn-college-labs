import socket

# To solve:
# 1. run /challenges/rev/level9_teaching1 in terminal 1
# 2. run this script in terminal 2

# from bin ninja: int32_t rax_5 = socket(AF_INET, SOCK_STREAM, 0)
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # for network socket
# port no from htons(0xb72a) => 46890
c.connect(("localhost", 46890))

EXPECTED_RESULT = bytes([0xcf, 0x8f, 0x3a, 0xba, 0xeb, 0x5e, 0xcf, 0x84, 0x2e, 0xa6])

output = list(EXPECTED_RESULT)

# for i in range(len(EXPECTED_RESULT)):
#   if i % 2 == 0:
#     output.append(EXPECTED_RESULT[i] ^ 0x2f)
#   else:
#     output.append(EXPECTED_RESULT[i] ^ 0x50)

# for i in range(len(output)):
#   if i % 3 == 0:
#     output[i] ^= 0x2d
#   if i % 3 == 1:
#     output[i] ^= 0x79
#   else:
#     output[i] ^= 0x89

# for i in range(len(output)):
#   if i % 3 == 0:
#     output[i] ^= 0xbf
#   if i % 3 == 1:
#     output[i] ^= 0xde
#   else:
#     output[i] ^= 0xef

# for i in range(len(output)):
#   rsi_10 = (i*0x55555556) >> 0x20 - (0 >> 0x1f)
#   rax_73 = i - (rsi_10 + rsi_10 + rsi_10)
#   if rax_73 == 2:
#     output[i] ^= 0x89
#   elif rax_73 == 0:
#     output[i] ^= 0x2d
#   else:
#     output[i] ^= 0x79

output = b'dgsrhcxsxr'

output = b'____________' + output

c.send(output)
c.close()