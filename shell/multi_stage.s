.global _start

_start:
 nop
 nop
 nop
 lea _start(%rip), %rdi
 mov $0x1000, %rsi
 mov $0x6, %rdx
 mov $0x0a, %rax
 syscall

 mov $0, %rdi
 mov $1000, %rdx 
 xor %rax, %rax
 lea _start(%rip), %rsi
 syscall
 jmp _start
