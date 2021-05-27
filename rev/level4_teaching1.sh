#!/bin/bash

# 'open("dtmyh", 0)' => read input from "dtmyh" file
# EXPECTED_RESULT=6e 61 7a 71 6d 66
# convert to string => nazqmf
# "skip 2 bytes" and "lseek(rax_6, 2, 0)" which means skip 2 bytes => __nzaqmf

echo "__nzaqmf" > dtmyh
exec /challenges/rev/level4_teaching1
