#!/bin/bash

# 'open("plpty", 0)' => read input from "plpty" file
# EXPECTED_RESULT after mangling: 4b 51 44 54 4e 59 5f 53 46 4a 50 57
# swap indexes 1 and 2 => 4b 44 51 54 4e 59 5f 53 46 4a 50 57
# "mmap(nullptr, 0x1000, 4, 1, rax_6, 0) + 4" which means skip 4 bytes => 61616161757a6f6a7067616d78746e69
# element-wise xor value = 0x3e => 5f5f5f5f757a6f6a7067616d78746e69

echo $(echo "5f5f5f5f757a6f6a7067616d78746e69" | xxd -p -r) > plpty
exec /challenges/rev/level5_testing1
