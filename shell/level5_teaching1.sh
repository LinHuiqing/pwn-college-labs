#!/bin/bash

gcc -static -nostdlib read_flag_5.s -o read_flag_5
objcopy --dump-section .text=out read_flag_5
cat out | /challenges/shell/level5_teaching1