#!/bin/bash

# 'open("vecya", 0)' => read input from "vecya" file
# EXPECTED_RESULT=02 09 0a 10 0e 1b
# after padding (4 bytes cos "lseek(rax_6, 4, 0)") => 6161616102090a100e1b
# element-wise xor value = 0x78 => for 10 chars = 78787878787878787878
# after padding and xor => 191919197a7172687663

echo $(echo "191919197a7172687663" | xxd -p -r) > vecya
exec /challenges/rev/level4_testing1
