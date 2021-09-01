gcc -static -nostdlib read_flag_6.s -o read_flag_6
objcopy --dump-section .text=out read_flag_6
cat out | /challenges/jail/level6_teaching1 /