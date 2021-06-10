#!/bin/bash

gcc -static -nostdlib read_flag.s -o read_flag
objcopy --dump-section .text=out read_flag
cat out | /challenges/shell/level2_testing1