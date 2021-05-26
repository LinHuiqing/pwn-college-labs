#!/bin/bash

# 'open("rzhhb", 0)' => read input from "rzhhb" file
# EXPECTED_RESULT after mangling: 6d 66 72 65 77 76 = mfrewv
# swap indexes 1 and 3 => merfwv
# swap indexes 0 and 4 => werfmv

echo "____werfmv" > rzhhb # skip 4 bytes
exec /challenges/rev/level5_teaching1
