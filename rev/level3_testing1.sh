#!/bin/bash

# env var=oxolv
# EXPECTED_RESULT=e8fceef7ebf5ffe7
# after padding (2 characters) => 6161e8fceef7ebf5ffe7
# element-wise xor value = 0x85 => for 10 chars = 85858585858585858585
# after padding and xor => e4e46d796b726e707a62

export oxolv=$(echo "e4e46d796b726e707a62" | xxd -p -r)
exec /challenges/rev/level3_testing1
