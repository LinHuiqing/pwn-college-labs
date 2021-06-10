#!/bin/bash

gcc -static -nostdlib read_flag_4.s -o read_flag_4
objcopy --dump-section .text=out read_flag_4
/challenges/shell/level4_testing1 < out