#!/bin/bash

gcc -static -nostdlib read_flag.s -o read_flag
objcopy --dump-section .text=out_stage2 read_flag
gcc -static -nostdlib multi_stage.s -o multi_stage
objcopy --dump-section .text=out_stage1 multi_stage

# then run level7_teaching1.py or level7_testing1.py line by line on the console (probably because of delay)